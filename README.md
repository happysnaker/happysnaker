# Shirong Lu / happysnaker

[![Profile docs CI](https://github.com/happysnaker/happysnaker/actions/workflows/ci.yml/badge.svg)](https://github.com/happysnaker/happysnaker/actions/workflows/ci.yml)
[![Profile CodeQL](https://github.com/happysnaker/happysnaker/actions/workflows/codeql.yml/badge.svg)](https://github.com/happysnaker/happysnaker/actions/workflows/codeql.yml)

Backend / systems engineer focused on **Go**, **Java**, distributed systems, protocol infrastructure, storage, and practical developer tooling.

I try to keep this profile centered on shipped code, upstream pull requests, and reusable engineering assets. Public forks are usually short-lived contribution workspaces for upstream fixes rather than portfolio projects.

## Current focus

- Reliable backend services, protocol bridges, and developer-facing infrastructure
- Distributed systems, storage engines, RPC, observability, and performance-oriented engineering
- Small, reviewable open-source fixes where behavior, API contracts, or documentation are ambiguous
- Public projects that are easy to run, inspect, and evaluate

## Highlighted projects

- **[qq-ai-bot](https://github.com/happysnaker/qq-ai-bot)** — self-hosted QQ ↔ AI bridge for OneBot 11 / NapCat / LLOneBot and ACP-compatible agents, with sessions, streaming progress, Docker packaging, metrics, and public project docs.
- **[RDLeader](https://github.com/happysnaker/RDLeader)** — local-first AI R&D worker control plane with ACP runtime dispatch, approval gates, public CI, and sanitized QA/runtime evidence.
- **[happydb](https://github.com/happysnaker/happydb)** — Java database internals project covering storage, indexing, MVCC-style visibility, recovery, query execution, optimization, and replication experiments.
- **[go-service-starter](https://github.com/happysnaker/go-service-starter)** — minimal production-minded Go HTTP service starter with config loading, structured logging, health checks, graceful shutdown, and Docker packaging.
- **[go-http-middleware-kit](https://github.com/happysnaker/go-http-middleware-kit)** — reusable `net/http` middleware for request IDs, structured logging, panic recovery, timeouts, and real IP handling.
- **[CSAPPLabsAndNotes](https://github.com/happysnaker/CSAPPLabsAndNotes)** — CS:APP lab notes and systems-learning material.

## Selected upstream work

- HashiCorp `go-retryablehttp`: retry semantics, logger safety, request-body edge cases, deadline-aware waits, and zero-value client behavior.
- Prometheus `client_golang` / `procfs`: timestamp limit handling, proc stat parser limits, and wrapped process counters.
- `golang-jwt/jwt`: required issued-at validation option.
- `go-chi/chi`: Host-based routing behavior in `RouteHeaders`.
- `spf13/pflag`: typed empty values, bool-like flags, IP defaults, and parser compatibility fixes.
- `urfave/cli`: shell-completion and legacy alias handling.
- GitHub CLI, OpenTelemetry, GitHub Docs, Docker Docs, and rclone documentation / developer-experience fixes.

## Reading guide

- For current systems / infra direction: start with **qq-ai-bot**, **RDLeader**, **happydb**, **go-service-starter**, and **go-http-middleware-kit**.
- For fundamentals and interview-style systems material: start with **CSAPPLabsAndNotes**, **happydb**, and the checklist repositories.
- For contribution history: see the linked upstream PRs in project READMEs and repository activity.

## Snapshot

```text
Languages:      Go, Java, C/C++, SQL, TypeScript
Interests:      Backend engineering, RPC, distributed systems, storage, networking
Strengths:      CS fundamentals, hands-on implementation, reusable engineering assets
Open to:        Backend / infrastructure / systems engineering opportunities
```

## Links

- Portfolio: [happysnaker.github.io/Resume](https://happysnaker.github.io/Resume/)
- Blog / project pages: [happysnaker.github.io](https://happysnaker.github.io/)
- Technical proof index: [docs/technical-proof-index.md](docs/technical-proof-index.md)
- Upstream contribution ledger: [docs/upstream-contribution-ledger.md](docs/upstream-contribution-ledger.md)
- Email: `happysnaker@foxmail.com`
