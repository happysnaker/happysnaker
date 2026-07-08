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
- Promo kit: <https://github.com/happysnaker/qq-ai-bot/blob/main/docs/public/promo-kit.md>
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
- CodeQL after transport hardening: <https://github.com/happysnaker/qq-ai-bot/actions/runs/28970038743>
- Feature release with Postgres session store: <https://github.com/happysnaker/qq-ai-bot/releases/tag/v0.1.6>
- Latest main CI after arm64 smoke-script docs: <https://github.com/happysnaker/qq-ai-bot/actions/runs/28958094897>
- Latest main Docker publish / multi-arch manifest refresh: <https://github.com/happysnaker/qq-ai-bot/actions/runs/28958094913>
- Latest README state refresh CI: <https://github.com/happysnaker/qq-ai-bot/actions/runs/28959110625>
- Latest README state refresh Docker publish: <https://github.com/happysnaker/qq-ai-bot/actions/runs/28959110697>
- Main-branch arm64 image smoke workflow: <https://github.com/happysnaker/qq-ai-bot/actions/runs/28965874894>
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
- External PR: awesome-coding-agents: <https://github.com/kailiu42/awesome-coding-agents/pull/13>
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
- External/community submission sponsorware slice: <https://github.com/happysnaker/RDLeader/issues/26> (closed with two external awesome-list PRs)
- Next sponsorware slice: external submission review follow-up: <https://github.com/happysnaker/RDLeader/issues/27>

What to look for:

- runtime boundaries instead of hidden chat sessions;
- structured task envelopes and runtime result events;
- stale task recovery and endurance posture;
- human-in-the-loop approval framing;
- public-safe documentation that avoids leaking private DevPlan artifacts.

## Upstream contribution signal

Recent upstream work is intentionally small but concrete: parser edge cases, retry semantics, CLI behavior, observability docs, and SDK/client correctness.

Representative links:

- HashiCorp retryablehttp fixes: <https://github.com/hashicorp/go-retryablehttp/pulls?q=author%3Ahappysnaker>
- Prometheus client/procfs work: <https://github.com/pulls?q=author%3Ahappysnaker+prometheus>
- pflag fixes: <https://github.com/spf13/pflag/pulls?q=author%3Ahappysnaker>
- urfave/cli work: <https://github.com/urfave/cli/pulls?q=author%3Ahappysnaker>
- GitHub CLI work: <https://github.com/cli/cli/pulls?q=author%3Ahappysnaker>

Review lens:

- Does the change fix a real edge case?
- Is the behavior covered by tests or docs?
- Does the patch avoid broad rewrites?
- Does the PR reduce ambiguity for future users?

## Maintenance proof

Both current flagship repos now have public, grouped dependency-maintenance config:

Profile docs now have public CI for link integrity and sensitive-pattern checks: <https://github.com/happysnaker/happysnaker/actions/runs/28951262138>.

- `qq-ai-bot`: npm and GitHub Actions Dependabot updates are grouped to reduce PR/job noise. Latest config push passed CI, Docker publish, and grouped update jobs.
- `RDLeader`: npm and GitHub Actions Dependabot updates are grouped to reduce PR/job noise. Latest config push passed public CI and grouped update jobs.

## Sponsorware / support proof

Central board:

- <https://github.com/happysnaker/happysnaker/blob/master/docs/sponsorware-board.md>

Current sponsor targets are intentionally concrete:

- `qq-ai-bot`: arm64 / CasaOS validation remains open for a physical host report, but multi-arch GHCR image evidence, an arm64 Compose override, an install report template, a reusable smoke script, and passing GitHub Actions QEMU arm64 smoke runs are documented, including v0.1.7 tag evidence; latency histograms shipped in v0.1.5 and Postgres session store shipped in v0.1.6;
- `RDLeader`: public-safe demo walkthrough, runtime/approval deep dive, one-command demo reset, employee-agent onboarding, browser walkthrough, landing-page copy, narrated video, distribution kit, submission tracker, two submission batches, external awesome-list PRs, CodeQL hardening, and Dependabot advisory remediation are shipped; next sponsorable slices are review follow-up, DevPlan bundle sanitization, and license posture resolution.

Support page:

- <https://happysnaker.github.io/support/>

## Known caveats

- `RDLeader` is public but its final license posture is not decided yet; see <https://github.com/happysnaker/RDLeader/issues/3>.
- Some RDLeader evidence remains local until redacted because raw DevPlan logs can contain private paths or live integration identifiers.
- `qq-ai-bot` is stronger as a bot infrastructure scaffold than as a polished consumer-facing app.
