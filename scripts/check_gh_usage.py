#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
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
    parser = argparse.ArgumentParser(description="Verify proof checkers use the shared GitHub CLI helper.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable GitHub CLI helper usage status.")
    args = parser.parse_args()

    failures: list[str] = []
    scanned_scripts: list[str] = []
    allowed_scripts: list[str] = []
    direct_matches: list[dict[str, object]] = []
    for path in sorted(SCRIPTS.glob("*.py")):
        rel = path.relative_to(ROOT).as_posix()
        if path.name in ALLOWED_DIRECT_GH:
            allowed_scripts.append(rel)
            continue
        scanned_scripts.append(rel)
        text = path.read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), 1):
            for pattern in GH_PATTERNS:
                if pattern.search(line):
                    direct_matches.append({
                        "file": rel,
                        "line": line_number,
                        "pattern": pattern.pattern,
                    })

    failed_files = sorted({str(match["file"]) for match in direct_matches})
    failures.extend(f"{file} uses direct gh subprocess; use scripts/github_cli.py" for file in failed_files)

    summary = {
        "ok": not failures,
        "scriptCount": len(scanned_scripts) + len(allowed_scripts),
        "scannedScriptCount": len(scanned_scripts),
        "scannedScripts": scanned_scripts,
        "allowedScriptCount": len(allowed_scripts),
        "allowedScripts": allowed_scripts,
        "allowedDirectGh": sorted(ALLOWED_DIRECT_GH),
        "directMatchCount": len(direct_matches),
        "directMatches": direct_matches,
        "failures": failures,
    }
    if args.json:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
    if failures:
        if not args.json:
            print("GitHub CLI usage check failures:", file=sys.stderr)
            for failure in failures:
                print(f"- {failure}", file=sys.stderr)
        return 1

    if not args.json:
        print("Checked GitHub CLI usage: all direct gh subprocess calls go through scripts/github_cli.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
