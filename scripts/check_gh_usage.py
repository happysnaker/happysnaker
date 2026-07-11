#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
ALLOWED_DIRECT_GH = {"github_cli.py"}
GH_PATTERNS = (
    re.compile(r"subprocess\.run\(\[\"gh\""),
    re.compile(r"subprocess\.run\(\[\'gh\'"),
)


def main() -> int:
    failures: list[str] = []
    for path in sorted(SCRIPTS.glob("*.py")):
        if path.name in ALLOWED_DIRECT_GH:
            continue
        text = path.read_text(encoding="utf-8")
        for pattern in GH_PATTERNS:
            if pattern.search(text):
                failures.append(f"{path.relative_to(ROOT)} uses direct gh subprocess; use scripts/github_cli.py")
                break

    if failures:
        print("GitHub CLI usage check failures:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print("Checked GitHub CLI usage: all direct gh subprocess calls go through scripts/github_cli.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
