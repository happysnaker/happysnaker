# Sponsor Scorecard Coverage

> Coverage map for where the sponsor conversion scorecard is now enforced. Use this after [sponsor-conversion-scorecard.md](sponsor-conversion-scorecard.md) to verify that support, review, issue, and external-follow-up paths route through Hot / Warm / Nurture / No-send before an ask is posted.

## Coverage rule

Every support or outreach surface should satisfy five properties before asking for money, a review, or an external update:

1. link to the sponsor conversion scorecard;
2. expose Hot / Warm / Nurture / No-send qualification;
3. preserve privacy / no-overclaim guardrails;
4. have a checker or live issue gate that fails when those routes drift.
5. keep productized offer cards tied to concrete public outcomes instead of vague donation asks.

## Covered surfaces

| Layer | Surfaces | Proof / checker | Current scorecard gate |
|---|---|---|---|
| Profile first screen | profile README support/proof block | `python3 scripts/check_readme_badges.py --json` | first-screen proof/support route includes sponsor conversion scorecard |
| Support / Pages funnel | support page productized offer cards, `qq-ai-bot`, `RDLeader`, review page, deploy-read sample | `python3 scripts/check_site_hygiene.py --site-root ../happysnaker.github.io --live --timeout 8 --json`; `python3 scripts/check_review_funnel.py --site-root ../happysnaker.github.io --live --timeout 8 --json` | Pages require scorecard links and Hot / Warm / Nurture / No-send before support or paid-review asks; offer cards route to fund a real host report, fund curator follow-up, buy a deploy read, or tip with attribution |
| Sponsor one-pager / release | `docs/sponsor-one-pager.md` and `v2026.07-sponsor-one-pager` | `python3 scripts/check_sponsor_release.py --json` | sponsor-facing release includes scorecard and No-send guardrail |
| Live sponsor/support issues | `qq-ai-bot#26`, `qq-ai-bot#28`, `RDLeader#1`, `RDLeader#3`, `RDLeader#27` | `python3 scripts/check_sponsor_issues.py --json` | issue bodies require scorecard, Hot / Warm / Nurture / No-send, and No-send blocks generic proof bumps |
| External follow-up queue | tracked external PRs plus flagship tracker issues | `python3 scripts/check_external_followups.py --summary`; `python3 scripts/check_external_followups.py --action-class optional-update --json` | rows emit `qualification`, `scorecardAction`, and `postedFollowupUrl`; optional-update rows are Warm, quiet rows are Nurture or No-send, and the `Posted follow-ups` summary prevents duplicate external bumps |
| Profile/default support fallback | profile support docs, profile issue contact links, default `.github` support/contact files | `python3 scripts/check_support_routes.py --json` | account-wide fallback includes scorecard before generic support asks |
| Flagship repos | `qq-ai-bot` and `RDLeader` README / SUPPORT / issue-contact files | `python3 scripts/check_support_routes.py --json` | flagship visitors classify before support, external follow-up, or reuse-adjacent asks |
| Paid-review repos | `Resume` and `github-profile-checklist` | `python3 scripts/check_support_routes.py --json` | profile / README buyers classify before paid review or support asks |
| Technical-review repos | `backend-engineer-checklist`, `system-design-checklist`, `production-readiness-checklist` | `python3 scripts/check_support_routes.py --json` | backend / system-design / launch-readiness buyers classify before paid review or support asks |
| Systems / indie content repos | `CSAPPLabsAndNotes`, `happydb`, `chinese-independent-developer` | `python3 scripts/check_support_routes.py --json` | study, database-internals, and indie-list readers classify before support or paid-review asks |
| Go docs/template repos | `go-service-starter` and `go-http-middleware-kit` | `python3 scripts/check_support_routes.py --json` | Go service and middleware readers classify before support, deploy-read, or paid-review asks |

## No-send guardrails

No-send wins over all conversion language when any of these is true:

- a real physical ARM / CasaOS / NAS / SBC report has not landed for `qq-ai-bot #26 arm64`;
- RDLeader license posture is unresolved in `RDLeader#3`;
- the planned external review gate is not due yet (`2026-07-23 UTC`);
- the next action would be a generic donation bump with no new public proof;
- the request would require private logs, credentials, QR codes, payment screenshots, internal URLs, or raw live integration output in public.

## Verification bundle

```bash
python3 scripts/check_sponsor_scorecard_coverage.py --json
python3 scripts/check_sponsor_conversion_scorecard.py --json
python3 scripts/check_support_routes.py --json
python3 scripts/check_review_funnel.py --site-root ../happysnaker.github.io --live --timeout 8 --json
python3 scripts/check_sponsor_issues.py --json
python3 scripts/check_external_followups.py --summary
```
