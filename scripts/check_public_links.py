#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
CORE_FILES = [
    ROOT / "docs" / "sponsor-one-pager.md",
    ROOT / "docs" / "support-surface-coverage.md",
    ROOT / "docs" / "flagship-status-snapshot.md",
]
PROFILE_FILES = [
    ROOT / "README.md",
    ROOT / "docs" / "technical-proof-index.md",
    ROOT / "docs" / "flagship-status-snapshot.md",
    ROOT / "docs" / "upstream-contribution-ledger.md",
    ROOT / "docs" / "sponsor-one-pager.md",
    ROOT / "docs" / "support-surface-coverage.md",
    ROOT / "docs" / "sponsorware-board.md",
    ROOT / "docs" / "portfolio-audit.md",
    ROOT / "docs" / "operations-cadence.md",
]

MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
AUTO_LINK_RE = re.compile(r"<(?P<url>https://[^>]+)>")
RAW_URL_RE = re.compile(r"(?<!\()https://[^\s)<>\]`]+")


@dataclass(frozen=True)
class Link:
    url: str
    source: Path


def iter_markdown_files(scope: str) -> list[Path]:
    if scope == "all":
        files = [ROOT / "README.md", *sorted((ROOT / "docs").glob("*.md"))]
    elif scope == "profile":
        files = PROFILE_FILES
    else:
        files = CORE_FILES
    return [path for path in files if path.exists()]


def clean_url(raw: str) -> str:
    return raw.strip().rstrip(".,;:")


def extract_links(path: Path) -> Iterable[Link]:
    text = path.read_text(encoding="utf-8")
    seen: set[str] = set()
    for pattern in (MARKDOWN_LINK_RE, AUTO_LINK_RE, RAW_URL_RE):
        for match in pattern.finditer(text):
            raw = match.group("url") if "url" in match.groupdict() else match.group(1 if pattern is MARKDOWN_LINK_RE else 0)
            url = clean_url(raw)
            if not url.startswith("https://"):
                continue
            if url in seen:
                continue
            seen.add(url)
            yield Link(url=url, source=path)


def should_skip(url: str) -> bool:
    # Dynamic GitHub search/badge pages are useful docs links but unstable as
    # proof assets. Keep this checker focused on shareable proof/support URLs.
    unstable_fragments = [
        "/issues?q=",
        "/pulls?q=",
        "/issues/new?",
        "/stargazers",
        "img.shields.io/",
        "/badge.svg",
    ]
    return any(fragment in url for fragment in unstable_fragments)


def run_curl(url: str, timeout: float, head: bool) -> tuple[bool, str]:
    command = [
        "curl",
        "--location",
        "--silent",
        "--show-error",
        "--output",
        "/dev/null",
        "--write-out",
        "%{http_code}",
        "--max-time",
        str(timeout),
        "--user-agent",
        "happysnaker-link-check/1.0",
    ]
    if head:
        command.append("--head")
    command.append(url)
    try:
        completed = subprocess.run(command, check=False, capture_output=True, text=True, timeout=timeout + 2)
    except subprocess.TimeoutExpired:
        return False, "curl timeout"

    status_text = completed.stdout.strip()[-3:]
    try:
        status = int(status_text)
    except ValueError:
        status = 0
    if 200 <= status < 400:
        return True, f"{'HEAD' if head else 'GET'} {status}"
    detail = completed.stderr.strip().split("\n")[-1] if completed.stderr.strip() else f"HTTP {status or 'unknown'}"
    return False, f"{'HEAD' if head else 'GET'} {detail}"


def fetch_status(url: str, timeout: float) -> tuple[bool, str]:
    ok, detail = run_curl(url, timeout=timeout, head=True)
    if ok:
        return ok, detail
    # Some GitHub/Pages endpoints reject HEAD but work with GET.
    return run_curl(url, timeout=timeout, head=False)


def main() -> int:
    parser = argparse.ArgumentParser(description="Check public proof/support links in profile docs.")
    parser.add_argument("--scope", choices=("core", "profile", "all"), default="core", help="Files to scan. Default: core sponsor/support docs.")
    parser.add_argument("--timeout", type=float, default=8.0, help="Per-request timeout in seconds.")
    args = parser.parse_args()

    files = iter_markdown_files(args.scope)
    links_by_url: dict[str, list[Path]] = {}
    for path in files:
        for link in extract_links(path):
            if should_skip(link.url):
                continue
            links_by_url.setdefault(link.url, []).append(link.source)

    failures: list[tuple[str, str, list[Path]]] = []
    for url, sources in sorted(links_by_url.items()):
        ok, detail = fetch_status(url, timeout=args.timeout)
        rel_sources = ", ".join(sorted({source.relative_to(ROOT).as_posix() for source in sources}))
        print(f"{'OK' if ok else 'FAIL'} {detail} {url} [{rel_sources}]", flush=True)
        if not ok:
            failures.append((url, detail, sources))

    if failures:
        print("\nBroken public links:", file=sys.stderr)
        for url, detail, sources in failures:
            rel_sources = ", ".join(sorted({source.relative_to(ROOT).as_posix() for source in sources}))
            print(f"- {url} ({detail}) in {rel_sources}", file=sys.stderr)
        return 1

    print(f"Checked {len(links_by_url)} public links from {len(files)} files", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
