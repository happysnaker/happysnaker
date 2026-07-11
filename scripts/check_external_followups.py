#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from collections import Counter
from dataclasses import dataclass
from datetime import date
from typing import Any

from github_cli import run_gh_json


@dataclass(frozen=True)
class PullRequestTarget:
    repo: str
    number: int
    project: str
    note: str
    action_class: str
    next_action: str


@dataclass(frozen=True)
class IssueTarget:
    repo: str
    number: int
    project: str
    note: str
    action_class: str
    next_action: str


PRS: tuple[PullRequestTarget, ...] = (
    PullRequestTarget("docker/awesome-compose", 781, "qq-ai-bot", "Docker Compose sample", "optional-update", "On scheduled review: one short update only if still review-required and no maintainer reply; if used, include project-page/support-router proof and avoid physical ARM completion claims. Otherwise stay quiet."),
    PullRequestTarget("Cp0204/CasaOS-AppStore-Play", 42, "qq-ai-bot", "CasaOS app-store PR", "stay-quiet", "Do not bump unless a real physical CasaOS/ARM report lands or maintainer asks."),
    PullRequestTarget("getumbrel/umbrel-apps", 5834, "qq-ai-bot", "Umbrel app PR", "recheck-only", "Recheck lint/mergeability; do not comment unless maintainer asks or checks regress."),
    PullRequestTarget("AwesomeHomelab/awesome-homelab", 98, "qq-ai-bot", "homelab listing PR", "optional-update", "On scheduled review: one short homelab-focused update may be useful after tester pack/project page/support-router render; avoid physical ARM completion claims."),
    PullRequestTarget("LLOneBot/LuckyLilliaDoc", 20, "qq-ai-bot", "LLOneBot docs PR", "stay-quiet", "Stay quiet unless maintainer replies."),
    PullRequestTarget("LLOneBot/llonebot.nix", 22, "qq-ai-bot", "LLOneBot Nix example PR", "stay-quiet", "Stay quiet unless maintainer replies or checks change."),
    PullRequestTarget("jbesomi/awesome-autonomous-agents", 20, "RDLeader", "autonomous-agents listing PR", "optional-update", "On scheduled review: use security-proof/project-page/support-router snippet only once if still open/no feedback; keep RDLeader license caveat explicit."),
    PullRequestTarget("kailiu42/awesome-coding-agents", 13, "RDLeader", "coding-agents listing PR", "no-action", "No action; keep as proof surface only."),
)

NEXT_REVIEW_DATE = date(2026, 7, 16)


ISSUES: tuple[IssueTarget, ...] = (
    IssueTarget("happysnaker/qq-ai-bot", 26, "qq-ai-bot", "physical ARM / CasaOS validation target", "keep-open", "Check for new real physical-host reports; keep open and avoid completion claims if none."),
    IssueTarget("happysnaker/RDLeader", 27, "RDLeader", "external submission review follow-up", "recheck-only", "Update only when external PR feedback or scheduled recheck finds meaningful state change."),
)


