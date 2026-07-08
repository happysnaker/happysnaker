# Technical Proof Index

> A compact evidence map for the repos and public work I most want reviewed. This is intentionally source-linked: prefer the repo, CI, docs, and issues over broad claims.

## Fast read

| Area | Best evidence | Why it matters |
|---|---|---|
| Bot infrastructure | [`qq-ai-bot`](https://github.com/happysnaker/qq-ai-bot) | OneBot transport, ACP agent bridge, session persistence, progress streaming, Docker, metrics, and deployment docs |
| Agent operations | [`RDLeader`](https://github.com/happysnaker/RDLeader) | Local-first control plane for AI R&D workers with runtime evidence, approvals, QA docs, and public CI |
| Systems learning | [`happydb`](https://github.com/happysnaker/happydb) | Java database internals: storage, B+ tree, MVCC, recovery, optimizer, and Raft experiments |
| Go service basics | [`go-service-starter`](https://github.com/happysnaker/go-service-starter) | Production-minded service starter: config, logging, health, graceful shutdown, Docker |
| Go middleware | [`go-http-middleware-kit`](https://github.com/happysnaker/go-http-middleware-kit) | Reusable net/http middleware for request IDs, logging, recovery, timeouts, and real IP handling |

## Flagship proof: qq-ai-bot

Public surfaces:

- Repo: <https://github.com/happysnaker/qq-ai-bot>
- Project page: <https://happysnaker.github.io/qq-ai-bot/>
- Promo kit: <https://github.com/happysnaker/qq-ai-bot/blob/main/docs/public/promo-kit.md>
- Sponsorware roadmap: <https://github.com/happysnaker/qq-ai-bot/blob/main/docs/public/sponsorware.md>
- Multi-instance notes: <https://github.com/happysnaker/qq-ai-bot/blob/main/docs/multi-instance-notes.md>

Current evidence:

- CI on latest public support/security baseline: <https://github.com/happysnaker/qq-ai-bot/actions/runs/28948017236>
- Docker image publish on latest public support/security baseline: <https://github.com/happysnaker/qq-ai-bot/actions/runs/28948017299>
- Public OneBot ecosystem placement: <https://onebot.dev/ecosystem>
- OneBot community discussion: <https://github.com/orgs/botuniverse/discussions/264>

What to look for:

- clear separation between QQ / OneBot transport and ACP-compatible agents;
- persistent sessions and explicit session-store tradeoffs;
- progress streaming back to QQ;
- Prometheus-style metrics and readiness/status endpoints;
- deployment honesty around Redis, multi-instance behavior, and OneBot WebSocket routing.

## Flagship proof: RDLeader

Public surfaces:

- Repo: <https://github.com/happysnaker/RDLeader>
- Public release roadmap: <https://github.com/happysnaker/RDLeader/blob/main/docs/public-release-roadmap.md>
- Public QA evidence: <https://github.com/happysnaker/RDLeader/blob/main/docs/public/qa-evidence.md>
- Runtime endurance model: <https://github.com/happysnaker/RDLeader/blob/main/docs/public/runtime-endurance.md>
- Demo walkthrough: <https://github.com/happysnaker/RDLeader/blob/main/docs/public/demo-walkthrough.md>
- Promo kit: <https://github.com/happysnaker/RDLeader/blob/main/docs/public/promo-kit.md>
- License / reuse note: <https://github.com/happysnaker/RDLeader/blob/main/docs/public/license-decision.md>
- Public roadmap discussion: <https://github.com/happysnaker/RDLeader/discussions/4>

Current evidence:

- Public CI on latest baseline: <https://github.com/happysnaker/RDLeader/actions/runs/28949090323>
- Public packaging / DevPlan sanitization tracker: <https://github.com/happysnaker/RDLeader/issues/1>
- Public-safe demo sponsorware tracker: <https://github.com/happysnaker/RDLeader/issues/2>
- License hygiene tracker: <https://github.com/happysnaker/RDLeader/issues/3>

What to look for:

- runtime boundaries instead of hidden chat sessions;
- structured task envelopes and runtime result events;
- stale task recovery and endurance posture;
- human-in-the-loop approval framing;
- public-safe documentation that avoids leaking private DevPlan artifacts.

## Upstream contribution signal

Recent upstream work is intentionally small but concrete: parser edge cases, retry semantics, CLI behavior, observability docs, and SDK/client correctness.

Representative links:

- HashiCorp retryablehttp fixes: <https://github.com/hashicorp/go-retryablehttp/pulls?q=author%3Ahappysnaker>
- Prometheus client/procfs work: <https://github.com/pulls?q=author%3Ahappysnaker+prometheus>
- pflag fixes: <https://github.com/spf13/pflag/pulls?q=author%3Ahappysnaker>
- urfave/cli work: <https://github.com/urfave/cli/pulls?q=author%3Ahappysnaker>
- GitHub CLI work: <https://github.com/cli/cli/pulls?q=author%3Ahappysnaker>

Review lens:

- Does the change fix a real edge case?
- Is the behavior covered by tests or docs?
- Does the patch avoid broad rewrites?
- Does the PR reduce ambiguity for future users?

## Sponsorware / support proof

Central board:

- <https://github.com/happysnaker/happysnaker/blob/master/docs/sponsorware-board.md>

Current sponsor targets are intentionally concrete:

- `qq-ai-bot`: latency histograms, Postgres session store, arm64 / CasaOS validation;
- `RDLeader`: public-safe demo walkthrough, DevPlan bundle sanitization.

Support page:

- <https://happysnaker.github.io/support/>

## Known caveats

- `RDLeader` is public but its final license posture is not decided yet; see <https://github.com/happysnaker/RDLeader/issues/3>.
- Some RDLeader evidence remains local until redacted because raw DevPlan logs can contain private paths or live integration identifiers.
- `qq-ai-bot` is stronger as a bot infrastructure scaffold than as a polished consumer-facing app.
