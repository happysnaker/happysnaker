# GitHub Operations Cadence

> Purpose: make the ongoing GitHub takeover auditable. This account should keep moving through small, evidence-backed operations instead of relying on a vague “keep improving” promise.

Tracking issue: <https://github.com/happysnaker/happysnaker/issues/2>.

First-read handoff for future operators: [operator-handoff.md](operator-handoff.md).

## Weekly checklist

Run this once per week, or whenever a major public-surface change lands.

### 1. Flagship health

Fast path:

```bash
python3 scripts/run_profile_preflight.py --link-scope core --workers 8
python3 scripts/run_profile_preflight.py --link-scope core --workers 8 --json
# Machine-readable quick state for automation / handoff.
python3 scripts/check_github_status.py --summary
python3 scripts/check_manual_blockers.py --json
python3 scripts/check_stable_profile_links.py --json
python3 scripts/check_gh_usage.py --json
python3 scripts/check_ci_workflow_contract.py --json
python3 scripts/check_checker_catalog.py --json
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
# Optional: focus external follow-up output on surfaces where a short scheduled update may be allowed.
python3 scripts/run_profile_preflight.py --external-only --action-class optional-update --external-summary --enforce-review-due
python3 scripts/check_github_status.py --markdown --as-of 'YYYY-MM-DD Asia/Shanghai' > docs/flagship-status-snapshot.md
```

The preflight wraps the docs verifier, stable profile-link checker, GitHub CLI helper-usage checker, share-kit guardrail checker, README badge checker, GitHub status checker, support-route checker, repository metadata checker, sponsor-release checker, sponsor-issue checker, paid-review funnel checker, operations-log checker, issue-label checker, manual-blocker report, public-link checker, and external-follow-up summary. It checks latest configured workflows for `happysnaker`, `qq-ai-bot`, `RDLeader`, and `happysnaker.github.io`, plus open CodeQL / Dependabot / secret-scanning alerts for the configured flagship repos. `check_gh_usage.py --json` prevents new proof/status scripts from bypassing the shared retry helper `scripts/github_cli.py`, requires that the helper remains the only allowed direct-`gh` script, and reports helper-usage drift; `check_stable_profile_links.py` rejects one-off profile Actions run links in public docs while allowing stable workflow links and snapshot references; `check_support_routes.py` verifies that profile, default community-health, flagship, high-traffic template, and pinned systems-study, and paid-review funnel and backend-readiness and architecture-review and launch-readiness and database-internals and Go-starter funding / support / issue-contact files still route to proof-before-payment, the 10-second support router, current asks, sponsor / paid-support intake replies, public-privacy guardrails, and concrete payment notes; `check_repo_metadata.py` verifies the core repository homepages, topics, descriptions, visibility, and archive state; `check_sponsor_release.py` verifies the source sponsor one-pager and frozen release both expose proof-before-payment, share kit, concrete support routes, operations-log link, reproducible proof commands, and that the release stays compact enough for GitHub release-note limits; `check_sponsor_issues.py` verifies the live sponsorship issues keep stable proof links, support routes, payment notes, and redaction/license guardrails; `check_review_funnel.py` verifies the support/review/qq-ai-bot paid-review path keeps prices, deploy-read sample links, mailto templates, and payment-screenshot fields intact; `check_ops_issue_log.py` verifies issue #2 stays open as the append-only operations log with evidence / verification markers; `check_issue_labels.py` verifies sponsor/manual/open-loop issue labels remain useful for public triage; `check_profile_pins.py` reports whether the manual `Resume` → `RDLeader` pin swap is still pending; `check_rdleader_license.py` reports whether RDLeader license/reuse posture is still unresolved; `check_manual_blockers.py` summarizes both manual blockers and verifies issue #1 stays open/labeled/aligned with the latest manual guidance; `--external-summary` keeps scheduled external follow-up output compact and `--enforce-review-due` prevents premature scheduled-review comments; profile CI also checks the local public Pages checkout with `check_site_hygiene.py` so support-page proof-before-payment content, project-page metadata drift, and one-off Actions run links on live landing pages are caught weekly. The Markdown mode refreshes the sponsor/curator-facing [flagship status snapshot](flagship-status-snapshot.md). Do not create a refresh-only loop solely to chase the profile repo's own newest CI run: editing the snapshot triggers another self-check. Refresh the snapshot when a flagship status, support route, or alert posture materially changes.

Manual checklist:

Check:

- `qq-ai-bot` CI
- `qq-ai-bot` Docker publish
- `qq-ai-bot` Dependabot grouped update jobs
- `RDLeader` CI
- `RDLeader` Dependabot grouped update jobs
- `happysnaker` profile docs CI
- `happysnaker.github.io` Pages deploy
- open CodeQL / Dependabot / secret-scanning alert counts for configured flagship repos

Evidence to record:

- latest commit SHA
- successful workflow links
- any failure triage or rerun notes

### 2. Sponsorware board

Check:

- `qq-ai-bot` sponsor issues: `#26` open; `#23` / `#24` shipped and should stay in the shipped section
- `RDLeader` sponsor / public packaging issues: `#1`, `#3`, `#27`; `#2` and later public packaging slices are shipped evidence
- profile sponsorware board, sponsor one-pager release, and support-surface coverage links

Evidence to record:

- open / closed state
- stale asks
- newly completed or funded work
- next concrete sponsor package

### 3. External follow-up queue

Before posting any external PR / discussion / community follow-up, check the queue:

- [external-follow-up-queue.md](external-follow-up-queue.md)

The queue records the next scheduled review date, current PR state, allowed follow-up material, and the conditions for staying quiet.

