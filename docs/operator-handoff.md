# Operator handoff

> Read this first when continuing the ongoing `happysnaker` GitHub takeover. Goal: keep the profile technically credible, keep flagship proof current, and keep sponsor/support paths visible without noisy external bumps.

Snapshot: 2026-07-11 Asia/Shanghai.

## Current source of truth

Run these from the profile repository before acting:

```bash
python3 scripts/check_github_status.py --summary
python3 scripts/run_profile_preflight.py --link-scope core --workers 8 --skip-external
python3 scripts/run_profile_preflight.py --link-scope core --workers 8 --skip-external --json
python3 scripts/check_manual_blockers.py --json
python3 scripts/check_operator_handoff.py
python3 scripts/check_operator_handoff.py --json
python3 scripts/check_stable_profile_links.py --json
python3 scripts/check_gh_usage.py --json
python3 scripts/check_ci_workflow_contract.py --json
python3 scripts/check_checker_catalog.py --json
python3 scripts/check_share_kit.py --json
python3 scripts/check_sponsor_pipeline.py --json
python3 scripts/check_sponsor_conversion_scorecard.py --json
python3 scripts/check_sponsor_scorecard_coverage.py --json
python3 scripts/check_review_funnel.py --site-root ../happysnaker.github.io --live --timeout 8 --json
python3 scripts/check_sponsor_issues.py --json
python3 scripts/check_sponsor_release.py --json
python3 scripts/check_support_routes.py --json
python3 scripts/check_repo_metadata.py --json
python3 scripts/check_issue_labels.py --json
python3 scripts/check_readme_badges.py --json
python3 scripts/check_ops_issue_log.py --json
python3 scripts/check_public_links.py --scope core --timeout 6 --workers 8 --json
python3 scripts/check_site_hygiene.py --site-root ../happysnaker.github.io --timeout 8 --json
python3 scripts/check_external_followups.py --summary
python3 scripts/check_external_followups.py --action-class optional-update --summary
python3 scripts/check_external_followups.py --action-class optional-update --json
```

Use `python3 scripts/run_profile_preflight.py --external-only --action-class optional-update --external-summary --enforce-review-due` only for the scheduled external review view; before the review date it should fail closed.

## Current flagship state

