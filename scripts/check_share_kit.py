#!/usr/bin/env python3
from __future__ import annotations

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
    "## Sponsorship CTA snippets",
    "### Concrete support ask",
    "### Paid review ask",
    "## Guardrails",
    "https://happysnaker.github.io/support/#proof-before-payment",
    "https://happysnaker.github.io/support/#current-asks",
    "https://happysnaker.github.io/qq-ai-bot/",
    "https://happysnaker.github.io/rdleader/",
    "https://happysnaker.github.io/review/",
    "qq-ai-bot #26 arm64",
    "RDLeader #27",
    "RDLeader#3",
    "external-follow-up-queue.md",
    "QEMU arm64 smoke",
    "Proof before payment",
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
    if not SHARE_KIT.exists():
        fail(f"missing {SHARE_KIT.relative_to(ROOT)}")

    text = SHARE_KIT.read_text(encoding="utf-8")
    for line_no, line in enumerate(text.splitlines(), 1):
        if line.rstrip() != line:
            fail(f"share-kit.md:{line_no}: trailing whitespace")

    missing = [needle for needle in REQUIRED_TEXT if needle not in text]
    if missing:
        fail(f"share kit missing required text: {missing}")

    lowered = text.lower()
    banned_hits = [phrase for phrase in BANNED_PHRASES if phrase in lowered]
    if banned_hits:
        fail(f"share kit contains banned hype phrase(s): {banned_hits}")

    text_fences = len(re.findall(r"^```text$", text, flags=re.MULTILINE))
    if text_fences < 6:
        fail(f"expected at least 6 copy-ready text snippets; found {text_fences}")

    guardrails = text.split("## Guardrails", 1)[-1]
    for guarded_claim in (
        "real physical ARM / CasaOS report",
        "reuse rights",
        "CodeQL-clean",
        "external PR has merged",
        "Do not post the same snippet repeatedly",
    ):
        if guarded_claim not in guardrails:
            fail(f"guardrails missing {guarded_claim!r}")

    print(f"Checked share kit: {text_fences} copy-ready snippets with required proof/support guardrails")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
