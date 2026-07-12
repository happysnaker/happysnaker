#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "ci.yml"
SCRIPTS = ROOT / "scripts"

REQUIRED_TEXT = (
    "name: CI",
    "- master",
    "workflow_dispatch:",
    "- cron: '17 2 * * 1'",
    "permissions:",
    "contents: read",
    "repository: happysnaker/happysnaker.github.io",
    "path: site/happysnaker.github.io",
    "python-version: '3.12'",
    "python3 -m py_compile",
    "python3 scripts/verify_public_docs.py",
    "python3 scripts/check_gh_usage.py",
    "python3 scripts/check_share_kit.py",
    "python3 scripts/check_sponsor_pipeline.py",
    "python3 scripts/check_sponsor_conversion_scorecard.py",
    "python3 scripts/check_readme_badges.py",
    "python3 scripts/check_support_routes.py",
    "python3 scripts/check_repo_metadata.py",
    "python3 scripts/check_sponsor_release.py",
    "python3 scripts/check_sponsor_issues.py",
    "python3 scripts/check_review_funnel.py --site-root site/happysnaker.github.io",
    "python3 scripts/check_ops_issue_log.py",
    "python3 scripts/check_issue_labels.py",
    "python3 scripts/check_profile_pins.py",
    "python3 scripts/check_rdleader_license.py",
    "python3 scripts/check_manual_blockers.py",
    "python3 scripts/check_site_hygiene.py --site-root site/happysnaker.github.io --timeout 8",
)

GH_TOKEN_STEPS = (
    "Verify README badges",
    "Verify support routes",
    "Verify repository metadata",
    "Verify sponsor release",
    "Verify sponsor issues",
    "Verify operations log",
    "Verify issue labels",
    "Report profile pins",
    "Report RDLeader license posture",
    "Report manual blockers",
    "Verify public site hygiene",
)


def workflow_step_block(text: str, step: str) -> str | None:
    index = text.find(f"- name: {step}")
    if index == -1:
        return None
    next_index = text.find("\n      - name:", index + 1)
    return text[index : next_index if next_index != -1 else len(text)]


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify the profile CI workflow proof-check contract.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable CI workflow contract status.")
    args = parser.parse_args()

    failures: list[str] = []
    workflow_rel = WORKFLOW.relative_to(ROOT).as_posix()
    workflow_present = WORKFLOW.exists()
    text = WORKFLOW.read_text(encoding="utf-8") if workflow_present else ""
    if not workflow_present:
        failures.append(f"missing workflow: {workflow_rel}")

    required_text_results = [{"needle": needle, "present": needle in text} for needle in REQUIRED_TEXT]
    missing_text = [item["needle"] for item in required_text_results if not item["present"]]
    if missing_text:
        failures.append(f"CI workflow missing required text: {missing_text}")

    compile_line = None
    compile_line_match = re.search(r"run: python3 -m py_compile (?P<scripts>.+)", text)
    if not compile_line_match:
        failures.append("CI workflow missing py_compile line")
    else:
        compile_line = compile_line_match.group("scripts")

    scripts_to_compile = [
        script.relative_to(ROOT).as_posix()
        for script in sorted(SCRIPTS.glob("*.py"))
        if script.name != "__init__.py"
    ]
    missing_scripts = [
        script
        for script in scripts_to_compile
        if compile_line is None or script not in compile_line
    ]
    if missing_scripts:
        failures.append(f"CI py_compile line missing scripts: {missing_scripts}")

    gh_token_results: list[dict[str, object]] = []
    for step in GH_TOKEN_STEPS:
        block = workflow_step_block(text, step)
        step_present = block is not None
        has_gh_token = bool(block and "GH_TOKEN: ${{ github.token }}" in block)
        gh_token_results.append({"step": step, "present": step_present, "hasGhToken": has_gh_token})
        if not step_present:
            failures.append(f"CI workflow missing step {step!r}")
        elif not has_gh_token:
            failures.append(f"CI step {step!r} is missing GH_TOKEN")

    summary = {
        "ok": not failures,
        "workflow": workflow_rel,
        "workflowPresent": workflow_present,
        "requiredTextCount": len(REQUIRED_TEXT),
        "requiredText": required_text_results,
        "missingRequiredText": missing_text,
        "compileLinePresent": compile_line is not None,
        "compiledScriptCount": len(scripts_to_compile),
        "missingCompiledScripts": missing_scripts,
        "ghTokenStepCount": len(GH_TOKEN_STEPS),
        "ghTokenSteps": gh_token_results,
        "failures": failures,
    }
    if args.json:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
    if failures:
        if not args.json:
            print("CI workflow contract failures:", file=sys.stderr)
            for failure in failures:
                print(f"- {failure}", file=sys.stderr)
        return 1

    if not args.json:
        print("Checked CI workflow contract: schedule, scripts, helper gate, GH_TOKEN steps, and site checkout are present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