- `qq-ai-bot`: CI, CodeQL, Docker publish, and arm64 smoke are green in the latest status checker. The project has Docker / metrics / session / ACP / OneBot proof, but `qq-ai-bot #26 arm64` still needs a real physical ARM / CasaOS / NAS / SBC report.
- `RDLeader`: CI and CodeQL are green in the latest status checker. The project has public demo / QA / runtime / security proof, but license posture is still unresolved in `RDLeader#3`; do not imply reuse rights.
- `happysnaker.github.io`: Pages deploy is green and the support page exposes proof-before-payment, current asks, share kit, and the deploy-read sample.
- The sponsor one-pager release is intentionally compact and now includes the `Deploy read` path; append-only operational detail belongs in [happysnaker#2](https://github.com/happysnaker/happysnaker/issues/2).

## Proof and support links

- Proof before payment: <https://happysnaker.github.io/support/#proof-before-payment>
- 10-second support router: <https://happysnaker.github.io/support/#sponsor-router>
- Default support fallback: <https://github.com/happysnaker/.github/commit/0ec8ed7> / funding fallback: <https://github.com/happysnaker/.github/commit/47eaa73>
- Current concrete asks: <https://happysnaker.github.io/support/#current-asks>
- Share kit: [share-kit.md](share-kit.md)
- Sponsor prospect pipeline: [sponsor-prospect-pipeline.md](sponsor-prospect-pipeline.md)
- Sponsor conversion scorecard: [sponsor-conversion-scorecard.md](sponsor-conversion-scorecard.md)
- Sponsor scorecard coverage: [sponsor-scorecard-coverage.md](sponsor-scorecard-coverage.md)
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
python3 scripts/check_external_followups.py --action-class optional-update --json
python3 scripts/check_external_followups.py --action-class optional-update --candidate-comments --enforce-review-due
python3 scripts/run_profile_preflight.py --external-only --action-class optional-update --external-candidate-comments --enforce-review-due
python3 scripts/run_profile_preflight.py --external-only --action-class optional-update --external-summary --enforce-review-due
python3 scripts/run_profile_preflight.py --external-only --external-summary --enforce-review-due
```

The optional-update JSON includes `qualification`, `scorecardAction`, `materials`, `candidateComment`, and `candidateGuardrails`; `--candidate-comments` (or preflight `--external-candidate-comments`) renders the prepared bodies without posting them. Only use a prepared candidate comment when `candidateGuardrails.ok` is true, the review gate is due, and the row guidance still allows a comment. The prepared comments are for `docker/awesome-compose#781`, `AwesomeHomelab#98`, and `jbesomi/awesome-autonomous-agents#20`; they must not be posted early or reused repeatedly.

## Automation guardrails

- Use `scripts/github_cli.py` for GitHub CLI JSON/API calls so transient GitHub API/network errors retry consistently.
- `python3 scripts/run_profile_preflight.py --link-scope core --workers 8 --skip-external --json` emits machine-readable pass/fail status for the core takeover proof gate and forwards `--json` into checker substeps where available, so captured stdout is machine-readable instead of prose.
- Use stable profile workflow links for evergreen profile proof; `python3 scripts/check_stable_profile_links.py --json` rejects one-off profile self-check run links in public docs and emits machine-readable drift evidence.
- `python3 scripts/check_gh_usage.py --json` fails if a proof/status checker bypasses that helper with a direct `gh` subprocess call, or if anything except `scripts/github_cli.py` is allowlisted for direct `gh`, and emits machine-readable helper-usage evidence.
- `python3 scripts/check_ci_workflow_contract.py --json` fails if scheduled CI stops compiling/running the required proof/support drift checks and emits machine-readable workflow-contract evidence.
- `python3 scripts/check_checker_catalog.py --json` fails if a new proof checker is not documented in the technical proof index or lacks `--json` support.
- `python3 scripts/check_public_links.py --scope core --timeout 6 --workers 8 --json` verifies sponsor/support/status links and emits machine-readable link evidence before broader promotion.
- `python3 scripts/check_support_routes.py --json` verifies profile/default funding links include both the root support page and the 10-second support router fallback.
- `python3 scripts/check_site_hygiene.py --site-root ../happysnaker.github.io --timeout 8 --json` verifies local public-page metadata, sitemap, support proof-before-payment content, and repo-link hygiene as machine-readable site evidence.
- `python3 scripts/check_review_funnel.py` verifies the paid review / deploy-read path across support, review, deploy-read sample, and flagship inbound pages.
- Payment screenshot privacy guard: mailto templates should ask users to attach payment screenshots privately by email only, never in public issues.
- `python3 scripts/check_external_followups.py --action-class optional-update --json` exposes scheduled-review materials, sponsor conversion qualification gates, candidate comments, and candidate-comment guardrails without posting externally.
- `python3 scripts/check_sponsor_pipeline.py --json` verifies audience segments, support notes, reply patterns, and no-overclaim guardrails before outreach or sponsor replies use the prospect pipeline.
- `python3 scripts/check_sponsor_conversion_scorecard.py --json` verifies the landing → proof → route → action → follow-up conversion stages, segment-to-offer fit, support notes, and privacy/license/no-spam guardrails before promotion asks become too vague.
- `python3 scripts/check_sponsor_scorecard_coverage.py --json` verifies the coverage map tying support pages, live issues, repo support files, review funnel, and external follow-up back to Hot / Warm / Nurture / No-send gates.

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
- improve share-kit / sponsor-prospect-pipeline / sponsor-conversion-scorecard / support-page routes without posting externally;
- keep deploy-read / paid-review routes visible from profile, flagship support files, default `.github`, sponsor packet, technical map, and share kit.

Avoid:

- repeated external PR comments without new evidence or maintainer request;
- broad claims that all old repos are CodeQL-clean;
- physical ARM / CasaOS completion claims before `qq-ai-bot#26` has a real host report;
- RDLeader reuse-rights claims before a root license and `RDLeader#3` are resolved;
- growing the sponsor release body again instead of using issue #2 for the append-only log.
