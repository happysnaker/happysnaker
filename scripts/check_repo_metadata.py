#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
import time
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class RepoMetadataExpectation:
    repo: str
    homepage: str
    description_terms: tuple[str, ...]
    required_topics: tuple[str, ...]


EXPECTATIONS: tuple[RepoMetadataExpectation, ...] = (
    RepoMetadataExpectation(
        repo="happysnaker/happysnaker",
        homepage="https://happysnaker.github.io/",
        description_terms=("Public GitHub profile", "backend", "systems", "OSS"),
        required_topics=("backend-engineering", "distributed-systems", "github-profile", "agent-ops", "oss-portfolio", "sponsorware"),
    ),
    RepoMetadataExpectation(
        repo="happysnaker/qq-ai-bot",
        homepage="https://happysnaker.github.io/qq-ai-bot/",
        description_terms=("OneBot", "ACP", "Docker", "sponsorware"),
        required_topics=("onebot", "acp", "docker", "observability", "casaos", "homelab", "agent-client-protocol", "sponsorware"),
    ),
    RepoMetadataExpectation(
        repo="happysnaker/RDLeader",
        homepage="https://happysnaker.github.io/rdleader/",
        description_terms=("Local-first", "control plane", "ACP", "public CI"),
        required_topics=("agent-ops", "control-plane", "local-first", "public-ci", "sponsorware", "ai-workers"),
    ),
    RepoMetadataExpectation(
        repo="happysnaker/happysnaker.github.io",
        homepage="https://happysnaker.github.io/",
        description_terms=("technical blog", "project landing pages", "backend"),
        required_topics=("developer-portfolio", "github-pages", "project-landing-pages", "sponsorware", "support"),
    ),
    RepoMetadataExpectation(
        repo="happysnaker/.github",
        homepage="https://happysnaker.github.io/support/",
        description_terms=("Default community health", "support", "contribution"),
        required_topics=("community-health", "support", "oss-maintenance", "sponsorware"),
    ),
)



def is_retryable_gh_error(message: str) -> bool:
    retryable_needles = (
        "HTTP 429",
        "HTTP 500",
        "HTTP 502",
        "HTTP 503",
        "HTTP 504",
        "connection reset",
        "connection refused",
        "can't assign requested address",
        "network is unreachable",
        "connection timed out",
        "i/o timeout",
        "TLS handshake timeout",
        "temporary failure",
    )
    lowered = message.lower()
    return any(needle.lower() in lowered for needle in retryable_needles)


def run_gh(args: list[str]) -> Any:
    last_error = "gh command failed"
    for attempt in range(1, 4):
        completed = subprocess.run(["gh", *args], check=False, capture_output=True, text=True)
        if completed.returncode == 0:
            try:
                return json.loads(completed.stdout)
            except json.JSONDecodeError as error:
                last_error = f"invalid JSON from gh: {error}"
        else:
            last_error = completed.stderr.strip() or completed.stdout.strip() or "gh command failed"
        if attempt < 3 and is_retryable_gh_error(last_error):
            time.sleep(attempt * 2)
            continue
        break
    raise RuntimeError(last_error)


def main() -> int:
    failures: list[str] = []
    for expected in EXPECTATIONS:
        try:
            data = run_gh([
                "repo",
                "view",
                expected.repo,
                "--json",
                "nameWithOwner,description,homepageUrl,repositoryTopics,isArchived,visibility",
            ])
        except RuntimeError as error:
            failures.append(f"{expected.repo}: {error}")
            continue

        description = data.get("description") or ""
        homepage = data.get("homepageUrl") or ""
        topics = {topic.get("name") for topic in data.get("repositoryTopics", [])}

        repo_failures: list[str] = []
        if data.get("visibility") != "PUBLIC":
            repo_failures.append(f"visibility is {data.get('visibility')!r}")
        if data.get("isArchived"):
            repo_failures.append("repository is archived")
        if homepage != expected.homepage:
            repo_failures.append(f"homepage is {homepage!r}; expected {expected.homepage!r}")
        missing_terms = [term for term in expected.description_terms if term.lower() not in description.lower()]
        if missing_terms:
            repo_failures.append(f"description missing {missing_terms}")
        missing_topics = [topic for topic in expected.required_topics if topic not in topics]
        if missing_topics:
            repo_failures.append(f"topics missing {missing_topics}")

        if repo_failures:
            failures.extend(f"{expected.repo}: {failure}" for failure in repo_failures)
            print(f"FAIL {expected.repo}")
        else:
            print(f"OK {expected.repo}: {homepage} ({len(topics)} topics)")

    if failures:
        print("\nRepository metadata check failures:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(f"Checked {len(EXPECTATIONS)} repository metadata surfaces")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
