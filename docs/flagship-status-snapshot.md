# Flagship GitHub status snapshot

> Generated from `scripts/check_github_status.py --markdown` on 2026-07-11 Asia/Shanghai.

This is a point-in-time proof snapshot for sponsor, curator, and reviewer links. It covers the configured flagship surfaces only; do not generalize the CodeQL claim to older repositories without CodeQL configured.

Because editing this file triggers a new profile CI / CodeQL run, the `happysnaker/happysnaker` self-check rows may intentionally trail the newest commit by one docs refresh. Run `python3 scripts/check_github_status.py` for the live source of truth before quoting current status.

## Workflow state

| Repo | Workflow | Status | Commit | Proof |
|---|---|---|---|---|
| `happysnaker/happysnaker` | CI | completed / success | `e4c6c6e` | [workflow](https://github.com/happysnaker/happysnaker/actions/workflows/ci.yml) |
| `happysnaker/happysnaker` | CodeQL | completed / success | `e4c6c6e` | [workflow](https://github.com/happysnaker/happysnaker/actions/workflows/codeql.yml) |
| `happysnaker/qq-ai-bot` | CI | completed / success | `0f13edc` | [run](https://github.com/happysnaker/qq-ai-bot/actions/runs/29153968913) |
| `happysnaker/qq-ai-bot` | CodeQL | completed / success | `0f13edc` | [run](https://github.com/happysnaker/qq-ai-bot/actions/runs/29153968934) |
| `happysnaker/qq-ai-bot` | Publish Docker image | completed / success | `0f13edc` | [run](https://github.com/happysnaker/qq-ai-bot/actions/runs/29153968904) |
| `happysnaker/qq-ai-bot` | Arm64 image smoke | completed / success | `0f13edc` | [run](https://github.com/happysnaker/qq-ai-bot/actions/runs/29154026332) |
| `happysnaker/RDLeader` | CI | completed / success | `2b0ad6a` | [run](https://github.com/happysnaker/RDLeader/actions/runs/29153737743) |
| `happysnaker/RDLeader` | CodeQL | completed / success | `2b0ad6a` | [run](https://github.com/happysnaker/RDLeader/actions/runs/29153737774) |
| `happysnaker/happysnaker.github.io` | pages-build-deployment | completed / success | `e9387ce` | [run](https://github.com/happysnaker/happysnaker.github.io/actions/runs/29152926142) |

## Configured alert state

| Repo | CodeQL open | Dependabot open | Secret scanning open |
|---|---:|---:|---:|
| `happysnaker/happysnaker` | 0 | 0 | 0 |
| `happysnaker/qq-ai-bot` | 0 | 0 | 0 |
| `happysnaker/RDLeader` | 0 | 0 | 0 |

## Current support routing

- Main support page: <https://happysnaker.github.io/support/>
- Current concrete asks: <https://happysnaker.github.io/support/#current-asks>
- `qq-ai-bot #26 arm64`: <https://github.com/happysnaker/qq-ai-bot/issues/26>
- `RDLeader #27`: <https://github.com/happysnaker/RDLeader/issues/27>
- Sponsor one-pager: [sponsor-one-pager.md](sponsor-one-pager.md)
- Share kit: [share-kit.md](share-kit.md)
- Technical proof index: [technical-proof-index.md](technical-proof-index.md)
- Operations log: <https://github.com/happysnaker/happysnaker/issues/2>

## Caveats

- `qq-ai-bot` has green QEMU / workflow arm64 smoke evidence, but still needs a real physical ARM / CasaOS / NAS / SBC host report before claiming physical-host validation.
- RDLeader currently exposes clean configured CodeQL / Dependabot / secret-scanning state, but its license posture is still tracked separately and should not be over-claimed.
- External PRs should be followed through the scheduled queue instead of repeated unsourced bumps: [external-follow-up-queue.md](external-follow-up-queue.md).
