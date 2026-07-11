#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from typing import Any

from github_cli import run_gh_json

LOGIN = "happysnaker"
CURRENT_RECOMMENDED = [
    "happysnaker/qq-ai-bot",
    "happysnaker/RDLeader",
    "happysnaker/happydb",
    "happysnaker/go-service-starter",
    "happysnaker/go-http-middleware-kit",
    "happysnaker/CSAPPLabsAndNotes",
]
KNOWN_MANUAL_REPLACEMENT = {
    "remove": "happysnaker/Resume",
    "add": "happysnaker/RDLeader",
}




run_gh = run_gh_json

def current_pins() -> list[str]:
    query = """
    query($login:String!) {
      user(login:$login) {
        pinnedItems(first:10, types:REPOSITORY) {
          nodes { ... on Repository { nameWithOwner } }
        }
      }
    }
    """
    data = run_gh(["api", "graphql", "-f", f"query={query}", "-F", f"login={LOGIN}"])
    return [node["nameWithOwner"] for node in data["data"]["user"]["pinnedItems"]["nodes"]]


def pin_mutations() -> list[str]:
    query = """
    query {
      __schema {
        mutationType {
          fields { name description }
        }
      }
    }
    """
    data = run_gh(["api", "graphql", "-f", f"query={query}"])
    names: list[str] = []
    for field in data["data"]["__schema"]["mutationType"]["fields"]:
        haystack = f"{field.get('name') or ''} {field.get('description') or ''}"
        if "pin" in haystack.lower() or "pinned" in haystack.lower():
            names.append(field["name"])
    return sorted(names)


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit happysnaker profile pinned repositories.")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero if current pins do not match the recommended technical-first set.")
    parser.add_argument("--json", action="store_true", help="Emit JSON summary.")
    args = parser.parse_args()

    pins = current_pins()
    mutations = pin_mutations()
    missing = [repo for repo in CURRENT_RECOMMENDED if repo not in pins]
    extra = [repo for repo in pins if repo not in CURRENT_RECOMMENDED]
    matches = not missing and not extra
    manual_only = "pinIssue" in mutations and "pinRepository" not in mutations and "updateUserPinnedItems" not in mutations

    summary = {
        "current": pins,
        "recommended": CURRENT_RECOMMENDED,
        "missing": missing,
        "extra": extra,
        "matchesRecommended": matches,
        "manualReplacement": KNOWN_MANUAL_REPLACEMENT,
        "availablePinMutations": mutations,
        "profileRepositoryPinAppearsManualOnly": manual_only,
    }

    if args.json:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
    else:
        print("## Current pinned repositories")
        for index, repo in enumerate(pins, 1):
            print(f"{index}. {repo}")
        print("\n## Recommended technical-first set")
        for index, repo in enumerate(CURRENT_RECOMMENDED, 1):
            print(f"{index}. {repo}")
        print("\n## Diff")
        print("missing: " + (", ".join(missing) if missing else "none"))
        print("extra: " + (", ".join(extra) if extra else "none"))
        print("\n## API capability")
        print("pin mutations: " + ", ".join(mutations))
        print("profile repository pin appears manual-only: " + str(manual_only).lower())
        if not matches:
            print("\nManual action: replace `happysnaker/Resume` with `happysnaker/RDLeader` in GitHub profile pinned repositories.")

    return 1 if args.strict and not matches else 0


if __name__ == "__main__":
    raise SystemExit(main())
