# Production Rollout Plan

## 1) Mandatory CI in target organization

1. Install this repository (or a mirrored policy repo) into the partner org.
2. Enable `.github/workflows/gatekeeper.yml`.
3. In branch protection for the target default branch, mark **Gatekeeper Enforcement / gatekeeper** as a **required status check**.
4. Require pull requests before merge.

**Scope:** Gatekeeper must run on every pull request targeting protected branches, including those created by automation or AI agents. This closes the loophole where non-human contributors bypass contract enforcement.

**Result:** Gatekeeper becomes unavoidable for merges.

---

## 2) Real organization deployment target

| Field | Value |
|---|---|
| Partner org | TBD by owner |
| Target repo | TBD by owner |
| Protected branch | TBD by owner |
| Owner action required | Org/repo admin permissions to apply required status checks |

---

## 3) Metric tracking

**Primary metric (public):**

```
incomplete_contract_block_rate = blocked PRs due to missing contract fields / total PRs
```

This is the headline metric. It proves behavioral change directly and is legible to non-technical stakeholders.

**Supporting metrics (internal):**

- `red_escalation_count` — number of RED-class changes that triggered escalation review
- `median_red_review_time_hours` — time from escalation trigger to human approval or rejection

Track weekly. Do not dilute the public narrative with supporting metrics.

---

## 4) First concrete save log

Use this section for institutional proof. One real instance of Gatekeeper catching or preventing a risky change.

| Field | Value |
|---|---|
| Date | |
| Repo | |
| PR | |
| Trigger | |
| Block reason | |
| Human escalation reviewer | |
| Outcome (fixed / prevented) | |
| Estimated risk exposure avoided | |
| Evidence links | |

### Pre-production validation event (repository-level simulation)

| Field | Value |
|---|---|
| Date | 2026-02-19 |
| Repo | Gatekeeper |
| Trigger | Simulated RED-class auth file change with missing escalation metadata |
| Block reason | Validator reports missing RED risk level and escalation fields |
| Outcome | Merge check fails until escalation metadata is supplied |
| Evidence | `python3 -m unittest discover -s tests` — includes `test_red_class_change_requires_escalation_section` |

**Note:** This is a pre-production validation, not a production save. It confirms technical blocking behavior prior to partner rollout. Do not count it toward the institutional proof log.

---

## 5) Narrative

> Gatekeeper is an authority contract and enforcement layer for AI-assisted development and high-risk code paths. It reduces silent risk introduction.

Do not expand this. Do not add features until Gatekeeper is solid in one production environment.

---

## 6) Technical brief

See [TECHNICAL_BRIEF.md](TECHNICAL_BRIEF.md).

---

## 7) Feature freeze

Until deployed and validated in one partner org:

- No new scoring systems
- No external integrations
- No token or billing logic
- No analytics or telemetry
- No UI

Make it undeniably solid first.