### 4. Technical proof index

Update `docs/technical-proof-index.md` when any of these change:

- new release / pre-release
- new successful CI / Docker proof worth preserving
- new public docs or demos
- upstream PRs that materially change the proof story
- dependency maintenance posture

### 5. Portfolio hygiene

Check:

- pinned repos still match the intended first-screen story; run `python3 scripts/check_profile_pins.py` to confirm whether replacing `Resume` with `RDLeader` is still pending
- active forks still have “not portfolio centerpiece” descriptions
- parked repos still should remain parked
- newly created repos have license / support / security posture appropriate to their role

### 6. Public docs integrity

Run:

```bash
python3 scripts/verify_public_docs.py
```

For sponsor/proof link hygiene, run the narrower external link check manually when support surfaces change:

```bash
python3 scripts/check_public_links.py --timeout 6 --workers 8 --json
# Use --scope profile for README + technical proof index + upstream ledger + core proof docs, or --scope all for a slower full-doc sweep.
```

For public site / project-page hygiene after changing `happysnaker.github.io`, run the site hygiene verifier from this profile repo:

```bash
python3 scripts/check_site_hygiene.py --site-root ../happysnaker.github.io --live --timeout 8 --json
```

What it checks:

- local and live canonical / OpenGraph / Twitter Card / JSON-LD metadata on support, review, flagship, and project landing pages;
- `robots.txt` sitemap pointer and sitemap entries / optional `lastmod`;
- public-site links to `happysnaker/*` repositories resolve to public repositories;
- local and live project/support landing pages use stable workflow/status links instead of one-off Actions run URLs;
- legacy unavailable repository URLs such as old private project CTAs stay out of public pages.

Profile CI runs the local site hygiene checks against a checked-out `happysnaker.github.io` tree. Keep the external `--live` check manual unless flakiness is acceptable; it depends on GitHub Pages and network responses.

Then verify profile CI passes after any docs change.

## Monthly checklist

### 1. Pin strategy

Review the manual pinned-repo checklist:

- <https://github.com/happysnaker/happysnaker/blob/master/docs/manual-github-actions.md>

If possible, manually replace `Resume` with `RDLeader` in pinned repos.

Metadata already prepared: RDLeader homepage points to <https://happysnaker.github.io/rdleader/> and profile/RDLeader topics include the current agent-ops/sponsorware positioning.

### 2. RDLeader license posture

Review:

- <https://github.com/happysnaker/RDLeader/issues/3>

Decide whether RDLeader should be MIT, Apache-2.0, copyleft, or source-available while the public release is still being sanitized.

### 3. Support surface coverage

Review:

- <https://github.com/happysnaker/happysnaker/blob/master/docs/support-surface-coverage.md>
- <https://github.com/happysnaker/happysnaker/releases/tag/v2026.07-sponsor-one-pager>

Keep the coverage table aligned when a pinned repo, support route, funding file, support-router fallback, or sponsor one-pager link changes. RDLeader demo assets from `#2` are already shipped evidence, not the next action.

When updating coverage, use this sequence:

1. Add or update the repository / page row in `docs/support-surface-coverage.md` with the exact evidence commit.
2. Run `python3 scripts/verify_public_docs.py`.
3. Run `python3 scripts/check_support_routes.py --json` to confirm funding/support/issue-contact files still include the 10-second support router, sponsor / paid-support intake replies, public-privacy guardrails, and default fallback; then run `python3 scripts/check_public_links.py --timeout 6 --workers 8 --json` for the core support/proof links; use `--scope profile --workers 12 --json` before claiming broader profile-link coverage.
4. If the change affects a public support or review page, verify the live page after Pages deployment.
5. Keep the frozen sponsor one-pager release compact. It should summarize the current proof packet and link to the append-only operations log in issue #2; do not keep appending every heartbeat to the release body because GitHub enforces a release-note size limit.
6. Record the result in `happysnaker#2`.

### 4. Fork/archive cleanup

Archive temporary forks only after verifying the related upstream PR or branch no longer needs maintenance.

Never archive active contribution forks just to make the profile look cleaner.

## Evidence standards

Use these words precisely:

- **inspected** — read the current state but did not change it
- **changed locally** — edited local files only
- **pushed** — remote branch/repo changed
- **verified** — current command/API output proves the claim
- **blocked** — no meaningful next action without user/external state

Do not claim “done” for broad goals unless current evidence proves all requirements.

## Current operating surfaces

- Technical proof index: <https://github.com/happysnaker/happysnaker/blob/master/docs/technical-proof-index.md>
- Upstream contribution ledger: <https://github.com/happysnaker/happysnaker/blob/master/docs/upstream-contribution-ledger.md>
- External follow-up queue: [external-follow-up-queue.md](external-follow-up-queue.md)
- Sponsorware board: <https://github.com/happysnaker/happysnaker/blob/master/docs/sponsorware-board.md>
- Sponsor one-pager release: <https://github.com/happysnaker/happysnaker/releases/tag/v2026.07-sponsor-one-pager>
- Support surface coverage: <https://github.com/happysnaker/happysnaker/blob/master/docs/support-surface-coverage.md>
- 10-second support router: <https://happysnaker.github.io/support/#sponsor-router>
- Default funding fallback: <https://github.com/happysnaker/.github/commit/47eaa73>
- Portfolio audit: <https://github.com/happysnaker/happysnaker/blob/master/docs/portfolio-audit.md>
- Manual GitHub checklist: <https://github.com/happysnaker/happysnaker/blob/master/docs/manual-github-actions.md>
- Manual tracking issue: <https://github.com/happysnaker/happysnaker/issues/1>
