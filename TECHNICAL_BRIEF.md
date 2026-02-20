# Gatekeeper — Technical Brief

**Authority contract and enforcement layer for AI-assisted development and high-risk code paths.**

---

## Architecture

```
Developer / AI Agent
        |
        | opens Pull Request
        v
 GitHub Branch Protection
        |
        | required status check
        v
 .github/workflows/gatekeeper.yml
        |
        |---- scripts/validate_contract.py   (contract files present?)
        |
        |---- scripts/validate_pr.py         (PR body fields complete?)
                |
                |-- Risk level declared?     (GREEN / YELLOW / RED)
                |-- Required sections filled? (What changed, Why, Invariants, Tests)
                |-- If RED: escalation present? (Approver + Approval evidence)
                |
                v
           PASS => merge allowed
           FAIL => merge blocked
```

---

## Where it sits in the workflow

Gatekeeper is a required GitHub Actions status check on protected branches. No pull request — whether from a human, a bot, or an AI agent — can merge without passing both validators.

---

## What it enforces

| Check | Validator | Blocks merge? |
|---|---|---|
| `AI.md` present | `validate_contract.py` | Yes |
| `INVARIANTS.md` present | `validate_contract.py` | Yes |
| `CHANGE_POLICY.md` present | `validate_contract.py` | Yes |
| PR body has required sections | `validate_pr.py` | Yes |
| Risk level explicitly set | `validate_pr.py` | Yes |
| RED change has escalation section | `validate_pr.py` | Yes |
| RED escalation names an Approver | `validate_pr.py` | Yes |
| RED escalation includes Approval evidence | `validate_pr.py` | Yes |

---

## What it logs

All pass/fail output is written to the GitHub Actions run log, linked from the PR status check. No external logging, no telemetry, no network calls beyond GitHub's own infrastructure.

---

## What it blocks

- PRs with missing or incomplete contract fields
- PRs where risk level is left as the default placeholder
- RED-class changes without a named human approver and documented approval evidence
- Any merge to a protected branch that has not passed both validators

---

## Constraints

- No external dependencies (stdlib only)
- No network calls from validators
- No repo mutation
- No secrets or credential handling
- No environment variable reads

---

## Primary metric

```
incomplete_contract_block_rate = blocked PRs / total PRs
```

---

## Deployment requirement

In GitHub branch protection: enable **Require status checks to pass before merging** and add `gatekeeper` as a required check. Require pull requests before merge. This makes enforcement unavoidable.
