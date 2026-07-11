# Sponsor one-pager

> A short, source-linked sponsor brief for `happysnaker` projects. Use this when someone asks what to support, what proof exists, or which link to share.

Snapshot: 2026-07-11 Asia/Shanghai.

## Short pitch

I build public backend, systems, and agent-ops assets with evidence attached: runnable repos, CI, CodeQL, deployment notes, public project pages, sponsorware issues, and external ecosystem PRs.

The current flagship line is:

- [`qq-ai-bot`](https://github.com/happysnaker/qq-ai-bot) — self-hosted QQ / OneBot / NapCat / LLOneBot bridge for ACP-compatible agents, with sessions, progress streaming, metrics, Docker, multi-arch image publishing, and arm64 smoke evidence.
- [`RDLeader`](https://github.com/happysnaker/RDLeader) — local-first AI R&D worker control plane with task ownership, runtime dispatch, approval gates, fake-data demos, public QA evidence, and external submission follow-up.

Current proof snapshot:

- `qq-ai-bot` and `RDLeader` currently have `0` open CodeQL / Dependabot / secret-scanning alerts.
- `qq-ai-bot` latest CI / CodeQL / Docker publish / arm64 smoke are green.
- `RDLeader` latest CI / CodeQL are green.
- Current concrete asks: <https://happysnaker.github.io/support/#current-asks>.
- Proof-before-payment path: <https://happysnaker.github.io/support/#proof-before-payment>.
- Source-linked status table: [flagship-status-snapshot.md](flagship-status-snapshot.md).

## Best links to share

| Need | Link |
|---|---|
| Main support page | <https://happysnaker.github.io/support/> |
| Proof before payment | <https://happysnaker.github.io/support/#proof-before-payment> |
| `qq-ai-bot` project page | <https://happysnaker.github.io/qq-ai-bot/> |
| `qq-ai-bot` support route | <https://happysnaker.github.io/support/#from-qq-ai-bot> |
| `RDLeader` project page | <https://happysnaker.github.io/rdleader/> |
| `RDLeader` support route | <https://happysnaker.github.io/support/#from-rdleader> |
| Full proof index | [technical-proof-index.md](technical-proof-index.md) |
| Flagship status snapshot | [flagship-status-snapshot.md](flagship-status-snapshot.md) |
| Upstream contribution ledger | [upstream-contribution-ledger.md](upstream-contribution-ledger.md) |
| Current concrete asks | <https://happysnaker.github.io/support/#current-asks> |
| Current sponsor board | [sponsorware-board.md](sponsorware-board.md) |

## Current sponsor notes

Use concrete payment notes instead of a vague donation label:

| Payment note | What it funds | Public tracker |
|---|---|---|
| `qq-ai-bot #26 arm64` | real physical ARM / CasaOS validation on top of the existing QEMU smoke path | [`qq-ai-bot#26`](https://github.com/happysnaker/qq-ai-bot/issues/26) |
| `RDLeader #27` | external PR review follow-up and curator replies | [`RDLeader#27`](https://github.com/happysnaker/RDLeader/issues/27) |
| `RDLeader #1` | DevPlan feature sanitization into public-safe commits and docs | [`RDLeader#1`](https://github.com/happysnaker/RDLeader/issues/1) |
| `RDLeader #3` | license posture decision packet and final reuse boundary | [`RDLeader#3`](https://github.com/happysnaker/RDLeader/issues/3) |
| `open-source maintenance` | general docs, CI, dependency, security, and packaging upkeep | [operations cadence](operations-cadence.md) |

## Proof already shipped

### qq-ai-bot

- Stable release `v0.1.7`: <https://github.com/happysnaker/qq-ai-bot/releases/tag/v0.1.7>
- Public project page: <https://happysnaker.github.io/qq-ai-bot/>
- Support issue: <https://github.com/happysnaker/qq-ai-bot/issues/28>
- Ecosystem tracker: <https://github.com/happysnaker/qq-ai-bot/blob/main/docs/public/ecosystem-tracker.md>
- Promo kit / review follow-up snippets: <https://github.com/happysnaker/qq-ai-bot/blob/main/docs/public/promo-kit.md>
- Arm64 / CasaOS tester pack: <https://github.com/happysnaker/qq-ai-bot/blob/main/docs/public/arm64-casaos-tester-pack.md>
- Homelab / CasaOS outreach kit: <https://github.com/happysnaker/qq-ai-bot/blob/main/docs/public/homelab-outreach-kit.md>
- Arm64 image smoke workflow is live; the latest tester/outreach refresh passed CI, CodeQL, Docker publish, arm64 smoke, and the project page now exposes both the tester path and copy/paste homelab outreach snippet.
- External surfaces include OneBot ecosystem placement, merged NapCat docs, merged NapCat Docker template, merged ACP clients docs, merged ACP community awesome-list entry, and open LLOneBot / Docker Compose / CasaOS / Umbrel / AwesomeHomelab PRs.
- Shipped sponsorware slices include latency histograms (`v0.1.5`) and Postgres session store (`v0.1.6`).

### RDLeader

- Public project page: <https://happysnaker.github.io/rdleader/>
- Proof-ladder pre-release: <https://github.com/happysnaker/RDLeader/releases/tag/v0.1.1-public-proof-ladder>
- Public distribution kit: <https://github.com/happysnaker/RDLeader/blob/main/docs/public/distribution-kit.md>
- Public submission tracker: <https://github.com/happysnaker/RDLeader/blob/main/docs/public/submission-tracker.md>
- External distribution now has one merged coding-agent awesome-list PR and one still-open autonomous-agent PR, with the public project page linked in both PR bodies.
- Security hardening and dependency remediation are documented in the proof index; latest runtime path hardening, canonical employee-id routing, Fastify rate limiting, README/support proof surfacing, project-page security proof, and follow-up copy passed CI / CodeQL / Pages deploy and reduced RDLeader open CodeQL alerts from 30 to 0.

## Why support helps

Support turns unfinished but useful engineering work into public assets that other people can inspect:

- real deployment validation instead of vague “works on my machine” claims;
- short docs that explain architecture, failure modes, and tradeoffs;
- fake-data demos and videos instead of private screenshots;
- CI / CodeQL / dependency-maintenance evidence;
- external curator follow-up that keeps submissions from going stale;
- project-page and README packaging that makes serious work easier to discover.

## What sponsorship does not buy

- no private logs, credentials, app IDs, chat IDs, open IDs, QR artifacts, internal links, or payment screenshots;
- no claim that a platform has accepted a PR before it has actually merged;
- no promise to publish RDLeader private DevPlan evidence before it is redacted;
- no implied license grant for RDLeader until the license issue is resolved.

## Copy/paste outreach blurbs

### Short

```text
I’m supporting happysnaker’s open-source backend / agent-ops work: qq-ai-bot for OneBot + ACP bot infrastructure, and RDLeader for local-first AI worker control-plane research. The useful sponsor notes are `qq-ai-bot #26 arm64` or `RDLeader #27`.
```

### Curator / maintainer

```text
The strongest current public proof links are the project pages, not just the repos:

qq-ai-bot: https://happysnaker.github.io/qq-ai-bot/
RDLeader: https://happysnaker.github.io/rdleader/

Both pages link back to CI, docs, release, demo, and sponsorware evidence. If someone wants proof before paying, use https://happysnaker.github.io/support/#proof-before-payment first.
```

### Sponsor

```text
If you want to fund concrete OSS work, use a payment note like `qq-ai-bot #26 arm64` for real ARM/CasaOS validation or `RDLeader #27` for external submission follow-up. The public board is here: https://github.com/happysnaker/happysnaker/blob/master/docs/sponsorware-board.md
```
