#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "sponsor-scorecard-coverage.md"

REQUIRED_TEXT = (
    "# Sponsor Scorecard Coverage",
    "sponsor conversion scorecard",
    "Hot / Warm / Nurture / No-send",
    "## Coverage rule",
    "keep productized offer cards tied to concrete public outcomes",
    "## Covered surfaces",
    "Profile first screen",
    "Support / Pages funnel",
    "Sponsor one-pager / release",
    "Live sponsor/support issues",
    "External follow-up queue",
    "Profile/default support fallback",
    "Flagship repos",
    "Paid-review repos",
    "Technical-review repos",
    "Systems / indie content repos",
    "Go docs/template repos",
    "profile README support/proof block",
    "support page productized offer cards, `qq-ai-bot`, `RDLeader`, review page, deploy-read sample",
    "fund a real host report, fund curator follow-up, buy a deploy read, or tip with attribution",
    "`qq-ai-bot#26`, `qq-ai-bot#28`, `RDLeader#1`, `RDLeader#3`, `RDLeader#27`",
    "tracked external PRs plus flagship tracker issues",
    "postedFollowupUrl",
    "Posted follow-ups",
    "prevents duplicate external bumps",
    "`Resume` and `github-profile-checklist`",
    "`backend-engineer-checklist`, `system-design-checklist`, `production-readiness-checklist`",
    "`CSAPPLabsAndNotes`, `happydb`, `chinese-independent-developer`",
    "`go-service-starter` and `go-http-middleware-kit`",
    "Go service and middleware readers classify before support, deploy-read, or paid-review asks",
    "## No-send guardrails",
    "qq-ai-bot #26 arm64",
    "RDLeader#3",
    "2026-07-23 UTC",
    "generic donation bump",
    "private logs, credentials, QR codes, payment screenshots, internal URLs, or raw live integration output",
    "## Verification bundle",
    "python3 scripts/check_sponsor_scorecard_coverage.py --json",
    "python3 scripts/check_sponsor_conversion_scorecard.py --json",
    "python3 scripts/check_support_routes.py --json",
    "python3 scripts/check_review_funnel.py --site-root ../happysnaker.github.io --live --timeout 8 --json",
    "python3 scripts/check_sponsor_issues.py --json",
    "python3 scripts/check_external_followups.py --summary",
)

BANNED_TEXT = (
    "physical ARM / CasaOS validation is complete",
    "RDLeader reuse rights are granted",
    "license granted",
    "payment screenshots are fine in public",
)

MIN_COVERAGE_ROWS = 11


def count_table_rows(section: str) -> int:
    rows = [line for line in section.splitlines() if line.startswith("| ") and "---" not in line]
    return max(0, len(rows) - 1)


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify sponsor scorecard coverage documentation and guardrails.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable scorecard coverage summary.")
    args = parser.parse_args()

    failures: list[str] = []
    if not DOC.exists():
        text = ""
        failures.append(f"missing {DOC.relative_to(ROOT)}")
    else:
        text = DOC.read_text(encoding="utf-8")

    for line_no, line in enumerate(text.splitlines(), 1):
        if line.rstrip() != line:
            failures.append(f"{DOC.relative_to(ROOT)}:{line_no}: trailing whitespace")

    missing_required = [needle for needle in REQUIRED_TEXT if needle not in text]
    banned_hits = [needle for needle in BANNED_TEXT if needle.lower() in text.lower()]
    coverage_section = text.split("## Covered surfaces", 1)[-1].split("## No-send guardrails", 1)[0]
    coverage_rows = count_table_rows(coverage_section)

    if missing_required:
        failures.append(f"missing required text: {missing_required}")
    if banned_hits:
        failures.append(f"banned text hits: {banned_hits}")
    if coverage_rows < MIN_COVERAGE_ROWS:
        failures.append(f"expected at least {MIN_COVERAGE_ROWS} coverage rows; found {coverage_rows}")

    summary = {
        "ok": not failures,
        "path": DOC.relative_to(ROOT).as_posix(),
        "requiredCount": len(REQUIRED_TEXT),
        "missingRequiredText": missing_required,
        "coverageRowCount": coverage_rows,
        "bannedTextHits": banned_hits,
        "failures": failures,
    }
    if args.json:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
    if failures:
        if not args.json:
            print("Sponsor scorecard coverage failures:", file=sys.stderr)
            for failure in failures:
                print(f"- {failure}", file=sys.stderr)
        return 1
    if not args.json:
        print(f"Checked sponsor scorecard coverage: {coverage_rows} coverage rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
