# Shirong Lu / happysnaker

Backend / systems engineer focused on **Go**, **Java**, distributed systems, protocol / RPC infrastructure, performance-oriented engineering, and selective real OSS fixes.

> Current flagship: **[qq-ai-bot](https://github.com/happysnaker/qq-ai-bot)** — a self-hosted QQ ↔ AI bot scaffold with **OneBot 11**, **NapCat / LLOneBot**, **ACP-compatible agents**, **persistent sessions**, **progress streaming**, **Prometheus-style `/metrics`**, and **Docker**. It now has a public project page, tagged releases, Docker quickstart, ecosystem placements, and deployment-facing docs, so reviewers can judge it as a small operator-facing systems asset rather than a one-night chat demo. Recent OSS work spans HashiCorp retry semantics, Prometheus client edge cases, jwt validation, chi routing, urfave/cli, GitHub CLI, OpenTelemetry, and Docker / GitHub Docs improvements.

> **Reading guide for recruiters / reviewers:** the repos that best represent my current direction are the **pinned repositories below** plus the linked **upstream PRs**. Some other public repos are temporary forks used to land targeted upstream fixes; they are contribution vehicles, not the main body of work I want to be judged on.

## Focus

- Building reliable backend services and reusable developer tooling
- Strong interest in distributed systems, storage, networking, performance, and CS fundamentals
- Shipping practical public assets and selective open-source fixes that are small but real
- Turning rough engineering ideas into public repos that feel closer to products than class projects

## Current flagship

- **Repo** — [qq-ai-bot](https://github.com/happysnaker/qq-ai-bot) · [project page](https://happysnaker.github.io/qq-ai-bot/)
- **Why it exists** — keep QQ / OneBot transport, session orchestration, and ACP agent execution clearly separated so the system feels like bot infrastructure rather than a one-off chat demo
- **What it already does** — supports NapCat / LLOneBot, forward / reverse WebSocket wiring, per-chat session reuse, progress messages back to QQ, Docker quickstart, and public image packaging via `ghcr.io/happysnaker/qq-ai-bot:latest`
- **External proof** — already listed on the public [OneBot ecosystem](https://onebot.dev/ecosystem) page and in [awesome-agent-client-protocol](https://github.com/nMaroulis/awesome-agent-client-protocol); current distribution work is also pushing it through Docker Compose / self-hosted AI channels
- **Why it is on this profile** — it best reflects the direction I want to be judged on: protocol integration, transport / agent boundaries, operator-friendly packaging, and reusable engineering assets

## Highlighted work

- **[qq-ai-bot](https://github.com/happysnaker/qq-ai-bot)** — self-hosted QQ ↔ AI bot scaffold using OneBot 11, ACP-compatible agent bridging, persistent sessions, progress streaming, Docker quickstart, and a public project page at [happysnaker.github.io/qq-ai-bot](https://happysnaker.github.io/qq-ai-bot/)
- **[happydb](https://github.com/happysnaker/happydb)** — learning-oriented relational database implementation in Java covering storage, indexing, MVCC-style visibility, recovery, query execution, optimization, and replication experiments
- **[HRpc](https://github.com/happysnaker/HRpc)** — Java 11 / Netty based RPC framework learning project with custom protocol, service registry, dynamic proxy invocation, heartbeats, reconnect, and load balancing
- **[go-service-starter](https://github.com/happysnaker/go-service-starter)** — minimal production-minded Go HTTP service starter with config loading, structured logging, health endpoints, graceful shutdown, and Docker packaging
- **[go-http-middleware-kit](https://github.com/happysnaker/go-http-middleware-kit)** — reusable `net/http` middleware for request IDs, structured logging, panic recovery, timeouts, and real IP handling
- **[CSAPPLabsAndNotes](https://github.com/happysnaker/CSAPPLabsAndNotes)** — CS:APP lab notes, systems-learning walkthroughs, and low-level computer-systems study material
- **[Resume](https://github.com/happysnaker/Resume)** — responsive HTML/CSS/JS resume and portfolio template for GitHub Pages, personal sites, and developer landing pages
- **[system-design-checklist](https://github.com/happysnaker/system-design-checklist)** — practical system-design checklist, answer sheet, and worked examples for backend interviews, architecture reviews, and distributed-systems tradeoffs
- **[production-readiness-checklist](https://github.com/happysnaker/production-readiness-checklist)** — practical release-review, launch-gate, and on-call handoff checklist with copy-paste templates for production work

## How to read this profile

- **For strongest signal first** — start with **qq-ai-bot**, **go-service-starter**, **go-http-middleware-kit**, **happydb**, and the linked upstream PRs below
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

## Support

If my open-source work, reusable templates, code contributions, or engineering assets save you time, you can support ongoing maintenance here.

- **Need the same cleanup on your own GitHub?** I offer a **¥29.9** quick blunt first-impression read and a **¥99** async packaging pass for pinned repos, README cleanup, and landing-page positioning. Preview the style in the [redacted sample audit](https://github.com/happysnaker/github-profile-checklist/blob/main/docs/redacted-audit-sample.md).
- **Support page:** [happysnaker.github.io/support](https://happysnaker.github.io/support/)
- **GitHub Sponsor button:** on repos that show **Sponsor**, it routes to the same support page
- **Direct support:** WeChat Pay / Alipay QR codes are available on the support page
- **Cheapest paid option:** `¥29.9` quick GitHub / README first-impression read (one blunt paragraph + top 3 fixes) via the review page: [happysnaker.github.io/review](https://happysnaker.github.io/review/)
- **Fastest low-friction tip:** if one repo, checklist, or contribution saved you 10 minutes, `¥9.9` / `¥19.9` is already meaningful
- **Best paid option:** `¥99` async review for GitHub profile packaging, pinned repo cleanup, README polish, or one focused landing page via the review page: [happysnaker.github.io/review](https://happysnaker.github.io/review/)
- **Current low-friction offer:** first paid request in July gets **one extra public page / README** in the same pass at no extra charge
- **Preview first:** redacted sample audit in **[github-profile-checklist](https://github.com/happysnaker/github-profile-checklist/blob/main/docs/redacted-audit-sample.md)**
- **One-click quick-read email:** [Quick read \| profile / repo / page link](mailto:happysnaker@foxmail.com?subject=Quick%20read%20%7C%20profile%2Frepo%2Fpage%20link&body=Public%20link%3A%0ATarget%20role%20(optional)%3A%0AWhat%20feels%20weak%3A%0APayment%20screenshot%3A%20attached)
- **One-click async-review email:** [Async review \| target role \| repo / profile link](mailto:happysnaker@foxmail.com?subject=Async%20review%20%7C%20target%20role%20%7C%20repo%2Fprofile%20link&body=Public%20link(s)%3A%0ATarget%20role%20or%20use%20case%3A%0AWhat%20feels%20weak%3A%0APayment%20screenshot%3A%20attached)
- If **qq-ai-bot** helped with OneBot / ACP wiring, the cleanest support note is simply `qq-ai-bot`.
- If **Resume (161★)** or **CSAPPLabsAndNotes (70★)** helped, direct support is especially appreciated.
- If **Resume (161★)**, **CSAPPLabsAndNotes (70★)**, **github-profile-checklist**, or one recent OSS fix helped, direct support is especially appreciated.
- If a repo helped your interview prep, design review, or implementation work, direct support is especially appreciated.
- Details for lightweight async feedback are also listed on the support page.

## Contact

- Email: `happysnaker@foxmail.com`
- Portfolio site: [happysnaker.github.io/Resume](https://happysnaker.github.io/Resume/)
- Blog: [happysnaker.github.io](https://happysnaker.github.io/)
