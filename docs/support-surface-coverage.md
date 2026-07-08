# Support surface coverage

> Public checklist showing which high-signal repositories route visitors to support pages, the frozen sponsor one-pager, and GitHub About metadata. This keeps sponsor routing auditable instead of hidden in one-off issue comments.

Snapshot: 2026-07-09 Asia/Shanghai.

## Canonical support assets

| Asset | Link | Purpose |
|---|---|---|
| Main support page | <https://happysnaker.github.io/support/> | QR codes, async review options, and project-specific support paths |
| Frozen sponsor one-pager | <https://github.com/happysnaker/happysnaker/releases/tag/v2026.07-sponsor-one-pager> | stable sponsor / curator brief for sharing |
| Source sponsor one-pager | [sponsor-one-pager.md](sponsor-one-pager.md) | editable source for future support updates |
| Sponsorware board | [sponsorware-board.md](sponsorware-board.md) | current and shipped sponsor targets |
| Operations cadence | [operations-cadence.md](operations-cadence.md) | maintenance loop and manual actions |

## Coverage table

| Repository | Why it matters | Support route | Frozen one-pager evidence | About metadata |
|---|---|---|---|---|
| [`qq-ai-bot`](https://github.com/happysnaker/qq-ai-bot) | flagship bot infrastructure / OneBot + ACP | `SUPPORT.md`, `.github/SUPPORT.md`, funding link, support page | [ed92992](https://github.com/happysnaker/qq-ai-bot/commit/ed9299246e9bfab608985a362baafc305fab3088) | `sponsorware` topic; project homepage |
| [`RDLeader`](https://github.com/happysnaker/RDLeader) | agent-ops / local-first control plane | `README.md`, `SUPPORT.md`, `.github/SUPPORT.md`, funding link, support page | [9668390](https://github.com/happysnaker/RDLeader/commit/96683908e16210794278518b12fcc931de61345e) | `sponsorware` topic; project homepage |
| [`go-service-starter`](https://github.com/happysnaker/go-service-starter) | pinned Go backend starter | `README.md`, `.github/SUPPORT.md`, funding link, support page | [c30697c](https://github.com/happysnaker/go-service-starter/commit/c30697c956de7541ef26494ddc6f8a5687a84fd8) | `sponsorware`, `oss-maintenance`; project homepage |
| [`go-http-middleware-kit`](https://github.com/happysnaker/go-http-middleware-kit) | pinned Go middleware library | `README.md`, `.github/SUPPORT.md`, funding link, support page | [9a6739b](https://github.com/happysnaker/go-http-middleware-kit/commit/9a6739b0b3a15a29bbb22ee411e131108eaaf4af) | `sponsorware`, `oss-maintenance`; project homepage |
| [`happydb`](https://github.com/happysnaker/happydb) | pinned Java/database internals proof | `README.md`, `.github/SUPPORT.md`, funding link, support page | [9c244d3](https://github.com/happysnaker/happydb/commit/9c244d33f5c2f82d629a1ae872f687364cc11229) | `sponsorware`, `oss-maintenance`; project homepage |
| [`Resume`](https://github.com/happysnaker/Resume) | highest-star inbound surface | `README.md`, `.github/SUPPORT.md`, funding link, support page | [71841a1](https://github.com/happysnaker/Resume/commit/71841a1cbd0502d468e2c3b6afe1d6764e8a28a0) | `sponsorware`, `oss-maintenance`; project homepage |
| [`CSAPPLabsAndNotes`](https://github.com/happysnaker/CSAPPLabsAndNotes) | systems-learning inbound surface | `README.md`, `.github/SUPPORT.md`, funding link, support page | [61c9789](https://github.com/happysnaker/CSAPPLabsAndNotes/commit/61c97899dc252b10577a7e292f00afbbec95d26a) | `sponsorware`, `oss-maintenance`; project homepage |
| [`github-profile-checklist`](https://github.com/happysnaker/github-profile-checklist) | profile / README packaging funnel asset | `README.md`, `.github/SUPPORT.md`, funding link, support page | [ef4df0d](https://github.com/happysnaker/github-profile-checklist/commit/ef4df0d) | `sponsorware`, `oss-maintenance`; project homepage |
| [`.github`](https://github.com/happysnaker/.github) | account-wide community-health defaults | `SUPPORT.md`, `CONTRIBUTING.md`, funding link, support page | [0086d78](https://github.com/happysnaker/.github/commit/0086d78898c55ea700e458585581b89b687dc45b) | `sponsorware`, `oss-maintenance`; support homepage |

## Current support notes

Use concrete notes when supporting a specific work item:

- `qq-ai-bot #26 arm64` — real physical ARM / CasaOS validation.
- `RDLeader #27` — external submission review follow-up.
- `RDLeader #1` — public-safe DevPlan bundle sanitization.
- `RDLeader #3` — license posture / reuse boundary.
- `open-source maintenance` — general docs, CI, dependency, security, and packaging upkeep.

## Verification policy

For this coverage table, do not infer completion from intention. Evidence should come from:

- remote README / SUPPORT content assertions;
- evidence commits linked in the coverage table;
- GitHub repository metadata checks for homepage and topics;
- release existence for `v2026.07-sponsor-one-pager`;
- support page live checks when site content changes;
- security alert checks where the API is available.

Known caveat: some older repos do not have CodeQL analysis configured. Do not describe those as “CodeQL clean”; describe only the checks that were actually available, such as Dependabot and secret-scanning alert state.
