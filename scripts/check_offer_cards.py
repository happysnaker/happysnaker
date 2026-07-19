#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SITE_ROOT = ROOT / "site" / "happysnaker.github.io"
FALLBACK_SITE_ROOT = ROOT.parent / "happysnaker.github.io"


@dataclass(frozen=True)
class OfferCard:
    name: str
    support_note: str
    proof_marker: str
    outcome_marker: str
    guardrail_marker: str


OFFER_CARDS = (
    OfferCard(
        name="Fund a real host report",
        support_note="qq-ai-bot #26 arm64",
        proof_marker="arm64-casaos-tester-pack.md",
        outcome_marker="one real physical ARM / CasaOS / NAS / SBC report added to the public tracker",
        guardrail_marker="Do not say physical ARM / CasaOS validation is complete",
    ),
    OfferCard(
        name="Fund curator follow-up",
        support_note="RDLeader #27",
        proof_marker="submission-tracker.md",
        outcome_marker="one scheduled-review update or maintainer reply follow-up",
        guardrail_marker="this is not a license grant",
    ),
    OfferCard(
        name="Buy a deploy read",
        support_note="Deploy read",
        proof_marker="review/deploy-read-sample",
        outcome_marker="top 3 fixes",
        guardrail_marker="keep payment evidence private by email",
    ),
    OfferCard(
        name="Tip with attribution",
        support_note="repo name",
        proof_marker="support/#sponsor-router",
        outcome_marker="maintenance credit can be summarized",
        guardrail_marker="generic fundraising spam",
    ),
)

REPO_REQUIREMENTS = {
    "README.md": (
        "Productized offer cards",
        "https://happysnaker.github.io/support/#offer-cards",
        "qq-ai-bot #26 arm64",
        "RDLeader #27",
        "Deploy read",
        "repo-name tip",
    ),
    "docs/share-kit.md": (
        "## Productized offer cards",
        "Each card keeps one proof link, one support note, and one guardrail visible",
        "Offer card — fund a public issue",
        "Offer card — buy a deploy read",
        "Offer card — proof-first tip",
    ),
    "docs/sponsor-one-pager.md": (
        "## Productized offer cards",
        "generic donation ask",
    ),
    "docs/sponsor-scorecard-coverage.md": (
        "keep productized offer cards tied to concrete public outcomes",
        "support page productized offer cards",
        "fund a real host report, fund curator follow-up, buy a deploy read, or tip with attribution",
    ),
}

SUPPORT_PAGE_REQUIREMENTS = (
    'id="offer-cards"',
    "Productized offer cards",
    "Specific notes convert better than a vague donation",
    "application/ld+json",
    "do not say physical ARM / CasaOS validation is complete",
    "RDLeader #27</code> is not a license grant",
    "keep payment evidence private by email",
)


def resolve_site_root(raw: str | None) -> Path:
    if raw:
        return Path(raw)
    if DEFAULT_SITE_ROOT.exists():
        return DEFAULT_SITE_ROOT
    return FALLBACK_SITE_ROOT


def missing_needles(text: str, needles: tuple[str, ...]) -> list[str]:
    return [needle for needle in needles if needle not in text]


def check_file(path: Path, needles: tuple[str, ...]) -> dict[str, object]:
    rel = path.relative_to(ROOT).as_posix() if path.is_relative_to(ROOT) else str(path)
    if not path.exists():
        return {
            "path": rel,
            "exists": False,
            "missingRequiredText": list(needles),
            "ok": False,
        }
    text = path.read_text(encoding="utf-8")
    missing = missing_needles(text, needles)
    return {
        "path": rel,
        "exists": True,
        "missingRequiredText": missing,
        "ok": not missing,
    }


def offer_needles() -> tuple[str, ...]:
    needles: list[str] = []
    for card in OFFER_CARDS:
        needles.extend(
            [
                card.name,
                card.support_note,
                card.proof_marker,
                card.outcome_marker,
                card.guardrail_marker,
            ]
        )
    return tuple(needles)


def support_page_offer_needles() -> tuple[str, ...]:
    needles: list[str] = []
    for card in OFFER_CARDS:
        proof_marker = "#donate-codes" if card.name == "Tip with attribution" else card.proof_marker
        needles.extend(
            [
                card.name,
                card.support_note,
                proof_marker,
                card.outcome_marker,
            ]
        )
    return tuple(needles)


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify productized offer cards stay consistent across profile surfaces.")
    parser.add_argument("--site-root", help="Local checkout of happysnaker.github.io. Defaults to CI checkout or sibling repo.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable offer-card summary.")
    args = parser.parse_args()

    site_root = resolve_site_root(args.site_root)
    support_page = site_root / "support" / "index.html"

    files: list[dict[str, object]] = []
    offer_card_needles = offer_needles()
    for rel, needles in REPO_REQUIREMENTS.items():
        required = (*needles, *offer_card_needles) if rel in {"docs/share-kit.md", "docs/sponsor-one-pager.md"} else needles
        files.append(check_file(ROOT / rel, required))

    support_needles = (*SUPPORT_PAGE_REQUIREMENTS, *support_page_offer_needles())
    support_result = check_file(support_page, support_needles)
    support_result["siteRoot"] = str(site_root)
    files.append(support_result)

    failures: list[str] = []
    for result in files:
        if not result["ok"]:
            failures.append(f"{result['path']}: missing {result['missingRequiredText']}")

    summary = {
        "ok": not failures,
        "offerCount": len(OFFER_CARDS),
        "offers": [card.name for card in OFFER_CARDS],
        "siteRoot": str(site_root),
        "checkedFileCount": len(files),
        "files": files,
        "failures": failures,
    }
    if args.json:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
    if failures:
        if not args.json:
            print("Offer card failures:", file=sys.stderr)
            for failure in failures:
                print(f"- {failure}", file=sys.stderr)
        return 1
    if not args.json:
        print(f"Checked {len(OFFER_CARDS)} productized offer cards across {len(files)} surfaces")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
