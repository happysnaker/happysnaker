# Flagship GitHub status snapshot

> Generated from `scripts/check_github_status.py --markdown` on 2026-07-11 Asia/Shanghai.

This is a point-in-time proof snapshot for sponsor, curator, and reviewer links. It covers the configured flagship surfaces only; do not generalize the CodeQL claim to older repositories without CodeQL configured.

## Workflow state

| Repo | Workflow | Status | Commit | Proof |
|---|---|---|---|---|
| `happysnaker/happysnaker` | CI | completed / success | `c94c542` | [run](https://github.com/happysnaker/happysnaker/actions/runs/29114730041) |
| `happysnaker/happysnaker` | CodeQL | completed / success | `c94c542` | [run](https://github.com/happysnaker/happysnaker/actions/runs/29114730043) |
| `happysnaker/qq-ai-bot` | CI | completed / success | `18413c3` | [run](https://github.com/happysnaker/qq-ai-bot/actions/runs/29102776397) |
| `happysnaker/qq-ai-bot` | CodeQL | completed / success | `18413c3` | [run](https://github.com/happysnaker/qq-ai-bot/actions/runs/29102776374) |
| `happysnaker/qq-ai-bot` | Publish Docker image | completed / success | `18413c3` | [run](https://github.com/happysnaker/qq-ai-bot/actions/runs/29102776459) |
| `happysnaker/qq-ai-bot` | Arm64 image smoke | completed / success | `18413c3` | [run](https://github.com/happysnaker/qq-ai-bot/actions/runs/29102901202) |
| `happysnaker/RDLeader` | CI | completed / success | `47e608a` | [run](https://github.com/happysnaker/RDLeader/actions/runs/29112782761) |
| `happysnaker/RDLeader` | CodeQL | completed / success | `47e608a` | [run](https://github.com/happysnaker/RDLeader/actions/runs/29112782768) |
| `happysnaker/happysnaker.github.io` | pages-build-deployment | completed / success | `9eaf51a` | [run](https://github.com/happysnaker/happysnaker.github.io/actions/runs/29106752206) |

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
- Technical proof index: [technical-proof-index.md](technical-proof-index.md)

## Caveats

- `qq-ai-bot` has green QEMU / workflow arm64 smoke evidence, but still needs a real physical ARM / CasaOS / NAS / SBC host report before claiming physical-host validation.
- RDLeader currently exposes clean configured CodeQL / Dependabot / secret-scanning state, but its license posture is still tracked separately and should not be over-claimed.
- External PRs should be followed through the scheduled queue instead of repeated unsourced bumps: [external-follow-up-queue.md](external-follow-up-queue.md).
