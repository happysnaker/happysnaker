#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class RepoCheck:
    repo: str
    branch: str
    workflows: tuple[str, ...]
    alerts: bool = True


REPOS: tuple[RepoCheck, ...] = (
    RepoCheck(
        repo="happysnaker/happysnaker",
        branch="master",
        workflows=("CI", "CodeQL"),
    ),
    RepoCheck(
        repo="happysnaker/qq-ai-bot",
        branch="main",
        workflows=("CI", "CodeQL", "Publish Docker image", "Arm64 image smoke"),
    ),
    RepoCheck(
        repo="happysnaker/RDLeader",
        branch="main",
        workflows=("CI", "CodeQL"),
    ),
    RepoCheck(
        repo="happysnaker/happysnaker.github.io",
        branch="master",
        workflows=("pages-build-deployment",),
        alerts=False,
    ),
)

ALERT_ENDPOINTS = {
    "codeql": "code-scanning/alerts?state=open&per_page=100",
    "dependabot": "dependabot/alerts?state=open&per_page=100",
    "secret": "secret-scanning/alerts?state=open&per_page=100",
}


def run_gh(args: list[str]) -> Any:
    completed = subprocess.run(
        ["gh", *args],
        check=False,
        capture_output=True,
        text=True,
    )
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr.strip() or completed.stdout.strip() or "gh command failed")
    stdout = completed.stdout.strip()
    return json.loads(stdout) if stdout else None


def latest_runs(repo: RepoCheck) -> dict[str, dict[str, Any]]:
    runs = run_gh(
        [
            "run",
            "list",
            "-R",
            repo.repo,
            "--branch",
            repo.branch,
            "--limit",
            "20",
            "--json",
            "workflowName,status,conclusion,headSha,createdAt,url,databaseId",
        ]
    )
    latest: dict[str, dict[str, Any]] = {}
    for run in runs:
        name = run.get("workflowName")
        if name and name not in latest:
            latest[name] = run
    return latest


def alert_count(repo: str, endpoint: str) -> int:
    path = f"repos/{repo}/{endpoint}"
    try:
        result = run_gh(["api", path])
    except RuntimeError as error:
        # Some repos may not have a scanner enabled. Surface this as an error
        # for configured alert checks instead of silently claiming clean.
        raise RuntimeError(f"{repo} {endpoint}: {error}") from error
    if not isinstance(result, list):
        raise RuntimeError(f"{repo} {endpoint}: unexpected API response")
    return len(result)


def main() -> int:
    parser = argparse.ArgumentParser(description="Check flagship GitHub workflow and alert state.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON summary.")
    args = parser.parse_args()

    failures: list[str] = []
    summary: dict[str, Any] = {}

    for repo in REPOS:
        repo_summary: dict[str, Any] = {"branch": repo.branch, "workflows": {}, "alerts": {}}
        try:
            runs = latest_runs(repo)
        except RuntimeError as error:
            failures.append(f"{repo.repo}: failed to list runs: {error}")
            summary[repo.repo] = repo_summary
            continue

        for workflow in repo.workflows:
            run = runs.get(workflow)
            if not run:
                failures.append(f"{repo.repo}: missing workflow run: {workflow}")
                repo_summary["workflows"][workflow] = None
                continue
            repo_summary["workflows"][workflow] = {
                "status": run.get("status"),
                "conclusion": run.get("conclusion"),
                "sha": (run.get("headSha") or "")[:7],
                "url": run.get("url"),
                "createdAt": run.get("createdAt"),
            }
            if run.get("status") != "completed" or run.get("conclusion") != "success":
                failures.append(
                    f"{repo.repo}: {workflow} is {run.get('status')}/{run.get('conclusion')} ({run.get('url')})"
                )

        if repo.alerts:
            for name, endpoint in ALERT_ENDPOINTS.items():
                try:
                    count = alert_count(repo.repo, endpoint)
                except RuntimeError as error:
                    failures.append(str(error))
                    repo_summary["alerts"][name] = None
                    continue
                repo_summary["alerts"][name] = count
                if count != 0:
                    failures.append(f"{repo.repo}: {name} open alerts = {count}")

        summary[repo.repo] = repo_summary

    if args.json:
        print(json.dumps({"ok": not failures, "summary": summary, "failures": failures}, indent=2, ensure_ascii=False))
    else:
        for repo, data in summary.items():
            print(f"## {repo} ({data['branch']})")
            for workflow, run in data["workflows"].items():
                if run is None:
                    print(f"- {workflow}: MISSING")
                else:
                    print(f"- {workflow}: {run['status']}/{run['conclusion']} {run['sha']} {run['url']}")
            if data["alerts"]:
                print("- alerts: " + ", ".join(f"{name}={count}" for name, count in data["alerts"].items()))
            print()
        if failures:
            print("Failures:", file=sys.stderr)
            for failure in failures:
                print(f"- {failure}", file=sys.stderr)

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
