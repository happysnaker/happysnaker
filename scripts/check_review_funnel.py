#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SITE_ROOT = ROOT.parent / "happysnaker.github.io"
BASE_URL = "https://happysnaker.github.io"


@dataclass(frozen=True)
class PageSpec:
    path: str
    purpose: str
    required: tuple[str, ...]


PAGE_SPECS: tuple[PageSpec, ...] = (
    PageSpec(
        path="support/index.html",
        purpose="main support and payment hub",
        required=(
            "#quick-read",
            "#async-review",
            "/review/deploy-read-sample/",
            "mailto:happysnaker@foxmail.com?subject=Quick%20read",
            "mailto:happysnaker@foxmail.com?subject=Async%20review",
            "Payment%20screenshot",
            "Proof before payment",
            "¥29.9",
            "¥99",
        ),
    ),
    PageSpec(
        path="review/index.html",
        purpose="paid review landing page",
        required=(
            "/support/#quick-read",
            "/support/#async-review",
            "/review/deploy-read-sample/",
            "mailto:happysnaker@foxmail.com?subject=Quick%20read",
            "mailto:happysnaker@foxmail.com?subject=Deploy%20read",
            "mailto:happysnaker@foxmail.com?subject=Async%20review",
            "Payment%20screenshot",
            "¥29.9",
            "¥99",
        ),
    ),
    PageSpec(
        path="review/deploy-read-sample/index.html",
        purpose="deploy-read sample and conversion preview",
        required=(
            "https://happysnaker.github.io/review/deploy-read-sample/",
            "application/ld+json",
            "Deploy Read Sample",
            "mailto:happysnaker@foxmail.com?subject=Deploy%20read",
            "mailto:happysnaker@foxmail.com?subject=Async%20review",
            "Payment%20screenshot",
            "top 3 fixes",
            "¥29.9",
            "¥99",
            "/support/#from-qq-ai-bot",
        ),
    ),
    PageSpec(
        path="qq-ai-bot/index.html",
        purpose="flagship inbound page for bot/agent repo review",
        required=(
            "/review/deploy-read-sample/",
            "mailto:happysnaker@foxmail.com?subject=Deploy%20read",
            "mailto:happysnaker@foxmail.com?subject=Quick%20read",
            "mailto:happysnaker@foxmail.com?subject=Async%20review",
            "Payment%20screenshot",
            "/support/#quick-read",
            "/support/#async-review",
            "¥29.9 deploy read",
            "¥99 async review",
        ),
    ),
)

SITEMAP_NEEDLE = "https://happysnaker.github.io/review/deploy-read-sample/"


def read_local(site_root: Path, rel: str) -> str:
    path = site_root / rel
    if not path.exists():
        raise FileNotFoundError(path)
    return path.read_text(encoding="utf-8", errors="ignore")


def fetch_live(url: str, timeout: float) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "happysnaker-review-funnel/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            if not (200 <= response.status < 400):
                raise RuntimeError(f"{url} returned HTTP {response.status}")
            return response.read().decode("utf-8", errors="ignore")
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"{url} returned HTTP {exc.code}") from exc


def page_url(base_url: str, rel: str) -> str:
    slug = rel.removesuffix("index.html").strip("/")
    return f"{base_url.rstrip('/')}/{slug}/" if slug else f"{base_url.rstrip('/')}/"


def check_text(label: str, text: str, required: tuple[str, ...], failures: list[str]) -> None:
    missing = [needle for needle in required if needle not in text]
    if missing:
        failures.append(f"{label}: missing {missing}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify the paid review / deploy-read conversion funnel on the public Pages site.")
    parser.add_argument("--site-root", type=Path, default=DEFAULT_SITE_ROOT, help="Local happysnaker.github.io checkout. Default: sibling repo.")
    parser.add_argument("--base-url", default=BASE_URL, help="Public Pages base URL.")
    parser.add_argument("--live", action="store_true", help="Also fetch live pages and verify the same conversion markers.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable review-funnel summary.")
    parser.add_argument("--timeout", type=float, default=8.0, help="Live fetch timeout in seconds.")
    args = parser.parse_args()

    site_root = args.site_root.resolve()
    failures: list[str] = []
    checked = 0

    if not site_root.exists():
        print(f"ERROR: site root missing: {site_root}", file=sys.stderr)
        return 1

    for spec in PAGE_SPECS:
        try:
            text = read_local(site_root, spec.path)
        except FileNotFoundError as exc:
            failures.append(f"local {spec.path}: missing file {exc.filename}")
            continue
        check_text(f"local {spec.path} ({spec.purpose})", text, spec.required, failures)
        checked += 1

        if args.live:
            url = page_url(args.base_url, spec.path)
            try:
                live_text = fetch_live(url, args.timeout)
            except RuntimeError as exc:
                failures.append(f"live {spec.path}: {exc}")
            else:
                check_text(f"live {spec.path} ({spec.purpose})", live_text, spec.required, failures)
                checked += 1

    sitemap = site_root / "sitemap.xml"
    if not sitemap.exists():
        failures.append(f"local sitemap.xml: missing {sitemap}")
    else:
        sitemap_text = sitemap.read_text(encoding="utf-8", errors="ignore")
        check_text("local sitemap.xml", sitemap_text, (SITEMAP_NEEDLE,), failures)
        checked += 1

    if args.live:
        try:
            live_sitemap = fetch_live(f"{args.base_url.rstrip('/')}/sitemap.xml", args.timeout)
        except RuntimeError as exc:
            failures.append(f"live sitemap.xml: {exc}")
        else:
            check_text("live sitemap.xml", live_sitemap, (SITEMAP_NEEDLE,), failures)
            checked += 1

    scope = "local+live" if args.live else "local"
    summary = {
        "ok": not failures,
        "scope": scope,
        "siteRoot": str(site_root),
        "baseUrl": args.base_url,
        "live": args.live,
        "checkedSurfaces": checked,
        "pageCount": len(PAGE_SPECS),
        "requiredMarkers": sum(len(spec.required) for spec in PAGE_SPECS) + 1,
        "failures": failures,
    }
    if args.json:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
    if failures:
        if not args.json:
            print("Review funnel check failures:", file=sys.stderr)
            for failure in failures:
                print(f"- {failure}", file=sys.stderr)
        return 1

    if not args.json:
        print(f"Checked {checked} {scope} paid review funnel surfaces")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
