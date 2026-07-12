#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from dataclasses import dataclass
from typing import Any

from github_cli import run_gh_json


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
    RepoMetadataExpectation(
        repo="happysnaker/go-service-starter",
        homepage="https://happysnaker.github.io/go-service-starter/",
        description_terms=("Go", "HTTP", "service starter", "Docker"),
        required_topics=("go", "backend", "service-template", "docker", "oss-maintenance", "sponsorware"),
    ),
    RepoMetadataExpectation(
        repo="happysnaker/go-http-middleware-kit",
        homepage="https://happysnaker.github.io/go-http-middleware-kit/",
        description_terms=("net/http", "middleware", "request IDs", "structured logging"),
        required_topics=("go", "middleware", "net-http", "request-id", "structured-logging", "oss-maintenance", "sponsorware"),
    ),
    RepoMetadataExpectation(
        repo="happysnaker/happydb",
        homepage="https://happysnaker.github.io/happydb/",
        description_terms=("Java", "database internals", "MVCC", "recovery"),
        required_topics=("java", "database", "storage-engine", "mvcc", "query-optimizer", "oss-maintenance", "sponsorware"),
    ),
    RepoMetadataExpectation(
        repo="happysnaker/Resume",
        homepage="https://happysnaker.github.io/Resume/",
        description_terms=("resume", "portfolio", "GitHub Pages"),
        required_topics=("developer-portfolio", "resume-template", "github-pages", "landing-page", "oss-maintenance", "sponsorware"),
    ),
    RepoMetadataExpectation(
        repo="happysnaker/CSAPPLabsAndNotes",
        homepage="https://happysnaker.github.io/csapp-labs-notes/",
        description_terms=("CSAPP", "systems", "interview"),
        required_topics=("csapp", "computer-systems", "systems-programming", "interview-prep", "oss-maintenance", "sponsorware"),
    ),
    RepoMetadataExpectation(
        repo="happysnaker/github-profile-checklist",
        homepage="https://happysnaker.github.io/github-profile-checklist/",
        description_terms=("GitHub profile", "proof of work", "README"),
        required_topics=("github-profile", "developer-portfolio", "github-readme", "template-repository", "oss-maintenance", "sponsorware"),
    ),
    RepoMetadataExpectation(
        repo="happysnaker/backend-engineer-checklist",
        homepage="https://happysnaker.github.io/backend-engineer-checklist/",
        description_terms=("Backend", "interviews", "public proof"),
        required_topics=("backend-engineering", "distributed-systems", "java", "golang", "template-repository", "oss-maintenance", "sponsorware"),
    ),
    RepoMetadataExpectation(
        repo="happysnaker/system-design-checklist",
        homepage="https://happysnaker.github.io/system-design-checklist/",
        description_terms=("System design", "architecture reviews", "tradeoff"),
        required_topics=("system-design", "software-architecture", "distributed-systems", "design-docs", "template-repository", "oss-maintenance", "sponsorware"),
    ),
    RepoMetadataExpectation(
        repo="happysnaker/production-readiness-checklist",
        homepage="https://happysnaker.github.io/production-readiness-checklist/",
        description_terms=("Production readiness", "launch reviews", "on-call"),
        required_topics=("production-readiness", "release-engineering", "observability", "sre", "template-repository", "oss-maintenance", "sponsorware"),
    ),
    RepoMetadataExpectation(
        repo="happysnaker/chinese-independent-developer",
        homepage="https://happysnaker.github.io/support/#from-indie-dev",
        description_terms=("Chinese indie developer", "make money"),
        required_topics=("indie-developer", "monetization", "saas", "remote-work", "oss-maintenance", "sponsorware"),
    ),
)




run_gh = run_gh_json

def main() -> int:
    parser = argparse.ArgumentParser(description="Verify portfolio-critical repository homepage, description, topic, visibility, and archive metadata.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable repository metadata summary.")
    args = parser.parse_args()

    failures: list[str] = []
    results: list[dict[str, Any]] = []
    for expected in EXPECTATIONS:
        data: dict[str, Any] = {}
        fetch_error: str | None = None
        try:
            data = run_gh([
                "repo",
                "view",
                expected.repo,
                "--json",
                "nameWithOwner,description,homepageUrl,repositoryTopics,isArchived,visibility",
            ])
        except RuntimeError as error:
            fetch_error = str(error)
            failures.append(f"{expected.repo}: {error}")

        description = data.get("description") or ""
        homepage = data.get("homepageUrl") or ""
        topics = {topic.get("name") for topic in data.get("repositoryTopics", [])} if data else set()

        repo_failures: list[str] = []
        if fetch_error:
            repo_failures.append(fetch_error)
        else:
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

        if repo_failures and not fetch_error:
            failures.extend(f"{expected.repo}: {failure}" for failure in repo_failures)
        results.append({
            "repo": expected.repo,
            "homepage": homepage,
            "expectedHomepage": expected.homepage,
            "description": description,
            "visibility": data.get("visibility") if data else None,
            "isArchived": data.get("isArchived") if data else None,
            "topicCount": len(topics),
            "requiredTopicCount": len(expected.required_topics),
            "missingTopics": [topic for topic in expected.required_topics if topic not in topics],
            "missingDescriptionTerms": [term for term in expected.description_terms if term.lower() not in description.lower()] if data else list(expected.description_terms),
            "fetchError": fetch_error,
            "ok": not repo_failures,
        })
        if not args.json:
            if repo_failures:
                print(f"FAIL {expected.repo}")
            else:
                print(f"OK {expected.repo}: {homepage} ({len(topics)} topics)")

    summary = {
        "ok": not failures,
        "repoCount": len(EXPECTATIONS),
        "checkedRepoCount": len(results),
        "repos": results,
        "failures": failures,
    }
    if args.json:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
    if failures:
        if not args.json:
            print("\nRepository metadata check failures:", file=sys.stderr)
            for failure in failures:
                print(f"- {failure}", file=sys.stderr)
        return 1

    if not args.json:
        print(f"Checked {len(EXPECTATIONS)} repository metadata surfaces")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
