#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import json
import subprocess
import sys
import time
from dataclasses import dataclass
from typing import Any

from github_cli import run_gh_json


@dataclass(frozen=True)
class FileExpectation:
    repo: str
    path: str
    required: tuple[str, ...]


PROOF_URL = "https://happysnaker.github.io/support/#proof-before-payment"
ASKS_URL = "https://happysnaker.github.io/support/#current-asks"
SUPPORT_ROUTER = "https://happysnaker.github.io/support/#sponsor-router"
SUPPORT_URL = "https://happysnaker.github.io/support/"
SPONSOR_RELEASE = "https://github.com/happysnaker/happysnaker/releases/tag/v2026.07-sponsor-one-pager"
FLAGSHIP_SNAPSHOT = "https://github.com/happysnaker/happysnaker/blob/master/docs/flagship-status-snapshot.md"
SHARE_KIT = "https://github.com/happysnaker/happysnaker/blob/master/docs/share-kit.md"
QQ_NOTE = "qq-ai-bot #26 arm64"
RD_NOTE = "RDLeader #27"
REVIEW_SAMPLE = "https://happysnaker.github.io/review/deploy-read-sample/"
INTAKE_REPLIES = "https://github.com/happysnaker/happysnaker/blob/master/docs/share-kit.md#sponsor--paid-support-intake-replies"
PUBLIC_PRIVACY_GUARDRAIL = "Do not paste private logs, credentials, QR codes, payment screenshots, internal URLs"

