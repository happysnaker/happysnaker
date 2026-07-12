#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

from github_cli import run_gh_json


REPO = "happysnaker/happysnaker"
MANUAL_ISSUE = "1"
REQUIRED_MANUAL_ISSUE_LABELS = {"operations", "portfolio", "manual-action"}
REQUIRED_MANUAL_ISSUE_TEXT = (
    "Profile pins still need the GitHub web UI",
    "missing: `happysnaker/RDLeader`",
    "extra: `happysnaker/Resume`",
    "Customize your pins",
    "logged-out (`Sign in` / `Sign up` visible)",
    "RDLeader license posture is still unresolved",
    "scripts/check_issue_labels.py",
    "scripts/check_ops_issue_log.py",
)

OWNER_ACTION_PACKET = "docs/owner-action-packet.md"
REQUIRED_OWNER_ACTION_PACKET_TEXT = (
    "Owner Action Packet",
    "ownerActionRequired",
    "agentBlockedOnOwnerAction",
    "profile-pin-rdleader",
    "rdleader-license-posture",
    "Customize your pins",
    "python3 scripts/check_profile_pins.py --strict",
    "Path A: Apache-2.0",
    "Path B: source-available for now",
    "Do not add a root `LICENSE`",
)



run_gh = run_gh_json

def run_script(args: list[str]) -> Any:
    completed = subprocess.run(["python3", *args], check=False, capture_output=True, text=True)
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr.strip() or completed.stdout.strip() or "script failed")
    try:
        return json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"failed to parse JSON from {' '.join(args)}: {exc}") from exc


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize manual GitHub blockers that affect profile positioning and promotion boundaries.")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero if any manual blocker remains unresolved.")
    parser.add_argument("--json", action="store_true", help="Emit JSON summary.")
    args = parser.parse_args()

    pins = run_script(["scripts/check_profile_pins.py", "--json"])
    license_state = run_script(["scripts/check_rdleader_license.py", "--json"])
    manual_issue = run_gh([
        "issue",
        "view",
        MANUAL_ISSUE,
        "-R",
        REPO,
        "--json",
        "number,title,state,url,updatedAt,labels,body,comments",
    ])
    blockers: list[dict[str, str]] = []
    manual_issue_failures: list[str] = []

    if not pins.get("matchesRecommended"):
        blockers.append({
            "id": "profile-pin-rdleader",
            "status": "open",
            "summary": "Replace happysnaker/Resume with happysnaker/RDLeader in profile pinned repositories.",
            "evidence": f"missing={pins.get('missing')} extra={pins.get('extra')}",
            "ownerActionRequired": True,
            "agentCanCompleteUnauthenticated": False,
            "nextActions": [
                "Log in to GitHub as happysnaker in a real browser session.",
                "Open https://github.com/happysnaker and use Customize your pins.",
                "Remove happysnaker/Resume and add happysnaker/RDLeader.",
                "Run python3 scripts/check_profile_pins.py --strict after saving.",
            ],
        })

    if not license_state.get("resolved"):
        issue = license_state.get("issue") or {}
        decision_packet = license_state.get("decisionPacket") or {}
        blockers.append({
            "id": "rdleader-license-posture",
            "status": "open",
            "summary": "Resolve RDLeader license posture before implying reuse rights.",
            "evidence": f"licenseInfo={license_state.get('licenseInfo')} rootLicenseExists={license_state.get('rootLicenseExists')} issue={issue.get('state')} {issue.get('url')} ownerActionReady={decision_packet.get('ownerActionReady')}",
            "ownerActionRequired": True,
            "agentCanChooseLicense": False,
            "decisionPacketReady": bool(decision_packet.get("ownerActionReady")),
            "nextActions": [
                "Owner chooses Path A: Apache-2.0, then agent can add root LICENSE and update README.",
                "Or owner chooses Path B: source-available for now, then agent keeps no-reuse wording and records re-evaluation trigger.",
                "Do not imply reuse rights until a choice is made and issue #3 is resolved accordingly.",
            ],
        })

    manual_labels = {label.get("name") for label in manual_issue.get("labels") or []}
    missing_labels = sorted(REQUIRED_MANUAL_ISSUE_LABELS - manual_labels)
    if manual_issue.get("state") != "OPEN":
        manual_issue_failures.append(f"manual issue state is {manual_issue.get('state')!r}; expected OPEN")
    if missing_labels:
        manual_issue_failures.append(f"manual issue missing labels {missing_labels}")
    manual_text = "\n".join([manual_issue.get("body") or "", *(comment.get("body") or "" for comment in manual_issue.get("comments") or [])])
    missing_text = [needle for needle in REQUIRED_MANUAL_ISSUE_TEXT if needle not in manual_text]
    if missing_text:
        manual_issue_failures.append(f"manual issue missing text {missing_text}")

    owner_packet_path = Path(OWNER_ACTION_PACKET)
    owner_packet_exists = owner_packet_path.exists()
    owner_packet_text = owner_packet_path.read_text(encoding="utf-8") if owner_packet_exists else ""
    owner_packet_missing = [needle for needle in REQUIRED_OWNER_ACTION_PACKET_TEXT if needle not in owner_packet_text]
    owner_packet_failures = []
    if not owner_packet_exists:
        owner_packet_failures.append(f"missing {OWNER_ACTION_PACKET}")
    if owner_packet_missing:
        owner_packet_failures.append(f"owner action packet missing text {owner_packet_missing}")
    manual_issue_failures.extend(owner_packet_failures)

    next_actions = [action for blocker in blockers for action in blocker.get("nextActions", [])]

    summary = {
        "blockers": blockers,
        "resolved": not blockers,
        "nextActions": next_actions,
        "ownerActionRequired": bool(blockers),
        "agentBlockedOnOwnerAction": bool(blockers),
        "ownerActionPacket": {
            "path": OWNER_ACTION_PACKET,
            "exists": owner_packet_exists,
            "requiredTextCount": len(REQUIRED_OWNER_ACTION_PACKET_TEXT),
            "missingRequiredText": owner_packet_missing,
            "ready": owner_packet_exists and not owner_packet_missing,
        },
        "profilePins": pins,
        "rdleaderLicense": license_state,
        "manualIssue": {
            "url": manual_issue.get("url"),
            "state": manual_issue.get("state"),
            "labels": sorted(manual_labels),
            "updatedAt": manual_issue.get("updatedAt"),
            "failures": manual_issue_failures,
        },
    }

    if args.json:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
    else:
        print("## Manual blockers")
        if not blockers:
            print("none")
        for blocker in blockers:
            print(f"- {blocker['id']}: {blocker['summary']} ({blocker['evidence']})")
            for action in blocker.get("nextActions", []):
                print(f"  - next: {action}")
        if manual_issue_failures:
            print("\nManual issue hygiene failures:")
            for failure in manual_issue_failures:
                print(f"- {failure}")
        else:
            print(f"\nManual issue: {manual_issue.get('url')} is open and aligned")
        print("\nUse --strict after manual actions to fail until all blockers are resolved.")

    if manual_issue_failures:
        print("Manual issue hygiene failures remain", file=sys.stderr)
        return 1
    if args.strict and blockers:
        print("Manual blockers remain open", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
