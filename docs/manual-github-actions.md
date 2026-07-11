# Manual GitHub Actions Checklist

> Some GitHub profile actions are not exposed through the available API surface here. This file keeps them visible instead of pretending they were automated.

## 1. Pin RDLeader on the profile

Current API check still shows profile pins include `Resume` and do not include `RDLeader`. Re-checked on 2026-07-11 Asia/Shanghai with `python3 scripts/check_profile_pins.py`: the current GraphQL mutation surface exposes issue/comment/environment pin mutations and repository metadata mutations, but still does not expose a profile repository-pin mutation, so this remains a manual web-UI action. The checker now runs in CI as a report-only step; use `python3 scripts/check_profile_pins.py --strict` after the manual swap to make it fail until the recommended pinned set is visible.

For the strongest technical first screen, replace `Resume` with `RDLeader`.

Recommended pinned set:

1. `qq-ai-bot`
2. `RDLeader`
3. `happydb`
4. `go-service-starter`
5. `go-http-middleware-kit`
6. `CSAPPLabsAndNotes`

Why:

- `qq-ai-bot` = bot infrastructure flagship
- `RDLeader` = agent-ops / control-plane flagship
- `happydb` = Java/database internals proof
- `go-service-starter` = Go backend service craft
- `go-http-middleware-kit` = reusable Go library craft
- `CSAPPLabsAndNotes` = systems fundamentals proof

Automation already completed around this item:

- RDLeader project page exists: <https://happysnaker.github.io/rdleader/>.
- RDLeader repository homepage now points to that project page.
- RDLeader topics include `agent-ops`, `control-plane`, `runtime-orchestration`, `sponsorware`, and `ai-workers`.
- The profile repo topics include `agent-ops`, `oss-portfolio`, and `sponsorware`.
- Weekly profile CI now checks support-route, repository metadata, compact sponsor-release, operations-log, issue-label, share-kit, manual-blocker, README badge, and public site hygiene drift.
- `docs/flagship-technical-map.md` now explains why RDLeader belongs in the first-screen technical proof set.
- `docs/share-kit.md` and the live support page now expose proof-safe share snippets for `qq-ai-bot` and `RDLeader`.
- `scripts/check_issue_labels.py` keeps the manual/profile and sponsor/open-loop issues labeled for public triage.
- `scripts/check_ops_issue_log.py` keeps [happysnaker#2](https://github.com/happysnaker/happysnaker/issues/2) as the append-only operations log now that the sponsor release is compact.

Manual path:

1. Open the GitHub profile page.
2. Edit pinned repositories.
3. Remove `Resume`.
4. Add `RDLeader`.
5. Keep the other five pins unchanged.
6. Confirm the visible pins match the list above.

## 2. Decide RDLeader license posture

Tracked in:

- <https://github.com/happysnaker/RDLeader/issues/3>

Current report command:

```bash
python3 scripts/check_rdleader_license.py
```

Before wider reuse/promotion, choose one of:

- MIT
- Apache-2.0
- AGPL-style copyleft
- Source-available for now

Do not imply unrestricted reuse until a license is published. The current share kit, sponsor release, support routes, and RDLeader support files intentionally preserve this caveat.

## 3. RDLeader public demo assets — completed

Tracked in:

- <https://github.com/happysnaker/RDLeader/issues/2>

Current status: completed with public-safe SVG demo assets, walkthrough video, browser walkthrough, fake-data reset path, onboarding guide, landing copy, distribution kit, and submission tracker. Keep future assets under the same safety rules:

- no private paths;
- no live group IDs;
- no open IDs;
- no message IDs;
- no app IDs;
- no QR onboarding artifacts;
- no raw integration logs.

## 4. Review parked repos before promotion

Before promoting `chinese-independent-developer`, decide whether it should become a serious content asset or stay parked.

Minimum before promotion:

- license decision
- README positioning
- support path
- proof of maintenance intent

## Tracking

This checklist is mirrored in [happysnaker#1](https://github.com/happysnaker/happysnaker/issues/1). Keep the issue and this file aligned when a manual item is completed. Operational evidence belongs in [happysnaker#2](https://github.com/happysnaker/happysnaker/issues/2), not in the compact sponsor release body.
