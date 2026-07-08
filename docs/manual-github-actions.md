# Manual GitHub Actions Checklist

> Some GitHub profile actions are not exposed through the available API surface here. This file keeps them visible instead of pretending they were automated.

## 1. Pin RDLeader on the profile

Current API check still shows profile pins include `Resume` and do not include `RDLeader`. Re-checked on 2026-07-08 UTC / 2026-07-09 Asia-Shanghai: the current GraphQL mutation surface exposes issue/comment pin mutations, not profile repository pin mutations, so this remains a manual web-UI action.

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

Before wider reuse/promotion, choose one of:

- MIT
- Apache-2.0
- AGPL-style copyleft
- Source-available for now

Do not imply unrestricted reuse until a license is published.

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

This checklist is mirrored in [happysnaker#1](https://github.com/happysnaker/happysnaker/issues/1). Keep the issue and this file aligned when a manual item is completed.
