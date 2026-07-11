#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from typing import Sequence

from github_cli import run_gh_json

SUPPORT_ROUTER = "https://happysnaker.github.io/support/#sponsor-router"


@dataclass(frozen=True)
class SponsorIssueSpec:
    repo: str
    number: int
    summary: str
    required: tuple[str, ...]
    banned: tuple[str, ...] = ()


SPECS: tuple[SponsorIssueSpec, ...] = (
    SponsorIssueSpec(
        repo="happysnaker/qq-ai-bot",
        number=28,
        summary="main qq-ai-bot sponsorship entrypoint",
        required=(
            "https://happysnaker.github.io/support/#from-qq-ai-bot",
            "https://happysnaker.github.io/support/#proof-before-payment",
            SUPPORT_ROUTER,
            "https://happysnaker.github.io/support/#current-asks",
            "qq-ai-bot #26 arm64",
            "https://github.com/happysnaker/qq-ai-bot/actions/workflows/ci.yml",
            "https://github.com/happysnaker/qq-ai-bot/actions/workflows/codeql.yml",
            "https://github.com/happysnaker/qq-ai-bot/actions/workflows/docker-publish.yml",
            "https://github.com/happysnaker/qq-ai-bot/actions/workflows/arm64-image-smoke.yml",
            "https://happysnaker.github.io/review/deploy-read-sample/",
            "https://happysnaker.github.io/support/#quick-read",
            "Deploy read",
            "Please redact QQ credentials",
            "¥29.9",
            "¥99",
        ),
        banned=(
            "https://github.com/happysnaker/qq-ai-bot/actions/runs/",
        ),
    ),
    SponsorIssueSpec(
        repo="happysnaker/qq-ai-bot",
        number=26,
        summary="arm64 / CasaOS validation funding target",
        required=(
            "real physical ARM / CasaOS / NAS / SBC install evidence",
            "https://github.com/happysnaker/qq-ai-bot/actions/workflows/ci.yml",
            "https://github.com/happysnaker/qq-ai-bot/actions/workflows/codeql.yml",
            "https://github.com/happysnaker/qq-ai-bot/actions/workflows/docker-publish.yml",
            "https://github.com/happysnaker/qq-ai-bot/actions/workflows/arm64-image-smoke.yml",
            "https://github.com/happysnaker/qq-ai-bot/blob/main/docs/public/arm64-casaos-tester-pack.md",
            "https://github.com/happysnaker/qq-ai-bot/discussions/43",
            "Best payment note: `qq-ai-bot #26 arm64`",
            "https://happysnaker.github.io/support/#from-qq-ai-bot",
            SUPPORT_ROUTER,
            "tokens / group IDs / user IDs removed",
        ),
        banned=(
            "https://github.com/happysnaker/qq-ai-bot/actions/runs/",
        ),
    ),
    SponsorIssueSpec(
        repo="happysnaker/RDLeader",
        number=27,
        summary="RDLeader external submission follow-up sponsor target",
        required=(
            "https://github.com/jbesomi/awesome-autonomous-agents/pull/20",
            "https://github.com/kailiu42/awesome-coding-agents/pull/13",
            "https://github.com/happysnaker/RDLeader/actions/workflows/ci.yml",
            "https://github.com/happysnaker/RDLeader/actions/workflows/codeql.yml",
            "https://github.com/happysnaker/happysnaker/releases/tag/v2026.07-sponsor-one-pager",
            "python3 scripts/check_external_followups.py --summary",
            "2026-07-16",
            "no private paths, IDs, QR artifacts, or raw integration output",
            "¥199",
            "https://happysnaker.github.io/support/#from-rdleader",
            SUPPORT_ROUTER,
            "Support does not imply RDLeader reuse rights",
        ),
        banned=(
            "https://github.com/happysnaker/RDLeader/actions/runs/",
        ),
    ),
    SponsorIssueSpec(
        repo="happysnaker/RDLeader",
        number=1,
        summary="RDLeader public release sponsorware roadmap",
        required=(
            "fake/demo identities",
            "sponsor-friendly roadmap table",
            "Public demo video / landing page",
            "Sanitized QA evidence bundle",
            "Employee-agent onboarding docs",
            "Runtime endurance deep dive",
            "Support page: https://happysnaker.github.io/support/",
            SUPPORT_ROUTER,
            "Support does not imply RDLeader reuse rights",
            "Decide whether this repo is ready for an explicit license",
        ),
    ),
    SponsorIssueSpec(
        repo="happysnaker/RDLeader",
        number=3,
        summary="RDLeader license guardrail",
        required=(
            "Do not add a root `LICENSE` automatically without owner decision.",
            "unrestricted reuse until the license is published.",
            "https://github.com/happysnaker/RDLeader/blob/main/docs/public/license-decision-packet.md",
            "https://happysnaker.github.io/support/#from-rdleader",
            SUPPORT_ROUTER,
            "Support does not imply RDLeader reuse rights",
            "GitHub metadata check",
        ),
    ),
)


def issue_id(spec: SponsorIssueSpec) -> str:
    return f"{spec.repo}#{spec.number}"


def check_issue(spec: SponsorIssueSpec, failures: list[str], results: list[dict[str, object]]) -> None:
    issue = run_gh_json(["issue", "view", str(spec.number), "-R", spec.repo, "--json", "number,title,state,url,body"])
    url = issue.get("url")
    body = issue.get("body") or ""
    missing = [needle for needle in spec.required if needle not in body]
    present_banned = [needle for needle in spec.banned if needle in body]
    issue_failures: list[str] = []
    if issue.get("state") != "OPEN":
        issue_failures.append(f"expected OPEN sponsor/support issue, got {issue.get('state')!r}")
    if missing:
        issue_failures.append(f"missing required sponsor/proof text {missing}")
    if present_banned:
        issue_failures.append(f"contains drift-prone one-off proof links {present_banned}; use stable workflow/status links")
    for failure in issue_failures:
        failures.append(f"{issue_id(spec)}: {spec.summary} {failure} ({url})")
    results.append({
        "id": issue_id(spec),
        "repo": spec.repo,
        "number": spec.number,
        "summary": spec.summary,
        "url": url,
        "state": issue.get("state"),
        "requiredCount": len(spec.required),
        "missingRequiredText": missing,
        "bannedPhraseHits": present_banned,
        "ok": not issue_failures,
    })


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Verify live sponsor/support issue bodies keep proof links, support routes, and guardrails.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable sponsor issue summary.")
    args = parser.parse_args(argv)

    failures: list[str] = []
    results: list[dict[str, object]] = []
    try:
        for spec in SPECS:
            check_issue(spec, failures, results)
    except RuntimeError as error:
        if args.json:
            print(json.dumps({"ok": False, "error": str(error), "issues": results, "failures": [str(error)]}, indent=2, ensure_ascii=False))
        else:
            print(f"ERROR: failed to check sponsor issues: {error}", file=sys.stderr)
        return 1

    summary = {
        "ok": not failures,
        "issueCount": len(SPECS),
        "checkedIssueCount": len(results),
        "requiredCount": sum(len(spec.required) for spec in SPECS),
        "issues": results,
        "failures": failures,
    }
    if args.json:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
    if failures:
        if not args.json:
            print("Sponsor issue check failures:", file=sys.stderr)
            for failure in failures:
                print(f"- {failure}", file=sys.stderr)
        return 1

    if not args.json:
        print(f"Checked {len(SPECS)} sponsor/support issue bodies for stable proof links, support routes, and guardrails")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
