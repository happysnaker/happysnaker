#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class Step:
    name: str
    command: tuple[str, ...]


@dataclass(frozen=True)
class StepResult:
    name: str
    command: tuple[str, ...]
    returncode: int
    stdout: str | None = None
    stderr: str | None = None

    @property
    def ok(self) -> bool:
        return self.returncode == 0


def run_step(step: Step, *, capture: bool = False) -> StepResult:
    if capture:
        completed = subprocess.run(step.command, check=False, capture_output=True, text=True)
        return StepResult(
            name=step.name,
            command=step.command,
            returncode=completed.returncode,
            stdout=completed.stdout,
            stderr=completed.stderr,
        )

    print(f"\n## {step.name}", flush=True)
    print("$ " + " ".join(step.command), flush=True)
    completed = subprocess.run(step.command, check=False)
    if completed.returncode != 0:
        print(f"FAILED {step.name}: exit {completed.returncode}", file=sys.stderr, flush=True)
    return StepResult(name=step.name, command=step.command, returncode=completed.returncode)


def maybe_json(command: Sequence[str], args: argparse.Namespace) -> tuple[str, ...]:
    if args.json:
        return (*command, "--json")
    return tuple(command)


def external_step(args: argparse.Namespace) -> Step:
    external_command = ["python3", "scripts/check_external_followups.py"]
    for action_class in args.action_class or []:
        external_command.extend(["--action-class", action_class])
    if args.external_candidate_comments:
        external_command.append("--candidate-comments")
    if args.external_summary:
        external_command.append("--summary")
    if args.today:
        external_command.extend(["--today", args.today])
    if args.review_date:
        external_command.extend(["--review-date", args.review_date])
    if args.enforce_review_due:
        external_command.append("--enforce-review-due")
    return Step("Summarize external follow-ups", maybe_json(external_command, args))


