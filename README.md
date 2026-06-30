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

- **[go-service-starter](https://github.com/happysnaker/go-service-starter)** — minimal production-minded Go HTTP service starter with structured logging, health endpoints, and graceful shutdown
- **[go-http-middleware-kit](https://github.com/happysnaker/go-http-middleware-kit)** — reusable `net/http` middleware for request IDs, real IP extraction, structured logs, panic recovery, and timeouts
- **[backend-engineer-checklist](https://github.com/happysnaker/backend-engineer-checklist)** — practical backend engineer checklist covering Go, Java, distributed systems, databases, networking, observability, and delivery
- **[system-design-checklist](https://github.com/happysnaker/system-design-checklist)** — practical system design checklist for interviews, architecture reviews, and distributed-systems tradeoff discussions
- **[HRpc](https://github.com/happysnaker/HRpc)** — Java / Netty based RPC framework learning project covering custom protocol design, service registry, dynamic proxy invocation, heartbeats, reconnect, and client-side load balancing
- **[Resume](https://github.com/happysnaker/Resume)** — responsive résumé / portfolio template with 161+ stars
- **[Blog](https://happysnaker.github.io/)** — technical notes on backend engineering, Java/Go, and CS topics

## Building in public

- **[go-service-starter](https://github.com/happysnaker/go-service-starter)** — a lightweight Go service starter aimed at real backend service scaffolding instead of throwaway demos
- **[go-http-middleware-kit](https://github.com/happysnaker/go-http-middleware-kit)** — a focused middleware pack for the boring-but-important HTTP concerns every backend service eventually needs
- **[backend-engineer-checklist](https://github.com/happysnaker/backend-engineer-checklist)** — a shareable backend engineering roadmap/checklist designed for self-study, onboarding, and interview prep
- **[system-design-checklist](https://github.com/happysnaker/system-design-checklist)** — a concise system design framework for interviews, design docs, and architecture reviews
- **[HRpc](https://github.com/happysnaker/HRpc)** — a Java / Netty RPC framework learning project that makes registry, transport, retry, and load-balancing internals visible
- Iterating on reusable assets that are actually useful to backend engineers, not just toy demos

## Open source contributions

**Merged**
- **[docker/docs#25462](https://github.com/docker/docs/pull/25462)** — clarified that the Ubuntu `noble` base-image example is version-specific and should be adjusted for the release being imported
- **[rclone/rclone#9559](https://github.com/rclone/rclone/pull/9559)** — clarified `copyto` command documentation with maintainer-aligned wording

**Selected recent PRs**

**Code / behavior fixes**
- **[urfave/cli#2379](https://github.com/urfave/cli/pull/2379)** — prevent v2 shell completion after `--` from accidentally executing command actions, with regression coverage
- **[go-chi/chi#1120](https://github.com/go-chi/chi/pull/1120)** — fix Host-based routing in `RouteHeaders` by using `Request.Host`, plus tests and doc updates
- **[hashicorp/go-retryablehttp#206](https://github.com/hashicorp/go-retryablehttp/issues/206)** — investigated the query-string leakage issue and tracked the maintainer-side PR state while lining up a future code contribution area
- Built and shipped **[go-http-middleware-kit](https://github.com/happysnaker/go-http-middleware-kit)** — a small Go middleware library for request IDs, logging, panic recovery, real IP extraction, and timeouts

**Docs / developer experience**
- **[prometheus/client_golang#2034](https://github.com/prometheus/client_golang/pull/2034)** — add an OTLP bridge tutorial for exporting existing Prometheus instrumentation through OpenTelemetry
- **[open-telemetry/opentelemetry-go#8527](https://github.com/open-telemetry/opentelemetry-go/pull/8527)** — document supported SDK environment variables across resource, trace, metric, and log package docs
- **[docker/docs#25464](https://github.com/docker/docs/pull/25464)** — add a legacy Docker Desktop Mac troubleshoot alias and fix the related docs-site redirect/build edge case
- **[github/docs#45002](https://github.com/github/docs/pull/45002)** — add SHA pinning notes to OIDC workflow examples across AWS, Azure, GCP, Vault, and PyPI docs

**Contribution focus**
- Small but real behavior fixes, API correctness, developer experience, and selective documentation where implementation ambiguity causes real user error
- Recent work spans urfave/cli, go-chi, Prometheus client_golang, OpenTelemetry, Docker Docs, and GitHub Docs

## Focus

```text
Languages:      Go, Java, C/C++, SQL
Interests:      Backend engineering, RPC, distributed systems, storage, networking
Strengths:      CS fundamentals, hands-on implementation, reusable engineering assets
Open to:        Backend / infrastructure / systems engineering opportunities
```

## Support my open-source work

If my open-source work, reusable templates, code contributions, or engineering assets save you time, you can support me directly.

- **Support page:** [happysnaker.github.io/support](https://happysnaker.github.io/support/)
- **Fastest support path:** scan the WeChat Pay / Alipay QR codes below
- **Common support amounts:** `¥9.9` / `¥19.9` / `¥49.9` / `¥99` — any amount helps
- **Async profile/repo polish:** `¥99` for one public GitHub profile / README / repo positioning / resume-site pass; `¥199` for a bundled GitHub profile + one repo README + one resume-site packaging pass
- **Sponsor a build:** if you want me to keep shipping backend starter kits, middleware, checklists, and open-source fixes, direct support helps fund that work
- If a repo helped your interview prep, design review, or implementation work, small direct support is especially appreciated.

<table>
  <tr>
    <td align="center">
      <img src="./assets/wechat-pay.jpg" alt="WeChat Pay QR code" width="240" /><br />
      <strong>WeChat Pay</strong>
    </td>
    <td align="center">
      <img src="./assets/alipay-pay.jpg" alt="Alipay QR code" width="240" /><br />
      <strong>Alipay</strong>
    </td>
  </tr>
</table>

- **WeChat Pay** — scan the QR code above
- **Alipay** — scan the QR code above

## Contact

- Email: `happysnaker@foxmail.com`
- Resume site: [happysnaker.github.io/Resume](https://happysnaker.github.io/Resume/)
- Blog: [happysnaker.github.io](https://happysnaker.github.io/)
