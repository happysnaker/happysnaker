#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import json
import subprocess
import sys
import time
from typing import Any

from github_cli import run_gh_json

REPO = "happysnaker/RDLeader"
LICENSE_ISSUE = 3
LICENSE_PACKET = "docs/public/license-decision-packet.md"
LICENSE_PACKET_REQUIRED_TEXT = (
    "Owner action required",
    "Path A: Apache-2.0",
    "Path B: source-available for now",
    "Do **not** add a root `LICENSE` or claim reuse rights until the owner chooses Path A",
    "Decision for RDLeader#3",
)




run_gh = run_gh_json

def has_root_license() -> bool:
    try:
        run_gh(["api", f"repos/{REPO}/contents/LICENSE"])
    except RuntimeError:
        return False
    return True


def fetch_text(path: str) -> str | None:
    try:
        data = run_gh(["api", f"repos/{REPO}/contents/{path}"])
    except RuntimeError:
        return None
    content = data.get("content")
    if not isinstance(content, str) or data.get("encoding") != "base64":
        return None
    return base64.b64decode(content).decode("utf-8", errors="replace")


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
    packet_text = fetch_text(LICENSE_PACKET)
    packet_missing = [needle for needle in LICENSE_PACKET_REQUIRED_TEXT if needle not in (packet_text or "")]

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
        "decisionPacket": {
            "path": LICENSE_PACKET,
            "exists": packet_text is not None,
            "requiredTextCount": len(LICENSE_PACKET_REQUIRED_TEXT),
            "missingRequiredText": packet_missing,
            "ownerActionReady": packet_text is not None and not packet_missing,
        },
        "acceptableOwnerChoices": [
            "Path A: Apache-2.0, then add root LICENSE and close issue #3 with metadata evidence.",
            "Path B: source-available for now, keep no root LICENSE and keep no-reuse wording until re-evaluation.",
        ],
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
        print(f"decision packet ready: {str(summary['decisionPacket']['ownerActionReady']).lower()} ({LICENSE_PACKET})")

    if args.strict_resolved and not resolved:
        print("RDLeader license posture is not resolved yet", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
