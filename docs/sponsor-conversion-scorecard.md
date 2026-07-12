# Sponsor Conversion Scorecard

> A public, evidence-first scorecard for turning GitHub attention into useful support without spam, overclaiming, or private-data leakage. Read it after the [sponsor prospect pipeline](sponsor-prospect-pipeline.md) and before posting any outreach from the [share kit](share-kit.md).

## Operating rule

A support path is conversion-ready only when it has all four pieces:

1. **Landing surface** — where the reader arrives.
2. **Proof surface** — what they can verify before paying, testing, or sharing.
3. **Concrete note** — the exact support note or review product to use.
4. **Follow-up owner** — what happens next, and what must not be claimed publicly.

If any piece is missing, do not ask for money yet; route the reader to proof, a tester request, or a paid-review sample instead.

## Funnel scorecard

| Funnel stage | Current public surface | Conversion question | Concrete next action | Guardrail |
|---|---|---|---|---|
| 1. Land | Profile README, project pages, default `.github` support files | Can a new reader understand the strongest projects in under one minute? | Lead with `qq-ai-bot`, `RDLeader`, `happydb`, Go starter / middleware, and the proof index | Do not promote random forks as portfolio centerpieces |
| 2. Trust | Flagship status snapshot, CI / CodeQL badges, support coverage, technical proof index | Can the reader verify current CI / alert / packaging claims before paying? | Run `python3 scripts/check_github_status.py --summary` and point to proof-before-payment | Do not quote stale green checks as live status |
| 3. Route | 10-second support router and current concrete asks | Does the reader know whether to Tip / Proof / Review / Fund? | Send <https://happysnaker.github.io/support/#sponsor-router> before payment links | Do not collect payment screenshots, tokens, QR codes, raw logs, or internal URLs in public |
| 4. Act | Sponsorware board, deploy-read sample, issue-backed support notes | Is there one exact note attached to the payment or help request? | Use `qq-ai-bot #26 arm64`, `RDLeader #27`, `Deploy read`, `Quick read`, or `Async review` | Do not create vague sponsor promises without a public tracker |
| 5. Follow up | External follow-up queue and operations cadence issue | Is the next message due, useful, and non-spammy? | Recheck optional external updates on `2026-07-16 UTC` and log material changes in `happysnaker#2` | Do not repeatedly bump external PRs before the review gate |
| 6. Resolve blockers | Owner action packet and manual GitHub checklist | Are owner-only blockers preventing stronger promotion? | Owner swaps profile pin `Resume` → `RDLeader`; owner chooses RDLeader license posture | Do not imply RDLeader reuse rights until license metadata/root `LICENSE` and issue state justify it |

## Segment-to-offer fit

| Audience | Best first proof | Best offer / ask | Support note | Do not say |
|---|---|---|---|---|
| Homelab / CasaOS / NAS / SBC testers | `qq-ai-bot` project page + arm64 tester pack | Real physical-host report or fund validation | `qq-ai-bot #26 arm64` | Physical ARM / CasaOS validation is complete |
| Bot / agent builders | OneBot / NapCat / LLOneBot / ACP proof chain | Deploy read for bot / agent / infra repo packaging | `Deploy read` | Private bot tokens or raw live integration logs are acceptable in public |
| Curators / maintainers | Project page + proof-before-payment + concise external queue row | One scheduled-review update when due | No payment ask in curator threads | External PRs should be bumped repeatedly |
| Sponsor / funder | Current asks + sponsorware board + status snapshot | Fund a public outcome with one note | `qq-ai-bot #26 arm64` or `RDLeader #27` | Sponsorship buys private priority or untracked deliverables |
| GitHub profile / README customer | Deploy-read sample + profile proof hub | `¥29.9 Quick read` or `¥99 Async review` | `Quick read` / `Async review` | Payment screenshots belong in public issues |
| RDLeader evaluator | RDLeader project page + distribution kit + submission tracker | Review public proof or fund submission follow-up | `RDLeader #27` | RDLeader reuse rights are granted while `RDLeader#3` is open |
| Backend / systems-study reader | happydb, Go starter / middleware, CSAPP notes, checklist repos | Tip if useful; buy a packaging pass for their repo | repo name or `Quick read` | Educational repo threads should become generic fundraising spam |

## Weekly review questions

Use these during the regular operations cadence:

- **Landing:** did profile README, pinned repos, project pages, and default support files still route readers to proof and support without dead ends?
- **Trust:** did `check_github_status.py`, `check_support_routes.py`, and `check_repo_metadata.py` still prove the claims being reused in share copy?
- **Route:** did the support page still separate Tip / Proof / Review / Fund before QR/payment links?
- **Act:** do current support notes still map to open public trackers and paid-review products?
- **Follow up:** are external comments due, or should we stay quiet until the scheduled review gate?
- **Blockers:** did the owner finish the profile pin swap or choose the RDLeader license path?

## Copy-safe conversion block

```text
If you want to support a visible public outcome, please pick one concrete route instead of a vague donation:

- Proof first: https://happysnaker.github.io/support/#proof-before-payment
- Choose path: https://happysnaker.github.io/support/#sponsor-router
- Funded issues: qq-ai-bot #26 arm64 / RDLeader #27
- Paid review sample: https://happysnaker.github.io/review/deploy-read-sample/

Please do not post tokens, QR codes, raw logs, internal URLs, private screenshots, or payment screenshots in public issues.
```

## Verification commands

```bash
python3 scripts/check_sponsor_conversion_scorecard.py --json
python3 scripts/check_sponsor_pipeline.py --json
python3 scripts/check_share_kit.py --json
python3 scripts/check_support_routes.py --json
python3 scripts/check_manual_blockers.py --json
python3 scripts/check_external_followups.py --summary
```
