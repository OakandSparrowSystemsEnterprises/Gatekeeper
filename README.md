# Gatekeeper

A lightweight authority contract for AI-assisted code changes. Defines context, invariants, and approval boundaries so agents don't guess.

## Contract Files

- [AI.md](AI.md) — Context and instructions for AI agents
- [INVARIANTS.md](INVARIANTS.md) — Rules that must never be violated
- [CHANGE_POLICY.md](CHANGE_POLICY.md) — GREEN/YELLOW/RED change classification

## Validation

```bash
python3 scripts/validate_contract.py   # contract files present
python3 scripts/validate_pr.py <file>  # PR body fields complete
python3 -m unittest discover -s tests  # full test suite
```

`validate_contract.py` checks that all contract files exist. `validate_pr.py` checks that a PR body declares a risk level, fills required sections, and — for RED changes — includes a named approver and approval evidence. Both run as required CI status checks on every pull request, including those from automation and AI agents.

## Deployment

- [ROLLOUT.md](ROLLOUT.md) — production rollout plan, metric definition, save log
- [TECHNICAL_BRIEF.md](TECHNICAL_BRIEF.md) — architecture, enforcement table, enterprise artifact

## License

Licensed under the Apache License, Version 2.0 — see the [LICENSE](LICENSE) file for details.
