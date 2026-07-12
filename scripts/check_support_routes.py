#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import json
import subprocess
import sys
import time
from dataclasses import dataclass
from typing import Any

from github_cli import run_gh_json


@dataclass(frozen=True)
class FileExpectation:
    repo: str
    path: str
    required: tuple[str, ...]


PROOF_URL = "https://happysnaker.github.io/support/#proof-before-payment"
ASKS_URL = "https://happysnaker.github.io/support/#current-asks"
SUPPORT_ROUTER = "https://happysnaker.github.io/support/#sponsor-router"
SUPPORT_URL = "https://happysnaker.github.io/support/"
SPONSOR_RELEASE = "https://github.com/happysnaker/happysnaker/releases/tag/v2026.07-sponsor-one-pager"
FLAGSHIP_SNAPSHOT = "https://github.com/happysnaker/happysnaker/blob/master/docs/flagship-status-snapshot.md"
SHARE_KIT = "https://github.com/happysnaker/happysnaker/blob/master/docs/share-kit.md"
PROSPECT_PIPELINE = "https://github.com/happysnaker/happysnaker/blob/master/docs/sponsor-prospect-pipeline.md"
CONVERSION_SCORECARD = "https://github.com/happysnaker/happysnaker/blob/master/docs/sponsor-conversion-scorecard.md"
QQ_NOTE = "qq-ai-bot #26 arm64"
RD_NOTE = "RDLeader #27"
REVIEW_SAMPLE = "https://happysnaker.github.io/review/deploy-read-sample/"
INTAKE_REPLIES = "https://github.com/happysnaker/happysnaker/blob/master/docs/share-kit.md#sponsor--paid-support-intake-replies"
PUBLIC_PRIVACY_GUARDRAIL = "Do not paste private logs, credentials, QR codes, payment screenshots, internal URLs"
PRIVATE_PAYMENT_MARKER = "Payment%20screenshot%3A%20attach%20privately%20by%20email%20only%2C%20never%20in%20public%20issues"
BANNED_PUBLIC_PAYMENT_MARKERS = (
    "Payment%20screenshot%3A%20attached",
    "Payment screenshot: attached",
)

