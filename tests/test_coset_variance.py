from pathlib import Path
import unittest

from tools.check_coset_variance import (
    Q,
    between_coset_variance,
    coset_masses,
    coset_variance_row,
    cosets,
    residue_masses,
    run_checks,
    subgroup_h,
    theta_active,
    unit_residues,
    within_coset_variance,
)


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "prime-operator-lane" / "HW-OPEN-014-coset-variance-theorem-target.md"


class TestCosetVariance(unittest.TestCase):
    def test_document_exists_and_is_open_target(self) -> None:
        self.assertTrue(DOC.exists())
        text = DOC.read_text(encoding="utf-8")
        self.assertIn("HW-OPEN-014", text)
        self.assertIn("Coset Variance Theorem", text)
        self.assertIn("does not prove the Coset Variance Theorem", text)

    def test_q37_coset_partition_is_exact(self) -> None:
        self.assertEqual(Q, 37)
        self.assertEqual(len(subgroup_h(Q)), 3)
        self.assertEqual(len(cosets(Q)), 12)
        self.assertEqual(sum(len(c) for c in cosets(Q)), 36)
        flattened = sorted(r for c in cosets(Q) for r in c)
        self.assertEqual(flattened, list(unit_residues(Q)))

    def test_coset_masses_partition_theta(self) -> None:
        for depth in (2, 3):
            self.assertAlmostEqual(sum(coset_masses(Q, depth)), theta_active(Q, depth), places=10)

    def test_between_within_variances_are_positive_diagnostics(self) -> None:
        rows = run_checks()
        self.assertEqual([row.depth for row in rows], [2, 3, 4, 5])
        for row in rows:
            self.assertGreaterEqual(row.between_variance, 0.0)
            self.assertGreaterEqual(row.within_variance, 0.0)
            self.assertGreater(row.ratio, 0.0)

    def test_direct_variance_functions_match_row(self) -> None:
        for depth in (2, 3):
            row = coset_variance_row(depth, Q)
            self.assertAlmostEqual(row.between_variance, between_coset_variance(Q, depth), places=10)
            self.assertAlmostEqual(row.within_variance, within_coset_variance(Q, depth), places=10)

    def test_residue_masses_cover_unit_residues(self) -> None:
        masses = residue_masses(Q, 2)
        self.assertEqual(sorted(masses.keys()), list(unit_residues(Q)))

    def test_theorem_remains_open(self) -> None:
        unconditional_coset_variance_theorem_proved = False
        closes_square_root_barrier = False
        self.assertFalse(unconditional_coset_variance_theorem_proved)
        self.assertFalse(closes_square_root_barrier)


if __name__ == "__main__":
    unittest.main()
