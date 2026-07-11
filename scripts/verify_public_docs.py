#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = [
    ROOT / "README.md",
    ROOT / ".github" / "SUPPORT.md",
    ROOT / ".github" / "ISSUE_TEMPLATE" / "profile_operations.md",
    *sorted((ROOT / "docs").glob("*.md")),
]

SENSITIVE_PATTERNS = [
    re.compile(pattern, re.IGNORECASE)
    for pattern in [
        r"\bcli_[a-z0-9]{8,}",
        r"\bou_[a-z0-9]{8,}",
        r"\boc_[a-z0-9]{8,}",
        r"\bom_[a-z0-9]{8,}",
        r"bytedance\.larkoffice\.com",
        r"\.uploads/",
        r"/Users/bytedance/",
        r"gho_[A-Za-z0-9_]+",
        r"\bsk-(?:proj|live|test|ant|org)-[A-Za-z0-9_-]{12,}",
    ]
]

REQUIRED = {
    "README.md": [
        "Current sponsorware board",
        "docs/sponsorware-board.md",
        "docs/technical-proof-index.md",
        "Sponsor one-pager",
        "docs/share-kit.md",
        "Proof before payment",
        "support/#proof-before-payment",
        "docs/flagship-technical-map.md",
        "docs/operator-handoff.md",
        "python3 scripts/run_profile_preflight.py --link-scope core --workers 8 --skip-external",
        "Profile CodeQL",
        "qq-ai-bot CodeQL",
        "RDLeader CodeQL",
        "actions/workflows/codeql.yml",
        "qq-ai-bot",
        "RDLeader",
    ],
    ".github/SUPPORT.md": [
        "Proof before payment",
        "Current concrete asks",
        "Sponsor one-pager",
        "qq-ai-bot #26 arm64",
        "RDLeader #27",
    ],
    ".github/ISSUE_TEMPLATE/profile_operations.md": [
        "Proof before payment",
        "Current concrete asks",
        "Flagship status snapshot",
        "python3 scripts/check_github_status.py",
        "Sponsor / support guardrails",
    ],
    "docs/sponsorware-board.md": [
        "Current targets",
        "qq-ai-bot #23",
        "RDLeader #2",
        "What sponsorship funds",
    ],
    "docs/share-kit.md": [
        "Core angle",
        "X / short post",
        "LinkedIn / longer post",
        "WeChat / private share",
        "Sponsorship CTA snippets",
        "qq-ai-bot #26 arm64",
        "RDLeader #27",
        "Guardrails",
    ],
    "docs/operator-handoff.md": [
        "Current source of truth",
        "python3 scripts/check_github_status.py",
        "Current flagship state",
        "Proof before payment",
        "qq-ai-bot #26 arm64",
        "RDLeader#3",
        "External follow-up rule",
        "--enforce-review-due",
        "2026-07-16 UTC",
        "Good next actions",
        "scripts/github_cli.py",
        "stable profile workflow links",
        "one-off profile self-check run links",
        "check_stable_profile_links.py",
        "check_gh_usage.py",
        "check_ci_workflow_contract.py",
        "check_checker_catalog.py",
        "happysnaker#2",
    ],
    "docs/manual-github-actions.md": [
        "Pin RDLeader on the profile",
        "replace `Resume` with `RDLeader`",
        "python3 scripts/check_profile_pins.py --strict",
        "Decide RDLeader license posture",
        "python3 scripts/check_rdleader_license.py",
        "Do not imply unrestricted reuse",
        "docs/share-kit.md",
        "scripts/check_issue_labels.py",
        "scripts/check_ops_issue_log.py",
        "happysnaker#2",
    ],
    "docs/technical-proof-index.md": [
        "Flagship proof: qq-ai-bot",
        "Flagship proof: RDLeader",
        "Maintenance proof",
        "Sponsorware / support proof",
        "actions/workflows/ci.yml",
        "actions/workflows/codeql.yml",
        "flagship status snapshot",
        "Stable profile proof-link checker",
        "rejects one-off profile self-check run links",
        "stable profile workflow links",
        "scripts/check_stable_profile_links.py",
        "python3 scripts/check_github_status.py",
        "Shared GitHub CLI helper",
        "GitHub CLI usage checker",
        "scripts/github_cli.py",
        "scripts/check_gh_usage.py",
        "scripts/check_ci_workflow_contract.py",
        "scripts/check_checker_catalog.py",
    ],
    "docs/flagship-technical-map.md": [
        "Fast read",
        "Systems boundary",
        "Operator proof",
        "Maintenance proof",
        "Current support note",
        "Proof before payment",
        "qq-ai-bot #26 arm64",
        "RDLeader #27",
        "Automation that keeps this map honest",
    ],
}

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def check_file(path: Path) -> None:
    if not path.exists():
        fail(f"missing file: {path.relative_to(ROOT)}")

    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT).as_posix()

    for line_no, line in enumerate(text.splitlines(), 1):
        if line.rstrip() != line:
            fail(f"{rel}:{line_no}: trailing whitespace")

    for pattern in SENSITIVE_PATTERNS:
        if pattern.search(text):
            fail(f"{rel}: sensitive-looking pattern matched: {pattern.pattern}")

    for needle in REQUIRED.get(rel, []):
        if needle not in text:
            fail(f"{rel}: missing required text: {needle}")

    for link in LINK_RE.findall(text):
        if link.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target_text = link.split("#", 1)[0]
        if not target_text:
            continue
        target = (path.parent / target_text).resolve()
        if not target.exists():
            fail(f"{rel}: broken local link: {link}")


def main() -> None:
    for path in DOCS:
        check_file(path)
    print(f"Verified {len(DOCS)} public markdown files")


if __name__ == "__main__":
    main()
