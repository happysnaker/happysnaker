#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path
from types import SimpleNamespace
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PREFLIGHT = ROOT / "scripts" / "run_profile_preflight.py"

CORE_JSON_SCRIPTS = (
    "scripts/check_operator_handoff.py",
    "scripts/check_stable_profile_links.py",
    "scripts/check_gh_usage.py",
    "scripts/check_ci_workflow_contract.py",
    "scripts/check_checker_catalog.py",
    "scripts/check_preflight_json_contract.py",
    "scripts/check_share_kit.py",
    "scripts/check_sponsor_pipeline.py",
    "scripts/check_sponsor_conversion_scorecard.py",
    "scripts/check_sponsor_scorecard_coverage.py",
    "scripts/check_readme_badges.py",
    "scripts/check_github_status.py",
    "scripts/check_support_routes.py",
    "scripts/check_repo_metadata.py",
    "scripts/check_sponsor_release.py",
    "scripts/check_sponsor_issues.py",
    "scripts/check_review_funnel.py",
    "scripts/check_ops_issue_log.py",
    "scripts/check_issue_labels.py",
    "scripts/check_manual_blockers.py",
    "scripts/check_public_links.py",
)

ALWAYS_JSON_SCRIPTS = (
    "scripts/verify_public_docs.py",
    "scripts/check_checker_catalog.py",
)


def load_preflight_module() -> Any:
    spec = importlib.util.spec_from_file_location("run_profile_preflight_contract_target", PREFLIGHT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {PREFLIGHT.relative_to(ROOT)}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def args_for(**overrides: Any) -> SimpleNamespace:
    values = {
        "external_only": False,
        "skip_external": True,
        "json": True,
        "link_scope": "core",
        "workers": 8,
        "timeout": 6.0,
        "external_summary": False,
        "external_candidate_comments": False,
        "today": None,
        "review_date": None,
        "enforce_review_due": False,
        "action_class": None,
        "snapshot_as_of": None,
    }
    values.update(overrides)
    return SimpleNamespace(**values)


def command_by_script(steps: list[Any]) -> dict[str, tuple[str, ...]]:
    commands: dict[str, tuple[str, ...]] = {}
    for step in steps:
        command = tuple(step.command)
        if len(command) < 2:
            continue
        commands[command[1]] = command
    return commands


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify profile preflight --json forwards JSON mode into checker substeps.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable preflight JSON contract status.")
    args = parser.parse_args()

    failures: list[str] = []
    module = load_preflight_module()

    core_steps = module.build_steps(args_for())
    core_commands = command_by_script(core_steps)

    missing_core_steps = [script for script in CORE_JSON_SCRIPTS if script not in core_commands]
    missing_json_forwarding = [
        script
        for script in CORE_JSON_SCRIPTS
        if script in core_commands and "--json" not in core_commands[script]
    ]

    non_json_core_steps = module.build_steps(args_for(json=False))
    non_json_commands = command_by_script(non_json_core_steps)
    unexpected_non_json_flags = [
        script
        for script, command in non_json_commands.items()
        if "--json" in command and script not in ALWAYS_JSON_SCRIPTS
    ]

    external_steps = module.build_steps(
        args_for(
            external_only=True,
            skip_external=False,
            external_summary=True,
            action_class=["optional-update"],
        )
    )
    external_command = tuple(external_steps[0].command) if external_steps else ()
    external_requirements = (
        "scripts/check_external_followups.py",
        "--action-class",
        "optional-update",
        "--summary",
        "--json",
    )
    missing_external_requirements = [item for item in external_requirements if item not in external_command]

    if missing_core_steps:
        failures.append(f"core preflight missing expected checker steps: {missing_core_steps}")
    if missing_json_forwarding:
        failures.append(f"core preflight JSON mode does not forward --json to: {missing_json_forwarding}")
    if unexpected_non_json_flags:
        failures.append(f"non-JSON preflight unexpectedly forwards --json to: {unexpected_non_json_flags}")
    if missing_external_requirements:
        failures.append(f"external-only JSON command missing required args: {missing_external_requirements}")

    summary = {
        "ok": not failures,
        "preflight": PREFLIGHT.relative_to(ROOT).as_posix(),
        "coreStepCount": len(core_steps),
        "requiredJsonForwardCount": len(CORE_JSON_SCRIPTS),
        "missingCoreSteps": missing_core_steps,
        "missingJsonForwarding": missing_json_forwarding,
        "unexpectedNonJsonFlags": unexpected_non_json_flags,
        "externalCommand": list(external_command),
        "missingExternalRequirements": missing_external_requirements,
        "failures": failures,
    }
    if args.json:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
    if failures:
        if not args.json:
            print("Preflight JSON contract failures:", file=sys.stderr)
            for failure in failures:
                print(f"- {failure}", file=sys.stderr)
        return 1
    if not args.json:
        print(
            "Checked preflight JSON contract: "
            f"{len(CORE_JSON_SCRIPTS)} checker steps forward --json and external-only JSON remains parseable"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
