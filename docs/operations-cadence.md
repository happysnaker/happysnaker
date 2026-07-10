# GitHub Operations Cadence

> Purpose: make the ongoing GitHub takeover auditable. This account should keep moving through small, evidence-backed operations instead of relying on a vague “keep improving” promise.

Tracking issue: <https://github.com/happysnaker/happysnaker/issues/2>.

## Weekly checklist

Run this once per week, or whenever a major public-surface change lands.

### 1. Flagship health

Check:

- `qq-ai-bot` CI
- `qq-ai-bot` Docker publish
- `qq-ai-bot` Dependabot grouped update jobs
- `RDLeader` CI
- `RDLeader` Dependabot grouped update jobs
- `happysnaker` profile docs CI

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

- pinned repos still match the intended first-screen story
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
python3 scripts/check_public_links.py
# Use --scope profile for README + technical proof index + upstream ledger + core proof docs, or --scope all for a slower full-doc sweep.
```

For public site / project-page hygiene after changing `happysnaker.github.io`, run the site hygiene verifier from this profile repo:

```bash
python3 scripts/check_site_hygiene.py --site-root ../happysnaker.github.io --expected-lastmod 2026-07-09 --live --timeout 8
```

What it checks:

- local and live canonical / OpenGraph / Twitter Card / JSON-LD metadata on support, review, flagship, and project landing pages;
- `robots.txt` sitemap pointer and sitemap entries / optional `lastmod`;
- public-site links to `happysnaker/*` repositories resolve to public repositories;
- legacy unavailable repository URLs such as old private project CTAs stay out of public pages.

Do not put the external live checks in CI unless flakiness is acceptable; they depend on GitHub Pages, GitHub HTML, and third-party network responses.

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

Keep the coverage table aligned when a pinned repo, support route, funding file, or sponsor one-pager link changes. RDLeader demo assets from `#2` are already shipped evidence, not the next action.

When updating coverage, use this sequence:

1. Add or update the repository / page row in `docs/support-surface-coverage.md` with the exact evidence commit.
2. Run `python3 scripts/verify_public_docs.py`.
3. Run `python3 scripts/check_public_links.py --timeout 6` for the core support/proof links; use `--scope profile` before claiming broader profile-link coverage.
4. If the change affects a public support or review page, verify the live page after Pages deployment.
5. Update the frozen sponsor one-pager release note when the coverage change affects sponsor-facing evidence.
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
- Portfolio audit: <https://github.com/happysnaker/happysnaker/blob/master/docs/portfolio-audit.md>
- Manual GitHub checklist: <https://github.com/happysnaker/happysnaker/blob/master/docs/manual-github-actions.md>
- Manual tracking issue: <https://github.com/happysnaker/happysnaker/issues/1>
