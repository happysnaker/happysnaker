# Current Sponsorware Board

> Concrete public work that can be accelerated by sponsorship. The core projects remain public; sponsorship funds implementation, documentation, validation, and packaging work that takes time to do well.

Support page: <https://happysnaker.github.io/support/>

## How to sponsor a specific item

Use the issue number in the payment note or follow-up email:

- `qq-ai-bot #23`
- `qq-ai-bot #24`
- `qq-ai-bot #26`
- `RDLeader #2`
- `RDLeader #1`

If you are not sure which item fits, use `open-source maintenance` or the project name.

## Current targets

| Project | Target | Funding use | Public issue |
|---|---|---|---|
| `qq-ai-bot` | End-to-end latency histograms | **shipped in [v0.1.5](https://github.com/happysnaker/qq-ai-bot/releases/tag/v0.1.5)** | [#23](https://github.com/happysnaker/qq-ai-bot/issues/23) |
| `qq-ai-bot` | Postgres session store | **shipped in [v0.1.6](https://github.com/happysnaker/qq-ai-bot/releases/tag/v0.1.6)** | [#24](https://github.com/happysnaker/qq-ai-bot/issues/24) |
| `qq-ai-bot` | arm64 / CasaOS validation | Multi-arch image evidence and report template documented; real CasaOS/arm64 install report still open | [#26](https://github.com/happysnaker/qq-ai-bot/issues/26) |
| `RDLeader` | Public-safe demo walkthrough | Create fake-data screenshots or a short demo video for the agent-ops control plane | [#2](https://github.com/happysnaker/RDLeader/issues/2) |
| `RDLeader` | DevPlan bundle sanitization | Split local features into public-safe commits and docs | [#1](https://github.com/happysnaker/RDLeader/issues/1) |


## Recently shipped

| Project | Shipped item | Evidence |
|---|---|---|
| `qq-ai-bot` | End-to-end turn / agent / reply latency histograms | [v0.1.5](https://github.com/happysnaker/qq-ai-bot/releases/tag/v0.1.5), [#23](https://github.com/happysnaker/qq-ai-bot/issues/23) |
| `qq-ai-bot` | Postgres session store | [v0.1.6](https://github.com/happysnaker/qq-ai-bot/releases/tag/v0.1.6), [#24](https://github.com/happysnaker/qq-ai-bot/issues/24) |

## What sponsorship funds

Sponsorship funds public work by default:

- implementation work;
- tests, smoke checks, or validation where practical;
- README / documentation updates;
- public demo assets;
- issue closure with evidence;
- clear caveats and non-goals.

## What sponsorship does not imply

Sponsorship does not mean:

- publishing private credentials, screenshots, logs, or workspace paths;
- bypassing platform safety boundaries;
- promising exact timelines for external systems outside maintainer control;
- merging unreviewable changes;
- implying unrestricted reuse for projects whose license posture is still undecided.

## Project-specific notes

### qq-ai-bot

`qq-ai-bot` is the strongest current flagship: a self-hosted QQ ↔ AI bridge for OneBot 11 / NapCat / LLOneBot and ACP-compatible agents. The public sponsor targets are operator-facing features: observability, session storage, and deployment validation.

Useful links:

- Repo: <https://github.com/happysnaker/qq-ai-bot>
- Promo kit: <https://github.com/happysnaker/qq-ai-bot/blob/main/docs/public/promo-kit.md>
- Sponsorware roadmap: <https://github.com/happysnaker/qq-ai-bot/blob/main/docs/public/sponsorware.md>

### RDLeader

`RDLeader` is a local-first control-plane experiment for supervising AI R&D workers. The public sponsor targets focus on safe packaging: fake-data demos, public QA evidence, runtime endurance explanations, and DevPlan bundle sanitization.

Useful links:

- Repo: <https://github.com/happysnaker/RDLeader>
- Public release roadmap: <https://github.com/happysnaker/RDLeader/blob/main/docs/public-release-roadmap.md>
- Public demo walkthrough: <https://github.com/happysnaker/RDLeader/blob/main/docs/public/demo-walkthrough.md>
- License posture tracker: <https://github.com/happysnaker/RDLeader/issues/3>
