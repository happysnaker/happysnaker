# External Follow-up Queue

> Purpose: keep ecosystem PRs, discussions, tester calls, and sponsor/support updates moving without noisy repeated bumps. Use this queue before posting any external follow-up.

Tracking issue: <https://github.com/happysnaker/happysnaker/issues/2>.

## Rules

- Recheck current state before any comment or PR-body edit.
- Do not comment externally if there is no maintainer feedback, no failed check, and no new public proof relevant to that surface.
- Prefer updating internal trackers over bumping external maintainers.
- Keep every follow-up source-linked and short.
- Do not paste private QQ data, OneBot tokens, app IDs, chat IDs, open IDs, QR screenshots, private paths, raw live logs, or payment screenshots.
- Do not claim physical ARM / CasaOS validation until a real physical-host report lands.
- Do not imply RDLeader reuse rights until <https://github.com/happysnaker/RDLeader/issues/3> is resolved.


## Latest audit snapshot: 2026-07-11 Asia/Shanghai / 2026-07-10 UTC

Current audit result:

- `qq-ai-bot`, `RDLeader`, `happysnaker`, and `happysnaker.github.io` working trees were clean at audit time.
- `qq-ai-bot` latest CI / CodeQL / Docker publish / arm64 smoke were successful.
- `RDLeader` latest CI / CodeQL were successful.
- `happysnaker` profile CI / CodeQL were successful.
- `happysnaker.github.io` latest Pages deploy was successful.
- `qq-ai-bot` and `RDLeader` open CodeQL / Dependabot / secret-scanning alerts were all `0`.
- No new maintainer feedback was found on the tracked external PRs during this audit.
- No real physical ARM / CasaOS / NAS / SBC report had landed for `qq-ai-bot#26` during this audit.
- Decision: do not post external follow-up now; keep the next planned review on 2026-07-16 unless a maintainer or tester replies earlier.

## Prepared material for the 2026-07-16 review window

Use this only if the row guidance below allows an update. Do not post it before the review gate is due, and do not paste the same snippet repeatedly across PRs.

New internal proof since the last queue audit:

- profile README now routes uncertain visitors through the 10-second support router before payment;
- `qq-ai-bot` and `RDLeader` project pages now expose first-screen `Pick Tip / Proof / Review / Fund` CTAs;
- `qq-ai-bot` README / support / issue-contact surfaces now include the support router and `qq-ai-bot #26 arm64` note;
- `RDLeader` README / support / issue-contact surfaces now include the support router while preserving the unresolved license / reuse-rights guardrail;
- share-kit now has a copy-ready `Project-page closed loop update` snippet.

Reusable links for scheduled review comments:

