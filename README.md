# Shirong Lu / happysnaker

[![Profile docs CI](https://github.com/happysnaker/happysnaker/actions/workflows/ci.yml/badge.svg)](https://github.com/happysnaker/happysnaker/actions/workflows/ci.yml)
[![Profile CodeQL](https://github.com/happysnaker/happysnaker/actions/workflows/codeql.yml/badge.svg)](https://github.com/happysnaker/happysnaker/actions/workflows/codeql.yml)

Backend / infrastructure engineer focused on **Go**, **Java**, distributed systems, storage, networking, and practical developer tooling.

I keep this profile centered on code that can be read, run, and reviewed: reusable service foundations, database internals, systems notes, and small upstream fixes where behavior, API contracts, or documentation were ambiguous.

## Engineering focus

- Backend service foundations: configuration, structured logging, health checks, graceful shutdown, Docker packaging, and CI hygiene.
- Distributed systems and storage: database internals, indexing, recovery, query execution, replication experiments, RPC, and observability.
- Open-source maintenance work: narrow fixes, reproducible reports, compatibility edge cases, and documentation that reduces reviewer ambiguity.
- Developer-facing assets: templates, notes, checklists, and examples that are easy to run locally and inspect in public.

## Technical projects

- **[happydb](https://github.com/happysnaker/happydb)** — Java database internals project covering storage, indexing, MVCC-style visibility, recovery, query execution, optimization, and replication experiments.
- **[go-service-starter](https://github.com/happysnaker/go-service-starter)** — minimal production-minded Go HTTP service starter with config loading, structured logging, health checks, graceful shutdown, and Docker packaging.
- **[go-http-middleware-kit](https://github.com/happysnaker/go-http-middleware-kit)** — reusable `net/http` middleware for request IDs, structured logging, panic recovery, timeouts, and real IP handling.
- **[CSAPPLabsAndNotes](https://github.com/happysnaker/CSAPPLabsAndNotes)** — CS:APP lab notes and systems-learning material.

## Open-source contributions

Selected upstream work includes behavior fixes, compatibility cleanup, and documentation improvements across infrastructure projects:

- HashiCorp `go-retryablehttp`: retry semantics, logger safety, request-body edge cases, deadline-aware waits, and zero-value client behavior.
- Prometheus `client_golang` / `procfs`: timestamp limit handling, proc stat parser limits, and wrapped process counters.
- `golang-jwt/jwt`: required issued-at validation option.
- `go-chi/chi`: Host-based routing behavior in `RouteHeaders`.
- `spf13/pflag`: typed empty values, bool-like flags, IP defaults, and parser compatibility fixes.
- `urfave/cli`: shell-completion and legacy alias handling.
- GitHub CLI, OpenTelemetry, GitHub Docs, Docker Docs, and rclone documentation / developer-experience fixes.

## Reading guide

- For backend engineering style: start with **go-service-starter** and **go-http-middleware-kit**.
- For storage and systems depth: start with **happydb** and **CSAPPLabsAndNotes**.
- For upstream contribution history: see the linked contribution ledger and repository activity.

## Snapshot

```text
Languages:      Go, Java, C/C++, SQL, TypeScript
Interests:      Backend infrastructure, RPC, distributed systems, storage, networking
Strengths:      CS fundamentals, source-level debugging, reusable engineering assets
Open to:        Backend / infrastructure / systems engineering opportunities
```

## Links

- Portfolio: [happysnaker.github.io/Resume](https://happysnaker.github.io/Resume/)
- Blog / project pages: [happysnaker.github.io](https://happysnaker.github.io/)
- Technical proof index: [docs/technical-proof-index.md](docs/technical-proof-index.md)
- Upstream contribution ledger: [docs/upstream-contribution-ledger.md](docs/upstream-contribution-ledger.md)
- Email: `happysnaker@foxmail.com`
