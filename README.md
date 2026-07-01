# Shirong Lu / happysnaker

Backend / systems engineer focused on **Go**, **Java**, distributed systems, RPC infrastructure, and performance-oriented engineering.

- Building reliable backend services and developer tooling
- Strong interest in distributed systems, storage, networking, and performance
- Packaging engineering experience into reusable starters, middleware, checklists, and notes

## What I do

- Backend engineering with Go / Java
- Infrastructure and RPC-oriented system design
- Reusable backend assets, engineering notes, and selective developer-experience improvements
- Practical, implementation-first problem solving grounded in CS fundamentals

## Selected work

- **[happydb](https://github.com/happysnaker/happydb)** — learning-oriented relational database implementation in Java covering storage, indexing, MVCC-style visibility, recovery, query execution, optimization, and replication experiments
- **[HRpc](https://github.com/happysnaker/HRpc)** — Java / Netty RPC framework learning project with service registry, dynamic proxy invocation, heartbeats, reconnect, and load balancing
- **[go-service-starter](https://github.com/happysnaker/go-service-starter)** — minimal production-minded Go HTTP service starter with structured logging, health endpoints, and graceful shutdown
- **[go-http-middleware-kit](https://github.com/happysnaker/go-http-middleware-kit)** — reusable `net/http` middleware for request IDs, real IP extraction, structured logs, panic recovery, and timeouts
- **[backend-engineer-checklist](https://github.com/happysnaker/backend-engineer-checklist)** — practical backend engineer checklist covering Go, Java, distributed systems, databases, networking, observability, and delivery
- **[system-design-checklist](https://github.com/happysnaker/system-design-checklist)** — practical system design checklist for interviews, architecture reviews, and distributed-systems tradeoff discussions
- **[production-readiness-checklist](https://github.com/happysnaker/production-readiness-checklist)** — production launch, release review, and on-call handoff checklist for backend services
- **[github-profile-checklist](https://github.com/happysnaker/github-profile-checklist)** — practical checklist for engineers who want a stronger GitHub profile, cleaner proof of work, and a more credible public portfolio
- **[CSAPPLabsAndNotes](https://github.com/happysnaker/CSAPPLabsAndNotes)** — CS:APP lab notes, systems-learning walkthroughs, and low-level computer-systems study material
- **[Resume](https://github.com/happysnaker/Resume)** — responsive résumé / portfolio template with 160+ stars
- **[Blog](https://happysnaker.github.io/)** — technical notes on backend engineering, Java/Go, and CS topics

## Building in public

- **[happydb](https://github.com/happysnaker/happydb)** — a database internals learning project spanning pages, indexes, MVCC-style visibility, redo/undo logging, query operators, and replication experiments
- **[HRpc](https://github.com/happysnaker/HRpc)** — a Java / Netty RPC framework exploration with registry, proxy invocation, load balancing, reconnect handling, and service wiring
- **[go-service-starter](https://github.com/happysnaker/go-service-starter)** — a lightweight Go service starter aimed at real backend service scaffolding instead of throwaway demos
- **[go-http-middleware-kit](https://github.com/happysnaker/go-http-middleware-kit)** — a focused middleware pack for the boring-but-important HTTP concerns every backend service eventually needs
- **[backend-engineer-checklist](https://github.com/happysnaker/backend-engineer-checklist)** — a shareable backend engineering roadmap/checklist designed for self-study, onboarding, and interview prep
- **[system-design-checklist](https://github.com/happysnaker/system-design-checklist)** — a concise system design framework for interviews, design docs, and architecture reviews
- **[production-readiness-checklist](https://github.com/happysnaker/production-readiness-checklist)** — a launch / readiness / on-call checklist built for real backend delivery work
- **[github-profile-checklist](https://github.com/happysnaker/github-profile-checklist)** — a practical packaging checklist for engineers who want their GitHub to look more intentional, technical, and hireable
- **[Resume](https://github.com/happysnaker/Resume)** — a public template with strong reuse signal and social proof from developers building portfolio pages
- **[CSAPPLabsAndNotes](https://github.com/happysnaker/CSAPPLabsAndNotes)** — a systems-fundamentals study repo covering CS:APP labs, memory, binaries, shells, and proxies
- Iterating on reusable assets that are actually useful to backend engineers, not just toy demos

## Open source contributions

**Merged**
- **[docker/docs#25462](https://github.com/docker/docs/pull/25462)** — clarified that the Ubuntu `noble` base-image example is version-specific and should be adjusted for the release being imported
- **[rclone/rclone#9559](https://github.com/rclone/rclone/pull/9559)** — clarified `copyto` command documentation with maintainer-aligned wording

**High-signal open PRs**
- **[hashicorp/go-retryablehttp#288](https://github.com/hashicorp/go-retryablehttp/pull/288) / [#289](https://github.com/hashicorp/go-retryablehttp/pull/289) / [#290](https://github.com/hashicorp/go-retryablehttp/pull/290) / [#291](https://github.com/hashicorp/go-retryablehttp/pull/291) / [#292](https://github.com/hashicorp/go-retryablehttp/pull/292) / [#293](https://github.com/hashicorp/go-retryablehttp/pull/293)** — six focused Go behavior fixes around final-response preservation, typed-nil request bodies, logger safety, readable `Backoff` bodies, deadline-aware retry waits, and safe zero-value defaults
- **[go-chi/chi#1120](https://github.com/go-chi/chi/pull/1120)** — fix Host-based routing behavior in chi middleware, with tests
- **[urfave/cli-altsrc#50](https://github.com/urfave/cli-altsrc/pull/50)** — add `StringMapFlag`-compatible config value support for JSON / YAML / TOML sources in the extracted `cli-altsrc` module
- **[urfave/cli#2379](https://github.com/urfave/cli/pull/2379)** — prevent v2 shell completion after `--` from accidentally executing command actions, with regression coverage

**Selected recent PRs**

**Code / behavior fixes**
- **[hashicorp/go-retryablehttp#288](https://github.com/hashicorp/go-retryablehttp/pull/288) / [#289](https://github.com/hashicorp/go-retryablehttp/pull/289) / [#290](https://github.com/hashicorp/go-retryablehttp/pull/290) / [#291](https://github.com/hashicorp/go-retryablehttp/pull/291) / [#292](https://github.com/hashicorp/go-retryablehttp/pull/292) / [#293](https://github.com/hashicorp/go-retryablehttp/pull/293)** — a run of focused fixes for final-response preservation, typed-nil request bodies, logger safety, readable retry `Backoff` bodies, deadline-aware retry waits, and zero-value `Client` safety
- **[go-chi/chi#1120](https://github.com/go-chi/chi/pull/1120)** — fix Host-based routing in `RouteHeaders` by using `Request.Host`, plus tests and doc updates
- **[urfave/cli#2379](https://github.com/urfave/cli/pull/2379)** — prevent v2 shell completion after `--` from accidentally executing command actions, with regression coverage
- **[urfave/cli-altsrc#50](https://github.com/urfave/cli-altsrc/pull/50)** — make config-backed map/object values round-trip correctly into `StringMapFlag` via the same serialized format used by `urfave/cli/v3`
- Built and shipped **[go-http-middleware-kit](https://github.com/happysnaker/go-http-middleware-kit)** — a small Go middleware library for request IDs, logging, panic recovery, real IP extraction, and timeouts
- Packaged and published **[happydb](https://github.com/happysnaker/happydb)** and **[HRpc](https://github.com/happysnaker/HRpc)** as public systems-learning projects around database internals, RPC design, networking, and distributed systems

**Docs / developer experience**
- **[prometheus/client_golang#2034](https://github.com/prometheus/client_golang/pull/2034)** — add an OTLP bridge tutorial for exporting existing Prometheus instrumentation through OpenTelemetry
- **[open-telemetry/opentelemetry-go#8527](https://github.com/open-telemetry/opentelemetry-go/pull/8527)** — document supported SDK environment variables across resource, trace, metric, and log package docs
- **[github/docs#45002](https://github.com/github/docs/pull/45002)** — add SHA pinning notes to OIDC workflow examples across AWS, Azure, GCP, Vault, and PyPI docs
- **[docker/docs#25462](https://github.com/docker/docs/pull/25462)** — clarify version-specific Ubuntu `noble` import guidance in Docker image docs

**Contribution focus**
- Small but real behavior fixes, API correctness, retry semantics, edge-case handling, and selective documentation where implementation ambiguity causes real user error
- Recent work spans HashiCorp libraries, chi, urfave/cli, Prometheus client_golang, OpenTelemetry, GitHub Docs, Docker Docs, and rclone

## Focus

```text
Languages:      Go, Java, C/C++, SQL
Interests:      Backend engineering, RPC, distributed systems, storage, networking
Strengths:      CS fundamentals, hands-on implementation, reusable engineering assets
Open to:        Backend / infrastructure / systems engineering opportunities
```

## Support

If my open-source work, reusable templates, code contributions, or engineering assets save you time, you can support ongoing maintenance here.

- **Support page:** [happysnaker.github.io/support](https://happysnaker.github.io/support/)
- **Direct support:** WeChat Pay / Alipay QR codes are available on the support page
- If a repo helped your interview prep, design review, or implementation work, direct support is especially appreciated.
- Details for lightweight async feedback are also listed on the support page.

## Contact

- Email: `happysnaker@foxmail.com`
- Portfolio site: [happysnaker.github.io/Resume](https://happysnaker.github.io/Resume/)
- Blog: [happysnaker.github.io](https://happysnaker.github.io/)
