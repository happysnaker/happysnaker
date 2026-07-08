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

- `qq-ai-bot` sponsor issues: `#23`, `#24`, `#26`
- `RDLeader` sponsor / public packaging issues: `#1`, `#2`, `#3`
- profile sponsorware board links

Evidence to record:

- open / closed state
- stale asks
- newly completed or funded work
- next concrete sponsor package

### 3. Technical proof index

Update `docs/technical-proof-index.md` when any of these change:

- new release / pre-release
- new successful CI / Docker proof worth preserving
- new public docs or demos
- upstream PRs that materially change the proof story
- dependency maintenance posture

### 4. Portfolio hygiene

Check:

- pinned repos still match the intended first-screen story
- active forks still have “not portfolio centerpiece” descriptions
- parked repos still should remain parked
- newly created repos have license / support / security posture appropriate to their role

### 5. Public docs integrity

Run:

```bash
python3 scripts/verify_public_docs.py
```

Then verify profile CI passes after any docs change.

## Monthly checklist

### 1. Pin strategy

Review the manual pinned-repo checklist:

- <https://github.com/happysnaker/happysnaker/blob/master/docs/manual-github-actions.md>

If possible, manually replace `Resume` with `RDLeader` in pinned repos.

### 2. RDLeader license posture

Review:

- <https://github.com/happysnaker/RDLeader/issues/3>

Decide whether RDLeader should be MIT, Apache-2.0, copyleft, or source-available while the public release is still being sanitized.

### 3. Demo assets

Review:

- <https://github.com/happysnaker/RDLeader/issues/2>

The next useful public artifact is still fake-data screenshots or a short video walkthrough.

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
- Sponsorware board: <https://github.com/happysnaker/happysnaker/blob/master/docs/sponsorware-board.md>
- Portfolio audit: <https://github.com/happysnaker/happysnaker/blob/master/docs/portfolio-audit.md>
- Manual GitHub checklist: <https://github.com/happysnaker/happysnaker/blob/master/docs/manual-github-actions.md>
- Manual tracking issue: <https://github.com/happysnaker/happysnaker/issues/1>
