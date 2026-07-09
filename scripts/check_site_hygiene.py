#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SITE_ROOT = ROOT.parent / "happysnaker.github.io"
BASE_URL = "https://happysnaker.github.io"

# Pages that are used as project/support/funnel surfaces and should share well.
METADATA_PAGES = [
    "support",
    "review",
    "qq-ai-bot",
    "rdleader",
    "github-profile-checklist",
    "backend-engineer-checklist",
    "system-design-checklist",
    "production-readiness-checklist",
    "go-service-starter",
    "go-http-middleware-kit",
    "happydb",
    "hrpc",
]

# Pages that should be discoverable from sitemap.xml.
SITEMAP_PAGES = [
    "",
    "support",
    "review",
    "qq-ai-bot",
    "rdleader",
    "github-profile-checklist",
    "backend-engineer-checklist",
    "system-design-checklist",
    "production-readiness-checklist",
    "go-service-starter",
    "go-http-middleware-kit",
    "happydb",
    "hrpc",
]

BLOCKED_PUBLIC_REPO_LINKS = {
    "Gobang",
    "HRpc",
    "JavaLearningNotes",
}

GITHUB_REPO_RE = re.compile(r"https://github\.com/happysnaker/([A-Za-z0-9_.-]+)")
JSON_LD_RE = re.compile(r'<script\s+type=["\']application/ld\+json["\']\s*>(.*?)</script>', re.IGNORECASE | re.DOTALL)


@dataclass(frozen=True)
class Finding:
    ok: bool
    label: str
    detail: str


def emit(finding: Finding) -> None:
    status = "OK" if finding.ok else "FAIL"
    print(f"{status} {finding.label}: {finding.detail}", flush=True)


def fail(label: str, detail: str, findings: list[Finding]) -> None:
    finding = Finding(False, label, detail)
    findings.append(finding)
    emit(finding)


def ok(label: str, detail: str, findings: list[Finding]) -> None:
    finding = Finding(True, label, detail)
    findings.append(finding)
    emit(finding)


def site_url(base_url: str, slug: str) -> str:
    return f"{base_url.rstrip('/')}/{slug.strip('/')}/" if slug else f"{base_url.rstrip('/')}/"


def page_path(site_root: Path, slug: str) -> Path:
    return site_root / "index.html" if not slug else site_root / slug / "index.html"


def read_local_page(site_root: Path, slug: str) -> str:
    path = page_path(site_root, slug)
    return path.read_text(encoding="utf-8", errors="ignore")


