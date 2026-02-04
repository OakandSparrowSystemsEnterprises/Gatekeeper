#!/usr/bin/env python3
"""Tests for validate_contract.py"""

import tempfile
import unittest
from pathlib import Path

from scripts.validate_contract import REQUIRED_FILES, validate_contract


class TestValidateContract(unittest.TestCase):
    def test_all_files_present(self):
        """Returns empty list when all contract files exist."""
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            for filename in REQUIRED_FILES:
                (repo_root / filename).write_text("")

            missing = validate_contract(repo_root)
            self.assertEqual(missing, [])

    def test_all_files_missing(self):
        """Returns all files when none exist."""
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            missing = validate_contract(repo_root)
            self.assertEqual(missing, REQUIRED_FILES)

    def test_partial_files_missing(self):
        """Returns only missing files."""
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            (repo_root / "AI.md").write_text("")

            missing = validate_contract(repo_root)
            self.assertNotIn("AI.md", missing)
            self.assertIn("INVARIANTS.md", missing)
            self.assertIn("CHANGE_POLICY.md", missing)


if __name__ == "__main__":
    unittest.main()
