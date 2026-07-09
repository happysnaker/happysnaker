# Upstream contribution ledger

> Snapshot: 2026-07-09 Asia/Shanghai. Source: GitHub PR state via `gh pr view`; this file is a stable proof ledger so the profile does not rely only on dynamic search URLs.

## Summary

- Merged upstream PRs tracked here: **9**.
- Open upstream PRs tracked here: **15**.
- Closed / superseded upstream PRs tracked here: **7**.
- Do not treat closed PRs as shipped proof; they are included to show honest maintenance follow-up and avoid stale notification drift.

## Merged proof

| PR | Status | Contribution | Evidence notes |
|---|---|---|---|
| [`cli/cli#13756`](https://github.com/cli/cli/pull/13756) | merged 2026-07-01 | docs(search): add examples for multiple qualifiers | review: approved; checks green / neutral |
| [`cli/cli#13766`](https://github.com/cli/cli/pull/13766) | merged 2026-07-02 | fix(skills): honor --dir without agent prompt | review: approved; checks green / neutral |
| [`go-chi/chi#1127`](https://github.com/go-chi/chi/pull/1127) | merged 2026-07-03 | feat(middleware): add text/xml and application/xml to default compressible types | review: review_required; checks green / neutral |
| [`rclone/rclone#9559`](https://github.com/rclone/rclone/pull/9559) | merged 2026-06-29 | docs: clarify copyto command description | review: approved; has failing/cancelled checks |
| [`spf13/pflag#483`](https://github.com/spf13/pflag/pull/483) | merged 2026-07-02 | fix: allow nil default IP flags in GetIP | review: approved; checks green / neutral |
| [`spf13/pflag#484`](https://github.com/spf13/pflag/pull/484) | merged 2026-07-02 | fix: allow hex input in UintSlice | review: approved; checks green / neutral |
| [`spf13/pflag#487`](https://github.com/spf13/pflag/pull/487) | merged 2026-07-02 | fix: honor custom IsBoolFlag compatibility | review: approved; checks green / neutral |
| [`spf13/pflag#488`](https://github.com/spf13/pflag/pull/488) | merged 2026-07-03 | docs: clarify SortFlags example with complete runnable program | review: approved; checks green / neutral |
| [`spf13/pflag#490`](https://github.com/spf13/pflag/pull/490) | merged 2026-07-03 | docs: add release process documentation | review: approved; checks green / neutral |

## Open review priorities

| Priority | Items | Next action |
|---|---|---|
| P1: unblock before nudging maintainers | [`urfave/cli#2379`](https://github.com/urfave/cli/pull/2379), [`urfave/cli#2381`](https://github.com/urfave/cli/pull/2381), [`urfave/cli#2384`](https://github.com/urfave/cli/pull/2384), [`cli/cli#13788`](https://github.com/cli/cli/pull/13788), [`gin-gonic/gin#4727`](https://github.com/gin-gonic/gin/pull/4727), [`vuejs/docs#3425`](https://github.com/vuejs/docs/pull/3425) | inspect failing checks / requested changes first; do not ping maintainers while evidence is red or changes are requested |
| P2: green or API-not-reported review queue | [`urfave/cli#2382`](https://github.com/urfave/cli/pull/2382), [`golang-jwt/jwt#524`](https://github.com/golang-jwt/jwt/pull/524), [`hashicorp/go-retryablehttp#288`](https://github.com/hashicorp/go-retryablehttp/pull/288), [`hashicorp/go-retryablehttp#289`](https://github.com/hashicorp/go-retryablehttp/pull/289), [`hashicorp/go-retryablehttp#290`](https://github.com/hashicorp/go-retryablehttp/pull/290), [`open-telemetry/opentelemetry-go#8527`](https://github.com/open-telemetry/opentelemetry-go/pull/8527), [`github/docs#44984`](https://github.com/github/docs/pull/44984), [`github/docs#45002`](https://github.com/github/docs/pull/45002), [`vuejs/docs#3424`](https://github.com/vuejs/docs/pull/3424) | monitor maintainer feedback; only follow up if a maintainer asks for changes or the PR becomes stale |
| P3: issue-only follow-up | [`prometheus/procfs#831`](https://github.com/prometheus/procfs/issues/831), [`spf13/pflag#312`](https://github.com/spf13/pflag/issues/312) | keep as open issue context, not shipped proof; revisit only if continuing the related patch line |

## Open review queue

| PR | Status | Contribution | Evidence notes |
|---|---|---|---|
| [`cli/cli#13788`](https://github.com/cli/cli/pull/13788) | open | fix: preserve percent-encoded path in DisplayURL | review: review_required; mergeable: mergeable; has failing/cancelled checks |
| [`gin-gonic/gin#4727`](https://github.com/gin-gonic/gin/pull/4727) | open | fix: handle bracketed IPv6 and port notation in X-Forwarded-For | review: review_required; mergeable: mergeable; has failing/cancelled checks |
| [`github/docs#44984`](https://github.com/github/docs/pull/44984) | open | docs(actions): add workflow run status reference | review: review_required; mergeable: mergeable; checks green / neutral |
| [`github/docs#45002`](https://github.com/github/docs/pull/45002) | open | docs(actions): add SHA pinning notes to OIDC examples | review: review_required; checks green / neutral |
| [`golang-jwt/jwt#524`](https://github.com/golang-jwt/jwt/pull/524) | open | fix: enable IssuedAt verification when WithIssuedAt() is used | review: review_required; mergeable: mergeable; not reported by API |
| [`hashicorp/go-retryablehttp#288`](https://github.com/hashicorp/go-retryablehttp/pull/288) | open | fix: preserve final response in PassthroughErrorHandler | review: review_required; mergeable: mergeable; not reported by API |
| [`hashicorp/go-retryablehttp#289`](https://github.com/hashicorp/go-retryablehttp/pull/289) | open | fix: avoid panics on typed nil request bodies | review: review_required; mergeable: mergeable; not reported by API |
| [`hashicorp/go-retryablehttp#290`](https://github.com/hashicorp/go-retryablehttp/pull/290) | open | fix: avoid panics on unsupported logger types | review: review_required; mergeable: mergeable; not reported by API |
| [`open-telemetry/opentelemetry-go#8527`](https://github.com/open-telemetry/opentelemetry-go/pull/8527) | open | docs(sdk): document supported environment variables | review: review_required; checks green / neutral |
| [`urfave/cli#2379`](https://github.com/urfave/cli/pull/2379) | open | fix: avoid executing actions when completing `--` in v2 | review: review_required; mergeable: mergeable; has failing/cancelled checks |
| [`urfave/cli#2381`](https://github.com/urfave/cli/pull/2381) | open | fix: error on legacy v1-style flag alias syntax | review: review_required; mergeable: mergeable; has failing/cancelled checks |
| [`urfave/cli#2382`](https://github.com/urfave/cli/pull/2382) | open | fix: ignore non-command args after help flag | review: review_required; mergeable: mergeable; checks green / neutral |
| [`urfave/cli#2384`](https://github.com/urfave/cli/pull/2384) | open | feat: add Parent() accessor to Command | review: review_required; mergeable: mergeable; has failing/cancelled checks |
| [`vuejs/docs#3424`](https://github.com/vuejs/docs/pull/3424) | open | docs: clarify async onWatcherCleanup usage | mergeable: mergeable; checks green / neutral |
| [`vuejs/docs#3425`](https://github.com/vuejs/docs/pull/3425) | open | docs: clarify `.once` listener attachment semantics | review: changes_requested; mergeable: mergeable; checks green / neutral |

## Closed or superseded

| PR | Status | Contribution | Evidence notes |
|---|---|---|---|
| [`github/docs#45001`](https://github.com/github/docs/pull/45001) | closed | docs(pages): clarify when to create _config.yml | review: review_required; mergeable: mergeable; checks green / neutral |
| [`go-chi/chi#1125`](https://github.com/go-chi/chi/pull/1125) | closed | fix(middleware): Logger.Panic respects NoColor in DefaultLogFormatter | review: review_required; mergeable: conflicting; not reported by API |
| [`go-chi/chi#1126`](https://github.com/go-chi/chi/pull/1126) | closed | feat(middleware): add text/xml and application/xml to default compressible types | review: changes_requested; mergeable: mergeable; has failing/cancelled checks |
| [`spf13/pflag#485`](https://github.com/spf13/pflag/pull/485) | closed | fix: allow empty typed slice flag values | mergeable: mergeable; not reported by API |
| [`spf13/pflag#486`](https://github.com/spf13/pflag/pull/486) | closed | fix: allow empty StringToString values | mergeable: mergeable; not reported by API |
| [`vuejs/docs#3422`](https://github.com/vuejs/docs/pull/3422) | closed | docs: clarify async onWatcherCleanup usage | mergeable: mergeable; checks green / neutral |
| [`vuejs/docs#3423`](https://github.com/vuejs/docs/pull/3423) | closed | docs: clarify `.once` listener attachment semantics | mergeable: mergeable; checks green / neutral |

## Related issue follow-up

| Issue | Status | Related proof | Next action |
|---|---|---|---|
| [`cli/cli#13763`](https://github.com/cli/cli/issues/13763) | closed / completed | closed by merged [`cli/cli#13766`](https://github.com/cli/cli/pull/13766) | no action |
| [`spf13/pflag#351`](https://github.com/spf13/pflag/issues/351) | closed / completed | closed by merged [`spf13/pflag#483`](https://github.com/spf13/pflag/pull/483) | no action |
| [`spf13/pflag#229`](https://github.com/spf13/pflag/issues/229) | closed / completed | closed by merged [`spf13/pflag#484`](https://github.com/spf13/pflag/pull/484) | no action |
| [`spf13/pflag#281`](https://github.com/spf13/pflag/issues/281) | closed / completed | closed by merged [`spf13/pflag#487`](https://github.com/spf13/pflag/pull/487) | no action |
| [`spf13/pflag#360`](https://github.com/spf13/pflag/issues/360) | closed / completed | closed by merged [`spf13/pflag#487`](https://github.com/spf13/pflag/pull/487) | no action |
| [`spf13/pflag#312`](https://github.com/spf13/pflag/issues/312) | open | related [`spf13/pflag#486`](https://github.com/spf13/pflag/pull/486) is closed / unmerged | do not count as shipped; revisit only with a revised patch |
| [`prometheus/procfs#831`](https://github.com/prometheus/procfs/issues/831) | open | no shipped PR recorded in this ledger | keep as issue context; revisit only if continuing procfs parser work |

## Maintenance rules

- Update this ledger when an upstream PR/issue merges, closes, receives requested changes, or changes CI state materially.
- Keep dynamic GitHub search URLs out of this file; use direct PR URLs for durable proof.
- For Go upstream projects, this profile-maintenance pass only records public GitHub state; do not run `go test` or `go build` from this workflow.
- Prefer source-linked facts over broad claims like “many upstream contributions”.
