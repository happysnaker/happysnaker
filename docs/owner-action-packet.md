# Owner Action Packet

> Two remaining actions require the `happysnaker` owner account. Everything else should keep moving through proof/support automation and issue #2.

## Current owner-only blockers

Run this first:

```bash
python3 scripts/check_manual_blockers.py --json
```

Expected current state:

- `ownerActionRequired`: `true`
- `agentBlockedOnOwnerAction`: `true`
- blocker `profile-pin-rdleader`: open
- blocker `rdleader-license-posture`: open

## 1. Profile pin swap

Goal: make the profile first screen more technical by replacing `Resume` with `RDLeader`.

Owner steps:

1. Log in to GitHub as `happysnaker` in a real browser session.
2. Open <https://github.com/happysnaker>.
3. Use `Customize your pins`.
4. Remove `happysnaker/Resume`.
5. Add `happysnaker/RDLeader`.
6. Save pins.
7. Run:

```bash
python3 scripts/check_profile_pins.py --strict
python3 scripts/check_manual_blockers.py --json
```

Expected recommended pins:

1. `happysnaker/qq-ai-bot`
2. `happysnaker/RDLeader`
3. `happysnaker/happydb`
4. `happysnaker/go-service-starter`
5. `happysnaker/go-http-middleware-kit`
6. `happysnaker/CSAPPLabsAndNotes`

## 2. RDLeader license posture

Goal: choose whether RDLeader is reusable open source or source-available for now. Do not imply reuse rights until this is decided.

Read first:

- Issue: <https://github.com/happysnaker/RDLeader/issues/3>
- Decision packet: <https://github.com/happysnaker/RDLeader/blob/main/docs/public/license-decision-packet.md>
- Decision note: <https://github.com/happysnaker/RDLeader/blob/main/docs/public/license-decision.md>

Owner chooses exactly one path:

### Path A: Apache-2.0

Choose this if RDLeader should become a normal permissive open-source project.

After owner approval, the agent can:

1. Add a root `LICENSE` file with Apache-2.0.
2. Update README license / reuse wording.
3. Verify GitHub `licenseInfo` is populated.
4. Close `RDLeader#3` with evidence.

### Path B: source-available for now

Choose this if the DevPlan-derived bundle should stay conservative until more sanitization is complete.

After owner approval, the agent can:

1. Keep no root `LICENSE`.
2. Strengthen no-reuse wording.
3. Record a re-evaluation trigger after `RDLeader#1`.
4. Keep external promotion focused on proof / demo / review visibility, not reuse.

## Do not do these without owner action

- Do not add a root `LICENSE` to RDLeader without a Path A decision.
- Do not claim RDLeader reuse rights while `licenseInfo=null`, root `LICENSE` is absent, and `RDLeader#3` is open.
- Do not claim profile pins are fixed until `python3 scripts/check_profile_pins.py --strict` passes.

## Evidence to record after owner action

After either owner-only action completes, record proof in:

- manual issue: <https://github.com/happysnaker/happysnaker/issues/1>
- operations log: <https://github.com/happysnaker/happysnaker/issues/2>
