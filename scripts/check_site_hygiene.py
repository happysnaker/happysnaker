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

from github_cli import run_gh_json

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SITE_ROOT = ROOT.parent / "happysnaker.github.io"
BASE_URL = "https://happysnaker.github.io"

# Pages that are used as project/support/funnel surfaces and should share well.
METADATA_PAGES = [
    "support",
    "review",
    "review/deploy-read-sample",
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
    "csapp-labs-notes",
]

# Pages that should be discoverable from sitemap.xml.
SITEMAP_PAGES = [
    "",
    "support",
    "review",
    "review/deploy-read-sample",
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
    "csapp-labs-notes",
]

BLOCKED_PUBLIC_REPO_LINKS = {
    "Gobang",
    "HRpc",
    "JavaLearningNotes",
}

GITHUB_REPO_RE = re.compile(r"https://github\.com/happysnaker/([A-Za-z0-9_.-]+)")
SITE_ONE_OFF_RUN_RE = re.compile(r"https://github\.com/happysnaker/(?:happysnaker|qq-ai-bot|RDLeader|happysnaker\.github\.io)/actions/runs/\d+")
JSON_LD_RE = re.compile(r'<script\s+type=["\']application/ld\+json["\']\s*>(.*?)</script>', re.IGNORECASE | re.DOTALL)
SUPPORT_ANCHOR_RE = re.compile(r"/support/#(?P<anchor>from-[A-Za-z0-9_-]+)")
HTML_ID_RE = re.compile(r"id=[\"'](?P<id>[^\"']+)[\"']")

SUPPORT_CONTENT_NEEDLES = [
    "Proof before payment",
    "Pick the right support path in 10 seconds",
    "Specific notes convert better than a vague donation",
    "flagship-technical-map.md",
    "Open technical map",
    "Share kit",
    "share-kit.md",
    "Sponsor prospect pipeline",
    "sponsor-prospect-pipeline.md",
    "Route by audience",
    "homelab testers, bot builders, curators, sponsors, RDLeader evaluators, and paid-review customers",
    "Sponsor / paid-support intake replies",
    "#public-intake-guardrail",
    "Public privacy guardrail",
    "Do not paste private logs, credentials, QR codes, payment screenshots, internal URLs, or raw live integration output in public issues",
    "Payment%20screenshot%3A%20attach%20privately%20by%20email%20only%2C%20never%20in%20public%20issues",
    "Current concrete asks",
    "qq-ai-bot #26 arm64",
    "RDLeader #27",
    "support does not imply a reuse grant",
]

SUPPORT_INTAKE_PAGE_NEEDLES = [
    "/support/#sponsor-router",
    "Sponsor / paid-support intake replies",
    "Public intake guardrail",
    "private logs, credentials, QR codes, payment screenshots, internal URLs, or raw live integration output in public issues",
]

PROJECT_CONTENT_NEEDLES: dict[str, list[str]] = {
    "qq-ai-bot": [
        "/support/#sponsor-router",
        "Pick Tip / Proof / Review / Fund",
        "10-second support router",
        "qq-ai-bot #26 arm64",
        "Sponsor / paid-support intake replies",
        "Sponsor prospect pipeline",
        "sponsor-prospect-pipeline.md",
        "Route by audience",
        "right proof, CTA, support note, and guardrail",
        "Public intake guardrail",
        "payment screenshots out of public issues",
        "no private logs, credentials, QR codes, payment screenshots, internal URLs, or raw live integration output in public issues",
    ],
    "rdleader": [
        "/support/#sponsor-router",
        "Pick Tip / Proof / Review / Fund",
        "10-second support router",
        "Support does not imply reuse rights",
        "Sponsor / paid-support intake replies",
        "Sponsor prospect pipeline",
        "sponsor-prospect-pipeline.md",
        "Route by audience",
        "right proof, CTA, support note, and guardrail",
        "Public intake guardrail",
        "payment screenshots",
        "raw live integration output in public issues",
    ],
    "github-profile-checklist": SUPPORT_INTAKE_PAGE_NEEDLES,
    "backend-engineer-checklist": SUPPORT_INTAKE_PAGE_NEEDLES,
    "system-design-checklist": SUPPORT_INTAKE_PAGE_NEEDLES,
    "production-readiness-checklist": SUPPORT_INTAKE_PAGE_NEEDLES,
    "go-service-starter": SUPPORT_INTAKE_PAGE_NEEDLES,
    "go-http-middleware-kit": SUPPORT_INTAKE_PAGE_NEEDLES,
    "happydb": SUPPORT_INTAKE_PAGE_NEEDLES,
    "hrpc": SUPPORT_INTAKE_PAGE_NEEDLES,
    "csapp-labs-notes": SUPPORT_INTAKE_PAGE_NEEDLES,
}


@dataclass(frozen=True)
class Finding:
    ok: bool
    label: str
    detail: str


EMIT_TEXT = True


def emit(finding: Finding) -> None:
    if not EMIT_TEXT:
        return
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


def check_support_content(html: str, source_label: str, findings: list[Finding]) -> None:
    for needle in SUPPORT_CONTENT_NEEDLES:
        (ok if needle in html else fail)(f"{source_label} support content", needle, findings)


