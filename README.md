# Gatekeeper

A lightweight authority contract for AI-assisted code changes. Defines context, invariants, and approval boundaries so agents don't guess.

## Contract Files

- [AI.md](AI.md) — Context and instructions for AI agents
- [INVARIANTS.md](INVARIANTS.md) — Rules that must never be violated
- [CHANGE_POLICY.md](CHANGE_POLICY.md) — GREEN/YELLOW/RED change classification

## Validation

```bash
python3 scripts/validate_contract.py
```

Verifies all contract files are present. Exits 0 on success, 1 if any are missing.
