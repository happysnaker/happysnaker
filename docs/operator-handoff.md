# Operator handoff

> Read this first when continuing the ongoing `happysnaker` GitHub takeover. Goal: keep the profile technically credible, keep flagship proof current, and keep sponsor/support paths visible without noisy external bumps.

Snapshot: 2026-07-11 Asia/Shanghai.

## Current source of truth

Run these from the profile repository before acting:

```bash
python3 scripts/check_github_status.py --summary
python3 scripts/run_profile_preflight.py --link-scope core --workers 8 --skip-external
python3 scripts/check_manual_blockers.py --json
python3 scripts/check_operator_handoff.py
python3 scripts/check_stable_profile_links.py
python3 scripts/check_gh_usage.py
python3 scripts/check_ci_workflow_contract.py
python3 scripts/check_checker_catalog.py --json
python3 scripts/check_share_kit.py --json
python3 scripts/check_review_funnel.py --site-root ../happysnaker.github.io --live --timeout 8 --json
python3 scripts/check_sponsor_issues.py --json
python3 scripts/check_external_followups.py --summary
```

Use `python3 scripts/run_profile_preflight.py --external-only --action-class optional-update --external-summary --enforce-review-due` only for the scheduled external review view; before the review date it should fail closed.

## Current flagship state

- `qq-ai-bot`: CI, CodeQL, Docker publish, and arm64 smoke are green in the latest status checker. The project has Docker / metrics / session / ACP / OneBot proof, but `qq-ai-bot #26 arm64` still needs a real physical ARM / CasaOS / NAS / SBC report.
- `RDLeader`: CI and CodeQL are green in the latest status checker. The project has public demo / QA / runtime / security proof, but license posture is still unresolved in `RDLeader#3`; do not imply reuse rights.
- `happysnaker.github.io`: Pages deploy is green and the support page exposes proof-before-payment, current asks, share kit, and the deploy-read sample.
- The sponsor one-pager release is intentionally compact and now includes the `Deploy read` path; append-only operational detail belongs in [happysnaker#2](https://github.com/happysnaker/happysnaker/issues/2).

## Proof and support links

- Proof before payment: <https://happysnaker.github.io/support/#proof-before-payment>
- Current concrete asks: <https://happysnaker.github.io/support/#current-asks>
- Share kit: [share-kit.md](share-kit.md)
- Deploy-read sample: <https://happysnaker.github.io/review/deploy-read-sample/>
- Flagship technical map: [flagship-technical-map.md](flagship-technical-map.md)
- Flagship status snapshot: [flagship-status-snapshot.md](flagship-status-snapshot.md)
- Sponsor one-pager source: [sponsor-one-pager.md](sponsor-one-pager.md)
- Sponsor one-pager release: <https://github.com/happysnaker/happysnaker/releases/tag/v2026.07-sponsor-one-pager>
- Support surface coverage: [support-surface-coverage.md](support-surface-coverage.md)
- Operations cadence: [operations-cadence.md](operations-cadence.md)

## Open blockers

1. Profile pinned repositories still require manual GitHub web UI action: replace `happysnaker/Resume` with `happysnaker/RDLeader`.
2. RDLeader license posture still requires a human decision before wider reuse claims.

Tracked by:

- Manual checklist: [manual-github-actions.md](manual-github-actions.md)
- Manual issue: <https://github.com/happysnaker/happysnaker/issues/1>
- RDLeader license issue: <https://github.com/happysnaker/RDLeader/issues/3>

## External follow-up rule

Do not comment on external PRs just to bump them. Use [external-follow-up-queue.md](external-follow-up-queue.md).

Current planned review remains `2026-07-16 UTC` unless a maintainer or tester replies earlier. For scheduled review, run:

```bash
python3 scripts/run_profile_preflight.py --link-scope profile --workers 12
python3 scripts/run_profile_preflight.py --external-only --action-class optional-update --external-summary --enforce-review-due
python3 scripts/run_profile_preflight.py --external-only --external-summary --enforce-review-due
```

## Automation guardrails

- Use `scripts/github_cli.py` for GitHub CLI JSON/API calls so transient GitHub API/network errors retry consistently.
- Use stable profile workflow links for evergreen profile proof; `python3 scripts/check_stable_profile_links.py` rejects one-off profile self-check run links in public docs.
- `python3 scripts/check_gh_usage.py` fails if a proof/status checker bypasses that helper with a direct `gh` subprocess call.
- `python3 scripts/check_ci_workflow_contract.py` fails if scheduled CI stops compiling/running the required proof/support drift checks.
- `python3 scripts/check_checker_catalog.py` fails if a new proof checker is not documented in the technical proof index.
- `python3 scripts/check_review_funnel.py` verifies the paid review / deploy-read path across support, review, deploy-read sample, and flagship inbound pages.

## Good next actions

Prefer small, reversible moves that make one of these more true:

- public proof is easier to inspect;
- support/sponsor routes are easier to find;
- claims are better guarded against overstatement;
- external follow-up becomes less noisy and more evidence-backed;
- manual blockers are easier for the account owner to resolve.

Good examples:

- improve a checker so drift is caught automatically;
- update a proof doc after a meaningful workflow/security/support change;
- refresh a compact status snapshot when flagship state materially changes;
- update issue #1 or #2 with evidence after a manual-blocker or operations audit;
- improve share-kit / support-page routes without posting externally;
- keep deploy-read / paid-review routes visible from profile, flagship support files, default `.github`, sponsor packet, technical map, and share kit.

Avoid:

- repeated external PR comments without new evidence or maintainer request;
- broad claims that all old repos are CodeQL-clean;
- physical ARM / CasaOS completion claims before `qq-ai-bot#26` has a real host report;
- RDLeader reuse-rights claims before a root license and `RDLeader#3` are resolved;
- growing the sponsor release body again instead of using issue #2 for the append-only log.
