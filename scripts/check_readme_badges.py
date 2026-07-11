#!/usr/bin/env python3
from __future__ import annotations

import re
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"


@dataclass(frozen=True)
class BadgeExpectation:
    label: str
    repo: str
    workflow: str

    @property
    def target_url(self) -> str:
        return f"https://github.com/{self.repo}/actions/workflows/{self.workflow}"

    @property
    def image_url(self) -> str:
        return f"{self.target_url}/badge.svg"


EXPECTATIONS = (
    BadgeExpectation("Profile docs CI", "happysnaker/happysnaker", "ci.yml"),
    BadgeExpectation("Profile CodeQL", "happysnaker/happysnaker", "codeql.yml"),
    BadgeExpectation("qq-ai-bot CI", "happysnaker/qq-ai-bot", "ci.yml"),
    BadgeExpectation("qq-ai-bot CodeQL", "happysnaker/qq-ai-bot", "codeql.yml"),
    BadgeExpectation("RDLeader CI", "happysnaker/RDLeader", "ci.yml"),
    BadgeExpectation("RDLeader CodeQL", "happysnaker/RDLeader", "codeql.yml"),
)

BADGE_RE = re.compile(r"\[!\[(?P<label>[^\]]+)\]\((?P<image>[^)]+)\)\]\((?P<target>[^)]+)\)")


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


def workflow_exists(repo: str, workflow: str) -> bool:
    last_error = "gh command failed"
    for attempt in range(1, 4):
        completed = subprocess.run(
            ["gh", "api", f"repos/{repo}/contents/.github/workflows/{workflow}"],
            check=False,
            capture_output=True,
            text=True,
        )
        if completed.returncode == 0:
            return True
        last_error = completed.stderr.strip() or completed.stdout.strip() or "gh command failed"
        if attempt < 3 and is_retryable_gh_error(last_error):
            time.sleep(attempt * 2)
            continue
        return False
    return False


def main() -> int:
    text = README.read_text(encoding="utf-8")
    badges = {match.group("label"): (match.group("image"), match.group("target")) for match in BADGE_RE.finditer(text)}
    failures: list[str] = []

    for expected in EXPECTATIONS:
        actual = badges.get(expected.label)
        if not actual:
            failures.append(f"missing badge {expected.label!r}")
            continue
        image, target = actual
        if image != expected.image_url:
            failures.append(f"{expected.label}: image {image!r} != {expected.image_url!r}")
        if target != expected.target_url:
            failures.append(f"{expected.label}: target {target!r} != {expected.target_url!r}")
        if not workflow_exists(expected.repo, expected.workflow):
            failures.append(f"{expected.label}: workflow missing in {expected.repo}/.github/workflows/{expected.workflow}")

    if failures:
        print("README badge check failures:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(f"Checked {len(EXPECTATIONS)} README workflow badges")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