- Project-page closed loop share snippet: [share-kit.md#project-page-closed-loop-update](share-kit.md#project-page-closed-loop-update)
- 10-second support router: <https://happysnaker.github.io/support/#sponsor-router>
- qq-ai-bot project page: <https://happysnaker.github.io/qq-ai-bot/>
- RDLeader project page: <https://happysnaker.github.io/rdleader/>
- Deploy-read sample: <https://happysnaker.github.io/review/deploy-read-sample/>

Short scheduled-review copy, if a row below explicitly allows an update:

```text
Since the last check I tightened the public proof/support path so reviewers do not need to infer the state from the repo alone: profile README → project page → 10-second support router → concrete Tip / Proof / Review / Fund paths.

Project page: <project-page-url>
Support router: https://happysnaker.github.io/support/#sponsor-router
Proof caveat: qq-ai-bot still needs a real physical ARM/CasaOS host report; RDLeader reuse rights are still blocked on the license issue.
```

## Next scheduled review: 2026-07-16

Run this check on 2026-07-16 UTC, or earlier only if a maintainer/tester replies.

### qq-ai-bot surfaces

| Surface | Current state checked 2026-07-11 | Next action on 2026-07-16 | Follow-up material |
|---|---|---|---|
| [docker/awesome-compose#781](https://github.com/docker/awesome-compose/pull/781) | open / mergeable; DCO success; review required | If still review-required and no maintainer reply, one short update is acceptable only if it links the project page, stable image, latest Docker publish, and tester pack. Otherwise stay quiet. | [promo kit](https://github.com/happysnaker/qq-ai-bot/blob/main/docs/public/promo-kit.md), [homelab outreach kit](https://github.com/happysnaker/qq-ai-bot/blob/main/docs/public/homelab-outreach-kit.md), [project-page loop snippet](share-kit.md#project-page-closed-loop-update), [support router](https://happysnaker.github.io/support/#sponsor-router) |
| [Cp0204/CasaOS-AppStore-Play#42](https://github.com/Cp0204/CasaOS-AppStore-Play/pull/42) | open / mergeable; no checks; no maintainer feedback | If still open, update only if a real tester report lands or maintainer asks. Otherwise keep waiting because physical CasaOS validation is still missing. | [tester pack](https://github.com/happysnaker/qq-ai-bot/blob/main/docs/public/arm64-casaos-tester-pack.md) |
| [getumbrel/umbrel-apps#5834](https://github.com/getumbrel/umbrel-apps/pull/5834) | open / mergeable; lint success; no maintainer feedback | Recheck lint / mergeability. Do not comment unless maintainer asks or checks regress. | [project page](https://happysnaker.github.io/qq-ai-bot/), [ecosystem tracker](https://github.com/happysnaker/qq-ai-bot/blob/main/docs/public/ecosystem-tracker.md) |
| [AwesomeHomelab#98](https://github.com/AwesomeHomelab/awesome-homelab/pull/98) | open / mergeable; no checks; no maintainer feedback | If still no feedback, one short homelab-focused update may be useful, but only after confirming the tester pack and project page still render. | [homelab outreach kit](https://github.com/happysnaker/qq-ai-bot/blob/main/docs/public/homelab-outreach-kit.md), [project-page loop snippet](share-kit.md#project-page-closed-loop-update) |
| [LLOneBot/LuckyLilliaDoc#20](https://github.com/LLOneBot/LuckyLilliaDoc/pull/20) | open / mergeable; Sourcery success; no maintainer feedback | Do not bump unless maintainer replies. This is docs, not a support emergency. | [promo kit LLOneBot snippet](https://github.com/happysnaker/qq-ai-bot/blob/main/docs/public/promo-kit.md) |
| [LLOneBot/llonebot.nix#22](https://github.com/LLOneBot/llonebot.nix/pull/22) | open / mergeable; Sourcery success; no maintainer feedback | Do not bump unless maintainer replies or checks change. | [promo kit LLOneBot snippet](https://github.com/happysnaker/qq-ai-bot/blob/main/docs/public/promo-kit.md) |
| [qq-ai-bot#26](https://github.com/happysnaker/qq-ai-bot/issues/26) | open; QEMU smoke green; tester pack + outreach kit published; no physical-host report yet | Check for new issue/discussion reports. If none, keep issue open and avoid claiming completion. | [tester pack](https://github.com/happysnaker/qq-ai-bot/blob/main/docs/public/arm64-casaos-tester-pack.md), [outreach kit](https://github.com/happysnaker/qq-ai-bot/blob/main/docs/public/homelab-outreach-kit.md) |

### RDLeader surfaces

| Surface | Current state checked 2026-07-11 | Next action on 2026-07-16 | Follow-up material |
|---|---|---|---|
| [awesome-autonomous-agents#20](https://github.com/jbesomi/awesome-autonomous-agents/pull/20) | open / mergeable; no checks; no maintainer feedback | If still open and no feedback, use the security-proof snippet only once, or stay quiet if the PR was recently touched by maintainers. | [RDLeader promo kit](https://github.com/happysnaker/RDLeader/blob/main/docs/public/promo-kit.md), [project page](https://happysnaker.github.io/rdleader/), [support router](https://happysnaker.github.io/support/#sponsor-router) |
| [awesome-coding-agents#13](https://github.com/kailiu42/awesome-coding-agents/pull/13) | merged; validate-catalog success | No action. Keep as proof surface only. | [submission tracker](https://github.com/happysnaker/RDLeader/blob/main/docs/public/submission-tracker.md) |
| [RDLeader#27](https://github.com/happysnaker/RDLeader/issues/27) | open; copy kit and submission tracker updated | Update only when an external PR receives feedback or a scheduled recheck finds a meaningful status change. | [submission tracker](https://github.com/happysnaker/RDLeader/blob/main/docs/public/submission-tracker.md) |

## Commands for the scheduled check

```bash
# Profile / support-route preflight
python3 scripts/run_profile_preflight.py --link-scope profile --workers 12
python3 scripts/run_profile_preflight.py --external-only --action-class optional-update --external-summary --enforce-review-due
python3 scripts/run_profile_preflight.py --external-only --external-summary --enforce-review-due

# Strict flagship alert state. Use explicit state=open so API defaults/pagination do not hide open alerts.
for repo in happysnaker/qq-ai-bot happysnaker/RDLeader; do
  echo "## $repo"
  gh api "repos/$repo/code-scanning/alerts?state=open&per_page=100" --jq 'length'
  gh api "repos/$repo/dependabot/alerts?state=open&per_page=100" --jq 'length'
  gh api "repos/$repo/secret-scanning/alerts?state=open&per_page=100" --jq 'length'
done
```

## Evidence to record after the scheduled check

- current PR / tracked issue state, checks, action class, next-action guidance, due-gate status, and compact summary from `python3 scripts/run_profile_preflight.py --external-only --external-summary --enforce-review-due`; use `--action-class optional-update` to isolate surfaces where a short scheduled update may be allowed;
- whether any external maintainer replied;
- whether a real ARM / CasaOS physical-host report landed;
- whether any flagship alert count became non-zero using explicit `state=open` API queries;
- whether support-route checker, metadata checker, profile-pin checker, RDLeader license checker, or profile-scope link checker failed;
- manual blocker summary from `python3 scripts/check_manual_blockers.py`, including whether `RDLeader` is still missing from profile pins or RDLeader license posture is still unresolved;
- whether a new external comment was actually posted, or why no comment was posted.

Record the outcome in <https://github.com/happysnaker/happysnaker/issues/2> and update project trackers only if the state changed.