EXPECTATIONS: tuple[FileExpectation, ...] = (
    FileExpectation(
        "happysnaker/happysnaker",
        ".github/FUNDING.yml",
        (SUPPORT_URL, SUPPORT_ROUTER),
    ),
    FileExpectation(
        "happysnaker/happysnaker",
        "README.md",
        (PROOF_URL, SUPPORT_ROUTER, "docs/share-kit.md", REVIEW_SAMPLE, PRIVATE_PAYMENT_MARKER, "sponsor / paid-support intake replies", "10-second support router", "¥29.9", "¥99"),
    ),
    FileExpectation(
        "happysnaker/happysnaker",
        ".github/SUPPORT.md",
        (PROOF_URL, SUPPORT_ROUTER, ASKS_URL, SPONSOR_RELEASE, SHARE_KIT, PROSPECT_PIPELINE, CONVERSION_SCORECARD, INTAKE_REPLIES, REVIEW_SAMPLE, FLAGSHIP_SNAPSHOT, QQ_NOTE, RD_NOTE, "Quick read", "Async review", "Deploy read", PUBLIC_PRIVACY_GUARDRAIL, "Hot / Warm / Nurture / No-send"),
    ),
    FileExpectation(
        "happysnaker/happysnaker",
        ".github/ISSUE_TEMPLATE/config.yml",
        ("Proof before payment", PROOF_URL, "10-second support router", SUPPORT_ROUTER, "Current concrete asks", ASKS_URL, "Share kit", SHARE_KIT, "Sponsor prospect pipeline", PROSPECT_PIPELINE, "Sponsor conversion scorecard", CONVERSION_SCORECARD, "Hot / Warm / Nurture / No-send", "sponsor / paid-support intake replies", "privacy", "Technical proof index"),
    ),
    FileExpectation(
        "happysnaker/happysnaker",
        ".github/ISSUE_TEMPLATE/profile_operations.md",
        ("Proof before payment", PROOF_URL, "10-second support router", SUPPORT_ROUTER, "Current concrete asks", ASKS_URL, INTAKE_REPLIES, CONVERSION_SCORECARD, "Hot / Warm / Nurture / No-send", "python3 scripts/check_github_status.py", "Sponsor / support guardrails", "Do not ask for private logs, credentials, QR codes, internal URLs, or payment screenshots in public"),
    ),
    FileExpectation(
        "happysnaker/.github",
        ".github/FUNDING.yml",
        (SUPPORT_URL, SUPPORT_ROUTER),
    ),
    FileExpectation(
        "happysnaker/.github",
        "SUPPORT.md",
        (PROOF_URL, SUPPORT_ROUTER, ASKS_URL, SPONSOR_RELEASE, SHARE_KIT, PROSPECT_PIPELINE, CONVERSION_SCORECARD, INTAKE_REPLIES, REVIEW_SAMPLE, FLAGSHIP_SNAPSHOT, QQ_NOTE, RD_NOTE, "Quick read", "Async review", "Deploy read", PUBLIC_PRIVACY_GUARDRAIL, "Hot / Warm / Nurture / No-send"),
    ),
    FileExpectation(
        "happysnaker/.github",
        ".github/SUPPORT.md",
        (PROOF_URL, SUPPORT_ROUTER, ASKS_URL, SPONSOR_RELEASE, SHARE_KIT, PROSPECT_PIPELINE, CONVERSION_SCORECARD, INTAKE_REPLIES, REVIEW_SAMPLE, FLAGSHIP_SNAPSHOT, QQ_NOTE, RD_NOTE, "Quick read", "Async review", "Deploy read", PUBLIC_PRIVACY_GUARDRAIL, "Hot / Warm / Nurture / No-send"),
    ),
    FileExpectation(
        "happysnaker/.github",
        "CONTRIBUTING.md",
        (PROOF_URL, SUPPORT_ROUTER, ASKS_URL, SPONSOR_RELEASE, SHARE_KIT, PROSPECT_PIPELINE, CONVERSION_SCORECARD, INTAKE_REPLIES, REVIEW_SAMPLE, "qq-ai-bot", "RDLeader", "Hot / Warm / Nurture / No-send", "Do not send private logs, credentials, QR codes, payment screenshots, or internal URLs in public issues or PRs"),
    ),
    FileExpectation(
        "happysnaker/.github",
        ".github/ISSUE_TEMPLATE/config.yml",
        ("Proof before payment", PROOF_URL, "10-second support router", SUPPORT_ROUTER, "Current concrete asks", ASKS_URL, "Share kit", SHARE_KIT, "Sponsor prospect pipeline", PROSPECT_PIPELINE, "Sponsor conversion scorecard", CONVERSION_SCORECARD, "Hot / Warm / Nurture / No-send", "sponsor / paid-support intake replies", "privacy", REVIEW_SAMPLE, SUPPORT_URL),
    ),
    FileExpectation(
        "happysnaker/qq-ai-bot",
        ".github/FUNDING.yml",
        ("https://happysnaker.github.io/support/#from-qq-ai-bot",),
    ),
    FileExpectation(
        "happysnaker/qq-ai-bot",
        "README.md",
        (SUPPORT_ROUTER, "10-second support router", INTAKE_REPLIES, PROSPECT_PIPELINE, CONVERSION_SCORECARD, "Hot / Warm / Nurture / No-send", "private logs", "payment screenshots", "¥29.9", "¥99", QQ_NOTE),
    ),
    FileExpectation(
        "happysnaker/qq-ai-bot",
        "SUPPORT.md",
        (PROOF_URL, SUPPORT_ROUTER, ASKS_URL, SPONSOR_RELEASE, SHARE_KIT, PROSPECT_PIPELINE, CONVERSION_SCORECARD, INTAKE_REPLIES, REVIEW_SAMPLE, QQ_NOTE, "Latest CI", "Latest CodeQL", "Latest Docker publish", "Latest arm64 smoke", "¥29.9", "¥99", PUBLIC_PRIVACY_GUARDRAIL, "Hot / Warm / Nurture / No-send"),
    ),
    FileExpectation(
        "happysnaker/qq-ai-bot",
        ".github/SUPPORT.md",
        (PROOF_URL, SUPPORT_ROUTER, ASKS_URL, SPONSOR_RELEASE, SHARE_KIT, PROSPECT_PIPELINE, CONVERSION_SCORECARD, INTAKE_REPLIES, REVIEW_SAMPLE, FLAGSHIP_SNAPSHOT, "issues/26", "issues/28", "¥29.9", "¥99", PUBLIC_PRIVACY_GUARDRAIL, "Hot / Warm / Nurture / No-send"),
    ),
    FileExpectation(
        "happysnaker/qq-ai-bot",
        ".github/ISSUE_TEMPLATE/config.yml",
        ("Proof before payment", PROOF_URL, "10-second support router", SUPPORT_ROUTER, "Current concrete asks", ASKS_URL, "Share kit", SHARE_KIT, "Sponsor prospect pipeline", PROSPECT_PIPELINE, "Sponsor conversion scorecard", CONVERSION_SCORECARD, "Hot / Warm / Nurture / No-send", "sponsor / paid-support intake replies", "privacy", "arm64 / CasaOS install report"),
    ),
    FileExpectation(
        "happysnaker/RDLeader",
        ".github/FUNDING.yml",
        ("https://happysnaker.github.io/support/#from-rdleader",),
    ),
    FileExpectation(
        "happysnaker/RDLeader",
        "README.md",
        (SUPPORT_ROUTER, "10-second support router", INTAKE_REPLIES, PROSPECT_PIPELINE, CONVERSION_SCORECARD, "Hot / Warm / Nurture / No-send", PUBLIC_PRIVACY_GUARDRAIL, "Tip / Proof / Review / Fund", RD_NOTE, "RDLeader #1", "RDLeader #3", "reuse rights"),
    ),
    FileExpectation(
        "happysnaker/RDLeader",
        "SUPPORT.md",
        (PROOF_URL, SUPPORT_ROUTER, ASKS_URL, SPONSOR_RELEASE, SHARE_KIT, PROSPECT_PIPELINE, CONVERSION_SCORECARD, INTAKE_REPLIES, REVIEW_SAMPLE, RD_NOTE, "Security proof", "CI", "CodeQL", "License posture", "¥29.9", "¥99", PUBLIC_PRIVACY_GUARDRAIL, "Hot / Warm / Nurture / No-send"),
    ),
    FileExpectation(
        "happysnaker/RDLeader",
        ".github/SUPPORT.md",
        (PROOF_URL, SUPPORT_ROUTER, ASKS_URL, SPONSOR_RELEASE, SHARE_KIT, PROSPECT_PIPELINE, CONVERSION_SCORECARD, INTAKE_REPLIES, REVIEW_SAMPLE, FLAGSHIP_SNAPSHOT, "Latest CI proof", "Latest CodeQL proof", "License posture", "¥29.9", "¥99", PUBLIC_PRIVACY_GUARDRAIL, "Hot / Warm / Nurture / No-send"),
    ),
    FileExpectation(
        "happysnaker/RDLeader",
        ".github/ISSUE_TEMPLATE/config.yml",
        ("Proof before payment", PROOF_URL, "10-second support router", SUPPORT_ROUTER, "Current concrete asks", ASKS_URL, "Share kit", SHARE_KIT, "Sponsor prospect pipeline", PROSPECT_PIPELINE, "Sponsor conversion scorecard", CONVERSION_SCORECARD, "Hot / Warm / Nurture / No-send", "sponsor / paid-support intake replies", "privacy", "Security report"),
    ),
    FileExpectation(
        "happysnaker/Resume",
        ".github/FUNDING.yml",
        ("https://happysnaker.github.io/support/#from-resume", SUPPORT_ROUTER),
    ),
    FileExpectation(
        "happysnaker/Resume",
        "README.md",
        (PROOF_URL, SUPPORT_ROUTER, SPONSOR_RELEASE, INTAKE_REPLIES, PROSPECT_PIPELINE, REVIEW_SAMPLE, "Payment%20screenshot", "¥29.9", "¥99", "Resume", "private logs", "payment screenshots"),
    ),
    FileExpectation(
        "happysnaker/Resume",
        ".github/SUPPORT.md",
        (PROOF_URL, SUPPORT_ROUTER, SPONSOR_RELEASE, INTAKE_REPLIES, PROSPECT_PIPELINE, REVIEW_SAMPLE, "Best payment note", "Resume", "private logs", "payment screenshots", "internal URLs"),
    ),
    FileExpectation(
        "happysnaker/Resume",
        ".github/ISSUE_TEMPLATE/config.yml",
        ("Proof before payment", PROOF_URL, "10-second support router", SUPPORT_ROUTER, "Sponsor / paid-support intake replies", INTAKE_REPLIES, "Sponsor prospect pipeline", PROSPECT_PIPELINE, "privacy guardrails", "Support / direct feedback"),
    ),
    FileExpectation(
        "happysnaker/CSAPPLabsAndNotes",
        ".github/FUNDING.yml",
        ("https://happysnaker.github.io/support/#from-csapplabsandnotes", SUPPORT_ROUTER),
    ),
    FileExpectation(
        "happysnaker/CSAPPLabsAndNotes",
        "README.md",
        (PROOF_URL, SUPPORT_ROUTER, SPONSOR_RELEASE, INTAKE_REPLIES, PROSPECT_PIPELINE, REVIEW_SAMPLE, "Payment%20screenshot", "¥29.9", "¥99", "CSAPPLabsAndNotes", "private logs", "payment screenshots"),
    ),
    FileExpectation(
        "happysnaker/CSAPPLabsAndNotes",
        ".github/SUPPORT.md",
        (PROOF_URL, SUPPORT_ROUTER, SPONSOR_RELEASE, INTAKE_REPLIES, PROSPECT_PIPELINE, REVIEW_SAMPLE, "Best payment note", "CSAPPLabsAndNotes", "private logs", "payment screenshots", "internal URLs"),
    ),
    FileExpectation(
        "happysnaker/CSAPPLabsAndNotes",
        ".github/ISSUE_TEMPLATE/config.yml",
        ("Proof before payment", PROOF_URL, "10-second support router", SUPPORT_ROUTER, "Sponsor / paid-support intake replies", INTAKE_REPLIES, "Sponsor prospect pipeline", PROSPECT_PIPELINE, "privacy guardrails", "Support / direct feedback"),
    ),
    FileExpectation(
        "happysnaker/github-profile-checklist",
        ".github/FUNDING.yml",
        ("https://happysnaker.github.io/support/#from-github-profile-checklist", SUPPORT_ROUTER),
    ),
    FileExpectation(
        "happysnaker/github-profile-checklist",
        "README.md",
        (PROOF_URL, SUPPORT_ROUTER, SPONSOR_RELEASE, INTAKE_REPLIES, PROSPECT_PIPELINE, REVIEW_SAMPLE, "Payment%20screenshot", "¥29.9", "¥99", "github-profile-checklist", "private logs", "payment screenshots"),
    ),
    FileExpectation(
        "happysnaker/github-profile-checklist",
        ".github/SUPPORT.md",
        (PROOF_URL, SUPPORT_ROUTER, SPONSOR_RELEASE, INTAKE_REPLIES, PROSPECT_PIPELINE, REVIEW_SAMPLE, "Best payment note", "github-profile-checklist", "private logs", "payment screenshots", "internal URLs"),
    ),
    FileExpectation(
        "happysnaker/github-profile-checklist",
        ".github/ISSUE_TEMPLATE/config.yml",
        ("Proof before payment", PROOF_URL, "10-second support router", SUPPORT_ROUTER, "Sponsor / paid-support intake replies", INTAKE_REPLIES, "Sponsor prospect pipeline", PROSPECT_PIPELINE, "privacy guardrails", "Support / direct feedback"),
    ),
    FileExpectation(
        "happysnaker/backend-engineer-checklist",
        ".github/FUNDING.yml",
        ("https://happysnaker.github.io/support/#from-backend-engineer-checklist", SUPPORT_ROUTER),
    ),
    FileExpectation(
        "happysnaker/backend-engineer-checklist",
        "README.md",
        (PROOF_URL, SUPPORT_ROUTER, SPONSOR_RELEASE, INTAKE_REPLIES, PROSPECT_PIPELINE, REVIEW_SAMPLE, "Payment%20screenshot", "¥29.9", "¥99", "backend-engineer-checklist", "private logs", "payment screenshots"),
    ),
    FileExpectation(
        "happysnaker/backend-engineer-checklist",
        ".github/SUPPORT.md",
        (PROOF_URL, SUPPORT_ROUTER, SPONSOR_RELEASE, INTAKE_REPLIES, PROSPECT_PIPELINE, REVIEW_SAMPLE, "Low-friction thanks", "backend-engineer-checklist", "private logs", "payment screenshots", "internal URLs"),
    ),
    FileExpectation(
        "happysnaker/backend-engineer-checklist",
        ".github/ISSUE_TEMPLATE/config.yml",
        ("Proof before payment", PROOF_URL, "10-second support router", SUPPORT_ROUTER, "Sponsor / paid-support intake replies", INTAKE_REPLIES, "Sponsor prospect pipeline", PROSPECT_PIPELINE, "privacy guardrails", "Support / direct feedback"),
    ),
    FileExpectation(
        "happysnaker/system-design-checklist",
        ".github/FUNDING.yml",
        ("https://happysnaker.github.io/support/#from-system-design-checklist", SUPPORT_ROUTER),
    ),
    FileExpectation(
        "happysnaker/system-design-checklist",
        "README.md",
        (PROOF_URL, SUPPORT_ROUTER, SPONSOR_RELEASE, INTAKE_REPLIES, PROSPECT_PIPELINE, REVIEW_SAMPLE, "Payment%20screenshot", "¥29.9", "¥99", "system-design-checklist", "private logs", "payment screenshots"),
    ),
    FileExpectation(
        "happysnaker/system-design-checklist",
        ".github/SUPPORT.md",
        (PROOF_URL, SUPPORT_ROUTER, SPONSOR_RELEASE, INTAKE_REPLIES, PROSPECT_PIPELINE, REVIEW_SAMPLE, "Low-friction thanks", "system-design-checklist", "private logs", "payment screenshots", "internal URLs"),
    ),
    FileExpectation(
        "happysnaker/system-design-checklist",
        ".github/ISSUE_TEMPLATE/config.yml",
        ("Proof before payment", PROOF_URL, "10-second support router", SUPPORT_ROUTER, "Sponsor / paid-support intake replies", INTAKE_REPLIES, "Sponsor prospect pipeline", PROSPECT_PIPELINE, "privacy guardrails", "Support / direct feedback"),
    ),
    FileExpectation(
        "happysnaker/production-readiness-checklist",
        ".github/FUNDING.yml",
        ("https://happysnaker.github.io/support/#from-production-readiness-checklist", SUPPORT_ROUTER),
    ),
    FileExpectation(
        "happysnaker/production-readiness-checklist",
        "README.md",
        (PROOF_URL, SUPPORT_ROUTER, SPONSOR_RELEASE, INTAKE_REPLIES, PROSPECT_PIPELINE, REVIEW_SAMPLE, "Payment%20screenshot", "¥29.9", "¥99", "production-readiness-checklist", "private logs", "payment screenshots"),
    ),
    FileExpectation(
        "happysnaker/production-readiness-checklist",
        ".github/SUPPORT.md",
        (PROOF_URL, SUPPORT_ROUTER, SPONSOR_RELEASE, INTAKE_REPLIES, PROSPECT_PIPELINE, REVIEW_SAMPLE, "Low-friction thanks", "production-readiness-checklist", "private logs", "payment screenshots", "internal URLs"),
    ),
    FileExpectation(
        "happysnaker/production-readiness-checklist",
        ".github/ISSUE_TEMPLATE/config.yml",
        ("Proof before payment", PROOF_URL, "10-second support router", SUPPORT_ROUTER, "Sponsor / paid-support intake replies", INTAKE_REPLIES, "Sponsor prospect pipeline", PROSPECT_PIPELINE, "privacy guardrails", "Support / direct feedback"),
    ),
    FileExpectation(
        "happysnaker/happydb",
        ".github/FUNDING.yml",
        ("https://happysnaker.github.io/support/#from-happydb", SUPPORT_ROUTER),
    ),
    FileExpectation(
        "happysnaker/happydb",
        "README.md",
        (PROOF_URL, SUPPORT_ROUTER, SPONSOR_RELEASE, INTAKE_REPLIES, PROSPECT_PIPELINE, REVIEW_SAMPLE, "¥99", "happydb", "database internals", "private logs", "payment screenshots"),
    ),
    FileExpectation(
        "happysnaker/happydb",
        ".github/SUPPORT.md",
        (PROOF_URL, SUPPORT_ROUTER, SPONSOR_RELEASE, INTAKE_REPLIES, PROSPECT_PIPELINE, REVIEW_SAMPLE, "Best payment note", "happydb", "database internals", "private logs", "payment screenshots", "internal URLs"),
    ),
    FileExpectation(
        "happysnaker/happydb",
        ".github/ISSUE_TEMPLATE/config.yml",
        ("Proof before payment", PROOF_URL, "10-second support router", SUPPORT_ROUTER, "Sponsor / paid-support intake replies", INTAKE_REPLIES, "Sponsor prospect pipeline", PROSPECT_PIPELINE, "privacy guardrails", "Support / direct feedback"),
    ),
    FileExpectation(
        "happysnaker/go-service-starter",
        ".github/FUNDING.yml",
        ("https://happysnaker.github.io/support/#from-go-service-starter", SUPPORT_ROUTER),
    ),
    FileExpectation(
        "happysnaker/go-service-starter",
        "README.md",
        (PROOF_URL, SUPPORT_ROUTER, SPONSOR_RELEASE, INTAKE_REPLIES, PROSPECT_PIPELINE, REVIEW_SAMPLE, "¥99", "go-service-starter", "private logs", "payment screenshots"),
    ),
    FileExpectation(
        "happysnaker/go-service-starter",
        ".github/SUPPORT.md",
        (PROOF_URL, SUPPORT_ROUTER, SPONSOR_RELEASE, INTAKE_REPLIES, PROSPECT_PIPELINE, REVIEW_SAMPLE, "Low-friction thanks", "go-service-starter", "private logs", "payment screenshots", "internal URLs"),
    ),
    FileExpectation(
        "happysnaker/go-service-starter",
        ".github/ISSUE_TEMPLATE/config.yml",
        ("Proof before payment", PROOF_URL, "10-second support router", SUPPORT_ROUTER, "Sponsor / paid-support intake replies", INTAKE_REPLIES, "privacy guardrails", "Support / direct feedback"),
    ),
    FileExpectation(
        "happysnaker/go-http-middleware-kit",
        ".github/FUNDING.yml",
        ("https://happysnaker.github.io/support/#from-go-http-middleware-kit", SUPPORT_ROUTER),
    ),
    FileExpectation(
        "happysnaker/go-http-middleware-kit",
        "README.md",
        (PROOF_URL, SUPPORT_ROUTER, SPONSOR_RELEASE, INTAKE_REPLIES, PROSPECT_PIPELINE, REVIEW_SAMPLE, "¥99", "go-http-middleware-kit", "request-id middleware", "private logs", "payment screenshots"),
    ),
    FileExpectation(
        "happysnaker/go-http-middleware-kit",
        ".github/SUPPORT.md",
        (PROOF_URL, SUPPORT_ROUTER, SPONSOR_RELEASE, INTAKE_REPLIES, PROSPECT_PIPELINE, REVIEW_SAMPLE, "Low-friction thanks", "go-http-middleware-kit", "private logs", "payment screenshots", "internal URLs"),
    ),
    FileExpectation(
        "happysnaker/go-http-middleware-kit",
        ".github/ISSUE_TEMPLATE/config.yml",
        ("Proof before payment", PROOF_URL, "10-second support router", SUPPORT_ROUTER, "Sponsor / paid-support intake replies", INTAKE_REPLIES, "privacy guardrails", "Support / direct feedback"),
    ),
    FileExpectation(
        "happysnaker/chinese-independent-developer",
        ".github/FUNDING.yml",
        ("https://happysnaker.github.io/support/#from-indie-dev", SUPPORT_ROUTER),
    ),
    FileExpectation(
        "happysnaker/chinese-independent-developer",
        "README.md",
        (PROOF_URL, SUPPORT_ROUTER, PROSPECT_PIPELINE, INTAKE_REPLIES, REVIEW_SAMPLE, "happysnaker@foxmail.com", "indie", "payment screenshots", "public issue"),
    ),
    FileExpectation(
        "happysnaker/chinese-independent-developer",
        "SUPPORT.md",
        (PROOF_URL, SUPPORT_ROUTER, PROSPECT_PIPELINE, INTAKE_REPLIES, REVIEW_SAMPLE, "Best payment note", "indie", "payment screenshots", "internal URLs"),
    ),
    FileExpectation(
        "happysnaker/chinese-independent-developer",
        ".github/SUPPORT.md",
        (PROOF_URL, SUPPORT_ROUTER, PROSPECT_PIPELINE, INTAKE_REPLIES, REVIEW_SAMPLE, "payment screenshots", "internal URLs"),
    ),
    FileExpectation(
        "happysnaker/chinese-independent-developer",
        ".github/ISSUE_TEMPLATE/config.yml",
        ("Proof before payment", PROOF_URL, "10-second support router", SUPPORT_ROUTER, "Sponsor / paid-support intake replies", INTAKE_REPLIES, "Sponsor prospect pipeline", PROSPECT_PIPELINE, "Support this list"),
    ),
)



