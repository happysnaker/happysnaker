#!/usr/bin/env python3
from __future__ import annotations

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
SUPPORT_URL = "https://happysnaker.github.io/support/"
SPONSOR_RELEASE = "https://github.com/happysnaker/happysnaker/releases/tag/v2026.07-sponsor-one-pager"
FLAGSHIP_SNAPSHOT = "https://github.com/happysnaker/happysnaker/blob/master/docs/flagship-status-snapshot.md"
SHARE_KIT = "https://github.com/happysnaker/happysnaker/blob/master/docs/share-kit.md"
QQ_NOTE = "qq-ai-bot #26 arm64"
RD_NOTE = "RDLeader #27"
REVIEW_SAMPLE = "https://happysnaker.github.io/review/deploy-read-sample/"

EXPECTATIONS: tuple[FileExpectation, ...] = (
    FileExpectation(
        "happysnaker/happysnaker",
        ".github/FUNDING.yml",
        (SUPPORT_URL,),
    ),
    FileExpectation(
        "happysnaker/happysnaker",
        ".github/SUPPORT.md",
        (PROOF_URL, ASKS_URL, SPONSOR_RELEASE, SHARE_KIT, REVIEW_SAMPLE, FLAGSHIP_SNAPSHOT, QQ_NOTE, RD_NOTE, "Quick read", "Async review", "Deploy read"),
    ),
    FileExpectation(
        "happysnaker/happysnaker",
        ".github/ISSUE_TEMPLATE/config.yml",
        ("Proof before payment", PROOF_URL, "Current concrete asks", ASKS_URL, "Share kit", SHARE_KIT, "Technical proof index"),
    ),
    FileExpectation(
        "happysnaker/happysnaker",
        ".github/ISSUE_TEMPLATE/profile_operations.md",
        ("Proof before payment", PROOF_URL, "Current concrete asks", ASKS_URL, "python3 scripts/check_github_status.py", "Sponsor / support guardrails"),
    ),
    FileExpectation(
        "happysnaker/.github",
        ".github/FUNDING.yml",
        (SUPPORT_URL,),
    ),
    FileExpectation(
        "happysnaker/.github",
        "SUPPORT.md",
        (PROOF_URL, ASKS_URL, SPONSOR_RELEASE, SHARE_KIT, REVIEW_SAMPLE, FLAGSHIP_SNAPSHOT, QQ_NOTE, RD_NOTE, "Quick read", "Async review", "Deploy read"),
    ),
    FileExpectation(
        "happysnaker/.github",
        ".github/SUPPORT.md",
        (PROOF_URL, ASKS_URL, SPONSOR_RELEASE, SHARE_KIT, REVIEW_SAMPLE, FLAGSHIP_SNAPSHOT, QQ_NOTE, RD_NOTE, "Quick read", "Async review", "Deploy read"),
    ),
    FileExpectation(
        "happysnaker/.github",
        "CONTRIBUTING.md",
        (PROOF_URL, ASKS_URL, SPONSOR_RELEASE, SHARE_KIT, REVIEW_SAMPLE, "qq-ai-bot", "RDLeader"),
    ),
    FileExpectation(
        "happysnaker/.github",
        ".github/ISSUE_TEMPLATE/config.yml",
        ("Proof before payment", PROOF_URL, "Current concrete asks", ASKS_URL, "Share kit", SHARE_KIT, REVIEW_SAMPLE, SUPPORT_URL),
    ),
    FileExpectation(
        "happysnaker/qq-ai-bot",
        ".github/FUNDING.yml",
        ("https://happysnaker.github.io/support/#from-qq-ai-bot",),
    ),
    FileExpectation(
        "happysnaker/qq-ai-bot",
        "SUPPORT.md",
        (PROOF_URL, ASKS_URL, SPONSOR_RELEASE, SHARE_KIT, REVIEW_SAMPLE, QQ_NOTE, "Latest CI", "Latest CodeQL", "Latest Docker publish", "Latest arm64 smoke", "¥29.9", "¥99"),
    ),
    FileExpectation(
        "happysnaker/qq-ai-bot",
        ".github/SUPPORT.md",
        (PROOF_URL, ASKS_URL, SPONSOR_RELEASE, SHARE_KIT, REVIEW_SAMPLE, FLAGSHIP_SNAPSHOT, "issues/26", "issues/28", "¥29.9", "¥99"),
    ),
    FileExpectation(
        "happysnaker/qq-ai-bot",
        ".github/ISSUE_TEMPLATE/config.yml",
        ("Proof before payment", PROOF_URL, "Current concrete asks", ASKS_URL, "Share kit", SHARE_KIT, "arm64 / CasaOS install report"),
    ),
    FileExpectation(
        "happysnaker/RDLeader",
        ".github/FUNDING.yml",
        ("https://happysnaker.github.io/support/#from-rdleader",),
    ),
    FileExpectation(
        "happysnaker/RDLeader",
        "SUPPORT.md",
        (PROOF_URL, ASKS_URL, SPONSOR_RELEASE, SHARE_KIT, REVIEW_SAMPLE, RD_NOTE, "Security proof", "CI", "CodeQL", "License posture", "¥29.9", "¥99"),
    ),
    FileExpectation(
        "happysnaker/RDLeader",
        ".github/SUPPORT.md",
        (PROOF_URL, ASKS_URL, SPONSOR_RELEASE, SHARE_KIT, REVIEW_SAMPLE, FLAGSHIP_SNAPSHOT, "Latest CI proof", "Latest CodeQL proof", "License posture", "¥29.9", "¥99"),
    ),
    FileExpectation(
        "happysnaker/RDLeader",
        ".github/ISSUE_TEMPLATE/config.yml",
        ("Proof before payment", PROOF_URL, "Current concrete asks", ASKS_URL, "Share kit", SHARE_KIT, "Security report"),
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
    failures: list[str] = []
    for expected in EXPECTATIONS:
        try:
            text = fetch_file(expected.repo, expected.path)
        except RuntimeError as error:
            failures.append(str(error))
            continue
        missing = [needle for needle in expected.required if needle not in text]
        if missing:
            failures.append(f"{expected.repo}:{expected.path}: missing {missing}")
            print(f"FAIL {expected.repo}:{expected.path}")
        else:
            print(f"OK {expected.repo}:{expected.path}")

    if failures:
        print("\nSupport route check failures:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(f"Checked {len(EXPECTATIONS)} support route files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
