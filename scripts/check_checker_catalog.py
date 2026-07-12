#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
PROOF_INDEX = ROOT / "docs" / "technical-proof-index.md"

JSON_FLAG_RE = re.compile(r"\.add_argument\(\s*['\"]--json['\"]")


def has_json_flag(path: Path) -> bool:
    """Return true only when a checker defines a real argparse --json flag."""
    return bool(JSON_FLAG_RE.search(path.read_text(encoding="utf-8")))


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify every proof checker is documented in technical-proof-index.md.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable checker catalog summary.")
    args = parser.parse_args()

    proof_text = PROOF_INDEX.read_text(encoding="utf-8")
    checker_paths = sorted(SCRIPTS.glob("check_*.py"))
    checkers = [path.name for path in checker_paths]
    missing = [name for name in checkers if f"scripts/{name}" not in proof_text]
    missing_json = [path.name for path in checker_paths if not has_json_flag(path)]
    summary = {
        "proofIndex": PROOF_INDEX.relative_to(ROOT).as_posix(),
        "documented": not missing,
        "jsonSupported": not missing_json,
        "checkers": checkers,
        "missing": missing,
        "missingJsonSupport": missing_json,
        "count": len(checkers),
    }
    if args.json:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
    failures = []
    failures.extend(f"docs/technical-proof-index.md missing scripts/{name}" for name in missing)
    failures.extend(f"scripts/{name} is missing --json support" for name in missing_json)
    if failures:
        if not args.json:
            print("Checker catalog failures:", file=sys.stderr)
            for failure in failures:
                print(f"- {failure}", file=sys.stderr)
        return 1
    if not args.json:
        print(f"Checked checker catalog: {len(checkers)} proof checkers documented in technical-proof-index.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
