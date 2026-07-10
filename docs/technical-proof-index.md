# Technical Proof Index

> A compact evidence map for the repos and public work I most want reviewed. This is intentionally source-linked: prefer the repo, CI, docs, and issues over broad claims.

Current proof hub release: <https://github.com/happysnaker/happysnaker/releases/tag/v2026.07-public-proof-hub>.
Portfolio audit: <https://github.com/happysnaker/happysnaker/blob/master/docs/portfolio-audit.md>.
Operations cadence: <https://github.com/happysnaker/happysnaker/blob/master/docs/operations-cadence.md>.

## Fast read

| Area | Best evidence | Why it matters |
|---|---|---|
| Bot infrastructure | [`qq-ai-bot`](https://github.com/happysnaker/qq-ai-bot) | OneBot transport, ACP agent bridge, session persistence, progress streaming, Docker, metrics, and deployment docs |
| Agent operations | [`RDLeader`](https://github.com/happysnaker/RDLeader) | Local-first control plane for AI R&D workers with runtime evidence, approvals, QA docs, and public CI |
| Systems learning | [`happydb`](https://github.com/happysnaker/happydb) | Java database internals: storage, B+ tree, MVCC, recovery, optimizer, and Raft experiments |
| Go service basics | [`go-service-starter`](https://github.com/happysnaker/go-service-starter) | Production-minded service starter: config, logging, health, graceful shutdown, Docker |
| Go middleware | [`go-http-middleware-kit`](https://github.com/happysnaker/go-http-middleware-kit) | Reusable net/http middleware for request IDs, logging, recovery, timeouts, and real IP handling |

## Flagship proof: qq-ai-bot

Public surfaces:

- Repo: <https://github.com/happysnaker/qq-ai-bot>
- Project page: <https://happysnaker.github.io/qq-ai-bot/>
- Public landing / proof ladder: <https://github.com/happysnaker/qq-ai-bot/blob/main/docs/public/landing-page.md>
- Ecosystem tracker: <https://github.com/happysnaker/qq-ai-bot/blob/main/docs/public/ecosystem-tracker.md>
- Promo kit with review follow-up snippets: <https://github.com/happysnaker/qq-ai-bot/blob/main/docs/public/promo-kit.md>
- Sponsorware roadmap: <https://github.com/happysnaker/qq-ai-bot/blob/main/docs/public/sponsorware.md>
- Sponsorware discussion: <https://github.com/happysnaker/qq-ai-bot/discussions/30>
- Metadata is aligned for GitHub search/profile cards: bot-infrastructure, metrics, multi-instance, sponsorware.
- Multi-instance notes: <https://github.com/happysnaker/qq-ai-bot/blob/main/docs/multi-instance-notes.md>
- Deployment validation: <https://github.com/happysnaker/qq-ai-bot/blob/main/docs/deployment-validation.md>
- arm64 / CasaOS install report template: <https://github.com/happysnaker/qq-ai-bot/blob/main/.github/ISSUE_TEMPLATE/arm64_casaos_report.md>
- arm64 Compose override: <https://github.com/happysnaker/qq-ai-bot/blob/main/docker-compose.arm64.yml>
- Reusable arm64 image smoke script: <https://github.com/happysnaker/qq-ai-bot/blob/main/scripts/smoke-arm64-image.sh>

Current evidence:

- Latest release: <https://github.com/happysnaker/qq-ai-bot/releases/tag/v0.1.7>
- Tag CI for v0.1.7: <https://github.com/happysnaker/qq-ai-bot/actions/runs/28968030296>
- Tag Docker image publish for v0.1.7: <https://github.com/happysnaker/qq-ai-bot/actions/runs/28968030324>
- Tag arm64 QEMU smoke for v0.1.7: <https://github.com/happysnaker/qq-ai-bot/actions/runs/28968114761>
- Latest landing/proof-ladder docs CI: <https://github.com/happysnaker/qq-ai-bot/actions/runs/28968624185>
- Latest landing/proof-ladder Docker publish: <https://github.com/happysnaker/qq-ai-bot/actions/runs/28968624066>
- Latest landing/proof-ladder arm64 smoke: <https://github.com/happysnaker/qq-ai-bot/actions/runs/28968761875>
- Ecosystem tracker CI: <https://github.com/happysnaker/qq-ai-bot/actions/runs/28973811909>
- Ecosystem tracker Docker publish: <https://github.com/happysnaker/qq-ai-bot/actions/runs/28973812030>
- Ecosystem tracker arm64 smoke: <https://github.com/happysnaker/qq-ai-bot/actions/runs/28973931073>
- Support-funnel refresh CI: <https://github.com/happysnaker/qq-ai-bot/actions/runs/28977581165>
- Support-funnel refresh CodeQL: <https://github.com/happysnaker/qq-ai-bot/actions/runs/28977581173>
- Support-funnel refresh Docker publish: <https://github.com/happysnaker/qq-ai-bot/actions/runs/28977581093>
- Support-funnel refresh arm64 smoke: <https://github.com/happysnaker/qq-ai-bot/actions/runs/28977689490>
- Ecosystem expansion refresh CI: <https://github.com/happysnaker/qq-ai-bot/actions/runs/28996238878>
- Ecosystem expansion refresh CodeQL: <https://github.com/happysnaker/qq-ai-bot/actions/runs/28996238891>
- Ecosystem expansion refresh Docker publish: <https://github.com/happysnaker/qq-ai-bot/actions/runs/28996238880>
- Ecosystem expansion refresh arm64 smoke: <https://github.com/happysnaker/qq-ai-bot/actions/runs/28996310644>
- Promotion outcome proof-run update CI: <https://github.com/happysnaker/qq-ai-bot/actions/runs/29026416836>
- Promotion outcome proof-run update CodeQL: <https://github.com/happysnaker/qq-ai-bot/actions/runs/29026415796>
- Promotion outcome proof-run update Docker publish: <https://github.com/happysnaker/qq-ai-bot/actions/runs/29026418551>
- Promotion outcome proof-run update arm64 smoke: <https://github.com/happysnaker/qq-ai-bot/actions/runs/29026549935>
- Promo follow-up snippets CI: <https://github.com/happysnaker/qq-ai-bot/actions/runs/29070102008>
- Promo follow-up snippets CodeQL: <https://github.com/happysnaker/qq-ai-bot/actions/runs/29070102007>
- Promo follow-up snippets Docker publish: <https://github.com/happysnaker/qq-ai-bot/actions/runs/29070102090>
- Promo follow-up snippets arm64 smoke: <https://github.com/happysnaker/qq-ai-bot/actions/runs/29070243291>
- CodeQL after transport hardening: <https://github.com/happysnaker/qq-ai-bot/actions/runs/28970038743>
- Feature release with Postgres session store: <https://github.com/happysnaker/qq-ai-bot/releases/tag/v0.1.6>
- Latest main CI after arm64 smoke-script docs: <https://github.com/happysnaker/qq-ai-bot/actions/runs/28958094897>
- Latest main Docker publish / multi-arch manifest refresh: <https://github.com/happysnaker/qq-ai-bot/actions/runs/28958094913>
- Latest README state refresh CI: <https://github.com/happysnaker/qq-ai-bot/actions/runs/28959110625>
- Latest README state refresh Docker publish: <https://github.com/happysnaker/qq-ai-bot/actions/runs/28959110697>
- Main-branch arm64 image smoke workflow: <https://github.com/happysnaker/qq-ai-bot/actions/runs/28965874894>
- AwesomeHomelab listing PR: <https://github.com/AwesomeHomelab/awesome-homelab/pull/98>
- NapCat Docker compose template merged: <https://github.com/NapNeko/NapCat-Docker/pull/132>
- ACP community awesome list merged: <https://github.com/nMaroulis/awesome-agent-client-protocol/pull/2>
- LLOneBot Nix integration PR: <https://github.com/LLOneBot/llonebot.nix/pull/22>
- Haxxnet Compose example closed/deferred as too young: <https://github.com/Haxxnet/Compose-Examples/pull/137>
- awesome-selfhosted issue closed/rule-deferred until release age is sufficient: <https://github.com/awesome-selfhosted/awesome-selfhosted-data/issues/2668>
- Public OneBot ecosystem placement: <https://onebot.dev/ecosystem>
- OneBot community discussion: <https://github.com/orgs/botuniverse/discussions/264>
- Official ACP clients docs PR merged: <https://github.com/agentclientprotocol/agent-client-protocol/pull/1592>

What to look for:

- latency histograms: `qq_ai_bot_turn_duration_seconds`, `qq_ai_bot_agent_roundtrip_seconds`, `qq_ai_bot_reply_send_seconds`;
- Postgres session store via `SESSION_STORE=postgres`;
- clear separation between QQ / OneBot transport and ACP-compatible agents;
- persistent sessions and explicit session-store tradeoffs;
- progress streaming back to QQ;
- Prometheus-style metrics and readiness/status endpoints;
- deployment honesty around Redis, multi-instance behavior, and OneBot WebSocket routing.

## Flagship proof: RDLeader

Public surfaces:

- Repo: <https://github.com/happysnaker/RDLeader>
- Public project page: <https://happysnaker.github.io/rdleader/>
- Public baseline pre-release: <https://github.com/happysnaker/RDLeader/releases/tag/v0.1.0-public-baseline>
- Public release roadmap: <https://github.com/happysnaker/RDLeader/blob/main/docs/public-release-roadmap.md>
- Public QA evidence: <https://github.com/happysnaker/RDLeader/blob/main/docs/public/qa-evidence.md>
- Runtime endurance model: <https://github.com/happysnaker/RDLeader/blob/main/docs/public/runtime-endurance.md>
- Demo walkthrough: <https://github.com/happysnaker/RDLeader/blob/main/docs/public/demo-walkthrough.md>
- Public-safe SVG demo assets: <https://github.com/happysnaker/RDLeader/blob/main/docs/public/demo-assets.md>
- Public-safe walkthrough video: <https://github.com/happysnaker/RDLeader/blob/main/docs/public/walkthrough-video.md>
- Runtime / approval deep dive: <https://github.com/happysnaker/RDLeader/blob/main/docs/public/runtime-approval-deep-dive.md>
- One-command public demo reset: <https://github.com/happysnaker/RDLeader/blob/main/docs/public/demo-reset.md>
- Employee-agent onboarding guide: <https://github.com/happysnaker/RDLeader/blob/main/docs/public/employee-agent-onboarding.md>
- Browser walkthrough over public demo state: <https://github.com/happysnaker/RDLeader/blob/main/docs/public/browser-walkthrough.md>
- Public landing-page section: <https://github.com/happysnaker/RDLeader/blob/main/docs/public/landing-page.md>
- Narrated browser walkthrough video: <https://github.com/happysnaker/RDLeader/blob/main/docs/public/narrated-walkthrough-video.md>
- Public demo distribution kit: <https://github.com/happysnaker/RDLeader/blob/main/docs/public/distribution-kit.md>
- Public submission/follow-up tracker: <https://github.com/happysnaker/RDLeader/blob/main/docs/public/submission-tracker.md>
- Public proof-ladder pre-release: <https://github.com/happysnaker/RDLeader/releases/tag/v0.1.1-public-proof-ladder>
- Public Show-and-tell discussion: <https://github.com/happysnaker/RDLeader/discussions/23>
- Public demo Q&A: <https://github.com/happysnaker/RDLeader/discussions/25>
- Profile proof-hub release for RDLeader demo kit: <https://github.com/happysnaker/happysnaker/releases/tag/v2026.07-rdleader-demo-kit>
- External PR: awesome-autonomous-agents: <https://github.com/jbesomi/awesome-autonomous-agents/pull/20>
- External PR merged: awesome-coding-agents: <https://github.com/kailiu42/awesome-coding-agents/pull/13>
- Promo kit: <https://github.com/happysnaker/RDLeader/blob/main/docs/public/promo-kit.md>
- License / reuse note: <https://github.com/happysnaker/RDLeader/blob/main/docs/public/license-decision.md>
- License decision packet: <https://github.com/happysnaker/RDLeader/blob/main/docs/public/license-decision-packet.md>
- Public roadmap discussion: <https://github.com/happysnaker/RDLeader/discussions/4>

Current evidence:

- Public CI on latest baseline: <https://github.com/happysnaker/RDLeader/actions/runs/28949090323>
- Public CI after walkthrough video: <https://github.com/happysnaker/RDLeader/actions/runs/28958624395>
- Public CI after runtime/approval deep dive: <https://github.com/happysnaker/RDLeader/actions/runs/28959592886>
- Public CI after next-sponsor-target link refresh: <https://github.com/happysnaker/RDLeader/actions/runs/28959719430>
- Public CI after demo reset path: <https://github.com/happysnaker/RDLeader/actions/runs/28960253396>
- Public CI after employee-agent onboarding target link refresh: <https://github.com/happysnaker/RDLeader/actions/runs/28960377824>
- Public CI after employee-agent onboarding guide and docs gate: <https://github.com/happysnaker/RDLeader/actions/runs/28960733793>
- Public CI after browser-walkthrough target link refresh: <https://github.com/happysnaker/RDLeader/actions/runs/28960890911>
- Public CI after browser walkthrough and demo seed mode: <https://github.com/happysnaker/RDLeader/actions/runs/28961498365>
- Public CI after landing-page target link refresh: <https://github.com/happysnaker/RDLeader/actions/runs/28961620848>
- Public CI after landing-page section: <https://github.com/happysnaker/RDLeader/actions/runs/28961948901>
- Public CI after narrated-walkthrough target link refresh: <https://github.com/happysnaker/RDLeader/actions/runs/28962053255>
- Public CI after narrated walkthrough video: <https://github.com/happysnaker/RDLeader/actions/runs/28962480308>
- Public CI after distribution-kit target link refresh: <https://github.com/happysnaker/RDLeader/actions/runs/28962594132>
- Public CI after distribution kit: <https://github.com/happysnaker/RDLeader/actions/runs/28962965032>
- Public CI after submission-tracker target link refresh: <https://github.com/happysnaker/RDLeader/actions/runs/28963077996>
- Public CI after submission tracker: <https://github.com/happysnaker/RDLeader/actions/runs/28963350579>
- Public CI after submission-batch target link refresh: <https://github.com/happysnaker/RDLeader/actions/runs/28963460740>
- Public CI after submission batch 1 tracker update: <https://github.com/happysnaker/RDLeader/actions/runs/28963810853>
- Public CI after submission batch 2 tracker update: <https://github.com/happysnaker/RDLeader/actions/runs/28964203194>
- Public CI after external-submission target link refresh: <https://github.com/happysnaker/RDLeader/actions/runs/28964342417>
- Public CI after external/community tracker update: <https://github.com/happysnaker/RDLeader/actions/runs/28964840654>
- Public CI after external-review target link refresh: <https://github.com/happysnaker/RDLeader/actions/runs/28964979942>
- CodeQL after RDLeader security hardening: <https://github.com/happysnaker/RDLeader/actions/runs/28971614737>
- Dependabot high-severity drizzle-orm advisory fixed: <https://github.com/happysnaker/RDLeader/actions/runs/28972228715>
- CodeQL after dependency security fix: <https://github.com/happysnaker/RDLeader/actions/runs/28972228636>
- Public CI after project-page distribution kit update: <https://github.com/happysnaker/RDLeader/actions/runs/28976906213>
- CodeQL after project-page distribution kit update: <https://github.com/happysnaker/RDLeader/actions/runs/28976906233>
- Public CI after RDLeader support-funnel refresh: <https://github.com/happysnaker/RDLeader/actions/runs/28977419611>
- CodeQL after RDLeader support-funnel refresh: <https://github.com/happysnaker/RDLeader/actions/runs/28977419605>
- Public packaging / DevPlan sanitization tracker: <https://github.com/happysnaker/RDLeader/issues/1>
- Public-safe demo sponsorware tracker: <https://github.com/happysnaker/RDLeader/issues/2> (closed with a rendered public walkthrough video)
- License hygiene tracker: <https://github.com/happysnaker/RDLeader/issues/3> (now has a decision packet; final owner choice still open)
- Runtime and approval sponsorware slice: <https://github.com/happysnaker/RDLeader/issues/14> (closed with public deep dive)
- One-command public demo reset sponsorware slice: <https://github.com/happysnaker/RDLeader/issues/15> (closed with `pnpm demo:reset`)
- Employee-agent onboarding sponsorware slice: <https://github.com/happysnaker/RDLeader/issues/16> (closed with public guide and `pnpm docs:check`)
- Browser walkthrough sponsorware slice: <https://github.com/happysnaker/RDLeader/issues/17> (closed with demo seed-mode support and browser walkthrough)
- Public landing-page sponsorware slice: <https://github.com/happysnaker/RDLeader/issues/18> (closed with proof ladder and copy snippets)
- Narrated browser walkthrough sponsorware slice: <https://github.com/happysnaker/RDLeader/issues/19> (closed with captioned MP4 and rebuild script)
- Public demo distribution kit sponsorware slice: <https://github.com/happysnaker/RDLeader/issues/20> (closed with copy snippets and target-community checklist)
- Public submission/follow-up tracker sponsorware slice: <https://github.com/happysnaker/RDLeader/issues/21> (closed with tracker and follow-up checklist)
- Public submission batch 1 sponsorware slice: <https://github.com/happysnaker/RDLeader/issues/22> (closed with proof-ladder release and Show-and-tell discussion)
- Public submission batch 2 sponsorware slice: <https://github.com/happysnaker/RDLeader/issues/24> (closed with public demo Q&A and profile proof-hub release)
- External/community submission sponsorware slice: <https://github.com/happysnaker/RDLeader/issues/26> (closed with one merged coding-agent awesome-list PR and one still-open autonomous-agent PR)
- Next sponsorware slice: external submission review follow-up: <https://github.com/happysnaker/RDLeader/issues/27>

What to look for:

- runtime boundaries instead of hidden chat sessions;
- structured task envelopes and runtime result events;
- stale task recovery and endurance posture;
- human-in-the-loop approval framing;
- public-safe documentation that avoids leaking private DevPlan artifacts.

## Upstream contribution signal

Recent upstream work is intentionally small but concrete: parser edge cases, retry semantics, CLI behavior, observability docs, and SDK/client correctness.

Stable ledger:

- [Upstream contribution ledger](upstream-contribution-ledger.md) — direct PR / issue URLs, current merged/open/closed state, CI/review notes, and next-action triage for tracked upstream work.

Representative shipped examples from the ledger:

- `spf13/pflag`: nil IP defaults, hex `UintSlice`, custom `IsBoolFlag` compatibility, SortFlags docs, and release-process docs.
- `cli/cli`: search docs and `gh skill install --dir` behavior.
- `go-chi/chi`: XML compression media types landed through the follow-up PR.
- `rclone/rclone`: `copyto` command description clarified.

Review lens:

- Does the change fix a real edge case?
- Is the behavior covered by tests or docs?
- Does the patch avoid broad rewrites?
- Does the PR reduce ambiguity for future users?

## Maintenance proof

Both current flagship repos have public, grouped dependency-maintenance config and a recent Dependabot queue sweep:

Profile docs now have public CI for local link integrity and sensitive-pattern checks, CodeQL for Python tooling, a manual public-link checker for sponsor/proof URLs, a reusable site hygiene verifier for project-page metadata / sitemap / public-repo-link checks, and repository secret scanning / push protection enabled. Latest profile tooling run: [CI](https://github.com/happysnaker/happysnaker/actions/runs/28994249998) and [CodeQL](https://github.com/happysnaker/happysnaker/actions/runs/28994250007).

- `qq-ai-bot`: npm and GitHub Actions Dependabot updates are grouped to reduce PR/job noise. The grouped npm-development PR [#42](https://github.com/happysnaker/qq-ai-bot/pull/42) merged on 2026-07-08 with passing CI; the older individual Dependabot PRs [#31](https://github.com/happysnaker/qq-ai-bot/pull/31)-[#40](https://github.com/happysnaker/qq-ai-bot/pull/40) are closed/superseded. Latest post-merge evidence: [CI](https://github.com/happysnaker/qq-ai-bot/actions/runs/28988955760), [CodeQL](https://github.com/happysnaker/qq-ai-bot/actions/runs/28988955689), [Docker publish](https://github.com/happysnaker/qq-ai-bot/actions/runs/28988955703), and [arm64 image smoke](https://github.com/happysnaker/qq-ai-bot/actions/runs/28989034477).
- `RDLeader`: npm and GitHub Actions Dependabot updates are grouped to reduce PR/job noise. The grouped npm-development PR [#13](https://github.com/happysnaker/RDLeader/pull/13) merged on 2026-07-08 with passing CI. Latest post-merge evidence: [CI](https://github.com/happysnaker/RDLeader/actions/runs/28988111295) and [CodeQL](https://github.com/happysnaker/RDLeader/actions/runs/28988111304).

## Sponsorware / support proof

Central board:

- <https://github.com/happysnaker/happysnaker/blob/master/docs/sponsorware-board.md>
- Sponsor one-pager: [sponsor-one-pager.md](sponsor-one-pager.md) / [frozen release](https://github.com/happysnaker/happysnaker/releases/tag/v2026.07-sponsor-one-pager)
- Support surface coverage: [support-surface-coverage.md](support-surface-coverage.md), including the paid [review page](https://happysnaker.github.io/review/) sponsor path ([site commit](https://github.com/happysnaker/happysnaker.github.io/commit/8e869fee9383832903e2a766510ce11c54ff4541))
- Public link checker: [scripts/check_public_links.py](../scripts/check_public_links.py) ([commit](https://github.com/happysnaker/happysnaker/commit/6af92879d651342ad5958f45f75981bc0ed08521)); latest profile-scope run checked 258 public links across README, this technical proof index, the upstream contribution ledger, and core proof docs.
- Public site hygiene verifier: [scripts/check_site_hygiene.py](../scripts/check_site_hygiene.py) ([commit](https://github.com/happysnaker/happysnaker/commit/ef88985863a24042f5f8be35c0b2979e44441d71)); latest live run checked 152 site hygiene assertions across project-page metadata, sitemap, and public repo-link hygiene.

Current sponsor targets are intentionally concrete:

- `qq-ai-bot`: arm64 / CasaOS validation remains open for a physical host report, but multi-arch GHCR image evidence, an arm64 Compose override, an install report template, a reusable smoke script, support-funnel refresh, and passing GitHub Actions QEMU arm64 smoke runs are documented, including v0.1.7 tag evidence; latency histograms shipped in v0.1.5 and Postgres session store shipped in v0.1.6;
- `RDLeader`: public-safe demo walkthrough, runtime/approval deep dive, one-command demo reset, employee-agent onboarding, browser walkthrough, landing-page copy, public project page, support-funnel refresh, narrated video, distribution kit, submission tracker, two submission batches, one merged coding-agent awesome-list PR, one open autonomous-agent PR, CodeQL hardening, and Dependabot advisory remediation are shipped; next sponsorable slices are review follow-up, DevPlan bundle sanitization, and license posture resolution.

Support page:

- <https://happysnaker.github.io/support/>

## Known caveats

- `RDLeader` is public but its final license posture is not decided yet; see <https://github.com/happysnaker/RDLeader/issues/3>.
- Some RDLeader evidence remains local until redacted because raw DevPlan logs can contain private paths or live integration identifiers.
- `qq-ai-bot` is stronger as a bot infrastructure scaffold than as a polished consumer-facing app.
