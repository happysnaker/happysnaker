#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HANDOFF = ROOT / "docs" / "operator-handoff.md"

REQUIRED_TEXT = (
    "# Operator handoff",
    "Current source of truth",
    "python3 scripts/check_github_status.py --summary",
    "python3 scripts/run_profile_preflight.py --link-scope core --workers 8 --skip-external",
    "python3 scripts/check_manual_blockers.py --json",
    "python3 scripts/check_stable_profile_links.py",
    "python3 scripts/check_gh_usage.py",
    "python3 scripts/check_ci_workflow_contract.py",
    "python3 scripts/check_checker_catalog.py --json",
    "python3 scripts/check_external_followups.py --summary",
    "Current flagship state",
    "qq-ai-bot #26 arm64",
    "RDLeader#3",
    "Proof before payment",
    "Share kit",
    "Deploy-read sample",
    "https://happysnaker.github.io/review/deploy-read-sample/",
    "Sponsor one-pager release",
    "Open blockers",
    "Manual checklist",
    "External follow-up rule",
    "2026-07-16 UTC",
    "--enforce-review-due",
    "Automation guardrails",
    "scripts/github_cli.py",
    "scripts/check_review_funnel.py",
    "python3 scripts/check_review_funnel.py --site-root ../happysnaker.github.io --live --timeout 8 --json",
    "python3 scripts/check_sponsor_issues.py --json",
    "python3 scripts/check_sponsor_release.py --json",
    "python3 scripts/check_support_routes.py --json",
    "python3 scripts/check_repo_metadata.py --json",
    "stable profile workflow links",
    "one-off profile self-check run links",
    "Good next actions",
    "Avoid",
    "issue #2",
    "Deploy read",
)

BANNED_TEXT = (
    "happysnaker/happysnaker/actions/runs/",
    "physical ARM / CasaOS validation is complete",
    "RDLeader reuse rights are granted",
)


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> int:
    if not HANDOFF.exists():
        fail("missing docs/operator-handoff.md")
    text = HANDOFF.read_text(encoding="utf-8")
    for line_no, line in enumerate(text.splitlines(), 1):
        if line.rstrip() != line:
            fail(f"docs/operator-handoff.md:{line_no}: trailing whitespace")
    missing = [needle for needle in REQUIRED_TEXT if needle not in text]
    if missing:
        fail(f"operator handoff missing required text: {missing}")
    banned = [needle for needle in BANNED_TEXT if needle in text]
    if banned:
        fail(f"operator handoff contains banned text: {banned}")
    print(f"Checked operator handoff: {len(REQUIRED_TEXT)} required markers and {len(BANNED_TEXT)} banned claims")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
