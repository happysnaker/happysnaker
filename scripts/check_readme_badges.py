#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path

from github_cli import gh_api_exists

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

FIRST_SCREEN_REQUIRED_TEXT = (
    "https://happysnaker.github.io/support/#sponsor-router",
    "https://happysnaker.github.io/support/#current-asks",
    "https://happysnaker.github.io/support/#offer-cards",
    "Productized offer cards",
    "https://happysnaker.github.io/support/#proof-before-payment",
    "https://happysnaker.github.io/review/deploy-read-sample/",
    "docs/sponsor-prospect-pipeline.md",
    "Sponsor prospect pipeline",
    "docs/sponsor-conversion-scorecard.md",
    "Sponsor conversion scorecard",
    "docs/sponsor-scorecard-coverage.md",
    "Sponsor scorecard coverage",
    "Tip / Proof / Review / Fund",
    "qq-ai-bot #26 arm64",
    "RDLeader #27",
)

BADGE_RE = re.compile(r"\[!\[(?P<label>[^\]]+)\]\((?P<image>[^)]+)\)\]\((?P<target>[^)]+)\)")



def workflow_exists(repo: str, workflow: str) -> bool:
    return gh_api_exists(["api", f"repos/{repo}/contents/.github/workflows/{workflow}"])


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify first-screen README workflow badges and workflow files.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable README badge summary.")
    args = parser.parse_args()

    text = README.read_text(encoding="utf-8")
    first_screen_text = "\n".join(text.splitlines()[:40])
    badges = {match.group("label"): (match.group("image"), match.group("target")) for match in BADGE_RE.finditer(text)}
    failures: list[str] = []
    results: list[dict[str, object]] = []

    for expected in EXPECTATIONS:
        actual = badges.get(expected.label)
        badge_failures: list[str] = []
        image = actual[0] if actual else None
        target = actual[1] if actual else None
        if not actual:
            badge_failures.append(f"missing badge {expected.label!r}")
            workflow_present = False
        else:
            if image != expected.image_url:
                badge_failures.append(f"image {image!r} != {expected.image_url!r}")
            if target != expected.target_url:
                badge_failures.append(f"target {target!r} != {expected.target_url!r}")
            workflow_present = workflow_exists(expected.repo, expected.workflow)
            if not workflow_present:
                badge_failures.append(f"workflow missing in {expected.repo}/.github/workflows/{expected.workflow}")
        failures.extend(f"{expected.label}: {failure}" for failure in badge_failures)
        results.append({
            "label": expected.label,
            "repo": expected.repo,
            "workflow": expected.workflow,
            "image": image,
            "expectedImage": expected.image_url,
            "target": target,
            "expectedTarget": expected.target_url,
            "workflowPresent": workflow_present,
            "ok": not badge_failures,
            "failures": badge_failures,
        })

    missing_first_screen_text = [needle for needle in FIRST_SCREEN_REQUIRED_TEXT if needle not in first_screen_text]
    failures.extend(f"first-screen support/proof route missing {needle!r}" for needle in missing_first_screen_text)

    summary = {
        "ok": not failures,
        "badgeCount": len(EXPECTATIONS),
        "foundBadgeCount": sum(1 for result in results if result["image"]),
        "firstScreenRequiredCount": len(FIRST_SCREEN_REQUIRED_TEXT),
        "missingFirstScreenText": missing_first_screen_text,
        "badges": results,
        "failures": failures,
    }
    if args.json:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
    if failures:
        if not args.json:
            print("README badge check failures:", file=sys.stderr)
            for failure in failures:
                print(f"- {failure}", file=sys.stderr)
        return 1

    if not args.json:
        print(f"Checked {len(EXPECTATIONS)} README workflow badges and {len(FIRST_SCREEN_REQUIRED_TEXT)} first-screen support/proof routes")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