def build_steps(args: argparse.Namespace) -> list[Step]:
    if args.external_only:
        return [external_step(args)]

    steps = [
        Step("Verify public docs", ("python3", "scripts/verify_public_docs.py", "--json")),
        Step("Check operator handoff", maybe_json(("python3", "scripts/check_operator_handoff.py"), args)),
        Step("Check stable profile proof links", maybe_json(("python3", "scripts/check_stable_profile_links.py"), args)),
        Step("Check GitHub CLI helper usage", maybe_json(("python3", "scripts/check_gh_usage.py"), args)),
        Step("Check CI workflow contract", maybe_json(("python3", "scripts/check_ci_workflow_contract.py"), args)),
        Step("Check checker catalog", ("python3", "scripts/check_checker_catalog.py", "--json")),
        Step("Check share kit", maybe_json(("python3", "scripts/check_share_kit.py"), args)),
        Step("Check sponsor prospect pipeline", maybe_json(("python3", "scripts/check_sponsor_pipeline.py"), args)),
        Step("Check sponsor conversion scorecard", maybe_json(("python3", "scripts/check_sponsor_conversion_scorecard.py"), args)),
        Step("Check sponsor scorecard coverage", maybe_json(("python3", "scripts/check_sponsor_scorecard_coverage.py"), args)),
        Step("Check README workflow badges", maybe_json(("python3", "scripts/check_readme_badges.py"), args)),
        Step("Check GitHub workflow / alert status", maybe_json(("python3", "scripts/check_github_status.py"), args)),
        Step("Check support routes", maybe_json(("python3", "scripts/check_support_routes.py"), args)),
        Step("Check repository metadata", maybe_json(("python3", "scripts/check_repo_metadata.py"), args)),
        Step("Check sponsor release", maybe_json(("python3", "scripts/check_sponsor_release.py"), args)),
        Step("Check sponsor issues", maybe_json(("python3", "scripts/check_sponsor_issues.py"), args)),
        Step("Check review funnel", maybe_json(("python3", "scripts/check_review_funnel.py"), args)),
        Step("Check operations log", maybe_json(("python3", "scripts/check_ops_issue_log.py"), args)),
        Step("Check issue labels", maybe_json(("python3", "scripts/check_issue_labels.py"), args)),
        Step("Report manual blockers", maybe_json(("python3", "scripts/check_manual_blockers.py"), args)),
        Step(
            f"Check public links ({args.link_scope})",
            maybe_json(
                (
                    "python3",
                    "scripts/check_public_links.py",
                    "--timeout",
                    str(args.timeout),
                    "--workers",
                    str(args.workers),
                    "--scope",
                    args.link_scope,
                ),
                args,
            ),
        ),
    ]
    if not args.skip_external:
        steps.append(external_step(args))
    if args.snapshot_as_of:
        steps.append(
            Step(
                "Generate flagship status snapshot",
                (
                    "python3",
                    "scripts/check_github_status.py",
                    "--markdown",
                    "--as-of",
                    args.snapshot_as_of,
                ),
            )
        )
    return steps


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run the happysnaker profile proof/support preflight checks.")
    parser.add_argument("--link-scope", choices=("core", "profile", "all"), default="core", help="Public-link scope to check. Default: core.")
    parser.add_argument("--workers", type=int, default=8, help="Concurrent link checker workers. Default: 8.")
    parser.add_argument("--timeout", type=float, default=6.0, help="Per-link timeout in seconds. Default: 6.")
    parser.add_argument("--skip-external", action="store_true", help="Skip dynamic external PR/issue summary.")
    parser.add_argument("--external-only", action="store_true", help="Run only the dynamic external PR/issue summary, preserving action-class filters.")
    parser.add_argument("--external-summary", action="store_true", help="Use compact summary output for the dynamic external PR/issue step.")
    parser.add_argument("--external-candidate-comments", action="store_true", help="Render prepared external follow-up candidate comments without posting them.")
    parser.add_argument("--today", help="Forward YYYY-MM-DD date to external follow-up review gate.")
    parser.add_argument("--review-date", help="Forward YYYY-MM-DD next scheduled review date to external follow-up checker.")
    parser.add_argument("--enforce-review-due", action="store_true", help="Make the external follow-up step fail before the scheduled review date.")
    parser.add_argument(
        "--action-class",
        action="append",
        choices=("optional-update", "stay-quiet", "recheck-only", "no-action", "keep-open"),
        help="Filter external follow-up rows by action class. Can be repeated.",
    )
    parser.add_argument("--snapshot-as-of", help="If set, emit a markdown status snapshot with this label at the end.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable preflight step status.")
    args = parser.parse_args(argv)

    if args.workers < 1:
        parser.error("--workers must be >= 1")
    if args.external_only and args.skip_external:
        parser.error("--external-only cannot be combined with --skip-external")

    results: list[StepResult] = []
    for step in build_steps(args):
        results.append(run_step(step, capture=args.json))

    failures = [result for result in results if not result.ok]
    if args.json:
        print(
            json.dumps(
                {
                    "ok": not failures,
                    "stepCount": len(results),
                    "failureCount": len(failures),
                    "steps": [
                        {
                            "name": result.name,
                            "command": list(result.command),
                            "returncode": result.returncode,
                            "ok": result.ok,
                            "stdout": result.stdout,
                            "stderr": result.stderr,
                        }
                        for result in results
                    ],
                    "failures": [
                        {
                            "name": result.name,
                            "command": list(result.command),
                            "returncode": result.returncode,
                        }
                        for result in failures
                    ],
                },
                indent=2,
                ensure_ascii=False,
            ),
            flush=True,
        )
    if failures:
        if not args.json:
            print("\nPreflight failures:", file=sys.stderr)
            for result in failures:
                print(f"- {result.name}: exit {result.returncode}", file=sys.stderr)
        if args.external_only and len(failures) == 1:
            return failures[0].returncode
        return 1

    if not args.json:
        print("\nPreflight passed", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
