# Flagship technical map

> A compact map from technical signal to public proof and support routes. Use this when a recruiter, curator, sponsor, or maintainer asks “what should I inspect first?”

Snapshot: 2026-07-11 Asia/Shanghai.

## Fast read

| Signal | `qq-ai-bot` | `RDLeader` |
|---|---|---|
| Systems boundary | OneBot / NapCat / LLOneBot transport stays separate from ACP agent execution and session orchestration | Local-first task ownership, progressive context assembly, runtime dispatch, approval gates, and public-safe QA evidence stay separated |
| Operator proof | Docker quickstart, stable `v0.1.7` image, multi-arch image publish, arm64 smoke, metrics, deployment notes | Public proof ladder, fake-data demos, runtime endurance notes, browser walkthrough, distribution kit, submission tracker |
| Maintenance proof | CI, CodeQL, Docker publish, arm64 smoke, grouped Dependabot, support-route checks | CI, CodeQL, grouped Dependabot, security hardening, support-route checks, license caveat tracking |
| External proof | OneBot ecosystem, ACP docs/client listing, NapCat docs/Docker template, Docker/CasaOS/Umbrel/Homelab PRs | one merged coding-agent list PR, one open autonomous-agent list PR, public project page and proof ladder |
| Current support note | `qq-ai-bot #26 arm64` | `RDLeader #27` |
| Caveat | QEMU / workflow arm64 smoke is green; physical ARM / CasaOS / NAS / SBC report is still open | Clean configured alert surface is public; reuse rights remain blocked on license issue |

## Start here

- Proof before payment: <https://happysnaker.github.io/support/#proof-before-payment>
- Current concrete asks: <https://happysnaker.github.io/support/#current-asks>
- Flagship status snapshot: [flagship-status-snapshot.md](flagship-status-snapshot.md)
- Technical proof index: [technical-proof-index.md](technical-proof-index.md)
- Support surface coverage: [support-surface-coverage.md](support-surface-coverage.md)
- Sponsor one-pager: [sponsor-one-pager.md](sponsor-one-pager.md)
- Deploy-read sample: <https://happysnaker.github.io/review/deploy-read-sample/>

## What to inspect in `qq-ai-bot`

Primary links:

- Repository: <https://github.com/happysnaker/qq-ai-bot>
- Project page: <https://happysnaker.github.io/qq-ai-bot/>
- Support route: <https://happysnaker.github.io/support/#from-qq-ai-bot>
- Current physical-host validation target: <https://github.com/happysnaker/qq-ai-bot/issues/26>
- Tester pack: <https://github.com/happysnaker/qq-ai-bot/blob/main/docs/public/arm64-casaos-tester-pack.md>
- Homelab outreach kit: <https://github.com/happysnaker/qq-ai-bot/blob/main/docs/public/homelab-outreach-kit.md>

Technical reading order:

1. Transport / agent boundary: OneBot 11, NapCat / LLOneBot, and ACP-compatible agent execution are positioned as separable layers.
2. Operator path: Docker quickstart, public image tags, multi-instance notes, deployment validation, and arm64 smoke are the proof chain.
3. Observability path: progress streaming and Prometheus-style `/metrics` make the project read as bot infrastructure instead of a one-off chat demo.
4. Ecosystem path: official/community docs and app-store PRs create discovery surfaces outside this profile.

Current funding conversion:

- Use payment note `qq-ai-bot #26 arm64` for real physical ARM / CasaOS / NAS / SBC validation.
- Use `Deploy read` / `Quick read` / `Async review` if the buyer wants the same bot / agent / infra packaging pass for their own public repo; preview the deliverable first at <https://happysnaker.github.io/review/deploy-read-sample/>.
- Do not claim physical-host validation until a real redacted report lands.

## What to inspect in `RDLeader`

Primary links:

- Repository: <https://github.com/happysnaker/RDLeader>
- Project page: <https://happysnaker.github.io/rdleader/>
- Support route: <https://happysnaker.github.io/support/#from-rdleader>
- External review follow-up: <https://github.com/happysnaker/RDLeader/issues/27>
- License posture tracker: <https://github.com/happysnaker/RDLeader/issues/3>
- Public distribution kit: <https://github.com/happysnaker/RDLeader/blob/main/docs/public/distribution-kit.md>
- Submission tracker: <https://github.com/happysnaker/RDLeader/blob/main/docs/public/submission-tracker.md>

Technical reading order:

1. Control-plane boundary: task ownership, runtime dispatch, approval gates, and worker context are presented as separate concerns.
2. Public-safe evidence: fake-data demos, QA evidence, runtime endurance notes, and browser walkthroughs avoid private DevPlan leakage.
3. Security posture: configured CodeQL / Dependabot / secret-scanning alert surfaces are tracked and currently clean.
4. Distribution path: project page, distribution kit, submission tracker, and external PRs turn the repo into a visible agent-ops proof surface.

Current funding conversion:

- Use payment note `RDLeader #27` for external submission review follow-up and curator-response work.
- Use `RDLeader #1` for further DevPlan bundle sanitization.
- Use `RDLeader #3` only for license/reuse-boundary work; do not imply reuse rights before that decision lands.
- Use `Deploy read` / `Quick read` / `Async review` for people who want their own agent / internal-tool repo packaged with the same proof-first style; preview: <https://happysnaker.github.io/review/deploy-read-sample/>.

## Automation that keeps this map honest

The profile repo now has CI / scheduled checks for:

- public docs and sensitive-pattern checks via [scripts/verify_public_docs.py](../scripts/verify_public_docs.py);
- support-route drift via [scripts/check_support_routes.py](../scripts/check_support_routes.py);
- repository metadata drift via [scripts/check_repo_metadata.py](../scripts/check_repo_metadata.py);
- sponsor release drift via [scripts/check_sponsor_release.py](../scripts/check_sponsor_release.py);
- paid review / deploy-read funnel drift via [scripts/check_review_funnel.py](../scripts/check_review_funnel.py);
- current workflow / alert state via [scripts/check_github_status.py](../scripts/check_github_status.py);
- external follow-up summary via [scripts/check_external_followups.py](../scripts/check_external_followups.py).

The goal is not to claim every repo is perfect. The goal is to make the current flagship proof and sponsor routes source-linked, repeatable, and hard to accidentally overstate.