EXPECTATIONS: tuple[FileExpectation, ...] = (
    FileExpectation(
        "happysnaker/happysnaker",
        ".github/FUNDING.yml",
        (SUPPORT_URL, SUPPORT_ROUTER),
    ),
    FileExpectation(
        "happysnaker/happysnaker",
        ".github/SUPPORT.md",
        (PROOF_URL, SUPPORT_ROUTER, ASKS_URL, SPONSOR_RELEASE, SHARE_KIT, INTAKE_REPLIES, REVIEW_SAMPLE, FLAGSHIP_SNAPSHOT, QQ_NOTE, RD_NOTE, "Quick read", "Async review", "Deploy read", PUBLIC_PRIVACY_GUARDRAIL),
    ),
    FileExpectation(
        "happysnaker/happysnaker",
        ".github/ISSUE_TEMPLATE/config.yml",
        ("Proof before payment", PROOF_URL, "10-second support router", SUPPORT_ROUTER, "Current concrete asks", ASKS_URL, "Share kit", SHARE_KIT, "sponsor / paid-support intake replies", "privacy", "Technical proof index"),
    ),
    FileExpectation(
        "happysnaker/happysnaker",
        ".github/ISSUE_TEMPLATE/profile_operations.md",
        ("Proof before payment", PROOF_URL, "10-second support router", SUPPORT_ROUTER, "Current concrete asks", ASKS_URL, INTAKE_REPLIES, "python3 scripts/check_github_status.py", "Sponsor / support guardrails", "Do not ask for private logs, credentials, QR codes, internal URLs, or payment screenshots in public"),
    ),
    FileExpectation(
        "happysnaker/.github",
        ".github/FUNDING.yml",
        (SUPPORT_URL, SUPPORT_ROUTER),
    ),
    FileExpectation(
        "happysnaker/.github",
        "SUPPORT.md",
        (PROOF_URL, SUPPORT_ROUTER, ASKS_URL, SPONSOR_RELEASE, SHARE_KIT, INTAKE_REPLIES, REVIEW_SAMPLE, FLAGSHIP_SNAPSHOT, QQ_NOTE, RD_NOTE, "Quick read", "Async review", "Deploy read", PUBLIC_PRIVACY_GUARDRAIL),
    ),
    FileExpectation(
        "happysnaker/.github",
        ".github/SUPPORT.md",
        (PROOF_URL, SUPPORT_ROUTER, ASKS_URL, SPONSOR_RELEASE, SHARE_KIT, INTAKE_REPLIES, REVIEW_SAMPLE, FLAGSHIP_SNAPSHOT, QQ_NOTE, RD_NOTE, "Quick read", "Async review", "Deploy read", PUBLIC_PRIVACY_GUARDRAIL),
    ),
    FileExpectation(
        "happysnaker/.github",
        "CONTRIBUTING.md",
        (PROOF_URL, SUPPORT_ROUTER, ASKS_URL, SPONSOR_RELEASE, SHARE_KIT, INTAKE_REPLIES, REVIEW_SAMPLE, "qq-ai-bot", "RDLeader", "Do not send private logs, credentials, QR codes, payment screenshots, or internal URLs in public issues or PRs"),
    ),
    FileExpectation(
        "happysnaker/.github",
        ".github/ISSUE_TEMPLATE/config.yml",
        ("Proof before payment", PROOF_URL, "10-second support router", SUPPORT_ROUTER, "Current concrete asks", ASKS_URL, "Share kit", SHARE_KIT, "sponsor / paid-support intake replies", "privacy", REVIEW_SAMPLE, SUPPORT_URL),
    ),
    FileExpectation(
        "happysnaker/qq-ai-bot",
        ".github/FUNDING.yml",
        ("https://happysnaker.github.io/support/#from-qq-ai-bot",),
    ),
    FileExpectation(
        "happysnaker/qq-ai-bot",
        "README.md",
        (SUPPORT_ROUTER, "10-second support router", INTAKE_REPLIES, "private logs", "payment screenshots", "¥29.9", "¥99", QQ_NOTE),
    ),
    FileExpectation(
        "happysnaker/qq-ai-bot",
        "SUPPORT.md",
        (PROOF_URL, SUPPORT_ROUTER, ASKS_URL, SPONSOR_RELEASE, SHARE_KIT, INTAKE_REPLIES, REVIEW_SAMPLE, QQ_NOTE, "Latest CI", "Latest CodeQL", "Latest Docker publish", "Latest arm64 smoke", "¥29.9", "¥99", PUBLIC_PRIVACY_GUARDRAIL),
    ),
    FileExpectation(
        "happysnaker/qq-ai-bot",
        ".github/SUPPORT.md",
        (PROOF_URL, SUPPORT_ROUTER, ASKS_URL, SPONSOR_RELEASE, SHARE_KIT, INTAKE_REPLIES, REVIEW_SAMPLE, FLAGSHIP_SNAPSHOT, "issues/26", "issues/28", "¥29.9", "¥99", PUBLIC_PRIVACY_GUARDRAIL),
    ),
    FileExpectation(
        "happysnaker/qq-ai-bot",
        ".github/ISSUE_TEMPLATE/config.yml",
        ("Proof before payment", PROOF_URL, "10-second support router", SUPPORT_ROUTER, "Current concrete asks", ASKS_URL, "Share kit", SHARE_KIT, "sponsor / paid-support intake replies", "privacy", "arm64 / CasaOS install report"),
    ),
    FileExpectation(
        "happysnaker/RDLeader",
        ".github/FUNDING.yml",
        ("https://happysnaker.github.io/support/#from-rdleader",),
    ),
    FileExpectation(
        "happysnaker/RDLeader",
        "README.md",
        (SUPPORT_ROUTER, "10-second support router", INTAKE_REPLIES, PUBLIC_PRIVACY_GUARDRAIL, "Tip / Proof / Review / Fund", RD_NOTE, "RDLeader #1", "RDLeader #3", "reuse rights"),
    ),
    FileExpectation(
        "happysnaker/RDLeader",
        "SUPPORT.md",
        (PROOF_URL, SUPPORT_ROUTER, ASKS_URL, SPONSOR_RELEASE, SHARE_KIT, INTAKE_REPLIES, REVIEW_SAMPLE, RD_NOTE, "Security proof", "CI", "CodeQL", "License posture", "¥29.9", "¥99", PUBLIC_PRIVACY_GUARDRAIL),
    ),
    FileExpectation(
        "happysnaker/RDLeader",
        ".github/SUPPORT.md",
        (PROOF_URL, SUPPORT_ROUTER, ASKS_URL, SPONSOR_RELEASE, SHARE_KIT, INTAKE_REPLIES, REVIEW_SAMPLE, FLAGSHIP_SNAPSHOT, "Latest CI proof", "Latest CodeQL proof", "License posture", "¥29.9", "¥99", PUBLIC_PRIVACY_GUARDRAIL),
    ),
    FileExpectation(
        "happysnaker/RDLeader",
        ".github/ISSUE_TEMPLATE/config.yml",
        ("Proof before payment", PROOF_URL, "10-second support router", SUPPORT_ROUTER, "Current concrete asks", ASKS_URL, "Share kit", SHARE_KIT, "sponsor / paid-support intake replies", "privacy", "Security report"),
    ),
    FileExpectation(
        "happysnaker/Resume",
        ".github/FUNDING.yml",
        ("https://happysnaker.github.io/support/#from-resume", SUPPORT_ROUTER),
    ),
    FileExpectation(
        "happysnaker/Resume",
        "README.md",
        (PROOF_URL, SUPPORT_ROUTER, SPONSOR_RELEASE, INTAKE_REPLIES, REVIEW_SAMPLE, "Payment%20screenshot", "¥29.9", "¥99", "Resume", "private logs", "payment screenshots"),
    ),
    FileExpectation(
        "happysnaker/Resume",
        ".github/SUPPORT.md",
        (PROOF_URL, SUPPORT_ROUTER, SPONSOR_RELEASE, INTAKE_REPLIES, REVIEW_SAMPLE, "Best payment note", "Resume", "private logs", "payment screenshots", "internal URLs"),
    ),
    FileExpectation(
        "happysnaker/Resume",
        ".github/ISSUE_TEMPLATE/config.yml",
        ("Proof before payment", PROOF_URL, "10-second support router", SUPPORT_ROUTER, "Sponsor / paid-support intake replies", INTAKE_REPLIES, "privacy guardrails", "Support / direct feedback"),
    ),
    FileExpectation(
        "happysnaker/CSAPPLabsAndNotes",
        ".github/FUNDING.yml",
        ("https://happysnaker.github.io/support/#from-csapplabsandnotes", SUPPORT_ROUTER),
    ),
    FileExpectation(
        "happysnaker/CSAPPLabsAndNotes",
        "README.md",
        (PROOF_URL, SUPPORT_ROUTER, SPONSOR_RELEASE, INTAKE_REPLIES, REVIEW_SAMPLE, "Payment%20screenshot", "¥29.9", "¥99", "CSAPPLabsAndNotes", "private logs", "payment screenshots"),
    ),
    FileExpectation(
        "happysnaker/CSAPPLabsAndNotes",
        ".github/SUPPORT.md",
        (PROOF_URL, SUPPORT_ROUTER, SPONSOR_RELEASE, INTAKE_REPLIES, REVIEW_SAMPLE, "Best payment note", "CSAPPLabsAndNotes", "private logs", "payment screenshots", "internal URLs"),
    ),
    FileExpectation(
        "happysnaker/CSAPPLabsAndNotes",
        ".github/ISSUE_TEMPLATE/config.yml",
        ("Proof before payment", PROOF_URL, "10-second support router", SUPPORT_ROUTER, "Sponsor / paid-support intake replies", INTAKE_REPLIES, "privacy guardrails", "Support / direct feedback"),
    ),
    FileExpectation(
        "happysnaker/github-profile-checklist",
        ".github/FUNDING.yml",
        ("https://happysnaker.github.io/support/#from-github-profile-checklist", SUPPORT_ROUTER),
    ),
    FileExpectation(
        "happysnaker/github-profile-checklist",
        "README.md",
        (PROOF_URL, SUPPORT_ROUTER, SPONSOR_RELEASE, INTAKE_REPLIES, REVIEW_SAMPLE, "Payment%20screenshot", "¥29.9", "¥99", "github-profile-checklist", "private logs", "payment screenshots"),
    ),
    FileExpectation(
        "happysnaker/github-profile-checklist",
        ".github/SUPPORT.md",
        (PROOF_URL, SUPPORT_ROUTER, SPONSOR_RELEASE, INTAKE_REPLIES, REVIEW_SAMPLE, "Best payment note", "github-profile-checklist", "private logs", "payment screenshots", "internal URLs"),
    ),
    FileExpectation(
        "happysnaker/github-profile-checklist",
        ".github/ISSUE_TEMPLATE/config.yml",
        ("Proof before payment", PROOF_URL, "10-second support router", SUPPORT_ROUTER, "Sponsor / paid-support intake replies", INTAKE_REPLIES, "privacy guardrails", "Support / direct feedback"),
    ),
)



