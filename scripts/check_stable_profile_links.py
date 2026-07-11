#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROFILE_RUN_RE = re.compile(r"https://github\.com/happysnaker/happysnaker/actions/runs/\d+")
STABLE_CI = "https://github.com/happysnaker/happysnaker/actions/workflows/ci.yml"
STABLE_CODEQL = "https://github.com/happysnaker/happysnaker/actions/workflows/codeql.yml"
STATUS_SNAPSHOT = "flagship-status-snapshot.md"
ALLOWED_ONE_OFF_RUN_FILES: set[str] = set()


def iter_public_files() -> list[Path]:
    files = [ROOT / "README.md", *sorted((ROOT / "docs").glob("*.md")), *sorted((ROOT / ".github").rglob("*.md")), *sorted((ROOT / ".github").rglob("*.yml"))]
    return [path for path in files if path.is_file()]


def main() -> int:
    failures: list[str] = []
    for path in iter_public_files():
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        if rel not in ALLOWED_ONE_OFF_RUN_FILES:
            for match in PROFILE_RUN_RE.finditer(text):
                failures.append(f"{rel}: hard-coded profile run link {match.group(0)}; use workflow links or {STATUS_SNAPSHOT}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    proof_index = (ROOT / "docs" / "technical-proof-index.md").read_text(encoding="utf-8")
    required_pairs = [
        ("README.md", readme, STABLE_CI),
        ("README.md", readme, STABLE_CODEQL),
        ("docs/technical-proof-index.md", proof_index, STABLE_CI),
        ("docs/technical-proof-index.md", proof_index, STABLE_CODEQL),
        ("docs/technical-proof-index.md", proof_index, STATUS_SNAPSHOT),
    ]
    for rel, text, needle in required_pairs:
        if needle not in text:
            failures.append(f"{rel}: missing stable profile proof link {needle}")

    if failures:
        print("Stable profile proof link check failures:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print("Checked stable profile proof links: no one-off profile run links in public docs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
