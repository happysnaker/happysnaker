#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import time
from typing import Any, Sequence

RETRYABLE_NEEDLES = (
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


def is_retryable_gh_error(message: str) -> bool:
    lowered = message.lower()
    return any(needle.lower() in lowered for needle in RETRYABLE_NEEDLES)


def run_gh_json(args: Sequence[str], *, attempts: int = 3) -> Any:
    last_error = "gh command failed"
    for attempt in range(1, attempts + 1):
        completed = subprocess.run(["gh", *args], check=False, capture_output=True, text=True)
        if completed.returncode == 0:
            stdout = completed.stdout.strip()
            try:
                return json.loads(stdout) if stdout else None
            except json.JSONDecodeError as error:
                last_error = f"invalid JSON from gh: {error}"
        else:
            last_error = completed.stderr.strip() or completed.stdout.strip() or "gh command failed"
        if attempt < attempts and is_retryable_gh_error(last_error):
            time.sleep(attempt * 2)
            continue
        break
    raise RuntimeError(last_error)


def gh_api_exists(args: Sequence[str], *, attempts: int = 3) -> bool:
    try:
        run_gh_json(args, attempts=attempts)
    except RuntimeError:
        return False
    return True
