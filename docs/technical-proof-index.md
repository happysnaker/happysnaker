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
- Sponsor/support issue: <https://github.com/happysnaker/qq-ai-bot/issues/28>
- Sponsorware discussion: <https://github.com/happysnaker/qq-ai-bot/discussions/30>
- Metadata is aligned for GitHub search/profile cards: bot-infrastructure, metrics, multi-instance, sponsorware.
- Multi-instance notes: <https://github.com/happysnaker/qq-ai-bot/blob/main/docs/multi-instance-notes.md>
- Deployment validation: <https://github.com/happysnaker/qq-ai-bot/blob/main/docs/deployment-validation.md>
- arm64 / CasaOS tester pack: <https://github.com/happysnaker/qq-ai-bot/blob/main/docs/public/arm64-casaos-tester-pack.md>
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
- Support proof-link refresh CI: <https://github.com/happysnaker/qq-ai-bot/actions/runs/29072149755>
- Support proof-link refresh CodeQL: <https://github.com/happysnaker/qq-ai-bot/actions/runs/29072149862>
- Support proof-link refresh Docker publish: <https://github.com/happysnaker/qq-ai-bot/actions/runs/29072149756>
- Support proof-link refresh arm64 smoke: <https://github.com/happysnaker/qq-ai-bot/actions/runs/29072241215>
- Arm64 / CasaOS tester pack CI: <https://github.com/happysnaker/qq-ai-bot/actions/runs/29100637570>
- Arm64 / CasaOS tester pack CodeQL: <https://github.com/happysnaker/qq-ai-bot/actions/runs/29100637607>
- Arm64 / CasaOS tester pack Docker publish: <https://github.com/happysnaker/qq-ai-bot/actions/runs/29100637608>
- Arm64 / CasaOS tester pack arm64 smoke: <https://github.com/happysnaker/qq-ai-bot/actions/runs/29100777408>
- Homelab / CasaOS outreach kit CI: <https://github.com/happysnaker/qq-ai-bot/actions/runs/29102776397>
- Homelab / CasaOS outreach kit CodeQL: <https://github.com/happysnaker/qq-ai-bot/actions/runs/29102776374>
- Homelab / CasaOS outreach kit Docker publish: <https://github.com/happysnaker/qq-ai-bot/actions/runs/29102776459>
- Homelab / CasaOS outreach kit arm64 smoke: <https://github.com/happysnaker/qq-ai-bot/actions/runs/29102901202>
- qq-ai-bot project-page tester path Pages deploy: <https://github.com/happysnaker/happysnaker.github.io/actions/runs/29101759975>
- qq-ai-bot project-page outreach snippet Pages deploy: <https://github.com/happysnaker/happysnaker.github.io/actions/runs/29103814071>
- Support page current-asks Pages deploy: <https://github.com/happysnaker/happysnaker.github.io/actions/runs/29106752206>
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
- CI restored after DevPlan feature-bundle publish / public docs gate repair: <https://github.com/happysnaker/RDLeader/actions/runs/29092788671>
- CodeQL after DevPlan feature-bundle publish / public docs gate repair: <https://github.com/happysnaker/RDLeader/actions/runs/29092788589>
- CI after drizzle-orm advisory remediation: <https://github.com/happysnaker/RDLeader/actions/runs/29092989950>
- CodeQL after drizzle-orm advisory remediation: <https://github.com/happysnaker/RDLeader/actions/runs/29092989978>
- CI after runtime path-injection hardening: <https://github.com/happysnaker/RDLeader/actions/runs/29094205044>
- CodeQL after runtime path-injection hardening: <https://github.com/happysnaker/RDLeader/actions/runs/29094205114>
- CI after canonical employee-id routing and route rate limiting: <https://github.com/happysnaker/RDLeader/actions/runs/29096512796>
- CodeQL after canonical employee-id routing and route rate limiting: <https://github.com/happysnaker/RDLeader/actions/runs/29096512589>
- CI after surfacing security proof in README / support docs: <https://github.com/happysnaker/RDLeader/actions/runs/29097583133>
- CodeQL after surfacing security proof in README / support docs: <https://github.com/happysnaker/RDLeader/actions/runs/29097583129>
- CI after final RDLeader CodeQL alert cleanup: <https://github.com/happysnaker/RDLeader/actions/runs/29112782761>
- CodeQL after final RDLeader CodeQL alert cleanup: <https://github.com/happysnaker/RDLeader/actions/runs/29112782768>
- RDLeader project-page security proof Pages deploy: <https://github.com/happysnaker/happysnaker.github.io/actions/runs/29098623836>
- CI after security-proof follow-up copy / submission tracker refresh: <https://github.com/happysnaker/RDLeader/actions/runs/29099617850>
- CodeQL after security-proof follow-up copy / submission tracker refresh: <https://github.com/happysnaker/RDLeader/actions/runs/29099618434>
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

