#!/usr/bin/env python3
from __future__ import annotations

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
    "python3 scripts/check_readme_badges.py",
    "python3 scripts/check_support_routes.py",
    "python3 scripts/check_repo_metadata.py",
    "python3 scripts/check_sponsor_release.py",
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
    "Verify operations log",
    "Verify issue labels",
    "Report profile pins",
    "Report RDLeader license posture",
    "Report manual blockers",
    "Verify public site hygiene",
)


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> int:
    if not WORKFLOW.exists():
        fail(f"missing workflow: {WORKFLOW.relative_to(ROOT)}")

    text = WORKFLOW.read_text(encoding="utf-8")
    missing_text = [needle for needle in REQUIRED_TEXT if needle not in text]
    if missing_text:
        fail(f"CI workflow missing required text: {missing_text}")

    compile_line_match = re.search(r"run: python3 -m py_compile (?P<scripts>.+)", text)
    if not compile_line_match:
        fail("CI workflow missing py_compile line")
    compile_line = compile_line_match.group("scripts")
    missing_scripts = [
        script.relative_to(ROOT).as_posix()
        for script in sorted(SCRIPTS.glob("*.py"))
        if script.name != "__init__.py" and script.relative_to(ROOT).as_posix() not in compile_line
    ]
    if missing_scripts:
        fail(f"CI py_compile line missing scripts: {missing_scripts}")

    for step in GH_TOKEN_STEPS:
        index = text.find(f"- name: {step}")
        if index == -1:
            fail(f"CI workflow missing step {step!r}")
        block = text[index : text.find("\n      - name:", index + 1) if text.find("\n      - name:", index + 1) != -1 else len(text)]
        if "GH_TOKEN: ${{ github.token }}" not in block:
            fail(f"CI step {step!r} is missing GH_TOKEN")

    print("Checked CI workflow contract: schedule, scripts, helper gate, GH_TOKEN steps, and site checkout are present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
