# Shirong Lu / happysnaker

Backend / systems engineer focused on **Go**, **Java**, distributed systems, RPC infrastructure, and performance-oriented engineering.

## Focus

- Building reliable backend services and reusable developer tooling
- Strong interest in distributed systems, storage, networking, performance, and CS fundamentals
- Shipping practical public assets and selective open-source fixes that are small but real

## Highlighted work

- **[happydb](https://github.com/happysnaker/happydb)** — learning-oriented relational database implementation in Java covering storage, indexing, MVCC-style visibility, recovery, query execution, optimization, and replication experiments
- **[HRpc](https://github.com/happysnaker/HRpc)** — Java / Netty RPC framework learning project with service registry, dynamic proxy invocation, heartbeats, reconnect handling, and load balancing
- **[go-service-starter](https://github.com/happysnaker/go-service-starter)** — minimal production-minded Go HTTP service starter with config loading, structured logging, health endpoints, graceful shutdown, and Docker packaging
- **[go-http-middleware-kit](https://github.com/happysnaker/go-http-middleware-kit)** — reusable `net/http` middleware for request IDs, structured logging, panic recovery, timeouts, and real IP handling
- **[CSAPPLabsAndNotes](https://github.com/happysnaker/CSAPPLabsAndNotes)** — CS:APP lab notes, systems-learning walkthroughs, and low-level computer-systems study material
- **[Resume](https://github.com/happysnaker/Resume)** — responsive résumé / portfolio template with 160+ stars and GitHub Pages reuse signal

## Open source contributions

**Merged**
- **[docker/docs#25462](https://github.com/docker/docs/pull/25462)** — clarified that the Ubuntu `noble` base-image example is version-specific and should be adjusted for the release being imported
- **[rclone/rclone#9559](https://github.com/rclone/rclone/pull/9559)** — clarified `copyto` command documentation with maintainer-aligned wording

**Code / behavior fixes**
- **[hashicorp/go-retryablehttp#288](https://github.com/hashicorp/go-retryablehttp/pull/288) / [#289](https://github.com/hashicorp/go-retryablehttp/pull/289) / [#290](https://github.com/hashicorp/go-retryablehttp/pull/290) / [#291](https://github.com/hashicorp/go-retryablehttp/pull/291) / [#292](https://github.com/hashicorp/go-retryablehttp/pull/292) / [#293](https://github.com/hashicorp/go-retryablehttp/pull/293)** — a run of focused fixes for final-response preservation, typed-nil request bodies, logger safety, readable retry `Backoff` bodies, deadline-aware retry waits, and zero-value `Client` safety
- **[golang-jwt/jwt#520](https://github.com/golang-jwt/jwt/pull/520)** — add a required issued-at validation option without changing the existing `WithIssuedAt()` behavior
- **[spf13/pflag#483](https://github.com/spf13/pflag/pull/483)** — fix `GetIP()` so optional IP flags with a nil default round-trip cleanly instead of erroring on the internal `<nil>` string form
- **[go-chi/chi#1120](https://github.com/go-chi/chi/pull/1120)** — fix Host-based routing in `RouteHeaders` by using `Request.Host`, plus tests and doc updates
- **[urfave/cli#2379](https://github.com/urfave/cli/pull/2379)** — prevent v2 shell completion after `--` from accidentally executing command actions, with regression coverage
- **[cli/cli#13766](https://github.com/cli/cli/pull/13766)** — fix `gh skill install --dir ...` so a custom install directory no longer still forces an interactive target-agent selection step
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
- Recent work spans HashiCorp libraries, golang-jwt, chi, urfave/cli, Prometheus client_golang, OpenTelemetry, GitHub Docs, Docker Docs, and rclone

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
