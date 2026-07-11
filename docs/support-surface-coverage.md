# Support surface coverage

> Public checklist showing which high-signal repositories route visitors to support pages, the frozen sponsor one-pager, and GitHub About metadata. This keeps sponsor routing auditable instead of hidden in one-off issue comments.

Snapshot: 2026-07-11 Asia/Shanghai.

## Canonical support assets

| Asset | Link | Purpose |
|---|---|---|
| Main support page | <https://happysnaker.github.io/support/> | QR codes, async review options, and project-specific support paths |
| Frozen sponsor one-pager | <https://github.com/happysnaker/happysnaker/releases/tag/v2026.07-sponsor-one-pager> | stable sponsor / curator brief for sharing |
| Source sponsor one-pager | [sponsor-one-pager.md](sponsor-one-pager.md) | editable source for future support updates |
| Sponsorware board | [sponsorware-board.md](sponsorware-board.md) | current and shipped sponsor targets |
| Share kit | [share-kit.md](share-kit.md) | copy-ready X / LinkedIn / WeChat / curator snippets with proof and sponsor guardrails |
| Operations cadence | [operations-cadence.md](operations-cadence.md) | maintenance loop and manual actions |

## Coverage table

| Repository | Why it matters | Support route | Frozen one-pager evidence | About metadata |
|---|---|---|---|---|
| [`profile README`](https://github.com/happysnaker/happysnaker) | main GitHub profile / proof hub entrypoint | README support section, sponsor board, coverage table | [4457f78](https://github.com/happysnaker/happysnaker/commit/4457f789b9c50a0bf7d3fc3060c983df08d070cf) | profile repo; public docs CI |
| [`support page`](https://happysnaker.github.io/support/) | main support / payment entrypoint | live support page, current concrete asks, frozen sponsor release, coverage table | [9eaf51a](https://github.com/happysnaker/happysnaker.github.io/commit/9eaf51a) | support homepage; Pages deployment; current asks route to `qq-ai-bot #26 arm64`, `RDLeader #27`, and quick-read review |
| [`project landing pages`](https://github.com/happysnaker/happysnaker.github.io) | GitHub Pages funnel for checklist / starter / systems project pages | project CTAs, local funding file, canonical / OpenGraph / Twitter / JSON-LD metadata, sitemap lastmod refresh, legacy private-link reroutes, RDLeader security proof, qq-ai-bot ARM/CasaOS tester path and copy/paste outreach snippet on project pages | [metadata](https://github.com/happysnaker/happysnaker.github.io/commit/c7da27e31e97e064c95d69bbb516b8f6f5e6b519), [sitemap](https://github.com/happysnaker/happysnaker.github.io/commit/42ad6755fb99b7a7bb7e8285010f83932b12a37b), [link hygiene](https://github.com/happysnaker/happysnaker.github.io/commit/60314e68d029cf69f4982005018e1855f469bf1f), [RDLeader security page](https://github.com/happysnaker/happysnaker.github.io/commit/e74e5ec), [qq-ai-bot tester path](https://github.com/happysnaker/happysnaker.github.io/commit/67aa7b7), [qq-ai-bot outreach snippet](https://github.com/happysnaker/happysnaker.github.io/commit/ee20d04) | site topics include `sponsorware`, `support`, `developer-portfolio`, `project-landing-pages` |
| [`qq-ai-bot`](https://github.com/happysnaker/qq-ai-bot) | flagship bot infrastructure / OneBot + ACP | `SUPPORT.md`, `.github/SUPPORT.md`, issue contact links, funding link, proof-before-payment, support page, support issue #28, arm64/CasaOS tester pack, homelab outreach kit | [#28 refresh](https://github.com/happysnaker/qq-ai-bot/issues/28#issuecomment-4937415575), [support proof path](https://github.com/happysnaker/qq-ai-bot/commit/b97bc42), [issue contact links](https://github.com/happysnaker/qq-ai-bot/commit/85a3ce5) | `sponsorware` topic; project homepage; support docs and issue-creation contact links now route proof-before-payment and current asks while preserving #26 physical-host validation |
| [`RDLeader license decision packet`](https://github.com/happysnaker/RDLeader/blob/main/docs/public/license-decision-packet.md) | reuse / license clarity for sponsors and curators | `SUPPORT.md`, `.github/SUPPORT.md`, license issue, README license section | [1e8f048](https://github.com/happysnaker/RDLeader/commit/1e8f0480503bc418e0ffd6758305957cadedbbbc) | license undecided; no root `LICENSE` yet |
| [`RDLeader`](https://github.com/happysnaker/RDLeader) | agent-ops / local-first control plane | `README.md`, `SUPPORT.md`, `.github/SUPPORT.md`, issue contact links, funding link, proof-before-payment, support page | [security proof](https://github.com/happysnaker/RDLeader/commit/58768cc), [support proof path](https://github.com/happysnaker/RDLeader/commit/e83ff4d), [issue contact links](https://github.com/happysnaker/RDLeader/commit/e7345e4) | `sponsorware` topic; project homepage; support docs and issue-creation contact links now route proof-before-payment and current asks while preserving license/reuse caveats |
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
| [`.github`](https://github.com/happysnaker/.github) | account-wide community-health defaults | `SUPPORT.md`, `.github/SUPPORT.md`, `CONTRIBUTING.md`, issue contact links, funding link, proof-before-payment path, current asks, support page | [support routes](https://github.com/happysnaker/.github/commit/4423803), [issue contact links](https://github.com/happysnaker/.github/commit/cb75da3) | `sponsorware`, `oss-maintenance`; default support routes and issue contact links now expose concrete payment notes and proof-before-payment |

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
- share-kit snippet / guardrail checks via `scripts/check_share_kit.py`;
- support page live checks when site content changes;
- `scripts/check_site_hygiene.py` for local/live project-page metadata, sitemap, public repo-link hygiene, and support-page proof-before-payment content;
- security alert checks where the API is available.

Latest proof-surface checks: scheduled profile CI now runs `python3 scripts/check_support_routes.py` to verify 17 remote funding/support/issue-contact files across profile, default `.github`, `qq-ai-bot`, and `RDLeader`; scheduled profile CI also runs `python3 scripts/check_repo_metadata.py` to verify core repository homepages, topics, descriptions, visibility, and archive state; scheduled profile CI verifies the frozen sponsor release with `python3 scripts/check_sponsor_release.py`; scheduled profile CI verifies share-kit snippets and guardrails with `python3 scripts/check_share_kit.py`; scheduled profile CI checks a local checkout of `happysnaker.github.io` with `python3 scripts/check_site_hygiene.py --site-root site/happysnaker.github.io --timeout 8`; `python3 scripts/check_public_links.py --timeout 6 --workers 8` checked 84 core sponsor/support/status links across `.github/SUPPORT.md`, profile issue contact links, sponsor one-pager, support coverage, and the flagship status snapshot; `python3 scripts/check_public_links.py --timeout 6 --workers 12 --scope profile` checked 318 profile-scope links across 12 files. Site metadata follow-up verified local/live canonical, OpenGraph image, Twitter card, JSON-LD, public repo-link hygiene, and the RDLeader sitemap `lastmod` refresh; the reusable site hygiene verifier checked 154 assertions with `python3 scripts/check_site_hygiene.py --site-root ../happysnaker.github.io --live --timeout 8`. The live support page now has a `Proof before payment` section linking the flagship technical map, flagship status snapshot, scheduled profile CI / CodeQL proof, maintenance proof, support coverage, and current concrete payment notes ([proof section](https://github.com/happysnaker/happysnaker.github.io/commit/d4c554b), [technical-map route](https://github.com/happysnaker/happysnaker.github.io/commit/c20b732), [stable workflow-link route](https://github.com/happysnaker/happysnaker.github.io/commit/cdce930), [Pages deploy](https://github.com/happysnaker/happysnaker.github.io/actions/runs/29140571745)).

Latest coverage security sweep: 2026-07-10 checked open Dependabot and secret-scanning alerts for the core support surfaces after RDLeader drizzle-orm remediation; `happysnaker`, `qq-ai-bot`, `RDLeader`, and `happysnaker.github.io` returned `[]` for open Dependabot and secret-scanning alerts. RDLeader runtime path hardening, canonical employee-id routing, Fastify rate limiting, README/SUPPORT evidence surfacing, the live RDLeader project-page security section, security-proof follow-up copy, and final strict `state=open` cleanup then passed [CI](https://github.com/happysnaker/RDLeader/actions/runs/29112782761), [CodeQL](https://github.com/happysnaker/RDLeader/actions/runs/29112782768), and [Pages deploy](https://github.com/happysnaker/happysnaker.github.io/actions/runs/29098623836), reducing RDLeader open CodeQL alerts to 0 and making the clean alert surface visible from the repository front door, the public project page, and curator/sponsor follow-up snippets. Do not generalize this to older repositories that do not have CodeQL configured.

Latest public-site private-link hygiene sweep: 2026-07-09 verified that the currently linked `happysnaker/*` repositories from the profile/site surface resolve to public repositories; legacy unavailable repository CTAs now route to public site pages or archives instead.

Known caveat: some older repos do not have CodeQL analysis configured. Do not describe those as “CodeQL clean”; describe only the checks that were actually available, such as Dependabot and secret-scanning alert state.