Profile docs now have public CI for local link integrity and sensitive-pattern checks, CodeQL for Python tooling, a manual public-link checker for sponsor/proof URLs, a reusable site hygiene verifier for project-page metadata / sitemap / public-repo-link checks plus support-page proof-before-payment and stable workflow-link checks, repository secret scanning / push protection enabled, and first-screen CI / CodeQL badges for the profile repo, `qq-ai-bot`, and `RDLeader`. Use the stable [profile CI workflow](https://github.com/happysnaker/happysnaker/actions/workflows/ci.yml), [profile CodeQL workflow](https://github.com/happysnaker/happysnaker/actions/workflows/codeql.yml), and [flagship status snapshot](flagship-status-snapshot.md) instead of a stale one-off run link; `python3 scripts/check_github_status.py` is the live source of truth.

- `qq-ai-bot`: npm and GitHub Actions Dependabot updates are grouped to reduce PR/job noise. The grouped npm-development PR [#42](https://github.com/happysnaker/qq-ai-bot/pull/42) merged on 2026-07-08 with passing CI; the older individual Dependabot PRs [#31](https://github.com/happysnaker/qq-ai-bot/pull/31)-[#40](https://github.com/happysnaker/qq-ai-bot/pull/40) are closed/superseded. Latest issue-contact refresh evidence after routing SUPPORT and issue-template contact links to proof-before-payment: [CI](https://github.com/happysnaker/qq-ai-bot/actions/runs/29136419535), [CodeQL](https://github.com/happysnaker/qq-ai-bot/actions/runs/29136419564), [Docker publish](https://github.com/happysnaker/qq-ai-bot/actions/runs/29136419547), and [arm64 image smoke](https://github.com/happysnaker/qq-ai-bot/actions/runs/29136482772).
- `RDLeader`: npm and GitHub Actions Dependabot updates are grouped to reduce PR/job noise. The grouped npm-development PR [#13](https://github.com/happysnaker/RDLeader/pull/13) merged on 2026-07-08 with passing CI. Latest maintenance evidence: [CI restored after DevPlan feature-bundle publish](https://github.com/happysnaker/RDLeader/actions/runs/29092788671), [drizzle-orm advisory remediation CI](https://github.com/happysnaker/RDLeader/actions/runs/29092989950), [runtime path-injection hardening CI](https://github.com/happysnaker/RDLeader/actions/runs/29094205044), [CodeQL after canonical employee-id routing plus route rate limiting](https://github.com/happysnaker/RDLeader/actions/runs/29096512589), [README/security-proof surfacing CI](https://github.com/happysnaker/RDLeader/actions/runs/29097583133), [project-page security proof deploy](https://github.com/happysnaker/happysnaker.github.io/actions/runs/29098623836), [security-proof follow-up copy CI](https://github.com/happysnaker/RDLeader/actions/runs/29099617850), [final CodeQL cleanup run](https://github.com/happysnaker/RDLeader/actions/runs/29112782768), support-proof refresh [CI](https://github.com/happysnaker/RDLeader/actions/runs/29136017531) and [CodeQL](https://github.com/happysnaker/RDLeader/actions/runs/29136017533), and issue-contact refresh [CI](https://github.com/happysnaker/RDLeader/actions/runs/29136421077) and [CodeQL](https://github.com/happysnaker/RDLeader/actions/runs/29136421002). The latest strict `state=open` security sweep shows RDLeader open Dependabot alerts at `0`, open secret-scanning alerts at `0`, and open CodeQL alerts at `0` after reducing the public DevPlan feature-bundle alert backlog to zero; the RDLeader README, support docs, public project page, promo kit, and submission tracker now expose that clean configured alert surface directly.

## Sponsorware / support proof

Central board:

- <https://github.com/happysnaker/happysnaker/blob/master/docs/sponsorware-board.md>
- Sponsor one-pager: [sponsor-one-pager.md](sponsor-one-pager.md) / [frozen release](https://github.com/happysnaker/happysnaker/releases/tag/v2026.07-sponsor-one-pager)
- Operator handoff: [operator-handoff.md](operator-handoff.md) — first-read state map for future GitHub takeover turns
- Share kit: [share-kit.md](share-kit.md) — copy-ready X / LinkedIn / WeChat / curator snippets with proof and sponsor guardrails
- Flagship technical map: [flagship-technical-map.md](flagship-technical-map.md)
- Support page current asks: <https://happysnaker.github.io/support/#current-asks>
- Support page proof-before-payment section: <https://happysnaker.github.io/support/#proof-before-payment> ([proof section](https://github.com/happysnaker/happysnaker.github.io/commit/d4c554b), [technical-map route](https://github.com/happysnaker/happysnaker.github.io/commit/c20b732), [stable workflow-link route](https://github.com/happysnaker/happysnaker.github.io/commit/cdce930), [share-kit route](https://github.com/happysnaker/happysnaker.github.io/commit/71696ea), [Pages deploy](https://github.com/happysnaker/happysnaker.github.io/actions/runs/29144326082))
- Repo-local GitHub support file: [.github/SUPPORT.md](../.github/SUPPORT.md), now routed to proof-before-payment, current asks, share kit, sponsor one-pager, deploy-read sample, and concrete payment notes.
- Account-wide default support files: <https://github.com/happysnaker/.github/blob/main/SUPPORT.md> and <https://github.com/happysnaker/.github/blob/main/.github/SUPPORT.md> ([support commit](https://github.com/happysnaker/.github/commit/4423803), [share-kit commit](https://github.com/happysnaker/.github/commit/7bbaab8), [deploy-read defaults](https://github.com/happysnaker/.github/commit/a747985)) route repositories without local support files to the same proof-before-payment, share-kit, deploy-read, and concrete payment-note flow.
- Flagship repo support files: `qq-ai-bot` [SUPPORT.md](https://github.com/happysnaker/qq-ai-bot/blob/main/SUPPORT.md) / [.github/SUPPORT.md](https://github.com/happysnaker/qq-ai-bot/blob/main/.github/SUPPORT.md) and `RDLeader` [SUPPORT.md](https://github.com/happysnaker/RDLeader/blob/main/SUPPORT.md) / [.github/SUPPORT.md](https://github.com/happysnaker/RDLeader/blob/main/.github/SUPPORT.md) now route to proof-before-payment, current asks, share kit, and deploy-read paid-review paths ([qq-ai-bot support proof](https://github.com/happysnaker/qq-ai-bot/commit/b97bc42), [qq-ai-bot deploy-read route](https://github.com/happysnaker/qq-ai-bot/commit/0f13edc), [RDLeader support proof](https://github.com/happysnaker/RDLeader/commit/e83ff4d), [RDLeader deploy-read route](https://github.com/happysnaker/RDLeader/commit/2b0ad6a)).
- GitHub issue contact links now expose proof-before-payment, current asks, and share-kit routes from the default `.github` community-health repo, the profile repo, `qq-ai-bot`, and `RDLeader` ([default proof/contact commit](https://github.com/happysnaker/.github/commit/cb75da3), [default share-kit commit](https://github.com/happysnaker/.github/commit/7bbaab8), [qq-ai-bot commit](https://github.com/happysnaker/qq-ai-bot/commit/85a3ce5), [RDLeader commit](https://github.com/happysnaker/RDLeader/commit/e7345e4)).
- qq-ai-bot support issue #28 routes current asks, tester pack, and latest proof: <https://github.com/happysnaker/qq-ai-bot/issues/28>
- Support surface coverage: [support-surface-coverage.md](support-surface-coverage.md), including the paid [review page](https://happysnaker.github.io/review/) sponsor path ([site commit](https://github.com/happysnaker/happysnaker.github.io/commit/8e869fee9383832903e2a766510ce11c54ff4541))
- Profile preflight runner: [scripts/run_profile_preflight.py](../scripts/run_profile_preflight.py) — wraps public-docs, GitHub CLI helper usage, share-kit, README badge, GitHub status, support-route, metadata, sponsor-release, sponsor-issue, paid-review funnel, operations-log, issue-label, manual-blocker, public-link, and external-follow-up checks into one command; supports `--external-only`, external `--action-class` filters, `--external-summary`, and scheduled-review due gating.
- README badge checker: [scripts/check_readme_badges.py](../scripts/check_readme_badges.py) — verifies first-screen CI / CodeQL badges and remote workflow-file existence for profile, `qq-ai-bot`, and `RDLeader`.
- Stable profile proof-link checker: [scripts/check_stable_profile_links.py](../scripts/check_stable_profile_links.py) — rejects one-off profile self-check run links in public docs; README, proof docs, sponsor release, and the status snapshot use stable profile workflow links instead.
- Shared GitHub CLI helper: [scripts/github_cli.py](../scripts/github_cli.py) — centralizes retry handling for transient GitHub API/network errors used by the proof checkers.
- GitHub CLI usage checker: [scripts/check_gh_usage.py](../scripts/check_gh_usage.py) — prevents new proof checkers from bypassing the shared retry helper with direct `gh` subprocess calls.
- CI workflow contract checker: [scripts/check_ci_workflow_contract.py](../scripts/check_ci_workflow_contract.py) — verifies scheduled CI keeps compiling every proof checker and keeps the required GH_TOKEN-backed drift checks wired.
- Operator handoff checker: [scripts/check_operator_handoff.py](../scripts/check_operator_handoff.py) — verifies the first-read handoff keeps current source-of-truth commands, blockers, external-follow-up rules, and overclaim guardrails.
- Checker catalog checker: [scripts/check_checker_catalog.py](../scripts/check_checker_catalog.py) — verifies this proof index documents every `scripts/check_*.py` proof checker so new checks do not become invisible; supports `--json` for machine-readable handoff state.
- GitHub status checker: [scripts/check_github_status.py](../scripts/check_github_status.py) — latest run verified profile, qq-ai-bot, RDLeader, and Pages workflows plus configured alert counts; `--summary` emits compact machine-readable status JSON and `--markdown` generates the shareable [flagship status snapshot](flagship-status-snapshot.md).
- Support route checker: [scripts/check_support_routes.py](../scripts/check_support_routes.py) — verifies profile, default `.github`, `qq-ai-bot`, and `RDLeader` funding/support/issue-contact files still route to proof-before-payment, current asks, share kit, and concrete payment notes; this now runs in scheduled profile CI, including weekly drift checks.
- Repository metadata checker: [scripts/check_repo_metadata.py](../scripts/check_repo_metadata.py) — verifies the core profile, flagship, Pages, and default community-health repository homepages, topics, descriptions, visibility, and archive state; this now runs in scheduled profile CI, including weekly drift checks.
- Sponsor release checker: [scripts/check_sponsor_release.py](../scripts/check_sponsor_release.py) — verifies the source sponsor one-pager and frozen sponsor release both expose reproducible proof commands, stay compact enough for GitHub release limits, include the issue #2 operations-log route, and still contain proof-before-payment, share-kit, and concrete payment-note routes; supports `--json` for machine-readable release/source state.
- Sponsor issue checker: [scripts/check_sponsor_issues.py](../scripts/check_sponsor_issues.py) — verifies the live `qq-ai-bot` / `RDLeader` sponsorship issues stay open, keep stable workflow proof links instead of stale one-off run URLs, route to proof-before-payment / current asks, and preserve redaction / license guardrails; supports `--json` for machine-readable live issue state.
- Review funnel checker: [scripts/check_review_funnel.py](../scripts/check_review_funnel.py) — verifies the public Pages paid-review path across support, review, deploy-read sample, and `qq-ai-bot` pages keeps the `¥29.9` / `¥99` offers, deploy-read sample links, mailto templates, payment-screenshot fields, and sitemap entry intact; supports `--live` for post-deploy checks and `--json` for machine-readable handoff state.
- Operations log checker: [scripts/check_ops_issue_log.py](../scripts/check_ops_issue_log.py) — verifies [issue #2](https://github.com/happysnaker/happysnaker/issues/2) remains the open append-only operations log with evidence and verification markers now that the release body is compact.
- Issue label checker: [scripts/check_issue_labels.py](../scripts/check_issue_labels.py) — verifies profile, `qq-ai-bot`, and `RDLeader` sponsor/manual/open-loop issues keep public triage labels such as `sponsorship`, `validation`, `external-follow-up`, `manual-action`, and `license`.
- External follow-up checker: [scripts/check_external_followups.py](../scripts/check_external_followups.py) — summarizes the tracked external PRs plus `qq-ai-bot#26` and `RDLeader#27` with machine-readable action classes and next-action guidance, without posting comments; supports `--action-class` filtering and `--summary` output for scheduled review.
- Profile pin checker: [scripts/check_profile_pins.py](../scripts/check_profile_pins.py) — reports whether the recommended technical-first pinned set still requires the manual `Resume` → `RDLeader` swap; CI runs it in report-only mode, while `--strict` is available for post-manual-change verification.
- RDLeader license posture checker: [scripts/check_rdleader_license.py](../scripts/check_rdleader_license.py) — reports whether RDLeader license metadata, root `LICENSE`, and issue #3 have resolved; CI runs it in report-only mode to keep reuse-rights claims guarded.
- Manual blockers checker: [scripts/check_manual_blockers.py](../scripts/check_manual_blockers.py) — summarizes the profile-pin and RDLeader-license blockers, and verifies [issue #1](https://github.com/happysnaker/happysnaker/issues/1) stays open/labeled/aligned with the latest manual guidance; supports `--json` for machine-readable blocker state and `--strict` after both manual actions are complete.
- Share kit checker: [scripts/check_share_kit.py](../scripts/check_share_kit.py) — verifies copy-ready share snippets keep proof-before-payment links, current support notes, and overclaim guardrails before they are used for sponsor/project promotion; supports `--json` for machine-readable snippet / guardrail status.
- Public link checker: [scripts/check_public_links.py](../scripts/check_public_links.py) ([commit](https://github.com/happysnaker/happysnaker/commit/6af92879d651342ad5958f45f75981bc0ed08521)); use `--scope core --workers 8` for the core sponsor/support/status surface and `--scope profile --workers 12` for README, proof index, upstream ledger, operations cadence, operator handoff, and core support docs. Treat command output as the current link-count source.
- Public site hygiene verifier: [scripts/check_site_hygiene.py](../scripts/check_site_hygiene.py) ([commit](https://github.com/happysnaker/happysnaker/commit/ef88985863a24042f5f8be35c0b2979e44441d71)); profile CI checks a local `happysnaker.github.io` checkout, and manual `--live` runs verify project-page metadata, sitemap, public repo-link hygiene, support-page proof-before-payment content, local/live stable workflow proof links instead of one-off Actions run URLs, and share-kit routing. Treat command output as the current assertion-count source.

Current sponsor targets are intentionally concrete:

- `qq-ai-bot`: arm64 / CasaOS validation remains open for a physical host report, but multi-arch GHCR image evidence, an arm64 Compose override, an install report template, a reusable smoke script, a tester pack, a homelab outreach kit, project-page tester path, project-page copy/paste outreach snippet, support-funnel refresh, and passing GitHub Actions QEMU arm64 smoke runs are documented, including v0.1.7 tag evidence; latency histograms shipped in v0.1.5 and Postgres session store shipped in v0.1.6;
- `RDLeader`: public-safe demo walkthrough, runtime/approval deep dive, one-command demo reset, employee-agent onboarding, browser walkthrough, landing-page copy, public project page, support-funnel refresh, narrated video, distribution kit, submission tracker, two submission batches, one merged coding-agent awesome-list PR, one open autonomous-agent PR, CodeQL hardening, and Dependabot advisory remediation are shipped; next sponsorable slices are review follow-up, DevPlan bundle sanitization, and license posture resolution.

Support page:

- <https://happysnaker.github.io/support/>

## Known caveats

- `RDLeader` is public but its final license posture is not decided yet; see <https://github.com/happysnaker/RDLeader/issues/3>.
- Some RDLeader evidence remains local until redacted because raw DevPlan logs can contain private paths or live integration identifiers.
- `qq-ai-bot` is stronger as a bot infrastructure scaffold than as a polished consumer-facing app.
