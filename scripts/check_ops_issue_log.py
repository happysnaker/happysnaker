#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from typing import Any

from github_cli import run_gh_json

REPO = "happysnaker/happysnaker"
ISSUE_NUMBER = "2"
ISSUE_URL = "https://github.com/happysnaker/happysnaker/issues/2"
MIN_COMMENTS = 20
REQUIRED_TITLE = "GitHub operations cadence"
REQUIRED_LOG_TEXT = (
    "Evidence:",
    "Verification:",
    "sponsor release",
    "125k",
    "compact",
    "share kit",
    "Profile CI",
    "CodeQL",
)



run_gh = run_gh_json

def main() -> int:
    parser = argparse.ArgumentParser(description="Verify issue #2 remains the append-only GitHub operations log.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable operations-log summary.")
    args = parser.parse_args()

    failures: list[str] = []
    issue: dict[str, Any] = {}
    load_error: str | None = None
    try:
        issue = run_gh([
            "issue",
            "view",
            ISSUE_NUMBER,
            "-R",
            REPO,
            "--json",
            "number,title,state,url,updatedAt,body,comments",
        ])
    except RuntimeError as error:
        load_error = str(error)
        failures.append(f"failed to load operations log issue: {error}")

    title = issue.get("title") or ""
    state = issue.get("state") or ""
    url = issue.get("url") or ""
    comments = issue.get("comments") or []
    body = issue.get("body") or ""
    combined_log = "\n".join([body, *(comment.get("body") or "" for comment in comments)])

    if not load_error:
        if title != REQUIRED_TITLE:
            failures.append(f"issue title is {title!r}; expected {REQUIRED_TITLE!r}")
        if state != "OPEN":
            failures.append(f"issue state is {state!r}; expected 'OPEN'")
        if url != ISSUE_URL:
            failures.append(f"issue url is {url!r}; expected {ISSUE_URL!r}")
        if len(comments) < MIN_COMMENTS:
            failures.append(f"issue has {len(comments)} comments; expected at least {MIN_COMMENTS} operation-log entries")

    missing = [needle for needle in REQUIRED_LOG_TEXT if needle not in combined_log]
    if missing and not load_error:
        failures.append(f"operations log missing required proof text: {missing}")

    summary = {
        "ok": not failures,
        "repo": REPO,
        "issueNumber": int(ISSUE_NUMBER),
        "url": url or ISSUE_URL,
        "title": title,
        "state": state,
        "updatedAt": issue.get("updatedAt") if issue else None,
        "commentCount": len(comments),
        "minComments": MIN_COMMENTS,
        "requiredMarkerCount": len(REQUIRED_LOG_TEXT),
        "missingRequiredText": missing,
        "loadError": load_error,
        "failures": failures,
    }
    if args.json:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
    if failures:
        if not args.json:
            print("Operations log check failures:", file=sys.stderr)
            for failure in failures:
                print(f"- {failure}", file=sys.stderr)
        return 1

    if not args.json:
        print(f"OK {ISSUE_URL}: {title} is open with {len(comments)} comments and required proof-log markers")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
