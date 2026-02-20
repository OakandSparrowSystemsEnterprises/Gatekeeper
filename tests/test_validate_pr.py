#!/usr/bin/env python3
"""Tests for validate_pr.py"""

import unittest

from scripts.validate_pr import validate_pr_body


VALID_GREEN_BODY = """\
## What changed
Adds a new helper function.

## Why it changed
Reduces duplication in the auth module.

## Risk level: GREEN

## Invariants checked
- INVARIANTS.md: no auth changes, no secrets, no new deps

## Tests
- python3 -m unittest discover -s tests => OK
"""

VALID_RED_BODY = """\
## What changed
Refactors the permission check middleware.

## Why it changed
Current logic has a gap that allows unauthenticated reads.

## Risk level: RED

## Invariants checked
- INVARIANTS.md: auth, access control sections reviewed

## Tests
- python3 -m unittest discover -s tests => OK

## Escalation
- Approver: Jane Smith (security lead)
- Approval evidence: https://example.com/approval-thread-42
"""


class TestValidatePrBody(unittest.TestCase):
    def test_valid_green_pr_passes(self):
        errors = validate_pr_body(VALID_GREEN_BODY)
        self.assertEqual(errors, [])

    def test_valid_red_pr_with_escalation_passes(self):
        errors = validate_pr_body(VALID_RED_BODY)
        self.assertEqual(errors, [])

    def test_missing_section_blocked(self):
        body = VALID_GREEN_BODY.replace("## Tests\n- python3 -m unittest discover -s tests => OK\n", "")
        errors = validate_pr_body(body)
        self.assertTrue(any("Tests" in e for e in errors))

    def test_empty_section_blocked(self):
        body = VALID_GREEN_BODY.replace(
            "Adds a new helper function.", ""
        )
        errors = validate_pr_body(body)
        self.assertTrue(any("What changed" in e for e in errors))

    def test_unset_risk_level_blocked(self):
        body = VALID_GREEN_BODY.replace("## Risk level: GREEN", "## Risk level: (not set)")
        errors = validate_pr_body(body)
        self.assertTrue(any("Risk level" in e for e in errors))

    def test_red_class_change_requires_escalation_section(self):
        """RED risk level without escalation section must be blocked."""
        body = VALID_RED_BODY.replace(
            "\n## Escalation\n- Approver: Jane Smith (security lead)\n- Approval evidence: https://example.com/approval-thread-42\n",
            ""
        )
        errors = validate_pr_body(body)
        self.assertTrue(
            any("Escalation" in e for e in errors),
            f"Expected escalation error, got: {errors}"
        )

    def test_red_class_change_requires_approver(self):
        """RED escalation section without Approver must be blocked."""
        body = VALID_RED_BODY.replace(
            "- Approver: Jane Smith (security lead)\n", ""
        )
        errors = validate_pr_body(body)
        self.assertTrue(any("Approver" in e for e in errors))

    def test_red_class_change_requires_approval_evidence(self):
        """RED escalation section without Approval evidence must be blocked."""
        body = VALID_RED_BODY.replace(
            "- Approval evidence: https://example.com/approval-thread-42\n", ""
        )
        errors = validate_pr_body(body)
        self.assertTrue(any("Approval evidence" in e for e in errors))

    def test_yellow_pr_does_not_require_escalation(self):
        body = VALID_GREEN_BODY.replace("## Risk level: GREEN", "## Risk level: YELLOW")
        errors = validate_pr_body(body)
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
