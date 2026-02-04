# Change Policy

GREEN — agent may implement directly
- Documentation, comments, tests
- Small bug fixes with clear scope
- Contract validation scripts (stdlib-only, no network, no mutation, no secrets)

YELLOW — agent may propose via PR, requires review
- Refactors, performance changes
- Config, CI, or build changes
- Dependency updates

RED — agent must stop and ask for approval
- Auth or permissions logic
- Payments or billing
- Data schema or migrations
- Privacy, analytics, telemetry
- Deleting features or breaking APIs
