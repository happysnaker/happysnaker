#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from typing import Any


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
    blockers: list[dict[str, str]] = []

    if not pins.get("matchesRecommended"):
        blockers.append({
            "id": "profile-pin-rdleader",
            "status": "open",
            "summary": "Replace happysnaker/Resume with happysnaker/RDLeader in profile pinned repositories.",
            "evidence": f"missing={pins.get('missing')} extra={pins.get('extra')}",
        })

    if not license_state.get("resolved"):
        issue = license_state.get("issue") or {}
        blockers.append({
            "id": "rdleader-license-posture",
            "status": "open",
            "summary": "Resolve RDLeader license posture before implying reuse rights.",
            "evidence": f"licenseInfo={license_state.get('licenseInfo')} rootLicenseExists={license_state.get('rootLicenseExists')} issue={issue.get('state')} {issue.get('url')}",
        })

    summary = {
        "blockers": blockers,
        "resolved": not blockers,
        "profilePins": pins,
        "rdleaderLicense": license_state,
    }

    if args.json:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
    else:
        print("## Manual blockers")
        if not blockers:
            print("none")
        for blocker in blockers:
            print(f"- {blocker['id']}: {blocker['summary']} ({blocker['evidence']})")
        print("\nUse --strict after manual actions to fail until all blockers are resolved.")

    if args.strict and blockers:
        print("Manual blockers remain open", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
