#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
import time
from dataclasses import dataclass
from typing import Any

from github_cli import run_gh_json


@dataclass(frozen=True)
class LabelSpec:
    name: str
    description_contains: str | None = None


@dataclass(frozen=True)
class IssueLabelSpec:
    repo: str
    number: int
    labels: tuple[str, ...]


LABEL_SPECS: dict[str, tuple[LabelSpec, ...]] = {
    "happysnaker/happysnaker": (
        LabelSpec("operations", "GitHub operations"),
        LabelSpec("portfolio", "Portfolio"),
        LabelSpec("manual-action", "manual GitHub UI"),
    ),
    "happysnaker/qq-ai-bot": (
        LabelSpec("sponsorship", "Funding"),
        LabelSpec("validation", "deployment validation"),
        LabelSpec("help wanted", "Extra attention"),
    ),
    "happysnaker/RDLeader": (
        LabelSpec("public-packaging", "Public-safe"),
        LabelSpec("roadmap", "Roadmap"),
        LabelSpec("sponsorship", "Funding"),
        LabelSpec("license", "License"),
        LabelSpec("external-follow-up", "External submission"),
    ),
}

ISSUE_SPECS: tuple[IssueLabelSpec, ...] = (
    IssueLabelSpec("happysnaker/happysnaker", 1, ("operations", "portfolio", "manual-action")),
    IssueLabelSpec("happysnaker/happysnaker", 2, ("operations", "portfolio")),
    IssueLabelSpec("happysnaker/qq-ai-bot", 26, ("enhancement", "help wanted", "sponsorship", "validation")),
    IssueLabelSpec("happysnaker/qq-ai-bot", 28, ("sponsorship",)),
    IssueLabelSpec("happysnaker/RDLeader", 1, ("public-packaging", "roadmap", "sponsorship")),
    IssueLabelSpec("happysnaker/RDLeader", 3, ("help wanted", "public-packaging", "roadmap", "license")),
    IssueLabelSpec("happysnaker/RDLeader", 27, ("public-packaging", "roadmap", "sponsorship", "external-follow-up")),
)



run_gh = run_gh_json

def check_label_catalog(repo: str, specs: tuple[LabelSpec, ...], failures: list[str]) -> None:
    labels = run_gh(["label", "list", "-R", repo, "--limit", "200", "--json", "name,description"])
    by_name = {label.get("name"): label for label in labels}
    for spec in specs:
        label = by_name.get(spec.name)
        if not label:
            failures.append(f"{repo}: missing label {spec.name!r}")
            continue
        if spec.description_contains:
            description = label.get("description") or ""
            if spec.description_contains.lower() not in description.lower():
                failures.append(
                    f"{repo}: label {spec.name!r} description {description!r} does not contain {spec.description_contains!r}"
                )


def check_issue_labels(spec: IssueLabelSpec, failures: list[str]) -> None:
    issue = run_gh(["issue", "view", str(spec.number), "-R", spec.repo, "--json", "number,title,state,url,labels"])
    state = issue.get("state")
    url = issue.get("url")
    labels = {label.get("name") for label in issue.get("labels") or []}
    if state != "OPEN":
        failures.append(f"{spec.repo}#{spec.number}: expected OPEN, got {state!r} ({url})")
    missing = [label for label in spec.labels if label not in labels]
    if missing:
        failures.append(f"{spec.repo}#{spec.number}: missing labels {missing}; current={sorted(labels)} ({url})")


def main() -> int:
    failures: list[str] = []
    try:
        for repo, specs in LABEL_SPECS.items():
            check_label_catalog(repo, specs, failures)
        for spec in ISSUE_SPECS:
            check_issue_labels(spec, failures)
    except RuntimeError as error:
        print(f"ERROR: failed to check issue labels: {error}", file=sys.stderr)
        return 1

    if failures:
        print("Issue label check failures:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(f"Checked labels for {len(ISSUE_SPECS)} open issues across {len(LABEL_SPECS)} repositories")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