def check_project_content(html: str, slug: str, source_label: str, findings: list[Finding]) -> None:
    for needle in PROJECT_CONTENT_NEEDLES.get(slug, []):
        (ok if needle in html else fail)(f"{source_label} {slug} support router content", needle, findings)


def check_local_metadata(site_root: Path, base_url: str, findings: list[Finding]) -> None:
    for slug in METADATA_PAGES:
        path = page_path(site_root, slug)
        if not path.exists():
            fail(f"local {slug} exists", str(path), findings)
            continue
        html = path.read_text(encoding="utf-8", errors="ignore")
        check_metadata(html, slug, base_url, "local", findings)
        if slug == "support":
            check_support_content(html, "local", findings)
        check_project_content(html, slug, "local", findings)


def check_live_metadata(base_url: str, timeout: float, findings: list[Finding]) -> None:
    live_pages: list[tuple[str, str]] = []
    for slug in METADATA_PAGES:
        url = site_url(base_url, slug)
        status, html = fetch_url(url, timeout=timeout)
        if not (200 <= status < 400):
            fail(f"live {slug} HTTP", f"{url} returned {status}", findings)
            continue
        live_pages.append((url, html))
        ok(f"live {slug} HTTP", f"{url} returned {status}", findings)
        check_metadata(html, slug, base_url, "live", findings)
        if slug == "support":
            check_support_content(html, "live", findings)
        check_project_content(html, slug, "live", findings)
    check_stable_workflow_link_texts("live site stable workflow links", live_pages, findings)


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


def check_stable_workflow_link_texts(label: str, pages: Iterable[tuple[str, str]], findings: list[Finding]) -> None:
    hits: list[str] = []
    for source, text in pages:
        for match in SITE_ONE_OFF_RUN_RE.finditer(text):
            hits.append(f"{source}: {match.group(0)}")

    if hits:
        for hit in hits:
            fail(label, f"replace one-off Actions run URL with workflow/status link: {hit}", findings)
    else:
        ok(label, "no one-off happysnaker Actions run URLs on public Pages surfaces", findings)


def check_site_stable_workflow_links(site_root: Path, findings: list[Finding]) -> None:
    pages = [
        (path.relative_to(site_root).as_posix(), path.read_text(encoding="utf-8", errors="ignore"))
        for path in iter_scan_files([site_root])
    ]
    check_stable_workflow_link_texts("site stable workflow links", pages, findings)


def check_support_anchor_integrity(site_root: Path, findings: list[Finding]) -> None:
    support_page = page_path(site_root, "support")
    if not support_page.exists():
        fail("support anchor integrity", f"missing {support_page}", findings)
        return
    support_text = support_page.read_text(encoding="utf-8", errors="ignore")
    defined_ids = set(HTML_ID_RE.findall(support_text))
    refs: dict[str, set[str]] = {}
    for path in iter_scan_files([site_root]):
        rel = path.relative_to(site_root).as_posix()
        text = path.read_text(encoding="utf-8", errors="ignore")
        for match in SUPPORT_ANCHOR_RE.finditer(text):
            refs.setdefault(match.group("anchor"), set()).add(rel)

    missing = sorted(anchor for anchor in refs if anchor not in defined_ids)
    if missing:
        for anchor in missing:
            sources = ", ".join(sorted(refs[anchor])[:5])
            fail("support anchor integrity", f"/support/#{anchor} is referenced but not defined in support/index.html; sources: {sources}", findings)
    else:
        ok("support anchor integrity", f"{len(refs)} /support/#from-* anchors have matching support page sections", findings)


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
    try:
        data = run_gh_json(["repo", "view", f"happysnaker/{repo}", "--json", "isPrivate"])
    except RuntimeError:
        return "unknown"
    return str(bool(data.get("isPrivate"))).lower()


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
    parser.add_argument("--json", action="store_true", help="Emit machine-readable site hygiene status.")
    args = parser.parse_args()

    global EMIT_TEXT
    EMIT_TEXT = not args.json

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
        check_site_stable_workflow_links(site_root, findings)
        check_support_anchor_integrity(site_root, findings)

    check_public_repo_links(scan_roots, findings)

    if args.live:
        check_live_metadata(args.base_url, args.timeout, findings)

    failures = [finding for finding in findings if not finding.ok]
    summary = {
        "ok": not failures,
        "siteRoot": str(site_root),
        "baseUrl": args.base_url,
        "expectedLastmod": args.expected_lastmod,
        "live": args.live,
        "timeout": args.timeout,
        "scanRoots": [str(path) for path in scan_roots],
        "findingCount": len(findings),
        "failureCount": len(failures),
        "findings": [
            {
                "ok": finding.ok,
                "label": finding.label,
                "detail": finding.detail,
            }
            for finding in findings
        ],
        "failures": [
            {
                "label": finding.label,
                "detail": finding.detail,
            }
            for finding in failures
        ],
    }
    if args.json:
        print(json.dumps(summary, indent=2, ensure_ascii=False), flush=True)
    if failures:
        if not args.json:
            print(f"\n{len(failures)} site hygiene check(s) failed", file=sys.stderr)
        return 1
    if not args.json:
        print(f"\nChecked {len(findings)} site hygiene assertions", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
