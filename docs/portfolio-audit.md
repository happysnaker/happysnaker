# Public Repository Portfolio Audit

> Purpose: keep the GitHub account focused. This is a maintenance map for deciding what to promote, what to keep as technical proof, what supports the funnel, and what should stay quiet until it is cleaned up.

## Buckets

- **DAILY** — active public surface; keep polished, checked, and linked from profile.
- **PROOF** — technical proof; useful to reviewers, but not necessarily sponsor-facing.
- **SUPPORT** — support assets, templates, or checklists that reinforce the profile.
- **PARK** — public but not a priority for promotion; keep from distracting the profile.
- **FORK / ARCHIVE** — contribution vehicles or historical forks; do not treat as portfolio centerpieces.

## DAILY

| Repo | Why it matters | Current posture | Next maintenance move |
|---|---|---|---|
| [`qq-ai-bot`](https://github.com/happysnaker/qq-ai-bot) | Flagship bot infrastructure: OneBot, ACP bridge, sessions, progress streaming, metrics, Docker, sponsorware | CI, Docker publish, discussions, sponsorware roadmap, promo kit, multi-instance docs, sponsor one-pager links | #23 and #24 shipped; keep #26 physical ARM / CasaOS validation moving and keep ecosystem PR status current |
| [`RDLeader`](https://github.com/happysnaker/RDLeader) / [project page](https://happysnaker.github.io/rdleader/) | Agent-ops control plane: runtime dispatch, approvals, QA evidence, public baseline | Public CI, pre-release, sponsorware, QA/runtime docs, discussions | Track external follow-up (#27); resolve license posture (#3); continue DevPlan sanitization (#1) |
| [`happysnaker`](https://github.com/happysnaker/happysnaker) | Central profile, proof index, sponsorware board | Public docs CI, proof hub pre-releases, sponsorware board, sponsor one-pager, support-surface coverage | Keep links, release notes, and CI fresh; update proof index / coverage table after major changes |

## PROOF

| Repo | Proof signal | Current posture | Next maintenance move |
|---|---|---|---|
| [`happydb`](https://github.com/happysnaker/happydb) | Java database internals: storage engine, B+ tree, MVCC, recovery, optimizer, Raft experiments | Good systems signal, pinned/highlighted | Consider proof index entry with architecture / tests / design notes |
| [`go-service-starter`](https://github.com/happysnaker/go-service-starter) | Production-minded Go service skeleton: config, logging, health, graceful shutdown, Docker | Good backend craft signal | Keep as pinned support proof; avoid overpromoting until it has more users/examples |
| [`go-http-middleware-kit`](https://github.com/happysnaker/go-http-middleware-kit) | Reusable net/http middleware: request IDs, logging, recovery, timeout, real IP | Good Go library signal | Keep docs/examples sharp; avoid running Go build/test locally per workspace rule |
| [`CSAPPLabsAndNotes`](https://github.com/happysnaker/CSAPPLabsAndNotes) | Systems fundamentals and CSAPP study proof | Strong stars/forks relative to account; now routes to the frozen sponsor one-pager | Keep as proof of fundamentals; sponsor route should stay light-touch |
| [`HRpc`](https://github.com/happysnaker/HRpc) | Java / Netty RPC learning project | Mentioned in profile, not audited in this pass | Later: inspect health, README, license, and whether it should remain highlighted |

## SUPPORT

| Repo | Role | Current posture | Next maintenance move |
|---|---|---|---|
| [`Resume`](https://github.com/happysnaker/Resume) | Portfolio template with existing stars/forks | Strong social proof, less aligned with current backend/agent direction; now routes to the frozen sponsor one-pager | Keep pinned only if social proof matters; otherwise consider replacing with RDLeader manually |
| [`github-profile-checklist`](https://github.com/happysnaker/github-profile-checklist) | Supports paid review / profile packaging offer | Useful funnel asset | Keep sample audit linked from profile support section |
| [`backend-engineer-checklist`](https://github.com/happysnaker/backend-engineer-checklist) | Backend interview / self-review checklist | Support content for profile | Keep as supportive asset, not flagship |
| [`system-design-checklist`](https://github.com/happysnaker/system-design-checklist) | Architecture / interview / design review checklist | Support content for profile | Keep as supportive asset, not flagship |
| [`production-readiness-checklist`](https://github.com/happysnaker/production-readiness-checklist) | Release / launch / on-call checklist | Aligns with reliability/backend positioning | Consider linking from proof index if it gets examples |
| [`.github`](https://github.com/happysnaker/.github) | Default community health files | Enables default support/contribution/code-of-conduct | Keep quiet; maintain default hygiene only |
| [`happysnaker.github.io`](https://github.com/happysnaker/happysnaker.github.io) | Blog / landing pages | Public site backing profile links | Keep accurate with support/review/project pages |

## PARK

| Repo | Why parked | Next action before promotion |
|---|---|---|
| [`chinese-independent-developer`](https://github.com/happysnaker/chinese-independent-developer) | Interesting topic, but not yet aligned with backend/agent flagship story; now has CC0/license, support/security entrypoints, and Discussions enabled | Decide whether it is a serious content asset or keep as quiet support/funnel project before promoting |

## FORK / ARCHIVE

Many public forks under the account are contribution vehicles for upstream PRs. Treat them as context, not as portfolio centerpieces.

Rules:

- Do not pin short-lived forks.
- Archive temporary forks after upstream PRs are closed/merged when no longer needed.
- Use descriptions like “Temporary contribution fork for upstream PR …” when they must remain public.
- Keep the profile README explicit that forks are not the main portfolio surface.

Current active fork hygiene notes:

- `gin`, `testify`, and `cli` descriptions were normalized to say they are contribution / historical forks, not portfolio centerpieces.
- `urfave-cli-fork`, `jwt`, `pflag`, and `chi` already have contribution-fork descriptions.
- Do not archive active forks automatically unless the associated upstream PR/branch no longer needs maintenance.

## Manual pin recommendation
See also: [manual GitHub actions checklist](manual-github-actions.md).


Current pinned repos still include `Resume`. If the goal is strongest technical signal, the best manual pin set is:

1. `qq-ai-bot`
2. `RDLeader`
3. `happydb`
4. `go-service-starter`
5. `go-http-middleware-kit`
6. `CSAPPLabsAndNotes`

Rationale: this keeps one flagship bot-infra repo, one agent-ops control-plane repo, one Java systems project, two Go/backend craft repos, and one CS fundamentals repo.

## Operating cadence
See also: [GitHub operations cadence](operations-cadence.md).


Weekly:

- Check CI and Dependabot status for `qq-ai-bot`, `RDLeader`, and `happysnaker`.
- Update `docs/technical-proof-index.md` if new proof links land.
- Review sponsorware issues and discussions for stale asks.

Monthly:

- Revisit pinned repos.
- Close or archive stale temporary forks.
- Decide whether parked repos should be promoted, renamed, relicensed, or left quiet.
