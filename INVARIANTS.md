# Invariants

These rules must always hold.

- Never weaken authentication, authorization, or access control.
- Never add secrets, tokens, keys, or credentials.
- Never log sensitive or personal data.
- No new dependencies without approval.
- No breaking API changes without explicit approval or versioning.
- No schema changes or migrations without explicit approval.
- Prefer minimal diffs. No broad refactors unless requested.
