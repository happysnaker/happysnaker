#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

from github_cli import run_gh_json

ROOT = Path(__file__).resolve().parents[1]
SOURCE_FILE = ROOT / "docs" / "sponsor-one-pager.md"
REPO = "happysnaker/happysnaker"
TAG = "v2026.07-sponsor-one-pager"
MAX_BODY_CHARS = 25000
MIN_BODY_CHARS = 1000

REQUIRED_BODY_TEXT = (
    "Sponsor one-pager",
    "https://github.com/happysnaker/happysnaker/blob/master/docs/sponsor-one-pager.md",
    "https://happysnaker.github.io/support/",
    "https://happysnaker.github.io/review/deploy-read-sample/",
    "https://happysnaker.github.io/support/#proof-before-payment",
    "https://github.com/happysnaker/happysnaker/blob/master/docs/flagship-technical-map.md",
    "https://github.com/happysnaker/happysnaker/blob/master/docs/share-kit.md",
    "https://github.com/happysnaker/happysnaker/actions/workflows/ci.yml",
    "https://github.com/happysnaker/happysnaker/actions/workflows/codeql.yml",
    "flagship technical map",
    "share kit",
    "qq-ai-bot #26 arm64",
    "RDLeader #27",
    "Deploy read",
    "¥29.9",
    "Proof before payment",
    "support route checker",
    "repository metadata checker",
    "Operations log",
    "https://github.com/happysnaker/happysnaker/issues/2",
    "python3 scripts/run_profile_preflight.py --link-scope core --workers 8 --skip-external",
    "python3 scripts/check_github_status.py --summary",
    "python3 scripts/check_checker_catalog.py --json",
)

REQUIRED_SOURCE_TEXT = (
    "Reproduce this proof packet",
    "https://happysnaker.github.io/review/deploy-read-sample/",
    "Deploy read",
    "python3 scripts/run_profile_preflight.py --link-scope core --workers 8 --skip-external",
    "python3 scripts/check_github_status.py --summary",
    "python3 scripts/check_checker_catalog.py --json",
    "Proof before payment",
    "qq-ai-bot #26 arm64",
    "RDLeader #27",
    "Deploy read",
    "¥29.9",
)


run_gh = run_gh_json

def main() -> int:
    failures: list[str] = []
    if not SOURCE_FILE.exists():
        failures.append(f"missing source sponsor one-pager: {SOURCE_FILE.relative_to(ROOT)}")
        source_text = ""
    else:
        source_text = SOURCE_FILE.read_text(encoding="utf-8")
        source_missing = [needle for needle in REQUIRED_SOURCE_TEXT if needle not in source_text]
        if source_missing:
            failures.append(f"source sponsor one-pager missing {source_missing}")

    try:
        release = run_gh(["release", "view", TAG, "-R", REPO, "--json", "tagName,name,isDraft,isPrerelease,url,body"])
    except RuntimeError as error:
        print(f"ERROR: failed to load release {TAG}: {error}", file=sys.stderr)
        return 1

    if release.get("tagName") != TAG:
        failures.append(f"tagName is {release.get('tagName')!r}; expected {TAG!r}")
    if release.get("isDraft"):
        failures.append("release is still draft")
    if not release.get("isPrerelease"):
        failures.append("release should remain a pre-release proof packet")
    body = release.get("body") or ""
    body_length = len(body)
    if body_length > MAX_BODY_CHARS:
        failures.append(f"release body is {body_length} chars; keep <= {MAX_BODY_CHARS} and put history in issue #2")
    if body_length < MIN_BODY_CHARS:
        failures.append(f"release body is only {body_length} chars; expected >= {MIN_BODY_CHARS} for a useful proof packet")
    missing = [needle for needle in REQUIRED_BODY_TEXT if needle not in body]
    if missing:
        failures.append(f"release body missing {missing}")
    if "https://github.com/happysnaker/happysnaker/actions/runs/" in body:
        failures.append("release body should use stable profile workflow links, not one-off profile run links")

    if failures:
        print("Sponsor release check failures:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(f"OK {release.get('url')}: {release.get('name')} and {SOURCE_FILE.relative_to(ROOT)} contain compact sponsor proof routes ({len(body)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
