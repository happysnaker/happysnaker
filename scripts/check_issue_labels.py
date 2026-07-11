#!/usr/bin/env python3
from __future__ import annotations

import argparse
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

def check_label_catalog(repo: str, specs: tuple[LabelSpec, ...], failures: list[str], results: list[dict[str, Any]]) -> None:
    labels = run_gh(["label", "list", "-R", repo, "--limit", "200", "--json", "name,description"])
    by_name = {label.get("name"): label for label in labels}
    for spec in specs:
        label = by_name.get(spec.name)
        missing = label is None
        description = (label.get("description") or "") if label else ""
        failure: str | None = None
        if missing:
            failure = f"{repo}: missing label {spec.name!r}"
        elif spec.description_contains and spec.description_contains.lower() not in description.lower():
            failure = f"{repo}: label {spec.name!r} description {description!r} does not contain {spec.description_contains!r}"
        if failure:
            failures.append(failure)
        results.append({
            "repo": repo,
            "label": spec.name,
            "description": description,
            "requiredDescriptionContains": spec.description_contains,
            "ok": failure is None,
            "failure": failure,
        })


def check_issue_labels(spec: IssueLabelSpec, failures: list[str], results: list[dict[str, Any]]) -> None:
    issue = run_gh(["issue", "view", str(spec.number), "-R", spec.repo, "--json", "number,title,state,url,labels"])
    state = issue.get("state")
    url = issue.get("url")
    labels = {label.get("name") for label in issue.get("labels") or []}
    issue_failures: list[str] = []
    if state != "OPEN":
        issue_failures.append(f"expected OPEN, got {state!r}")
    missing = [label for label in spec.labels if label not in labels]
    if missing:
        issue_failures.append(f"missing labels {missing}; current={sorted(labels)}")
    for failure in issue_failures:
        failures.append(f"{spec.repo}#{spec.number}: {failure} ({url})")
    results.append({
        "repo": spec.repo,
        "number": spec.number,
        "url": url,
        "state": state,
        "requiredLabels": list(spec.labels),
        "currentLabels": sorted(labels),
        "missingLabels": missing,
        "ok": not issue_failures,
        "failures": issue_failures,
    })


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify public triage labels on profile, sponsor, manual, and open-loop issues.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable issue-label summary.")
    args = parser.parse_args()

    failures: list[str] = []
    label_results: list[dict[str, Any]] = []
    issue_results: list[dict[str, Any]] = []
    try:
        for repo, specs in LABEL_SPECS.items():
            check_label_catalog(repo, specs, failures, label_results)
        for spec in ISSUE_SPECS:
            check_issue_labels(spec, failures, issue_results)
    except RuntimeError as error:
        if args.json:
            print(json.dumps({"ok": False, "error": str(error), "failures": [str(error)], "labels": label_results, "issues": issue_results}, indent=2, ensure_ascii=False))
        else:
            print(f"ERROR: failed to check issue labels: {error}", file=sys.stderr)
        return 1

    summary = {
        "ok": not failures,
        "repoCount": len(LABEL_SPECS),
        "issueCount": len(ISSUE_SPECS),
        "labelSpecCount": sum(len(specs) for specs in LABEL_SPECS.values()),
        "labels": label_results,
        "issues": issue_results,
        "failures": failures,
    }
    if args.json:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
    if failures:
        if not args.json:
            print("Issue label check failures:", file=sys.stderr)
            for failure in failures:
                print(f"- {failure}", file=sys.stderr)
        return 1

    if not args.json:
        print(f"Checked labels for {len(ISSUE_SPECS)} open issues across {len(LABEL_SPECS)} repositories")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
