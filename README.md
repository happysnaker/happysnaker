# Shirong Lu / happysnaker

[![Profile docs CI](https://github.com/happysnaker/happysnaker/actions/workflows/ci.yml/badge.svg)](https://github.com/happysnaker/happysnaker/actions/workflows/ci.yml) [![qq-ai-bot CI](https://github.com/happysnaker/qq-ai-bot/actions/workflows/ci.yml/badge.svg)](https://github.com/happysnaker/qq-ai-bot/actions/workflows/ci.yml) [![RDLeader CI](https://github.com/happysnaker/RDLeader/actions/workflows/ci.yml/badge.svg)](https://github.com/happysnaker/RDLeader/actions/workflows/ci.yml)

> 💛 **Sponsorware + 开源支持：** 当前可赞助任务见下方 **Current sponsorware board**；[qq-ai-bot](https://github.com/happysnaker/qq-ai-bot) / [RDLeader](https://github.com/happysnaker/RDLeader) 都在公开推进。也欢迎 [扫码支持](https://happysnaker.github.io/support/)（¥9.9 起）或购买付费评审服务 ¥29.9–¥199。

Backend / systems engineer focused on **Go**, **Java**, distributed systems, protocol / RPC infrastructure, performance-oriented engineering, and selective real OSS fixes.

> Current flagship: **[qq-ai-bot](https://github.com/happysnaker/qq-ai-bot)** — a self-hosted QQ ↔ AI bot scaffold with **OneBot 11**, **NapCat / LLOneBot**, **ACP-compatible agents**, **persistent sessions**, **progress streaming**, **Prometheus-style `/metrics`**, and **Docker**. It now has a public project page, Docker quickstart, a stable public image tag (`v0.1.6`) plus a moving `latest` tag, ecosystem references, an official OneBot community discussion, and active upstream docs / app-directory PRs, so reviewers can judge it as a small operator-facing systems asset rather than a one-night chat demo. Recent OSS work spans HashiCorp retry semantics, Prometheus client edge cases, jwt validation, chi routing, urfave/cli, GitHub CLI, OpenTelemetry, and Docker / GitHub Docs improvements.

> **Reading guide for recruiters / reviewers:** the repos that best represent my current direction are the **pinned / highlighted repositories below** plus the linked **upstream PRs**. If you see many public forks under my account, treat them as temporary contribution vehicles for upstream pull requests, not as portfolio centerpieces.

> **If you only open three repos:** start with **qq-ai-bot** → **RDLeader** → **happydb**.

> **Proof index:** [docs/technical-proof-index.md](docs/technical-proof-index.md) links the CI runs, public docs, upstream PR surfaces, and sponsorware board.

> **Portfolio audit:** [docs/portfolio-audit.md](docs/portfolio-audit.md) explains what to promote, what to keep as proof, and what to park.

> **Manual GitHub checklist:** [docs/manual-github-actions.md](docs/manual-github-actions.md) tracks profile-pin and license actions that require deliberate/manual handling.

> **Operations cadence:** [docs/operations-cadence.md](docs/operations-cadence.md) defines the weekly/monthly maintenance loop for CI, sponsorware, proof index, and portfolio hygiene.

> **Public proof hub release:** [https://github.com/happysnaker/happysnaker/releases/tag/v2026.07-public-proof-hub](https://github.com/happysnaker/happysnaker/releases/tag/v2026.07-public-proof-hub) freezes the current proof/sponsor surface.

## Focus

- Building reliable backend services and reusable developer tooling
- Strong interest in distributed systems, storage, networking, performance, and CS fundamentals
- Shipping practical public assets and selective open-source fixes that are small but real
- Turning rough engineering ideas into public repos that feel closer to products than class projects

## Current flagship

- **Repo** — [qq-ai-bot](https://github.com/happysnaker/qq-ai-bot) · [project page](https://happysnaker.github.io/qq-ai-bot/)
- **Why it exists** — keep QQ / OneBot transport, session orchestration, and ACP agent execution clearly separated so the system feels like bot infrastructure rather than a one-off chat demo
- **What it already does** — supports NapCat / LLOneBot, forward / reverse WebSocket wiring, per-chat session reuse, progress messages back to QQ, Docker quickstart, multi-arch public image packaging via both `ghcr.io/happysnaker/qq-ai-bot:v0.1.6` and `ghcr.io/happysnaker/qq-ai-bot:latest`, plus an arm64 smoke script for repeatable host reports
- **External proof** — already listed on the public [OneBot ecosystem](https://onebot.dev/ecosystem) page, posted in the official [OneBot Discussions / 应用 / SDK](https://github.com/orgs/botuniverse/discussions/264), and included in [awesome-agent-client-protocol](https://github.com/nMaroulis/awesome-agent-client-protocol)
- **Ecosystem work** — [official ACP clients docs PR merged](https://github.com/agentclientprotocol/agent-client-protocol/pull/1592) · [official LLOneBot docs PR active](https://github.com/LLOneBot/LuckyLilliaDoc/pull/20) · [NapCat docs integration landed](https://github.com/NapNeko/NapCatDocs/pull/132) · [Docker Compose sample PR active](https://github.com/docker/awesome-compose/pull/781) · [CasaOS app-store PR active](https://github.com/Cp0204/CasaOS-AppStore-Play/pull/42) · [ACP protocol discussion](https://github.com/orgs/agentclientprotocol/discussions/1591)
- **Why it is on this profile** — it best reflects the direction I want to be judged on: protocol integration, transport / agent boundaries, operator-friendly packaging, and reusable engineering assets

## Recent ecosystem signal around qq-ai-bot

- Public **[OneBot ecosystem](https://onebot.dev/ecosystem)** placement, so the project is no longer only self-claimed
- Public **[official OneBot discussion](https://github.com/orgs/botuniverse/discussions/264)** in the protocol community’s own “应用 / SDK” channel, so the repo now has one protocol-native showcase thread instead of only its own outbound links
- Public **[ACP protocol discussion](https://github.com/orgs/agentclientprotocol/discussions/1591)** grounded in a real richer-media / attachment boundary from implementation work
- Merged **[ACP clients docs PR](https://github.com/agentclientprotocol/agent-client-protocol/pull/1592)** adding `qq-ai-bot` to the official ACP clients docs
- Active **[LLOneBot docs PR](https://github.com/LLOneBot/LuckyLilliaDoc/pull/20)** to document `qq-ai-bot` as an integration path in the official LLOneBot docs
- **[NapCat docs integration landed](https://github.com/NapNeko/NapCatDocs/pull/132)**, so `qq-ai-bot` is now also present in NapCat community / integration-facing docs rather than only in outbound showcase threads
- Active **[docker/awesome-compose#781](https://github.com/docker/awesome-compose/pull/781)** to place a NapCat + `qq-ai-bot` local stack into a widely browsed Docker Compose samples repo
- Active **[CasaOS-AppStore-Play#42](https://github.com/Cp0204/CasaOS-AppStore-Play/pull/42)** to package `qq-ai-bot` as a more browser-first homelab install surface rather than only a README + Compose story
- Public recommendation / weekly threads are also live in **[HelloGitHub](https://github.com/521xueweihan/HelloGitHub/issues/3403)**, **[GitHubDaily](https://github.com/GitHubDaily/GitHubDaily/issues/906)**, **[阮一峰周刊](https://github.com/ruanyf/weekly/issues/10546)**, **[howie6879/weekly](https://github.com/howie6879/weekly/issues/225)**, and **[developer-plus/weekly](https://github.com/developer-plus/weekly/issues/60)**, so discovery is no longer limited to protocol-native communities

This is the strongest current “public proof” chain on the profile: a repo, a project page, ecosystem references, and upstream protocol / docs work around the same asset.

## Highlighted work

- **[qq-ai-bot](https://github.com/happysnaker/qq-ai-bot)** — self-hosted QQ ↔ AI bot scaffold using OneBot 11, ACP-compatible agent bridging, persistent sessions, progress streaming, Docker quickstart, multi-instance notes, public promo kit, sponsorware roadmap, and a project page at [happysnaker.github.io/qq-ai-bot](https://happysnaker.github.io/qq-ai-bot/)
- **[RDLeader](https://github.com/happysnaker/RDLeader)** — local-first AI R&D control plane for multi-agent task ownership, progressive context assembly, ACP runtime dispatch, approval gates, public CI, public-safe QA evidence, runtime endurance notes, SVG demo assets, a 40-second walkthrough video, a runtime/approval deep dive, `pnpm demo:reset`, employee-agent onboarding, a browser walkthrough, landing-page copy, a captioned browser walkthrough video, a distribution kit, a submission tracker, and two public submission batches
- **[happydb](https://github.com/happysnaker/happydb)** — learning-oriented relational database implementation in Java covering storage, indexing, MVCC-style visibility, recovery, query execution, optimization, and replication experiments
- **[HRpc](https://github.com/happysnaker/HRpc)** — Java 11 / Netty based RPC framework learning project with custom protocol, service registry, dynamic proxy invocation, heartbeats, reconnect, and load balancing
- **[go-service-starter](https://github.com/happysnaker/go-service-starter)** — minimal production-minded Go HTTP service starter with config loading, structured logging, health endpoints, graceful shutdown, and Docker packaging
- **[go-http-middleware-kit](https://github.com/happysnaker/go-http-middleware-kit)** — reusable `net/http` middleware for request IDs, structured logging, panic recovery, timeouts, and real IP handling
- **[CSAPPLabsAndNotes](https://github.com/happysnaker/CSAPPLabsAndNotes)** — CS:APP lab notes, systems-learning walkthroughs, and low-level computer-systems study material
- **[Resume](https://github.com/happysnaker/Resume)** — responsive HTML/CSS/JS resume and portfolio template for GitHub Pages, personal sites, and developer landing pages
- **[system-design-checklist](https://github.com/happysnaker/system-design-checklist)** — practical system-design checklist, answer sheet, and worked examples for backend interviews, architecture reviews, and distributed-systems tradeoffs
- **[production-readiness-checklist](https://github.com/happysnaker/production-readiness-checklist)** — practical release-review, launch-gate, and on-call handoff checklist with copy-paste templates for production work

## How to read this profile

- **For strongest signal first** — start with **qq-ai-bot**, **RDLeader**, **happydb**, **go-service-starter**, **go-http-middleware-kit**, and the linked upstream PRs below
- **For interview / systems fundamentals** — **CSAPPLabsAndNotes**, **happydb**, and the checklist repos are the fastest read
- **For portfolio / packaging signal** — **Resume**, **github-profile-checklist**, and the public project pages
- **What to de-prioritize** — short-lived public forks of external repos usually exist only because I was sending or updating upstream pull requests there

## Selected recent OSS work

**Code / behavior fixes**
- **[hashicorp/go-retryablehttp#288](https://github.com/hashicorp/go-retryablehttp/pull/288) / [#289](https://github.com/hashicorp/go-retryablehttp/pull/289) / [#290](https://github.com/hashicorp/go-retryablehttp/pull/290) / [#291](https://github.com/hashicorp/go-retryablehttp/pull/291) / [#292](https://github.com/hashicorp/go-retryablehttp/pull/292) / [#293](https://github.com/hashicorp/go-retryablehttp/pull/293)** — a run of focused fixes for final-response preservation, typed-nil request bodies, logger safety, readable retry `Backoff` bodies, deadline-aware retry waits, and zero-value `Client` safety
- **[prometheus/client_golang#2040](https://github.com/prometheus/client_golang/pull/2040)** — clamp out-of-range formatted timestamps so `model.Earliest` / `model.Latest` no longer serialize into values that can overflow back on the server side
- **[golang-jwt/jwt#520](https://github.com/golang-jwt/jwt/pull/520)** — add a required issued-at validation option without changing the existing `WithIssuedAt()` behavior
- **[spf13/pflag#483](https://github.com/spf13/pflag/pull/483) / [#484](https://github.com/spf13/pflag/pull/484) / [#485](https://github.com/spf13/pflag/pull/485) / [#486](https://github.com/spf13/pflag/pull/486) / [#487](https://github.com/spf13/pflag/pull/487)** — fix nil-default `GetIP()` handling, allow hex input in `UintSlice`, make explicit empty typed slice values round-trip as empty slices instead of parse errors, allow explicit empty `StringToString` overrides, and restore `IsBoolFlag()` compatibility for custom bool-like values
- **[go-chi/chi#1120](https://github.com/go-chi/chi/pull/1120)** — fix Host-based routing in `RouteHeaders` by using `Request.Host`, plus tests and doc updates
- **[urfave/cli#2379](https://github.com/urfave/cli/pull/2379)** — prevent v2 shell completion after `--` from accidentally executing command actions, with regression coverage
- **[urfave/cli#2381](https://github.com/urfave/cli/pull/2381)** — reject legacy v1-style `Name: "flag, f"` alias syntax with an explicit migration error instead of silently dropping the alias
- **[cli/cli#13766](https://github.com/cli/cli/pull/13766)** — fix `gh skill install --dir ...` so a custom install directory no longer still forces an interactive target-agent selection step
- **[urfave/cli-altsrc#50](https://github.com/urfave/cli-altsrc/pull/50)** — make config-backed map/object values round-trip correctly into `StringMapFlag` via the same serialized format used by `urfave/cli/v3`
- Built and shipped **[go-http-middleware-kit](https://github.com/happysnaker/go-http-middleware-kit)** — a small Go middleware library for request IDs, logging, panic recovery, real IP extraction, and timeouts
- Packaged and published **[happydb](https://github.com/happysnaker/happydb)** as a public systems-learning project around database internals, storage, recovery, and distributed-systems experiments

**Quality / observability / SDK**
- **[prometheus/procfs#836](https://github.com/prometheus/procfs/pull/836)** — tolerate wrapped signed `/proc/stat` `processes` counters so `Stat()` consumers do not fail on long-running systems exposing the wrapped fork count as a negative decimal string
- **[prometheus/procfs#833](https://github.com/prometheus/procfs/pull/833)** — split proc stat limit coverage by architecture so parser limit checks stay correct on both 32-bit and 64-bit targets
- **[open-telemetry/opentelemetry-go#8527](https://github.com/open-telemetry/opentelemetry-go/pull/8527)** — document supported SDK environment variables across resource, trace, metric, and log package docs

**Selective docs / developer experience**
- **[prometheus/client_golang#2034](https://github.com/prometheus/client_golang/pull/2034)** — add an OTLP bridge tutorial for exporting existing Prometheus instrumentation through OpenTelemetry
- **[github/docs#45002](https://github.com/github/docs/pull/45002)** — add SHA pinning notes to OIDC workflow examples across AWS, Azure, GCP, Vault, and PyPI docs
- **[docker/docs#25462](https://github.com/docker/docs/pull/25462)** — clarified that the Ubuntu `noble` base-image example is version-specific and should be adjusted for the release being imported
- **[rclone/rclone#9559](https://github.com/rclone/rclone/pull/9559)** — clarified `copyto` command documentation with maintainer-aligned wording

**Contribution focus**
- Small but real behavior fixes, API correctness, retry semantics, parser edge cases, routing behavior, observability/client edge cases, and selective documentation only where implementation ambiguity causes real user error
- Recent work spans HashiCorp libraries, Prometheus client_golang / procfs, golang-jwt, chi, urfave/cli, GitHub CLI, OpenTelemetry, GitHub Docs, Docker Docs, and rclone

## Snapshot

```text
Languages:      Go, Java, C/C++, SQL
Interests:      Backend engineering, RPC, distributed systems, storage, networking
Strengths:      CS fundamentals, hands-on implementation, reusable engineering assets
Open to:        Backend / infrastructure / systems engineering opportunities
```

## Current sponsorware board

Full board with notes: [docs/sponsorware-board.md](docs/sponsorware-board.md).

If you want to support concrete public work instead of sending a vague tip, these are the clearest current targets:

| Project | Sponsor target | What it funds | Link |
|---|---|---|---|
| `qq-ai-bot` | End-to-end latency histograms | **shipped in [v0.1.5](https://github.com/happysnaker/qq-ai-bot/releases/tag/v0.1.5)** | [#23](https://github.com/happysnaker/qq-ai-bot/issues/23) |
| `qq-ai-bot` | Postgres session store | **shipped in [v0.1.6](https://github.com/happysnaker/qq-ai-bot/releases/tag/v0.1.6)** | [#24](https://github.com/happysnaker/qq-ai-bot/issues/24) |
| `qq-ai-bot` | arm64 / CasaOS validation | multi-arch image evidence, arm64 compose override, smoke script, and report template documented; real CasaOS/arm64 report still open | [#26](https://github.com/happysnaker/qq-ai-bot/issues/26) |
| `RDLeader` | External/community submission batch | external or community-maintained submission batch using the distribution kit and tracker | [#26](https://github.com/happysnaker/RDLeader/issues/26) |
| `RDLeader` | DevPlan bundle sanitization | split local features into public-safe commits and docs | [#1](https://github.com/happysnaker/RDLeader/issues/1) |

Best payment note format: `repo #issue`, for example `qq-ai-bot #26` or `RDLeader #26`.

Public readiness note: `RDLeader` license posture is tracked separately in [RDLeader#3](https://github.com/happysnaker/RDLeader/issues/3) before wider reuse/promotion.

## Support

If my open-source work, reusable templates, code contributions, or engineering assets save you time, you can support ongoing maintenance here.

- **Support page:** [happysnaker.github.io/support](https://happysnaker.github.io/support/) — WeChat Pay / Alipay QR codes live there
- **If you came here from `qq-ai-bot`:** the cleanest support note is simply `qq-ai-bot`, and the fastest useful paid path is the **¥29.9 quick read** for another bot / repo / landing page
- **Fastest low-friction tip:** `¥9.9` / `¥19.9` if one repo, checklist, or OSS fix saved you time
- **Most useful paid entry:** **`¥29.9` quick read** for a blunt first-impression pass on your profile / repo / landing page — [review page](https://happysnaker.github.io/review/)
- **Best packaging option:** **`¥99` async review** for pinned repos, README cleanup, landing-page positioning, or profile packaging — [review page](https://happysnaker.github.io/review/)
- **Preview first:** [redacted sample audit](https://github.com/happysnaker/github-profile-checklist/blob/main/docs/redacted-audit-sample.md)
- **Current July offer:** first paid request gets **one extra public page / README** in the same pass at no extra charge
- **One-click quick-read email:** [Quick read \| profile / repo / page link](mailto:happysnaker@foxmail.com?subject=Quick%20read%20%7C%20profile%2Frepo%2Fpage%20link&body=Public%20link%3A%0ATarget%20role%20(optional)%3A%0AWhat%20feels%20weak%3A%0APayment%20screenshot%3A%20attached)
- **One-click async-review email:** [Async review \| target role \| repo / profile link](mailto:happysnaker@foxmail.com?subject=Async%20review%20%7C%20target%20role%20%7C%20repo%2Fprofile%20link&body=Public%20link(s)%3A%0ATarget%20role%20or%20use%20case%3A%0AWhat%20feels%20weak%3A%0APayment%20screenshot%3A%20attached)
- If **qq-ai-bot** helped with OneBot / ACP wiring, the cleanest support note is simply `qq-ai-bot`
- If **Resume**, **CSAPPLabsAndNotes**, **github-profile-checklist**, or one recent OSS fix helped, direct support is especially appreciated

## Contact

- Email: `happysnaker@foxmail.com`
- Portfolio site: [happysnaker.github.io/Resume](https://happysnaker.github.io/Resume/)
- Blog: [happysnaker.github.io](https://happysnaker.github.io/)
- Support / tip: [happysnaker.github.io/support](https://happysnaker.github.io/support/)
