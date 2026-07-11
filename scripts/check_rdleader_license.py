#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from typing import Any

from github_cli import run_gh_json

REPO = "happysnaker/RDLeader"
LICENSE_ISSUE = 3




run_gh = run_gh_json

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
