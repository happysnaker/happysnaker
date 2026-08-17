#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
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
    "python-version: '3.12'",
    "python3 -m py_compile scripts/*.py",
    "python3 scripts/verify_public_docs.py --json",
    "python3 scripts/check_stable_profile_links.py",
    "python3 scripts/check_readme_badges.py",
    "python3 scripts/check_ci_workflow_contract.py",
)

FORBIDDEN_TEXT = (
    "happysnaker/RDLeader",
    "happysnaker/qq-ai-bot",
    "check_rdleader_license.py",
    "check_issue_labels.py",
    "check_sponsor_issues.py",
    "check_repo_metadata.py",
    "check_site_hygiene.py",
)

GH_TOKEN_STEPS = ("Verify README badges",)


def workflow_step_block(text: str, step: str) -> str | None:
    index = text.find(f"- name: {step}")
    if index == -1:
        return None
    next_index = text.find("\n      - name:", index + 1)
    return text[index : next_index if next_index != -1 else len(text)]


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify the lean profile CI workflow contract.")
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

    forbidden_text_results = [{"needle": needle, "present": needle in text} for needle in FORBIDDEN_TEXT]
    present_forbidden = [item["needle"] for item in forbidden_text_results if item["present"]]
    if present_forbidden:
        failures.append(f"CI workflow still references deleted or retired project checks: {present_forbidden}")

    compile_line_match = re.search(r"run: python3 -m py_compile (?P<scripts>.+)", text)
    compile_line_present = compile_line_match is not None
    if not compile_line_present:
        failures.append("CI workflow missing py_compile line")

    scripts_to_compile = [
        script.relative_to(ROOT).as_posix()
        for script in sorted(SCRIPTS.glob("*.py"))
        if script.name != "__init__.py"
    ]

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
        "forbiddenText": forbidden_text_results,
        "compileLinePresent": compile_line_present,
        "compiledScriptCount": len(scripts_to_compile),
        "ghTokenStepCount": len(GH_TOKEN_STEPS),
        "ghTokenSteps": gh_token_results,
        "failures": failures,
    }
    if args.json:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
    if failures:
        if not args.json:
            print("CI workflow contract failures:")
            for failure in failures:
                print(f"- {failure}")
        return 1

    if not args.json:
        print("Checked CI workflow contract: lean profile documentation checks are present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