def parse_iso_date(value: str, label: str) -> date:
    try:
        return date.fromisoformat(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError(f"{label} must be YYYY-MM-DD, got {value!r}") from error


def review_gate(today: date, review_date: date) -> dict[str, Any]:
    days_until = (review_date - today).days
    due = days_until <= 0
    return {
        "today": today.isoformat(),
        "nextReviewDate": review_date.isoformat(),
        "due": due,
        "daysUntil": max(days_until, 0),
        "defaultAction": "scheduled review is due; still avoid comments unless the row guidance allows it" if due else "not due; stay quiet unless a maintainer/tester has replied or new material evidence lands",
    }



run_gh = run_gh_json

def summarize_checks(items: list[dict[str, Any]]) -> str:
    checks: list[str] = []
    for item in items:
        name = item.get("name") or item.get("context") or "check"
        conclusion = item.get("conclusion") or item.get("state") or item.get("status") or "unknown"
        status = item.get("status") or ""
        checks.append(f"{name}:{status}/{conclusion}" if status else f"{name}:{conclusion}")
    return "; ".join(checks) if checks else "none"


def pr_summary(target: PullRequestTarget) -> dict[str, Any]:
    data = run_gh([
        "pr",
        "view",
        str(target.number),
        "-R",
        target.repo,
        "--json",
        "number,title,state,mergeable,updatedAt,url,reviewDecision,statusCheckRollup",
    ])
    return {
        "kind": "pr",
        "project": target.project,
        "repo": target.repo,
        "number": data.get("number"),
        "title": data.get("title"),
        "state": data.get("state"),
        "mergeable": data.get("mergeable"),
        "reviewDecision": data.get("reviewDecision") or "",
        "updatedAt": data.get("updatedAt"),
        "url": data.get("url"),
        "checks": summarize_checks(data.get("statusCheckRollup") or []),
        "note": target.note,
        "actionClass": target.action_class,
        "nextAction": target.next_action,
    }


def issue_summary(target: IssueTarget) -> dict[str, Any]:
    data = run_gh([
        "issue",
        "view",
        str(target.number),
        "-R",
        target.repo,
        "--json",
        "number,title,state,updatedAt,url,comments",
    ])
    comments = data.get("comments") or []
    return {
        "kind": "issue",
        "project": target.project,
        "repo": target.repo,
        "number": data.get("number"),
        "title": data.get("title"),
        "state": data.get("state"),
        "mergeable": "",
        "reviewDecision": "",
        "updatedAt": data.get("updatedAt"),
        "url": data.get("url"),
        "checks": f"comments={len(comments)}",
        "note": target.note,
        "actionClass": target.action_class,
        "nextAction": target.next_action,
    }


def format_markdown(rows: list[dict[str, Any]]) -> str:
    lines = [
        "| Kind | Project | Surface | State | Mergeable | Review | Updated | Checks / comments | Action class | Note | Next action |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for row in rows:
        surface = f"[{row['repo']}#{row['number']}]({row['url']})"
        lines.append(
            "| {kind} | {project} | {surface} | {state} | {mergeable} | {review} | {updated} | {checks} | {action_class} | {note} | {next_action} |".format(
                kind=row["kind"],
                project=row["project"],
                surface=surface,
                state=row.get("state") or "",
                mergeable=row.get("mergeable") or "",
                review=row.get("reviewDecision") or "",
                updated=row.get("updatedAt") or "",
                checks=(row.get("checks") or "").replace("|", "/"),
                action_class=row.get("actionClass") or "",
                note=(row.get("note") or "").replace("|", "/"),
                next_action=(row.get("nextAction") or "").replace("|", "/"),
            )
        )
    return "\n".join(lines)


def format_review_gate(gate: dict[str, Any]) -> list[str]:
    due_text = "due" if gate["due"] else f"not due for {gate['daysUntil']} day(s)"
    return [
        "## Review gate",
        "",
        f"Today: {gate['today']}",
        f"Next scheduled review: {gate['nextReviewDate']} ({due_text})",
        f"Default action: {gate['defaultAction']}",
    ]


def format_summary(rows: list[dict[str, Any]], gate: dict[str, Any] | None = None) -> str:
    counts = Counter(row.get("actionClass") or "unknown" for row in rows)
    lines = []
    if gate is not None:
        lines.extend(format_review_gate(gate))
        lines.append("")
    lines.extend(["## External follow-up summary", ""])
    lines.append("Action classes: " + ", ".join(f"{key}={counts[key]}" for key in sorted(counts)))
    optional = [row for row in rows if row.get("actionClass") == "optional-update"]
    if optional:
        lines.extend(["", "Optional-update surfaces:"])
        for row in optional:
            lines.append(f"- {row['repo']}#{row['number']} — {row.get('nextAction')}")
    else:
        lines.extend(["", "Optional-update surfaces: none"])
    blockers = [row for row in rows if row.get("actionClass") in {"keep-open", "stay-quiet"}]
    if blockers:
        lines.extend(["", "Default quiet / keep-open surfaces:"])
        for row in blockers:
            lines.append(f"- {row['repo']}#{row['number']} ({row.get('actionClass')}) — {row.get('nextAction')}")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize tracked external follow-up PRs and issues.")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of markdown.")
    parser.add_argument("--summary", action="store_true", help="Emit a compact action-class summary instead of the full markdown table.")
    parser.add_argument("--today", type=lambda value: parse_iso_date(value, "--today"), default=date.today(), help="Date used for scheduled-review gating, in YYYY-MM-DD. Default: today.")
    parser.add_argument("--review-date", type=lambda value: parse_iso_date(value, "--review-date"), default=NEXT_REVIEW_DATE, help="Next scheduled review date in YYYY-MM-DD. Default: 2026-07-16.")
    parser.add_argument("--enforce-review-due", action="store_true", help="Exit non-zero before --review-date to prevent premature external follow-up.")
    parser.add_argument(
        "--action-class",
        action="append",
        choices=("optional-update", "stay-quiet", "recheck-only", "no-action", "keep-open"),
        help="Filter rows by action class. Can be repeated.",
    )
    args = parser.parse_args()

    failures: list[str] = []
    rows: list[dict[str, Any]] = []
    for target in PRS:
        try:
            rows.append(pr_summary(target))
        except RuntimeError as error:
            failures.append(f"{target.repo}#{target.number}: {error}")
    for target in ISSUES:
        try:
            rows.append(issue_summary(target))
        except RuntimeError as error:
            failures.append(f"{target.repo}#{target.number}: {error}")

    if args.action_class:
        allowed = set(args.action_class)
        rows = [row for row in rows if row.get("actionClass") in allowed]

    gate = review_gate(args.today, args.review_date)

    if args.json:
        print(json.dumps({"rows": rows, "failures": failures, "reviewGate": gate}, indent=2, ensure_ascii=False))
    elif args.summary:
        print(format_summary(rows, gate=gate))
    else:
        print(format_markdown(rows))

    if failures:
        print("\nExternal follow-up check failures:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    print(f"Checked {len(rows)} external follow-up surfaces", file=sys.stderr)
    if args.enforce_review_due and not gate["due"]:
        print(f"Scheduled external review is not due until {gate['nextReviewDate']} (today={gate['today']})", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
