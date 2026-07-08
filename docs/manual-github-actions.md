# Manual GitHub Actions Checklist

> Some GitHub profile actions are not exposed through the available API surface here. This file keeps them visible instead of pretending they were automated.

## 1. Pin RDLeader on the profile

Current pinned repos still include `Resume`. For the strongest technical first screen, replace `Resume` with `RDLeader`.

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

## 3. Create fake-data RDLeader screenshots / video

Tracked in:

- <https://github.com/happysnaker/RDLeader/issues/2>

Use only fake/demo identities. Do not show:

- private paths
- live group IDs
- open IDs
- message IDs
- app IDs
- QR onboarding artifacts
- raw integration logs

## 4. Review parked repos before promotion

Before promoting `chinese-independent-developer`, decide whether it should become a serious content asset or stay parked.

Minimum before promotion:

- license decision
- README positioning
- support path
- proof of maintenance intent

## Tracking

This checklist is mirrored in the profile repository issues once issues are enabled. Keep the issue and this file aligned when a manual item is completed.
