#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = [ROOT / "README.md", ROOT / ".github" / "SUPPORT.md", *sorted((ROOT / "docs").glob("*.md"))]

SENSITIVE_PATTERNS = [
    re.compile(pattern, re.IGNORECASE)
    for pattern in [
        r"\bcli_[a-z0-9]{8,}",
        r"\bou_[a-z0-9]{8,}",
        r"\boc_[a-z0-9]{8,}",
        r"\bom_[a-z0-9]{8,}",
        r"bytedance\.larkoffice\.com",
        r"\.uploads/",
        r"/Users/bytedance/",
        r"gho_[A-Za-z0-9_]+",
        r"\bsk-(?:proj|live|test|ant|org)-[A-Za-z0-9_-]{12,}",
    ]
]

REQUIRED = {
    "README.md": [
        "Current sponsorware board",
        "docs/sponsorware-board.md",
        "docs/technical-proof-index.md",
        "qq-ai-bot",
        "RDLeader",
    ],
    ".github/SUPPORT.md": [
        "Proof before payment",
        "Current concrete asks",
        "Sponsor one-pager",
        "qq-ai-bot #26 arm64",
        "RDLeader #27",
    ],
    "docs/sponsorware-board.md": [
        "Current targets",
        "qq-ai-bot #23",
        "RDLeader #2",
        "What sponsorship funds",
    ],
    "docs/technical-proof-index.md": [
        "Flagship proof: qq-ai-bot",
        "Flagship proof: RDLeader",
        "Maintenance proof",
        "Sponsorware / support proof",
    ],
}

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def check_file(path: Path) -> None:
    if not path.exists():
        fail(f"missing file: {path.relative_to(ROOT)}")

    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT).as_posix()

    for line_no, line in enumerate(text.splitlines(), 1):
        if line.rstrip() != line:
            fail(f"{rel}:{line_no}: trailing whitespace")

    for pattern in SENSITIVE_PATTERNS:
        if pattern.search(text):
            fail(f"{rel}: sensitive-looking pattern matched: {pattern.pattern}")

    for needle in REQUIRED.get(rel, []):
        if needle not in text:
            fail(f"{rel}: missing required text: {needle}")

    for link in LINK_RE.findall(text):
        if link.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target_text = link.split("#", 1)[0]
        if not target_text:
            continue
        target = (path.parent / target_text).resolve()
        if not target.exists():
            fail(f"{rel}: broken local link: {link}")


def main() -> None:
    for path in DOCS:
        check_file(path)
    print(f"Verified {len(DOCS)} public markdown files")


if __name__ == "__main__":
    main()
