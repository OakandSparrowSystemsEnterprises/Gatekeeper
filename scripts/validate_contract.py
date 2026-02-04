#!/usr/bin/env python3
"""Validate presence of authority contract files."""

import sys
from pathlib import Path


REQUIRED_FILES = [
    "AI.md",
    "INVARIANTS.md",
    "CHANGE_POLICY.md",
]


def validate_contract(repo_root: Path) -> list[str]:
    """Return list of missing contract files."""
    missing = []
    for filename in REQUIRED_FILES:
        if not (repo_root / filename).is_file():
            missing.append(filename)
    return missing


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    missing = validate_contract(repo_root)

    if missing:
        print(f"FAIL: Missing contract files: {', '.join(missing)}")
        return 1

    print("OK: All contract files present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
