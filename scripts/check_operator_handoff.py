#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HANDOFF = ROOT / "docs" / "operator-handoff.md"

REQUIRED_TEXT = (
    "# Operator handoff",
    "Current source of truth",
    "python3 scripts/check_github_status.py --summary",
    "python3 scripts/run_profile_preflight.py --link-scope core --workers 8 --skip-external",
    "python3 scripts/run_profile_preflight.py --link-scope core --workers 8 --skip-external --json",
    "python3 scripts/check_manual_blockers.py --json",
    "python3 scripts/check_operator_handoff.py --json",
    "python3 scripts/check_stable_profile_links.py --json",
    "python3 scripts/check_gh_usage.py --json",
    "python3 scripts/check_ci_workflow_contract.py --json",
    "python3 scripts/check_checker_catalog.py --json",
    "python3 scripts/check_preflight_json_contract.py --json",
    "python3 scripts/check_sponsor_pipeline.py --json",
    "python3 scripts/check_external_followups.py --summary",
    "python3 scripts/check_external_followups.py --action-class optional-update --summary",
    "python3 scripts/check_external_followups.py --action-class optional-update --json",
    "python3 scripts/check_external_followups.py --action-class optional-update --candidate-comments --enforce-review-due",
    "python3 scripts/run_profile_preflight.py --external-only --action-class optional-update --external-candidate-comments --enforce-review-due",
    "--external-candidate-comments",
    "--candidate-comments",
    "materials",
    "candidateComment",
    "candidateGuardrails",
    "candidateGuardrails.ok",
    "postedFollowupUrl",
    "docker/awesome-compose#781",
    "AwesomeHomelab#98",
    "jbesomi/awesome-autonomous-agents#20",
    "The 2026-07-16 review posted only the RDLeader proof update",
    "Current flagship state",
    "qq-ai-bot #26 arm64",
    "RDLeader#3",
    "Proof before payment",
    "default funding links include both the root support page and the 10-second support router fallback",
    "Default support fallback: <https://github.com/happysnaker/.github/commit/0ec8ed7> / funding fallback: <https://github.com/happysnaker/.github/commit/47eaa73>",
    "10-second support router: <https://happysnaker.github.io/support/#sponsor-router>",
    "Share kit",
    "Sponsor prospect pipeline",
    "Deploy-read sample",
    "https://happysnaker.github.io/review/deploy-read-sample/",
    "Sponsor one-pager release",
    "Open blockers",
    "Manual checklist",
    "External follow-up rule",
    "2026-07-23 UTC",
    "--enforce-review-due",
    "Automation guardrails",
    "scripts/github_cli.py",
    "anything except `scripts/github_cli.py` is allowlisted",
    "scripts/check_review_funnel.py",
    "python3 scripts/check_review_funnel.py --site-root ../happysnaker.github.io --live --timeout 8 --json",
    "python3 scripts/check_sponsor_issues.py --json",
    "python3 scripts/check_sponsor_release.py --json",
    "python3 scripts/check_support_routes.py --json",
    "python3 scripts/check_repo_metadata.py --json",
    "python3 scripts/check_issue_labels.py --json",
    "python3 scripts/check_readme_badges.py --json",
    "python3 scripts/check_ops_issue_log.py --json",
    "python3 scripts/check_public_links.py --scope core --timeout 6 --workers 8 --json",
    "python3 scripts/check_site_hygiene.py --site-root ../happysnaker.github.io --timeout 8 --json",
    "audience segments, support notes, reply patterns, and no-overclaim guardrails",
    "stable profile workflow links",
    "one-off profile self-check run links",
    "verifies this forwarding contract",
    "Good next actions",
    "Avoid",
    "issue #2",
    "Deploy read",
)

BANNED_TEXT = (
    "happysnaker/happysnaker/actions/runs/",
    "physical ARM / CasaOS validation is complete",
    "RDLeader reuse rights are granted",
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify the operator handoff has current takeover commands, blockers, and guardrails.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable operator-handoff status.")
    args = parser.parse_args()

    failures: list[str] = []
    rel = HANDOFF.relative_to(ROOT).as_posix()
    exists = HANDOFF.exists()
    text = HANDOFF.read_text(encoding="utf-8") if exists else ""
    if not exists:
        failures.append(f"missing {rel}")

    trailing_whitespace = []
    for line_no, line in enumerate(text.splitlines(), 1):
        if line.rstrip() != line:
            trailing_whitespace.append(line_no)
    failures.extend(f"{rel}:{line_no}: trailing whitespace" for line_no in trailing_whitespace)

    missing_required = [needle for needle in REQUIRED_TEXT if needle not in text]
    banned_hits = [needle for needle in BANNED_TEXT if needle in text]
    if missing_required:
        failures.append(f"operator handoff missing required text: {missing_required}")
    if banned_hits:
        failures.append(f"operator handoff contains banned text: {banned_hits}")

    summary = {
        "ok": not failures,
        "path": rel,
        "exists": exists,
        "requiredCount": len(REQUIRED_TEXT),
        "missingRequiredText": missing_required,
        "bannedCount": len(BANNED_TEXT),
        "bannedTextHits": banned_hits,
        "trailingWhitespaceLines": trailing_whitespace,
        "failures": failures,
    }
    if args.json:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
    if failures:
        if not args.json:
            print("Operator handoff failures:", file=sys.stderr)
            for failure in failures:
                print(f"- {failure}", file=sys.stderr)
        return 1
    if not args.json:
        print(f"Checked operator handoff: {len(REQUIRED_TEXT)} required markers and {len(BANNED_TEXT)} banned claims")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
