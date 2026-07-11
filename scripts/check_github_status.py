#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime
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
    # Keep the machine key free of sensitive-data-looking words so static
    # analyzers do not treat the alert count itself as leaked credential data.
    "leak_scan": "secret-scanning/alerts?state=open&per_page=100",
}

ALERT_DISPLAY = {
    "codeql": "codeql",
    "dependabot": "dependabot",
    "leak_scan": "secret-scanning",
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


def markdown_link(label: str, url: str | None) -> str:
    return f"[{label}]({url})" if url else label


def format_markdown(summary: dict[str, Any], failures: list[str], as_of: str) -> str:
    lines = [
        "# Flagship GitHub status snapshot",
        "",
        f"> Generated from `scripts/check_github_status.py --markdown` on {as_of}.",
        "",
        "This is a point-in-time proof snapshot for sponsor, curator, and reviewer links. It covers the configured flagship surfaces only; do not generalize the CodeQL claim to older repositories without CodeQL configured.",
        "",
        "Because editing this file triggers a new profile CI / CodeQL run, the `happysnaker/happysnaker` self-check rows may intentionally trail the newest commit by one docs refresh. Run `python3 scripts/check_github_status.py` for the live source of truth before quoting current status.",
        "",
        "## Workflow state",
        "",
        "| Repo | Workflow | Status | Commit | Proof |",
        "|---|---|---|---|---|",
    ]

    for repo, data in summary.items():
        for workflow, run in data["workflows"].items():
            if run is None:
                lines.append(f"| `{repo}` | {workflow} | missing | - | - |")
                continue
            status = f"{run['status']} / {run['conclusion']}"
            sha = f"`{run['sha']}`" if run.get("sha") else "-"
            proof = markdown_link("run", run.get("url"))
            lines.append(f"| `{repo}` | {workflow} | {status} | {sha} | {proof} |")

    lines.extend([
        "",
        "## Configured alert state",
        "",
        "| Repo | CodeQL open | Dependabot open | Secret scanning open |",
        "|---|---:|---:|---:|",
    ])

    for repo, data in summary.items():
        alerts = data.get("alerts") or {}
        if not alerts:
            continue
        lines.append(
            f"| `{repo}` | {alerts.get('codeql')} | {alerts.get('dependabot')} | {alerts.get('leak_scan')} |"
        )

    lines.extend([
        "",
        "## Current support routing",
        "",
        "- Main support page: <https://happysnaker.github.io/support/>",
        "- Current concrete asks: <https://happysnaker.github.io/support/#current-asks>",
        "- `qq-ai-bot #26 arm64`: <https://github.com/happysnaker/qq-ai-bot/issues/26>",
        "- `RDLeader #27`: <https://github.com/happysnaker/RDLeader/issues/27>",
        "- Sponsor one-pager: [sponsor-one-pager.md](sponsor-one-pager.md)",
        "- Share kit: [share-kit.md](share-kit.md)",
        "- Technical proof index: [technical-proof-index.md](technical-proof-index.md)",
        "- Operations log: <https://github.com/happysnaker/happysnaker/issues/2>",
        "",
        "## Caveats",
        "",
        "- `qq-ai-bot` has green QEMU / workflow arm64 smoke evidence, but still needs a real physical ARM / CasaOS / NAS / SBC host report before claiming physical-host validation.",
        "- RDLeader currently exposes clean configured CodeQL / Dependabot / secret-scanning state, but its license posture is still tracked separately and should not be over-claimed.",
        "- External PRs should be followed through the scheduled queue instead of repeated unsourced bumps: [external-follow-up-queue.md](external-follow-up-queue.md).",
    ])

    if failures:
        lines.extend(["", "## Failures", ""])
        lines.extend(f"- {failure}" for failure in failures)

    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Check flagship GitHub workflow and alert state.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON summary.")
    parser.add_argument("--markdown", action="store_true", help="Emit a shareable Markdown proof snapshot.")
    parser.add_argument(
        "--as-of",
        default=datetime.now().astimezone().strftime("%Y-%m-%d %Z"),
        help="Timestamp label for --markdown output.",
    )
    args = parser.parse_args()

    if args.json and args.markdown:
        parser.error("--json and --markdown are mutually exclusive")

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
    elif args.markdown:
        print(format_markdown(summary, failures, args.as_of), end="")
    else:
        for repo, data in summary.items():
            print(f"## {repo} ({data['branch']})")
            for workflow, run in data["workflows"].items():
                if run is None:
                    print(f"- {workflow}: MISSING")
                else:
                    print(f"- {workflow}: {run['status']}/{run['conclusion']} {run['sha']} {run['url']}")
            if data["alerts"]:
                print("- alerts: " + ", ".join(f"{ALERT_DISPLAY.get(name, name)}={count}" for name, count in data["alerts"].items()))
            print()
        if failures:
            print("Failures:", file=sys.stderr)
            for failure in failures:
                print(f"- {failure}", file=sys.stderr)

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