run_gh = run_gh_json

def fetch_file(repo: str, path: str) -> str:
    data = run_gh(["api", f"repos/{repo}/contents/{path}"])
    content = data.get("content")
    encoding = data.get("encoding")
    if not isinstance(content, str) or encoding != "base64":
        raise RuntimeError(f"{repo}:{path}: unexpected content response")
    return base64.b64decode(content).decode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify remote support/funding/issue-contact routes across profile and flagship repositories.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable support route summary.")
    args = parser.parse_args()

    failures: list[str] = []
    results: list[dict[str, object]] = []
    for expected in EXPECTATIONS:
        text = ""
        fetch_error: str | None = None
        try:
            text = fetch_file(expected.repo, expected.path)
        except RuntimeError as error:
            fetch_error = str(error)
            failures.append(fetch_error)
        missing = [needle for needle in expected.required if needle not in text] if not fetch_error else list(expected.required)
        if missing and not fetch_error:
            failures.append(f"{expected.repo}:{expected.path}: missing {missing}")
        banned_payment_markers = [marker for marker in BANNED_PUBLIC_PAYMENT_MARKERS if marker in text] if not fetch_error else []
        if banned_payment_markers:
            failures.append(f"{expected.repo}:{expected.path}: banned public payment-screenshot marker(s) {banned_payment_markers}")
        payment_marker_ok = not ("Payment%20screenshot" in text and PRIVATE_PAYMENT_MARKER not in text)
        if not fetch_error and not payment_marker_ok:
            failures.append(f"{expected.repo}:{expected.path}: Payment%20screenshot mailto field must use private email-only wording")
        result = {
            "repo": expected.repo,
            "path": expected.path,
            "requiredCount": len(expected.required),
            "missingRequiredText": missing,
            "bannedPaymentMarkers": banned_payment_markers,
            "privatePaymentMarkerOk": payment_marker_ok,
            "fetchError": fetch_error,
            "ok": not fetch_error and not missing and not banned_payment_markers and payment_marker_ok,
        }
        results.append(result)
        if not args.json:
            print(("OK" if result["ok"] else "FAIL") + f" {expected.repo}:{expected.path}")

    summary = {
        "ok": not failures,
        "fileCount": len(EXPECTATIONS),
        "checkedFileCount": len(results),
        "requiredCount": sum(len(expected.required) for expected in EXPECTATIONS),
        "files": results,
        "failures": failures,
    }
    if args.json:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
    if failures:
        if not args.json:
            print("\nSupport route check failures:", file=sys.stderr)
            for failure in failures:
                print(f"- {failure}", file=sys.stderr)
        return 1

    if not args.json:
        print(f"Checked {len(EXPECTATIONS)} support route files")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
