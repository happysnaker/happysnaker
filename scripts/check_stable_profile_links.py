#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
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
    parser = argparse.ArgumentParser(description="Reject one-off profile Actions run links in public docs.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable stable profile proof-link status.")
    args = parser.parse_args()

    failures: list[str] = []
    scanned_files = iter_public_files()
    one_off_run_links: list[dict[str, str]] = []
    required_link_results: list[dict[str, object]] = []
    for path in scanned_files:
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        if rel not in ALLOWED_ONE_OFF_RUN_FILES:
            for match in PROFILE_RUN_RE.finditer(text):
                url = match.group(0)
                one_off_run_links.append({"file": rel, "url": url})
                failures.append(f"{rel}: hard-coded profile run link {url}; use workflow links or {STATUS_SNAPSHOT}")

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
        present = needle in text
        required_link_results.append({"file": rel, "needle": needle, "present": present})
        if not present:
            failures.append(f"{rel}: missing stable profile proof link {needle}")

    summary = {
        "ok": not failures,
        "publicFileCount": len(scanned_files),
        "allowedOneOffRunFiles": sorted(ALLOWED_ONE_OFF_RUN_FILES),
        "oneOffRunLinkCount": len(one_off_run_links),
        "oneOffRunLinks": one_off_run_links,
        "requiredLinks": required_link_results,
        "failures": failures,
    }
    if args.json:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
    if failures:
        if not args.json:
            print("Stable profile proof link check failures:", file=sys.stderr)
            for failure in failures:
                print(f"- {failure}", file=sys.stderr)
        return 1

    if not args.json:
        print("Checked stable profile proof links: no one-off profile run links in public docs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
