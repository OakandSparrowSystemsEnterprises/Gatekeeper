#!/usr/bin/env python3
"""Validate PR body contains required authority contract fields."""

import re
import sys

REQUIRED_SECTIONS = [
    "What changed",
    "Why it changed",
    "Invariants checked",
    "Tests",
]

VALID_RISK_LEVELS = {"GREEN", "YELLOW", "RED"}


def extract_section(body: str, heading: str) -> str:
    """Return the content beneath a ## heading, stripped."""
    pattern = rf"##\s+{re.escape(heading)}[^\n]*\n(.*?)(?=\n##\s|\Z)"
    match = re.search(pattern, body, re.DOTALL | re.IGNORECASE)
    if not match:
        return ""
    return match.group(1).strip()


def extract_risk_level(body: str) -> str | None:
    """Return GREEN, YELLOW, or RED if explicitly stated; None otherwise."""
    section = extract_section(body, "Risk level")
    for level in VALID_RISK_LEVELS:
        if level in section.upper():
            return level
    match = re.search(r"##\s+Risk level[:\s]*(GREEN|YELLOW|RED)", body, re.IGNORECASE)
    if match:
        return match.group(1).upper()
    return None


def validate_pr_body(body: str) -> list[str]:
    """Return list of validation error strings. Empty list means valid."""
    errors = []

    for section in REQUIRED_SECTIONS:
        content = extract_section(body, section)
        if not content:
            errors.append(f"Missing or empty section: '{section}'")

    risk_level = extract_risk_level(body)

    if risk_level is None:
        errors.append(
            "Risk level must be explicitly set to GREEN, YELLOW, or RED"
        )
    elif risk_level == "RED":
        escalation = extract_section(body, "Escalation")
        if not escalation:
            errors.append(
                "RED risk level requires an '## Escalation' section"
            )
        else:
            if "approver" not in escalation.lower():
                errors.append(
                    "RED escalation section must name an Approver"
                )
            if "approval evidence" not in escalation.lower():
                errors.append(
                    "RED escalation section must include Approval evidence"
                )

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_pr.py <pr_body_file>")
        return 2

    body = open(sys.argv[1]).read()
    errors = validate_pr_body(body)

    if errors:
        print("FAIL: PR body validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("OK: PR body is valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
