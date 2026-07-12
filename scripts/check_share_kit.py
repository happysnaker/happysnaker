#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHARE_KIT = ROOT / "docs" / "share-kit.md"

REQUIRED_TEXT = (
    "# Share kit",
    "## Core angle",
    "## Short share snippets",
    "### X / short post",
    "### LinkedIn / longer post",
    "### WeChat / private share",
    "### Curator / maintainer context",
    "### Project-page closed loop update",
    "## Sponsorship CTA snippets",
    "### 10-second support router ask",
    "### Concrete support ask",
    "### Paid review ask",
    "### Deploy-read sample ask",
    "## Sponsor / paid-support intake replies",
    "### Before-payment reply",
    "### Paid-review intake reply",
    "### Sponsor receipt follow-up",
    "## Guardrails",
    "https://happysnaker.github.io/support/#proof-before-payment",
    "https://happysnaker.github.io/support/#sponsor-router",
    "Default support fallback",
    "https://github.com/happysnaker/.github/commit/0ec8ed7",
    "https://happysnaker.github.io/support/#current-asks",
    "https://happysnaker.github.io/qq-ai-bot/",
    "https://happysnaker.github.io/rdleader/",
    "https://happysnaker.github.io/review/",
    "https://happysnaker.github.io/review/deploy-read-sample/",
    "## Audience routing matrix",
    "Homelab / CasaOS tester",
    "Bot / agent builder",
    "Curator / maintainer",
    "Sponsor / funder",
    "GitHub-profile / README customer",
    "RDLeader evaluator",
    "Do not say physical ARM / CasaOS validation is complete",
    "Do not repeatedly bump external PRs",
    "Do not request private payment screenshots in public issues",
    "Order route: https://happysnaker.github.io/support/#quick-read",
    "top 3 fixes",
    "qq-ai-bot #26 arm64",
    "RDLeader #27",
    "RDLeader#3",
    "external-follow-up-queue.md",
    "QEMU arm64 smoke",
    "Proof before payment",
    "Tip — if one repo saved you time",
    "Fund — if you want a visible public outcome",
    "profile README → project pages",
    "project pages → 10-second support router",
    "Support router: https://happysnaker.github.io/support/#sponsor-router",
    "do not send any private logs, credentials, QR codes, payment screenshots, or internal URLs in a public thread",
    "repo / profile / landing-page URL",
    "one blunt paragraph, top 3 fixes",
    "Received — I will keep the outcome public and tied to the note you used",
    "operations proof log: https://github.com/happysnaker/happysnaker/issues/2",
)

BANNED_PHRASES = (
    "in today's rapidly evolving landscape",
    "game-changer",
    "revolutionary",
    "cutting-edge",
    "transformative journey",
    "unlock the power",
)


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify proof-safe share kit snippets and guardrails.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable share-kit summary.")
    args = parser.parse_args()

    if not SHARE_KIT.exists():
        fail(f"missing {SHARE_KIT.relative_to(ROOT)}")

    text = SHARE_KIT.read_text(encoding="utf-8")
    for line_no, line in enumerate(text.splitlines(), 1):
        if line.rstrip() != line:
            fail(f"share-kit.md:{line_no}: trailing whitespace")

    missing = [needle for needle in REQUIRED_TEXT if needle not in text]

    lowered = text.lower()
    banned_hits = [phrase for phrase in BANNED_PHRASES if phrase in lowered]

    text_fences = len(re.findall(r"^```text$", text, flags=re.MULTILINE))

    guarded_claims = (
        "real physical ARM / CasaOS report",
        "reuse rights",
        "CodeQL-clean",
        "external PR has merged",
        "Do not post the same snippet repeatedly",
        "Never ask for private logs",
        "payment screenshots in public",
        "public tracker",
    )
    guardrails = text.split("## Guardrails", 1)[-1]
    missing_guardrails = [claim for claim in guarded_claims if claim not in guardrails]

    summary = {
        "ok": not missing and not banned_hits and text_fences >= 10 and not missing_guardrails,
        "path": SHARE_KIT.relative_to(ROOT).as_posix(),
        "snippetCount": text_fences,
        "requiredCount": len(REQUIRED_TEXT),
        "missingRequiredText": missing,
        "bannedPhraseHits": banned_hits,
        "missingGuardrails": missing_guardrails,
    }
    if args.json:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
    if missing:
        if not args.json:
            fail(f"share kit missing required text: {missing}")
        return 1
    if banned_hits:
        if not args.json:
            fail(f"share kit contains banned hype phrase(s): {banned_hits}")
        return 1
    if text_fences < 10:
        if not args.json:
            fail(f"expected at least 10 copy-ready text snippets; found {text_fences}")
        return 1
    if missing_guardrails:
        if not args.json:
            fail(f"guardrails missing {missing_guardrails!r}")
        return 1

    if not args.json:
        print(f"Checked share kit: {text_fences} copy-ready snippets with required proof/support guardrails")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
