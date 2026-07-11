#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
PROOF_INDEX = ROOT / "docs" / "technical-proof-index.md"
EXEMPT = {
    "check_checker_catalog.py",  # this script is self-evident and checked by CI workflow contract
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify every proof checker is documented in technical-proof-index.md.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable checker catalog summary.")
    args = parser.parse_args()

    proof_text = PROOF_INDEX.read_text(encoding="utf-8")
    checkers = sorted(path.name for path in SCRIPTS.glob("check_*.py") if path.name not in EXEMPT)
    missing = [name for name in checkers if f"scripts/{name}" not in proof_text]
    summary = {
        "proofIndex": PROOF_INDEX.relative_to(ROOT).as_posix(),
        "documented": not missing,
        "checkers": checkers,
        "missing": missing,
        "count": len(checkers),
    }
    if args.json:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
    if missing:
        if not args.json:
            print("Checker catalog failures:", file=sys.stderr)
            for name in missing:
                print(f"- docs/technical-proof-index.md missing scripts/{name}", file=sys.stderr)
        return 1
    if not args.json:
        print(f"Checked checker catalog: {len(checkers)} proof checkers documented in technical-proof-index.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
