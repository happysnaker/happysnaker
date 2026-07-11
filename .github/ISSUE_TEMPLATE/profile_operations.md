---
name: Profile operations task
about: Track a public profile, proof-index, sponsorware, support-route, or portfolio hygiene task
labels: operations,portfolio
---

## Task

What public profile / portfolio / proof-index / sponsor-support action should be done?

## Why it matters

What does this improve for reviewers, users, curators, or sponsors?

## Public route affected

- [ ] Profile README / proof hub
- [ ] Sponsor one-pager / sponsorware board
- [ ] Proof before payment: https://happysnaker.github.io/support/#proof-before-payment
- [ ] Current concrete asks: https://happysnaker.github.io/support/#current-asks
- [ ] Flagship status snapshot: https://github.com/happysnaker/happysnaker/blob/master/docs/flagship-status-snapshot.md
- [ ] External follow-up queue: https://github.com/happysnaker/happysnaker/blob/master/docs/external-follow-up-queue.md

## Evidence needed

- [ ] README / docs update
- [ ] support route or payment-note path checked
- [ ] `python3 scripts/verify_public_docs.py`
- [ ] `python3 scripts/check_github_status.py`
- [ ] public-link check for the changed proof surface
- [ ] CI / CodeQL pass
- [ ] issue / discussion / release link if relevant

## Sponsor / support guardrails

- Do not claim physical ARM / CasaOS validation until a real physical-host report lands for `qq-ai-bot #26 arm64`.
- Do not imply RDLeader reuse rights until the license posture is resolved.
- Do not post external follow-up before the scheduled review unless a maintainer or tester replies.
- Do not create a refresh-only loop solely to chase the profile repo's own newest CI run.

## Notes

Do not paste private workspace paths, app IDs, open IDs, chat IDs, message IDs, QR screenshots, payment screenshots, or raw live integration output.
