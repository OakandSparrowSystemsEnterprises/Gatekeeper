Gatekeeper
A lightweight authority contract for AI-assisted code changes.
Defines context, invariants, and approval boundaries so agents don’t guess.
This repository provides the core contract files that AI agents must follow before editing code:
AI.md — Describes the agent’s context and how it should operate.
INVARIANTS.md — Defines rules that must never be violated.
CHANGE_POLICY.md — Classifies what an agent may do directly, propose via PR, or stop and ask for approval.
.github/pull_request_template.md — Ensures every PR declares risk level and invariants checked.
Authority Contract
Agents working in this codebase must:
Load and respect every contract file.
Stop when a request conflicts with an invariant.
Declare risk level and invariants checked in every PR.
This creates a predictable governance layer that prevents “guessing” and unintended actions by AI agents.
Validator
A minimal Python utility (scripts/validate_contract.py) exists to confirm the contract files are present and valid.
Tests in tests/test_validate_contract.py verify expected behavior.
License
Licensed under the Apache License, Version 2.0 — see the LICENSE file for details.
