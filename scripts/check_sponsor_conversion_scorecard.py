#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCORECARD = ROOT / "docs" / "sponsor-conversion-scorecard.md"

REQUIRED_TEXT = (
    "# Sponsor Conversion Scorecard",
    "evidence-first scorecard",
    "## Operating rule",
    "Landing surface",
    "Proof surface",
    "Concrete note",
    "Follow-up owner",
    "## Qualification gates",
    "Hot",
    "Warm",
    "Nurture",
    "No-send",
    "Scoring rule",
    "Missing proof link or the ask requires private tokens / logs in public",
    "No maintainer reply and the scheduled review gate is not due",
    "generic donation ask",
    "blocks outreach",
    "## Funnel scorecard",
    "1. Land",
    "2. Trust",
    "3. Route",
    "4. Act",
    "5. Follow up",
    "6. Resolve blockers",
    "Profile README",
    "Flagship status snapshot",
    "10-second support router",
    "Sponsorware board",
    "External follow-up queue",
    "Owner action packet",
    "share-kit.md",
    "2026-07-23 UTC",
    "happysnaker#2",
    "Resume` → `RDLeader",
    "RDLeader license posture",
    "## Segment-to-offer fit",
    "Homelab / CasaOS / NAS / SBC testers",
    "Bot / agent builders",
    "Curators / maintainers",
    "Sponsor / funder",
    "GitHub profile / README customer",
    "RDLeader evaluator",
    "Backend / systems-study reader",
    "qq-ai-bot #26 arm64",
    "RDLeader #27",
    "Deploy read",
    "Quick read",
    "Async review",
    "¥29.9 Quick read",
    "¥99 Async review",
    "## Weekly review questions",
    "## Copy-safe conversion block",
    "## Verification commands",
    "python3 scripts/check_sponsor_conversion_scorecard.py --json",
    "python3 scripts/check_external_followups.py --summary",
)

REQUIRED_LINKS = (
    "https://happysnaker.github.io/support/#sponsor-router",
    "https://happysnaker.github.io/support/#proof-before-payment",
    "https://happysnaker.github.io/review/deploy-read-sample/",
)

REQUIRED_GUARDRAILS = (
    "Do not quote stale green checks as live status",
    "Do not collect payment screenshots, tokens, QR codes, raw logs, or internal URLs in public",
    "Do not repeatedly bump external PRs before the review gate",
    "Do not imply RDLeader reuse rights until license metadata/root `LICENSE` and issue state justify it",
    "Please do not post tokens, QR codes, raw logs, internal URLs, private screenshots, or payment screenshots in public issues",
)

BANNED_TEXT = (
    "physical ARM / CasaOS validation is complete",
    "RDLeader reuse rights are granted",
    "payment screenshots belong in public issues",
    "private bot tokens or raw live integration logs are acceptable in public",
    "external PRs should be bumped repeatedly",
)

MIN_FUNNEL_ROWS = 6
MIN_QUALIFICATION_ROWS = 4
MIN_SEGMENT_ROWS = 7
MIN_TEXT_SNIPPETS = 1


def table_row_count(section_text: str) -> int:
    rows = [line for line in section_text.splitlines() if line.startswith("| ") and "---" not in line]
    return max(0, len(rows) - 1)


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify sponsor conversion scorecard stages, offers, proof links, and guardrails.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable scorecard status.")
    args = parser.parse_args()

    failures: list[str] = []
    if not SCORECARD.exists():
        failures.append(f"missing {SCORECARD.relative_to(ROOT)}")
        text = ""
    else:
        text = SCORECARD.read_text(encoding="utf-8")

    for line_no, line in enumerate(text.splitlines(), 1):
        if line.rstrip() != line:
            failures.append(f"{SCORECARD.relative_to(ROOT)}:{line_no}: trailing whitespace")

    missing_required = [needle for needle in REQUIRED_TEXT if needle not in text]
    missing_links = [needle for needle in REQUIRED_LINKS if needle not in text]
    missing_guardrails = [needle for needle in REQUIRED_GUARDRAILS if needle not in text]

    qualification_section = text.split("## Qualification gates", 1)[-1].split("## Funnel scorecard", 1)[0]
    funnel_section = text.split("## Funnel scorecard", 1)[-1].split("## Segment-to-offer fit", 1)[0]
    segment_section = text.split("## Segment-to-offer fit", 1)[-1].split("## Weekly review questions", 1)[0]
    segment_lines = set(segment_section.splitlines())
    banned_hits = []
    for needle in BANNED_TEXT:
        needle_lower = needle.lower()
        for line in text.splitlines():
            line_lower = line.lower()
            if needle_lower not in line_lower:
                continue
            if "do not" in line_lower or "not " in line_lower or "no " in line_lower or "never " in line_lower:
                continue
            # The segment table has an explicit "Do not say" column. Phrases
            # in that column are guardrails, not positive claims.
            if line in segment_lines and line.startswith("| "):
                continue
            banned_hits.append(needle)
            break
    qualification_row_count = table_row_count(qualification_section)
    funnel_row_count = table_row_count(funnel_section)
    segment_row_count = table_row_count(segment_section)
    text_snippet_count = len(re.findall(r"^```text$", text, flags=re.MULTILINE))

    if qualification_row_count < MIN_QUALIFICATION_ROWS:
        failures.append(f"expected at least {MIN_QUALIFICATION_ROWS} qualification rows; found {qualification_row_count}")
    if funnel_row_count < MIN_FUNNEL_ROWS:
        failures.append(f"expected at least {MIN_FUNNEL_ROWS} funnel rows; found {funnel_row_count}")
    if segment_row_count < MIN_SEGMENT_ROWS:
        failures.append(f"expected at least {MIN_SEGMENT_ROWS} segment rows; found {segment_row_count}")
    if text_snippet_count < MIN_TEXT_SNIPPETS:
        failures.append(f"expected at least {MIN_TEXT_SNIPPETS} copy-safe text snippet; found {text_snippet_count}")
    if missing_required:
        failures.append(f"missing required text: {missing_required}")
    if missing_links:
        failures.append(f"missing required links: {missing_links}")
    if missing_guardrails:
        failures.append(f"missing guardrails: {missing_guardrails}")
    if banned_hits:
        failures.append(f"banned text hits: {banned_hits}")

    summary = {
        "ok": not failures,
        "path": SCORECARD.relative_to(ROOT).as_posix(),
        "requiredCount": len(REQUIRED_TEXT),
        "missingRequiredText": missing_required,
        "requiredLinkCount": len(REQUIRED_LINKS),
        "missingRequiredLinks": missing_links,
        "guardrailCount": len(REQUIRED_GUARDRAILS),
        "missingGuardrails": missing_guardrails,
        "qualificationRowCount": qualification_row_count,
        "funnelRowCount": funnel_row_count,
        "segmentRowCount": segment_row_count,
        "textSnippetCount": text_snippet_count,
        "bannedTextHits": banned_hits,
        "failures": failures,
    }
    if args.json:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
    if failures:
        if not args.json:
            print("Sponsor conversion scorecard failures:", file=sys.stderr)
            for failure in failures:
                print(f"- {failure}", file=sys.stderr)
        return 1
    if not args.json:
        print(
            f"Checked sponsor conversion scorecard: {qualification_row_count} qualification gates, "
            f"{funnel_row_count} funnel stages, "
            f"{segment_row_count} segment rows, and {text_snippet_count} copy-safe snippet"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
