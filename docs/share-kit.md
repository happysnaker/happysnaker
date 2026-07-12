# Share kit

> Copy-ready snippets for promoting `happysnaker` projects without overstating proof, spamming maintainers, or hiding the sponsor path. Source set: [sponsor one-pager](sponsor-one-pager.md), [flagship technical map](flagship-technical-map.md), [flagship status snapshot](flagship-status-snapshot.md), [sponsorware board](sponsorware-board.md), [sponsor conversion scorecard](sponsor-conversion-scorecard.md), and [proof before payment](https://happysnaker.github.io/support/#proof-before-payment).

## Core angle

Two public projects are easiest to share right now; repositories without local support docs now inherit the default `.github` support-router fallback.

- `qq-ai-bot`: self-hosted QQ / OneBot / NapCat / LLOneBot bridge for ACP-compatible agents, with Docker, metrics, persistent sessions, progress streaming, multi-arch image publishing, and QEMU arm64 smoke evidence.
- `RDLeader`: local-first AI worker control-plane research, with task ownership, runtime dispatch, approval gates, fake-data demos, public QA evidence, CodeQL cleanup, and external submission tracking.

Best links:

| Need | Link |
|---|---|
| Proof before payment | <https://happysnaker.github.io/support/#proof-before-payment> |
| 10-second support router | <https://happysnaker.github.io/support/#sponsor-router> |
| Default support fallback | <https://github.com/happysnaker/.github/commit/0ec8ed7> |
| Current concrete asks | <https://happysnaker.github.io/support/#current-asks> |
| qq-ai-bot project page | <https://happysnaker.github.io/qq-ai-bot/> |
| RDLeader project page | <https://happysnaker.github.io/rdleader/> |
| Technical map | [flagship-technical-map.md](flagship-technical-map.md) |
| Status snapshot | [flagship-status-snapshot.md](flagship-status-snapshot.md) |
| Sponsor board | [sponsorware-board.md](sponsorware-board.md) |
| Sponsor conversion scorecard | [sponsor-conversion-scorecard.md](sponsor-conversion-scorecard.md) |

## Audience routing matrix

Use this table before posting or replying so the CTA matches the reader instead of sounding like a generic donation ask. If [sponsor-conversion-scorecard.md](sponsor-conversion-scorecard.md) cannot identify a landing surface, proof surface, concrete note, and follow-up owner, do not post the ask yet.

| Audience | Lead with | Best next link | Ask / note | Do not claim |
|---|---|---|---|---|
| Homelab / CasaOS tester | `qq-ai-bot` multi-arch + QEMU arm64 smoke is ready for a real device report | <https://github.com/happysnaker/qq-ai-bot/blob/main/docs/public/arm64-casaos-tester-pack.md> | `qq-ai-bot #26 arm64` | Do not say physical ARM / CasaOS validation is complete |
| Bot / agent builder | A deploy-read can find the first README / Docker / token / WebSocket story gap | <https://happysnaker.github.io/review/deploy-read-sample/> | `Deploy read` or `Quick read` | Do not ask for secrets, private tokens, QR codes, or raw logs |
| Curator / maintainer | Start from project pages and proof links, not a long repo dump | <https://happysnaker.github.io/qq-ai-bot/> / <https://happysnaker.github.io/rdleader/> | One concise context comment only when the review gate allows it | Do not repeatedly bump external PRs |
| Sponsor / funder | Tie the payment note to a public outcome | <https://happysnaker.github.io/support/#current-asks> | `qq-ai-bot #26 arm64` or `RDLeader #27` | Do not promise private-only deliverables |
| GitHub-profile / README customer | Sell the proof-backed packaging pass, not vague “consulting” | <https://happysnaker.github.io/support/#quick-read> | `Quick read` / `Async review` | Do not request private payment screenshots in public issues |
| RDLeader evaluator | Show the fake-data demo / submission tracker and the license caveat together | <https://happysnaker.github.io/rdleader/> | `RDLeader #27` | Do not imply reuse rights until `RDLeader#3` is resolved |

## Productized offer cards

Use these cards when someone is close enough to support, sponsor, or buy a review but still needs a concrete package. Each card keeps one proof link, one support note, and one guardrail visible.

| Offer card | Best fit | Proof link | Buyer/support note | Public outcome | Guardrail |
|---|---|---|---|---|---|
| **Fund a real host report** | Homelab / CasaOS / NAS / SBC users who can validate deployment | <https://github.com/happysnaker/qq-ai-bot/blob/main/docs/public/arm64-casaos-tester-pack.md> | `qq-ai-bot #26 arm64` | one real physical ARM / CasaOS / NAS / SBC report added to the public tracker | Do not say physical ARM / CasaOS validation is complete before the report lands |
| **Fund curator follow-up** | People who want RDLeader reviewed in agent / coding-agent lists | <https://github.com/happysnaker/RDLeader/blob/main/docs/public/submission-tracker.md> | `RDLeader #27` | one scheduled-review update or maintainer reply follow-up, logged publicly | Keep the RDLeader license caveat visible; this is not a license grant |
| **Buy a deploy read** | Bot / agent / infra repos that run but still look toy-like | <https://happysnaker.github.io/review/deploy-read-sample/> | `Deploy read` / `Quick read` | one blunt first-impression pass with top 3 fixes and first rewrite target | Only send public links; keep payment evidence private by email |
| **Tip with attribution** | Readers helped by a repo, checklist, or OSS fix | <https://happysnaker.github.io/support/#sponsor-router> | repo name, for example `happydb` or `go-service-starter` | maintenance credit can be summarized in the operations log when material | Do not turn educational repo threads into generic fundraising spam |

### Offer card — fund a public issue

```text
If you want support to create a visible public outcome, use a concrete note instead of a vague donation:

- qq-ai-bot #26 arm64 — fund / unlock a real ARM, CasaOS, NAS, or SBC host report
- RDLeader #27 — fund external submission review follow-up and curator replies

Proof first: https://happysnaker.github.io/support/#proof-before-payment
Current asks: https://happysnaker.github.io/support/#current-asks

I will not claim physical ARM/CasaOS completion or RDLeader reuse rights until the public trackers prove it.
```

### Offer card — buy a deploy read

```text
If your bot, agent, or infra repo runs but still looks toy-like, buy a deploy read instead of a vague consultation.

Preview the output style first:
https://happysnaker.github.io/review/deploy-read-sample/

Send only public links. I will return one blunt paragraph, top 3 fixes, and the first deploy / README / landing-page wording I would rewrite. Keep payment screenshots and private logs out of public issues.
```

### Offer card — proof-first tip

```text
If one repo, checklist, or OSS fix saved you time, use the support router and include the repo name in the note:

https://happysnaker.github.io/support/#sponsor-router

Good notes: qq-ai-bot, happydb, go-service-starter, go-http-middleware-kit, CSAPP notes.
If you want a funded public outcome instead of a tip, use qq-ai-bot #26 arm64 or RDLeader #27.
```

## Short share snippets

### X / short post

```text
I’m supporting happysnaker’s OSS work because the proof is inspectable, not vibes:

- qq-ai-bot: OneBot / ACP bot infra with Docker, metrics, sessions, arm64 smoke
- RDLeader: local-first AI worker control plane with CI, CodeQL cleanup, public demos

Proof before payment: https://happysnaker.github.io/support/#proof-before-payment
```

### LinkedIn / longer post

```text
A public engineering portfolio is stronger when every claim has a proof link.

The best current examples in happysnaker’s GitHub are:

1. qq-ai-bot — self-hosted QQ / OneBot / ACP bot infrastructure with Docker, sessions, metrics, progress streaming, multi-arch image publishing, and arm64 smoke evidence.
2. RDLeader — local-first AI worker control-plane research with task ownership, runtime dispatch, approval gates, fake-data demos, public QA evidence, and CodeQL cleanup.

If you want to inspect before supporting, start here:
https://happysnaker.github.io/support/#proof-before-payment

Current concrete support notes: `qq-ai-bot #26 arm64` or `RDLeader #27`.
```

### WeChat / private share

```text
这个 GitHub 账号现在最值得看的不是单个 README，而是证据链：

- qq-ai-bot：OneBot / NapCat / LLOneBot / ACP 方向的自托管机器人基础设施，Docker、metrics、会话、进度流、arm64 smoke 都有公开证据。
- RDLeader：本地优先的 AI worker 控制平面实验，有公开 demo、CI、CodeQL 清理、submission tracker。

如果要支持/赞助，先看 proof-before-payment：
https://happysnaker.github.io/support/#proof-before-payment

当前最具体的支持备注：`qq-ai-bot #26 arm64` 或 `RDLeader #27`。
```

### Curator / maintainer context

```text
The most compact review path is not the raw repo list. Start with:

qq-ai-bot project page: https://happysnaker.github.io/qq-ai-bot/
RDLeader project page: https://happysnaker.github.io/rdleader/
Technical map: https://github.com/happysnaker/happysnaker/blob/master/docs/flagship-technical-map.md

Those pages link back to CI, CodeQL, release, support, demo, and current caveats.
```

### Project-page closed loop update

```text
I tightened the public proof/support loop around happysnaker's two current flagship repos:

- profile README → project pages
- project pages → 10-second support router
- support router → Tip / Proof / Review / Fund

qq-ai-bot: https://happysnaker.github.io/qq-ai-bot/
RDLeader: https://happysnaker.github.io/rdleader/
Support router: https://happysnaker.github.io/support/#sponsor-router

Caveats stay visible: qq-ai-bot still needs a real physical ARM/CasaOS report, and RDLeader reuse rights are not granted until license posture is resolved.
```

## Sponsorship CTA snippets

### 10-second support router ask

```text
If you want to support happysnaker but don’t know which path fits, use the 10-second router:

- Tip — if one repo saved you time
- Proof — if you want CI / CodeQL / issue evidence before paying
- Review — if you want your own repo/profile packaged better
- Fund — if you want a visible public outcome like `qq-ai-bot #26 arm64` or `RDLeader #27`

Start here: https://happysnaker.github.io/support/#sponsor-router
```

### Concrete support ask

```text
If this work saved you time, use a concrete support note instead of a vague donation label:

- `qq-ai-bot #26 arm64` funds real physical ARM / CasaOS validation on top of the green QEMU arm64 smoke path.
- `RDLeader #27` funds external submission review follow-up and curator reply handling.
- `Quick read` funds a blunt first-impression pass on a public profile / repo / landing page.

Support page: https://happysnaker.github.io/support/#current-asks
```

### Paid review ask

```text
Want the same packaging pass on your own GitHub profile, repo, README, or landing page?

Start with the ¥29.9 quick read, then upgrade only if the first pass is useful:
https://happysnaker.github.io/review/
```

### Deploy-read sample ask

```text
Have a bot, agent, or infra repo that technically runs but still looks toy-like?

The ¥29.9 deploy-read sample shows the exact output style: one blunt paragraph, top 3 fixes, and deploy / README / landing-page wording to rewrite first.

Preview before paying: https://happysnaker.github.io/review/deploy-read-sample/
Order route: https://happysnaker.github.io/support/#quick-read
```

## Sponsor / paid-support intake replies

Use these only in direct replies after someone asks how to support, sponsor, or buy a review. Keep public threads on proof links; move payment screenshots and repo-specific review requests to email / private chat.

### Before-payment reply

```text
Thanks — please do not send any private logs, credentials, QR codes, payment screenshots, or internal URLs in a public thread.

Pick one route first:

1. Tip / inspect proof / fund a public issue: https://happysnaker.github.io/support/#sponsor-router
2. Quick read for your repo/profile: https://happysnaker.github.io/support/#quick-read
3. Deploy-read sample before paying: https://happysnaker.github.io/review/deploy-read-sample/

If you fund a public task, use one concrete note: `qq-ai-bot #26 arm64`, `RDLeader #27`, `RDLeader #1`, or `RDLeader #3`.
```

### Paid-review intake reply

```text
For a ¥29.9 quick read / deploy read, send only public material:

- repo / profile / landing-page URL
- what you want judged first: README, deploy path, issue funnel, or sponsor CTA
- any public constraints or target audience

I will reply with one blunt paragraph, top 3 fixes, and the first wording / route I would rewrite. Do not send secrets or private screenshots.
```

### Sponsor receipt follow-up

```text
Received — I will keep the outcome public and tied to the note you used.

I will log progress against the public tracker instead of promising a private result:
- `qq-ai-bot #26 arm64`: https://github.com/happysnaker/qq-ai-bot/issues/26
- `RDLeader #27`: https://github.com/happysnaker/RDLeader/issues/27
- operations proof log: https://github.com/happysnaker/happysnaker/issues/2

If the support was for a review, I will only discuss public repo/profile/landing-page material unless you explicitly move details to private email.
```

## Guardrails

Do not claim:

- `qq-ai-bot` has a real physical ARM / CasaOS report until `qq-ai-bot#26` receives one;
- RDLeader grants reuse rights until `RDLeader#3` and root license posture are resolved;
- every older `happysnaker` repository is CodeQL-clean; the current clean configured alert claim applies to the profile, `qq-ai-bot`, and `RDLeader` surfaces covered by [flagship-status-snapshot.md](flagship-status-snapshot.md);
- an external PR has merged unless the PR state actually says merged.

Do not post the same snippet repeatedly under external PRs. Use [external-follow-up-queue.md](external-follow-up-queue.md) before any maintainer-facing follow-up.

Never ask for private logs, credentials, QR codes, internal URLs, or payment screenshots in public. Keep sponsor receipts tied to a public tracker or a paid-review deliverable, not vague private promises.
