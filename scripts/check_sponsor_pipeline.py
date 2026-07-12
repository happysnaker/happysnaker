#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIPELINE = ROOT / "docs" / "sponsor-prospect-pipeline.md"

REQUIRED_TEXT = (
    "# Sponsor Prospect Pipeline",
    "Evidence-first pipeline",
    "Do not start from “please donate.”",
    "## Active segments",
    "Homelab / CasaOS / NAS / SBC testers",
    "Bot / agent builders",
    "Curators / maintainers",
    "GitHub profile / README customers",
    "Sponsor / funder",
    "RDLeader evaluators",
    "Backend / systems-study readers",
    "## Current working list",
    "qq-ai-bot#26",
    "docker/awesome-compose#781",
    "AwesomeHomelab#98",
    "jbesomi/awesome-autonomous-agents#20",
    "RDLeader#27",
    "2026-07-16 UTC",
    "## Links to use",
    "https://happysnaker.github.io/support/#proof-before-payment",
    "https://happysnaker.github.io/support/#sponsor-router",
    "https://happysnaker.github.io/support/#current-asks",
    "https://happysnaker.github.io/review/deploy-read-sample/",
    "https://github.com/happysnaker/qq-ai-bot/blob/main/docs/public/arm64-casaos-tester-pack.md",
    "https://github.com/happysnaker/qq-ai-bot/blob/main/docs/public/homelab-outreach-kit.md",
    "https://github.com/happysnaker/RDLeader/blob/main/docs/public/distribution-kit.md",
    "https://github.com/happysnaker/RDLeader/blob/main/docs/public/submission-tracker.md",
    "## Reply patterns",
    "### Tester ask",
    "### Paid-review ask",
    "### Sponsor ask",
    "## Cadence",
    "python3 scripts/check_external_followups.py --summary",
    "python3 scripts/check_sponsor_pipeline.py --json",
)

REQUIRED_GUARDRAILS = (
    "Do not claim physical ARM / CasaOS validation is complete",
    "Do not request tokens, QR codes, raw logs, or private screenshots in public",
    "Do not repeatedly bump external PRs before the 2026-07-16 UTC gate",
    "Keep payment evidence private by email only, never in public issues",
    "Do not imply reuse rights until `RDLeader#3` and root license posture are resolved",
    "Do not send private logs, tokens, QR codes, payment screenshots, or internal URLs in public issues",
)

BANNED_TEXT = (
    "physical ARM / CasaOS validation is complete",
    "physical ARM/CasaOS completion is done",
    "RDLeader reuse rights are granted",
    "license granted",
    "guaranteed sponsor",
    "private logs are fine",
)

MIN_SEGMENT_ROWS = 7
MIN_REPLY_SNIPPETS = 3


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify sponsor prospect pipeline routing, proof links, and guardrails.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable sponsor-pipeline summary.")
    args = parser.parse_args()

    failures: list[str] = []
    if not PIPELINE.exists():
        failures.append(f"missing {PIPELINE.relative_to(ROOT)}")
        text = ""
    else:
        text = PIPELINE.read_text(encoding="utf-8")

    for line_no, line in enumerate(text.splitlines(), 1):
        if line.rstrip() != line:
            failures.append(f"{PIPELINE.relative_to(ROOT)}:{line_no}: trailing whitespace")

    missing_required = [needle for needle in REQUIRED_TEXT if needle not in text]
    missing_guardrails = [needle for needle in REQUIRED_GUARDRAILS if needle not in text]

    lowered = text.lower()
    banned_hits = [needle for needle in BANNED_TEXT if needle.lower() in lowered]
    # Allow banned phrases when they are part of an explicit "do not claim" guardrail.
    banned_hits = [
        needle
        for needle in banned_hits
        if f"do not claim {needle.lower()}" not in lowered
        and f"do not imply {needle.lower()}" not in lowered
    ]

    active_segments = text.split("## Active segments", 1)[-1].split("## Current working list", 1)[0]
    segment_rows = [line for line in active_segments.splitlines() if line.startswith("| ") and "---" not in line]
    segment_count = max(0, len(segment_rows) - 1)
    if segment_count < MIN_SEGMENT_ROWS:
        failures.append(f"expected at least {MIN_SEGMENT_ROWS} active segment rows; found {segment_count}")

    reply_snippets = len(re.findall(r"^```text$", text, flags=re.MULTILINE))
    if reply_snippets < MIN_REPLY_SNIPPETS:
        failures.append(f"expected at least {MIN_REPLY_SNIPPETS} copy-ready reply snippets; found {reply_snippets}")

    if missing_required:
        failures.append(f"missing required text: {missing_required}")
    if missing_guardrails:
        failures.append(f"missing guardrails: {missing_guardrails}")
    if banned_hits:
        failures.append(f"banned text hits: {banned_hits}")

    summary = {
        "ok": not failures,
        "path": PIPELINE.relative_to(ROOT).as_posix(),
        "requiredCount": len(REQUIRED_TEXT),
        "missingRequiredText": missing_required,
        "guardrailCount": len(REQUIRED_GUARDRAILS),
        "missingGuardrails": missing_guardrails,
        "segmentCount": segment_count,
        "replySnippetCount": reply_snippets,
        "bannedTextHits": banned_hits,
        "failures": failures,
    }
    if args.json:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
    if failures:
        if not args.json:
            print("Sponsor prospect pipeline failures:", file=sys.stderr)
            for failure in failures:
                print(f"- {failure}", file=sys.stderr)
        return 1
    if not args.json:
        print(f"Checked sponsor prospect pipeline: {segment_count} segments and {reply_snippets} reply snippets")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
