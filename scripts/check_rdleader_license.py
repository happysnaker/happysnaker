#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from typing import Any

REPO = "happysnaker/RDLeader"
LICENSE_ISSUE = 3



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


def has_root_license() -> bool:
    try:
        run_gh(["api", f"repos/{REPO}/contents/LICENSE"])
    except RuntimeError:
        return False
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Report RDLeader license posture without changing it.")
    parser.add_argument("--strict-resolved", action="store_true", help="Exit non-zero unless RDLeader has resolved license metadata and issue #3 is closed.")
    parser.add_argument("--json", action="store_true", help="Emit JSON summary.")
    args = parser.parse_args()

    repo = run_gh(["repo", "view", REPO, "--json", "nameWithOwner,licenseInfo,homepageUrl,repositoryTopics,isArchived,visibility"])
    issue = run_gh(["issue", "view", str(LICENSE_ISSUE), "-R", REPO, "--json", "number,title,state,updatedAt,url,labels"])
    root_license = has_root_license()
    license_info = repo.get("licenseInfo")
    issue_closed = issue.get("state") == "CLOSED"
    resolved = bool(license_info) and root_license and issue_closed
    unresolved_expected = not license_info and not root_license and not issue_closed

    summary = {
        "repo": REPO,
        "licenseInfo": license_info,
        "rootLicenseExists": root_license,
        "issue": {
            "number": issue.get("number"),
            "title": issue.get("title"),
            "state": issue.get("state"),
            "updatedAt": issue.get("updatedAt"),
            "url": issue.get("url"),
            "labels": [label.get("name") for label in issue.get("labels", [])],
        },
        "resolved": resolved,
        "currentGuardrailState": "unresolved-tracked" if unresolved_expected else "mixed-or-resolved",
        "guardrail": "Do not imply RDLeader reuse rights until licenseInfo/root LICENSE exist and issue #3 is closed.",
    }

    if args.json:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
    else:
        print("## RDLeader license posture")
        print(f"licenseInfo: {license_info or 'none'}")
        print(f"root LICENSE exists: {str(root_license).lower()}")
        print(f"issue #{LICENSE_ISSUE}: {issue.get('state')} {issue.get('url')}")
        print(f"resolved: {str(resolved).lower()}")
        print("guardrail: do not imply RDLeader reuse rights until licenseInfo/root LICENSE exist and issue #3 is closed")

    if args.strict_resolved and not resolved:
        print("RDLeader license posture is not resolved yet", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
