# Sponsor Prospect Pipeline

> Evidence-first pipeline for turning public GitHub attention into useful support without spam, overclaiming, or private-data leakage. Use this together with the [share kit](share-kit.md), [sponsorware board](sponsorware-board.md), and [external follow-up queue](external-follow-up-queue.md).

## Operating rule

Do not start from “please donate.” Start from the reader’s job, one proof link, and one concrete next action.

Every outreach / reply should answer four questions:

1. Who is this for?
2. What public proof can they inspect before paying or helping?
3. What exact note should they use if they support it?
4. What must not be claimed or requested in public?

## Active segments

| Segment | Proof to lead with | Best CTA | Concrete support note | Guardrail |
|---|---|---|---|---|
| Homelab / CasaOS / NAS / SBC testers | `qq-ai-bot` multi-arch image, QEMU arm64 smoke, tester pack, homelab outreach kit | Ask for a real device report or fund one | `qq-ai-bot #26 arm64` | Do not claim physical ARM / CasaOS validation is complete until a real host report lands |
| Bot / agent builders | `qq-ai-bot` project page, deploy-read sample, OneBot / NapCat / LLOneBot / Docker positioning | Buy a deploy read or quick read | `Deploy read` / `Quick read` | Do not request tokens, QR codes, raw logs, or private screenshots in public |
| Curators / maintainers | Project pages, status snapshot, support router, compact external-follow-up comments | One concise scheduled-review update only when allowed | No payment ask in curator threads | Do not repeatedly bump external PRs before the 2026-07-16 UTC gate |
| GitHub profile / README customers | Profile README, technical proof index, deploy-read sample, redacted examples | Buy `¥29.9 Quick read` or `¥99 Async review` | `Quick read` / `Async review` | Keep payment evidence private by email only, never in public issues |
| Sponsor / funder | Current asks, proof-before-payment section, issue-backed sponsorware board | Fund a public issue with a specific note | `qq-ai-bot #26 arm64` or `RDLeader #27` | Tie receipts to public trackers, not vague private promises |
| RDLeader evaluators | RDLeader project page, distribution kit, submission tracker, license-decision packet | Review public proof or fund submission follow-up | `RDLeader #27` | Do not imply reuse rights until `RDLeader#3` and root license posture are resolved |
| Backend / systems-study readers | Go starter, middleware kit, backend/system/production checklists, support router | Tip if saved time; buy a packaging pass if their repo needs sharper positioning | repo name or `Quick read` | Do not turn educational repo threads into generic fundraising spam |

## Current working list

| Surface | Segment | Current action | Next allowed move |
|---|---|---|---|
| `qq-ai-bot#26` | Homelab / CasaOS / NAS / SBC testers | Keep open for a real physical-host report | Update only when a real tester report lands |
| `docker/awesome-compose#781` | Curators / maintainers | Candidate scheduled-review comment prepared | Recheck on 2026-07-16 UTC, then post at most one short proof-path update if still review-required and no maintainer reply |
| `AwesomeHomelab#98` | Homelab / CasaOS / NAS / SBC testers | Candidate homelab-focused update prepared | Recheck on 2026-07-16 UTC, then post at most one short update if still no feedback |
| `jbesomi/awesome-autonomous-agents#20` | RDLeader evaluators / curators | Candidate RDLeader proof update prepared | Recheck on 2026-07-16 UTC, keep license caveat explicit |
| `RDLeader#27` | RDLeader evaluators | Keep as public tracker for external submission review follow-up | Update only when external review state changes |

## Links to use

| Need | Link |
|---|---|
| Proof before payment | <https://happysnaker.github.io/support/#proof-before-payment> |
| 10-second support router | <https://happysnaker.github.io/support/#sponsor-router> |
| Current concrete asks | <https://happysnaker.github.io/support/#current-asks> |
| Deploy-read sample | <https://happysnaker.github.io/review/deploy-read-sample/> |
| qq-ai-bot project page | <https://happysnaker.github.io/qq-ai-bot/> |
| RDLeader project page | <https://happysnaker.github.io/rdleader/> |
| qq-ai-bot tester pack | <https://github.com/happysnaker/qq-ai-bot/blob/main/docs/public/arm64-casaos-tester-pack.md> |
| qq-ai-bot homelab outreach kit | <https://github.com/happysnaker/qq-ai-bot/blob/main/docs/public/homelab-outreach-kit.md> |
| RDLeader distribution kit | <https://github.com/happysnaker/RDLeader/blob/main/docs/public/distribution-kit.md> |
| RDLeader submission tracker | <https://github.com/happysnaker/RDLeader/blob/main/docs/public/submission-tracker.md> |

## Reply patterns

### Tester ask

```text
If you have a real ARM / CasaOS / NAS / SBC host, the useful next step is not another star — it is a short install report against the tester pack.

Tester pack: https://github.com/happysnaker/qq-ai-bot/blob/main/docs/public/arm64-casaos-tester-pack.md
Support note if you want to fund the validation path: qq-ai-bot #26 arm64

Caveat: QEMU arm64 smoke is green, but physical ARM / CasaOS validation is not complete until a real host report lands.
```

### Paid-review ask

```text
If your repo technically works but still looks toy-like, use the deploy-read sample before paying.

Sample: https://happysnaker.github.io/review/deploy-read-sample/
Order route: https://happysnaker.github.io/support/#quick-read

Send only public links. Do not send private logs, tokens, QR codes, payment screenshots, or internal URLs in public issues.
```

### Sponsor ask

```text
If you want the support to create a visible public outcome, use a concrete note instead of a vague donation label:

- qq-ai-bot #26 arm64
- RDLeader #27

Proof before payment: https://happysnaker.github.io/support/#proof-before-payment
Current asks: https://happysnaker.github.io/support/#current-asks
```

## Cadence

- Daily / heartbeat: audit current GitHub status and blockers before acting.
- Before any external comment: run the external follow-up gate and obey the row-level action class.
- Scheduled external review: 2026-07-16 UTC unless a maintainer/tester replies earlier.
- After any material change: record a compact evidence comment in <https://github.com/happysnaker/happysnaker/issues/2>.

## Verification commands

```bash
python3 scripts/check_github_status.py --summary
python3 scripts/check_external_followups.py --summary
python3 scripts/check_sponsor_pipeline.py --json
python3 scripts/check_share_kit.py --json
python3 scripts/check_manual_blockers.py --json
```
