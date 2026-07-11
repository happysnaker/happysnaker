#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from typing import Any

REPO = "happysnaker/happysnaker"
TAG = "v2026.07-sponsor-one-pager"
REQUIRED_BODY_TEXT = (
    "Sponsor one-pager",
    "https://github.com/happysnaker/happysnaker/blob/master/docs/sponsor-one-pager.md",
    "https://happysnaker.github.io/support/",
    "https://happysnaker.github.io/support/#proof-before-payment",
    "qq-ai-bot #26 arm64",
    "RDLeader #27",
    "Proof before payment",
    "support route checker",
    "repository metadata checker",
)


def run_gh(args: list[str]) -> Any:
    completed = subprocess.run(["gh", *args], check=False, capture_output=True, text=True)
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr.strip() or completed.stdout.strip() or "gh command failed")
    return json.loads(completed.stdout)


def main() -> int:
    try:
        release = run_gh(["release", "view", TAG, "-R", REPO, "--json", "tagName,name,isDraft,isPrerelease,url,body"])
    except RuntimeError as error:
        print(f"ERROR: failed to load release {TAG}: {error}", file=sys.stderr)
        return 1

    failures: list[str] = []
    if release.get("tagName") != TAG:
        failures.append(f"tagName is {release.get('tagName')!r}; expected {TAG!r}")
    if release.get("isDraft"):
        failures.append("release is still draft")
    if not release.get("isPrerelease"):
        failures.append("release should remain a pre-release proof packet")
    body = release.get("body") or ""
    missing = [needle for needle in REQUIRED_BODY_TEXT if needle not in body]
    if missing:
        failures.append(f"release body missing {missing}")

    if failures:
        print("Sponsor release check failures:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(f"OK {release.get('url')}: {release.get('name')} contains sponsor proof routes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
