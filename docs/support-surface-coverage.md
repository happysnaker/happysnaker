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
| [`profile README`](https://github.com/happysnaker/happysnaker) | main GitHub profile / proof hub entrypoint | README support section, sponsor board, coverage table | [4457f78](https://github.com/happysnaker/happysnaker/commit/4457f789b9c50a0bf7d3fc3060c983df08d070cf) | profile repo; public docs CI |
| [`support page`](https://happysnaker.github.io/support/) | main support / payment entrypoint | live support page, frozen sponsor release, coverage table | [e11f449](https://github.com/happysnaker/happysnaker.github.io/commit/e11f449486c9d0a7d9d2d95e9421d7009a9285cf) | support homepage; Pages deployment |
| [`project landing pages`](https://github.com/happysnaker/happysnaker.github.io) | GitHub Pages funnel for checklist / starter / systems project pages | project CTAs, local funding file, canonical / OpenGraph / Twitter / JSON-LD metadata, sitemap lastmod refresh, legacy private-link reroutes | [metadata](https://github.com/happysnaker/happysnaker.github.io/commit/c7da27e31e97e064c95d69bbb516b8f6f5e6b519), [sitemap](https://github.com/happysnaker/happysnaker.github.io/commit/42ad6755fb99b7a7bb7e8285010f83932b12a37b), [link hygiene](https://github.com/happysnaker/happysnaker.github.io/commit/60314e68d029cf69f4982005018e1855f469bf1f) | site topics include `sponsorware`, `support`, `developer-portfolio`, `project-landing-pages` |
| [`qq-ai-bot`](https://github.com/happysnaker/qq-ai-bot) | flagship bot infrastructure / OneBot + ACP | `SUPPORT.md`, `.github/SUPPORT.md`, funding link, support page | [ed92992](https://github.com/happysnaker/qq-ai-bot/commit/ed9299246e9bfab608985a362baafc305fab3088) | `sponsorware` topic; project homepage |
| [`RDLeader license decision packet`](https://github.com/happysnaker/RDLeader/blob/main/docs/public/license-decision-packet.md) | reuse / license clarity for sponsors and curators | `SUPPORT.md`, `.github/SUPPORT.md`, license issue, README license section | [1e8f048](https://github.com/happysnaker/RDLeader/commit/1e8f0480503bc418e0ffd6758305957cadedbbbc) | license undecided; no root `LICENSE` yet |
| [`RDLeader`](https://github.com/happysnaker/RDLeader) | agent-ops / local-first control plane | `README.md`, `SUPPORT.md`, `.github/SUPPORT.md`, funding link, support page | [9668390](https://github.com/happysnaker/RDLeader/commit/96683908e16210794278518b12fcc931de61345e) | `sponsorware` topic; project homepage |
| [`go-service-starter`](https://github.com/happysnaker/go-service-starter) | pinned Go backend starter | `README.md`, `.github/SUPPORT.md`, funding link, support page | [c30697c](https://github.com/happysnaker/go-service-starter/commit/c30697c956de7541ef26494ddc6f8a5687a84fd8) | `sponsorware`, `oss-maintenance`; project homepage |
| [`go-http-middleware-kit`](https://github.com/happysnaker/go-http-middleware-kit) | pinned Go middleware library | `README.md`, `.github/SUPPORT.md`, funding link, support page | [9a6739b](https://github.com/happysnaker/go-http-middleware-kit/commit/9a6739b0b3a15a29bbb22ee411e131108eaaf4af) | `sponsorware`, `oss-maintenance`; project homepage |
| [`happydb`](https://github.com/happysnaker/happydb) | pinned Java/database internals proof | `README.md`, `.github/SUPPORT.md`, funding link, support page | [9c244d3](https://github.com/happysnaker/happydb/commit/9c244d33f5c2f82d629a1ae872f687364cc11229) | `sponsorware`, `oss-maintenance`; project homepage |
| [`Resume`](https://github.com/happysnaker/Resume) | highest-star inbound surface | `README.md`, `.github/SUPPORT.md`, funding link, support page | [71841a1](https://github.com/happysnaker/Resume/commit/71841a1cbd0502d468e2c3b6afe1d6764e8a28a0) | `sponsorware`, `oss-maintenance`; project homepage |
| [`CSAPPLabsAndNotes`](https://github.com/happysnaker/CSAPPLabsAndNotes) | systems-learning inbound surface | `README.md`, `.github/SUPPORT.md`, funding link, support page | [61c9789](https://github.com/happysnaker/CSAPPLabsAndNotes/commit/61c97899dc252b10577a7e292f00afbbec95d26a) | `sponsorware`, `oss-maintenance`; project homepage |
| [`github-profile-checklist`](https://github.com/happysnaker/github-profile-checklist) | profile / README packaging funnel asset | `README.md`, `.github/SUPPORT.md`, funding link, support page | [ef4df0d](https://github.com/happysnaker/github-profile-checklist/commit/ef4df0d) | `sponsorware`, `oss-maintenance`; project homepage |
| [`review page`](https://happysnaker.github.io/review/) | paid profile / README packaging conversion page | live review page, support page, frozen sponsor release | [8e869fe](https://github.com/happysnaker/happysnaker.github.io/commit/8e869fee9383832903e2a766510ce11c54ff4541) | project page; Pages deployment |
| [`backend-engineer-checklist`](https://github.com/happysnaker/backend-engineer-checklist) | backend interview / self-review funnel asset | `README.md`, `.github/SUPPORT.md`, funding link, support page | [fe622d3](https://github.com/happysnaker/backend-engineer-checklist/commit/fe622d3) | `sponsorware`, `oss-maintenance`; project homepage |
| [`system-design-checklist`](https://github.com/happysnaker/system-design-checklist) | system design / architecture review funnel asset | `README.md`, `.github/SUPPORT.md`, funding link, support page | [683fe0c](https://github.com/happysnaker/system-design-checklist/commit/683fe0c) | `sponsorware`, `oss-maintenance`; project homepage |
| [`production-readiness-checklist`](https://github.com/happysnaker/production-readiness-checklist) | release / reliability checklist funnel asset | `README.md`, `.github/SUPPORT.md`, funding link, support page | [d778196](https://github.com/happysnaker/production-readiness-checklist/commit/d778196) | `sponsorware`, `oss-maintenance`; project homepage |
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
- `scripts/check_site_hygiene.py` for local/live project-page metadata, sitemap, and public repo-link hygiene;
- security alert checks where the API is available.

Latest broader check: `python3 scripts/check_public_links.py --scope profile --timeout 6` checked 258 public links across README, the technical proof index, the upstream contribution ledger, and core proof docs. Site metadata follow-up also verified canonical, OpenGraph image, Twitter card, JSON-LD, and refreshed sitemap `lastmod` coverage for changed project landing pages. The reusable site hygiene verifier checked 152 assertions with `python3 scripts/check_site_hygiene.py --site-root ../happysnaker.github.io --expected-lastmod 2026-07-09 --live --timeout 8`.

Latest coverage security sweep: 2026-07-10 checked open Dependabot and secret-scanning alerts for the core support surfaces after RDLeader drizzle-orm remediation; `happysnaker`, `qq-ai-bot`, `RDLeader`, and `happysnaker.github.io` returned `[]` for open Dependabot and secret-scanning alerts. CodeQL open-alert state still needs separate per-alert triage before making broad “all clean” claims.

Latest public-site private-link hygiene sweep: 2026-07-09 verified that the currently linked `happysnaker/*` repositories from the profile/site surface resolve to public repositories; legacy unavailable repository CTAs now route to public site pages or archives instead.

Known caveat: some older repos do not have CodeQL analysis configured. Do not describe those as “CodeQL clean”; describe only the checks that were actually available, such as Dependabot and secret-scanning alert state.
