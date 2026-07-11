#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
import time
from typing import Any

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


def is_retryable_gh_error(message: str) -> bool:
    retryable_needles = (
        "HTTP 429",
        "HTTP 500",
        "HTTP 502",
        "HTTP 503",
        "HTTP 504",
        "connection reset",
        "connection refused",
        "can't assign requested address",
        "network is unreachable",
        "connection timed out",
        "i/o timeout",
        "TLS handshake timeout",
        "temporary failure",
    )
    lowered = message.lower()
    return any(needle.lower() in lowered for needle in retryable_needles)


def run_gh(args: list[str]) -> Any:
    last_error = "gh command failed"
    for attempt in range(1, 4):
        completed = subprocess.run(["gh", *args], check=False, capture_output=True, text=True)
        if completed.returncode == 0:
            try:
                return json.loads(completed.stdout)
            except json.JSONDecodeError as error:
                last_error = f"invalid JSON from gh: {error}"
        else:
            last_error = completed.stderr.strip() or completed.stdout.strip() or "gh command failed"
        if attempt < 3 and is_retryable_gh_error(last_error):
            time.sleep(attempt * 2)
            continue
        break
    raise RuntimeError(last_error)


def main() -> int:
    failures: list[str] = []
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
        print(f"ERROR: failed to load operations log issue: {error}", file=sys.stderr)
        return 1

    title = issue.get("title") or ""
    state = issue.get("state") or ""
    url = issue.get("url") or ""
    comments = issue.get("comments") or []
    body = issue.get("body") or ""
    combined_log = "\n".join([body, *(comment.get("body") or "" for comment in comments)])

    if title != REQUIRED_TITLE:
        failures.append(f"issue title is {title!r}; expected {REQUIRED_TITLE!r}")
    if state != "OPEN":
        failures.append(f"issue state is {state!r}; expected 'OPEN'")
    if url != ISSUE_URL:
        failures.append(f"issue url is {url!r}; expected {ISSUE_URL!r}")
    if len(comments) < MIN_COMMENTS:
        failures.append(f"issue has {len(comments)} comments; expected at least {MIN_COMMENTS} operation-log entries")

    missing = [needle for needle in REQUIRED_LOG_TEXT if needle not in combined_log]
    if missing:
        failures.append(f"operations log missing required proof text: {missing}")

    if failures:
        print("Operations log check failures:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(f"OK {ISSUE_URL}: {title} is open with {len(comments)} comments and required proof-log markers")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