def fetch_url(url: str, timeout: float) -> tuple[int, str]:
    request = urllib.request.Request(url, headers={"User-Agent": "happysnaker-site-hygiene/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            data = response.read().decode("utf-8", errors="ignore")
            return response.status, data
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", errors="ignore")


def check_metadata(html: str, slug: str, base_url: str, source_label: str, findings: list[Finding]) -> None:
    expected_url = site_url(base_url, slug)
    checks = {
        "canonical": f'rel="canonical" href="{expected_url}"' in html or f"rel='canonical' href='{expected_url}'" in html,
        "og:image": 'property="og:image"' in html or "property='og:image'" in html,
        "twitter:card": 'name="twitter:card"' in html or "name='twitter:card'" in html,
    }
    for name, passed in checks.items():
        (ok if passed else fail)(f"{source_label} {slug or 'home'} {name}", expected_url, findings)

    blocks = JSON_LD_RE.findall(html)
    if not blocks:
        fail(f"{source_label} {slug or 'home'} JSON-LD", "missing application/ld+json block", findings)
        return
    for index, block in enumerate(blocks, 1):
        try:
            json.loads(block.strip())
        except json.JSONDecodeError as exc:
            fail(f"{source_label} {slug or 'home'} JSON-LD #{index}", str(exc), findings)
        else:
            ok(f"{source_label} {slug or 'home'} JSON-LD #{index}", "valid JSON", findings)


def check_local_metadata(site_root: Path, base_url: str, findings: list[Finding]) -> None:
    for slug in METADATA_PAGES:
        path = page_path(site_root, slug)
        if not path.exists():
            fail(f"local {slug} exists", str(path), findings)
            continue
        html = path.read_text(encoding="utf-8", errors="ignore")
        check_metadata(html, slug, base_url, "local", findings)


def check_live_metadata(base_url: str, timeout: float, findings: list[Finding]) -> None:
    for slug in METADATA_PAGES:
        url = site_url(base_url, slug)
        status, html = fetch_url(url, timeout=timeout)
        if not (200 <= status < 400):
            fail(f"live {slug} HTTP", f"{url} returned {status}", findings)
            continue
        ok(f"live {slug} HTTP", f"{url} returned {status}", findings)
        check_metadata(html, slug, base_url, "live", findings)


def check_sitemap(site_root: Path, base_url: str, expected_lastmod: str | None, findings: list[Finding]) -> None:
    sitemap = site_root / "sitemap.xml"
    robots = site_root / "robots.txt"
    if not sitemap.exists():
        fail("sitemap exists", str(sitemap), findings)
        return
    if not robots.exists():
        fail("robots exists", str(robots), findings)
    else:
        robots_text = robots.read_text(encoding="utf-8", errors="ignore")
        sitemap_url = f"Sitemap: {base_url.rstrip('/')}/sitemap.xml"
        (ok if sitemap_url in robots_text else fail)("robots sitemap", sitemap_url, findings)

    try:
        tree = ET.parse(sitemap)
    except ET.ParseError as exc:
        fail("sitemap XML", str(exc), findings)
        return
    ok("sitemap XML", "parsed successfully", findings)

    root = tree.getroot()
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    entries: dict[str, str | None] = {}
    for url_node in root.findall("sm:url", ns):
        loc = url_node.find("sm:loc", ns)
        lastmod = url_node.find("sm:lastmod", ns)
        if loc is not None and loc.text:
            entries[loc.text] = lastmod.text if lastmod is not None else None

    for slug in SITEMAP_PAGES:
        url = site_url(base_url, slug)
        if url not in entries:
            fail("sitemap entry", url, findings)
            continue
        ok("sitemap entry", url, findings)
        if expected_lastmod and slug:
            actual = entries[url]
            (ok if actual == expected_lastmod else fail)("sitemap lastmod", f"{url} -> {actual} (expected {expected_lastmod})", findings)


def iter_scan_files(paths: Iterable[Path]) -> Iterable[Path]:
    suffixes = {".html", ".md", ".yml", ".yaml", ".json", ".txt", ".xml"}
    for root in paths:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if ".git" in path.parts or not path.is_file():
                continue
            if path.suffix.lower() in suffixes:
                yield path


def repo_visibility(repo: str) -> str:
    completed = subprocess.run(
        ["gh", "repo", "view", f"happysnaker/{repo}", "--json", "isPrivate", "--jq", ".isPrivate"],
        check=False,
        capture_output=True,
        text=True,
    )
    if completed.returncode != 0:
        return "unknown"
    return completed.stdout.strip()


def check_public_repo_links(scan_roots: list[Path], findings: list[Finding]) -> None:
    links: dict[str, set[Path]] = {}
    blocked_hits: list[tuple[str, Path]] = []
    for path in iter_scan_files(scan_roots):
        text = path.read_text(encoding="utf-8", errors="ignore")
        for match in GITHUB_REPO_RE.finditer(text):
            repo = match.group(1)
            links.setdefault(repo, set()).add(path)
            if repo in BLOCKED_PUBLIC_REPO_LINKS:
                blocked_hits.append((repo, path))

    if blocked_hits:
        for repo, path in blocked_hits:
            fail("blocked public repo link", f"{repo} in {path}", findings)
    else:
        ok("blocked public repo link", "no legacy private/unavailable repository URLs found", findings)

    for repo in sorted(links):
        visibility = repo_visibility(repo)
        if visibility == "false":
            ok("happysnaker repo visibility", f"{repo} is public", findings)
        else:
            locations = ", ".join(sorted(str(path) for path in links[repo])[:5])
            fail("happysnaker repo visibility", f"{repo} is {visibility}; locations: {locations}", findings)


def main() -> int:
    parser = argparse.ArgumentParser(description="Check public site/share/support hygiene for the happysnaker profile hub.")
    parser.add_argument("--site-root", type=Path, default=DEFAULT_SITE_ROOT, help="Local happysnaker.github.io checkout. Default: sibling repo.")
    parser.add_argument("--base-url", default=BASE_URL, help="Public Pages base URL.")
    parser.add_argument("--expected-lastmod", help="If set, require sitemap lastmod for project pages to match this date, e.g. 2026-07-09.")
    parser.add_argument("--live", action="store_true", help="Fetch live project pages and verify status/metadata.")
    parser.add_argument("--timeout", type=float, default=8.0, help="Live fetch timeout in seconds.")
    parser.add_argument("--scan-root", action="append", type=Path, help="Additional root to scan for happysnaker GitHub repo links. Can be repeated.")
    args = parser.parse_args()

    site_root = args.site_root.resolve()
    scan_roots = [ROOT, site_root]
    if args.scan_root:
        scan_roots.extend(path.resolve() for path in args.scan_root)

    findings: list[Finding] = []
    if not site_root.exists():
        fail("site root", f"missing {site_root}", findings)
    else:
        ok("site root", str(site_root), findings)
        check_local_metadata(site_root, args.base_url, findings)
        check_sitemap(site_root, args.base_url, args.expected_lastmod, findings)

    check_public_repo_links(scan_roots, findings)

    if args.live:
        check_live_metadata(args.base_url, args.timeout, findings)

    failures = [finding for finding in findings if not finding.ok]
    if failures:
        print(f"\n{len(failures)} site hygiene check(s) failed", file=sys.stderr)
        return 1
    print(f"\nChecked {len(findings)} site hygiene assertions", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
