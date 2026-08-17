# Technical Proof Index

> A compact evidence map for the public work I most want reviewed. It now focuses on durable technical assets and upstream maintenance work, not deleted flagship experiments.

## Fast read

| Area | Evidence | Why it matters |
|---|---|---|
| Backend service foundations | [`go-service-starter`](https://github.com/happysnaker/go-service-starter) | Minimal Go HTTP service structure with config loading, structured logging, health checks, graceful shutdown, Docker, and reusable docs |
| HTTP middleware | [`go-http-middleware-kit`](https://github.com/happysnaker/go-http-middleware-kit) | Reusable `net/http` middleware for request IDs, structured logging, panic recovery, timeouts, and real IP handling |
| Storage and systems depth | [`happydb`](https://github.com/happysnaker/happydb) | Java database internals covering storage, indexing, MVCC-style visibility, recovery, query execution, optimization, and replication experiments |
| Systems learning | [`CSAPPLabsAndNotes`](https://github.com/happysnaker/CSAPPLabsAndNotes) | CS:APP lab notes and low-level systems-learning material |
| Profile quality gates | [Profile CI](https://github.com/happysnaker/happysnaker/actions/workflows/ci.yml) and [Profile CodeQL](https://github.com/happysnaker/happysnaker/actions/workflows/codeql.yml) | Keeps the profile README, public docs, stable workflow links, and badges checked |

## Backend service foundations

- `go-service-starter` demonstrates a production-minded Go service baseline: configuration, structured logging, health endpoints, graceful shutdown, Docker packaging, and README-first operation.
- `go-http-middleware-kit` keeps reusable middleware small and reviewable: request IDs, structured access logs, panic recovery, timeouts, and real IP handling are split into inspectable units.
- These repositories are intended as practical engineering assets rather than demos: they should be easy to clone, read, run, and adapt.

## Storage and systems depth

- `happydb` is the strongest systems-code proof surface, covering database internals such as storage layout, indexing, MVCC-style visibility, recovery, query execution, optimization, and replication experiments.
- `CSAPPLabsAndNotes` complements the implementation work with systems-learning notes and lab material for C, memory, linking, shell, and architecture fundamentals.

## Maintenance proof

Selected upstream work includes behavior fixes, compatibility cleanup, and documentation improvements across infrastructure projects:

- HashiCorp `go-retryablehttp`: retry semantics, logger safety, request-body edge cases, deadline-aware waits, and zero-value client behavior.
- Prometheus `client_golang` / `procfs`: timestamp limit handling, proc stat parser limits, and wrapped process counters.
- `golang-jwt/jwt`: required issued-at validation option.
- `go-chi/chi`: Host-based routing behavior in `RouteHeaders`.
- `spf13/pflag`: typed empty values, bool-like flags, IP defaults, and parser compatibility fixes.
- `urfave/cli`: shell-completion and legacy alias handling.
- GitHub CLI, OpenTelemetry, GitHub Docs, Docker Docs, and rclone documentation / developer-experience fixes.

See [`upstream-contribution-ledger.md`](upstream-contribution-ledger.md) for the profile-facing contribution ledger.

## Profile checks

- [Profile CI](https://github.com/happysnaker/happysnaker/actions/workflows/ci.yml) compiles verification scripts and checks public Markdown, stable workflow links, README badges, and the CI workflow contract.
- [Profile CodeQL](https://github.com/happysnaker/happysnaker/actions/workflows/codeql.yml) keeps the profile repository covered by GitHub's static-analysis workflow.
- Historical point-in-time status remains in [`flagship-status-snapshot.md`](flagship-status-snapshot.md); current profile positioning is the README and this proof index.
- `scripts/verify_public_docs.py` checks required public README and proof-index markers, local links, trailing whitespace, and sensitive-looking tokens.
- Stable profile proof-link checker: `scripts/check_stable_profile_links.py` rejects one-off profile Actions run links in public docs.
- `scripts/check_ci_workflow_contract.py` checks that the lean profile CI remains focused on public profile quality rather than deleted project state.