run_gh = run_gh_json

def fetch_file(repo: str, path: str) -> str:
    data = run_gh(["api", f"repos/{repo}/contents/{path}"])
    content = data.get("content")
    encoding = data.get("encoding")
    if not isinstance(content, str) or encoding != "base64":
        raise RuntimeError(f"{repo}:{path}: unexpected content response")
    return base64.b64decode(content).decode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify remote support/funding/issue-contact routes across profile and flagship repositories.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable support route summary.")
    args = parser.parse_args()

    failures: list[str] = []
    results: list[dict[str, object]] = []
    for expected in EXPECTATIONS:
        text = ""
        fetch_error: str | None = None
        try:
            text = fetch_file(expected.repo, expected.path)
        except RuntimeError as error:
            fetch_error = str(error)
            failures.append(fetch_error)
        missing = [needle for needle in expected.required if needle not in text] if not fetch_error else list(expected.required)
        if missing and not fetch_error:
            failures.append(f"{expected.repo}:{expected.path}: missing {missing}")
        result = {
            "repo": expected.repo,
            "path": expected.path,
            "requiredCount": len(expected.required),
            "missingRequiredText": missing,
            "fetchError": fetch_error,
            "ok": not fetch_error and not missing,
        }
        results.append(result)
        if not args.json:
            print(("OK" if result["ok"] else "FAIL") + f" {expected.repo}:{expected.path}")

    summary = {
        "ok": not failures,
        "fileCount": len(EXPECTATIONS),
        "checkedFileCount": len(results),
        "requiredCount": sum(len(expected.required) for expected in EXPECTATIONS),
        "files": results,
        "failures": failures,
    }
    if args.json:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
    if failures:
        if not args.json:
            print("\nSupport route check failures:", file=sys.stderr)
            for failure in failures:
                print(f"- {failure}", file=sys.stderr)
        return 1

    if not args.json:
        print(f"Checked {len(EXPECTATIONS)} support route files")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
