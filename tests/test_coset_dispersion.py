from pathlib import Path
import unittest

from tools.check_coset_dispersion import coset_dispersion_row, run_checks


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "prime-operator-lane" / "HW-PRIME-WEIL-019-coset-dispersion-diagnostic.md"


class TestCosetDispersion(unittest.TestCase):
    def test_document_exists_and_is_diagnostic(self) -> None:
        self.assertTrue(DOC.exists())
        text = DOC.read_text(encoding="utf-8")
        self.assertIn("HW-PRIME-WEIL-019", text)
        self.assertIn("Coset Dispersion Diagnostic", text)
        self.assertIn("method-grade dispersion comparison", text)

    def test_run_checks(self) -> None:
        rows = run_checks()
        self.assertEqual([row.depth for row in rows], [2, 3, 4, 5])

    def test_q37_finite_values(self) -> None:
        expected = {
            2: (105.16828086302826, 126.32685250515715, 0.8325093103917466),
            3: (1694.7605578600942, 682.7725573941173, 2.482174392492208),
            4: (8623.482855618979, 13379.77317640568, 0.6445163712360912),
            5: (95181.84283496864, 100520.91659258083, 0.9468859423631016),
        }
        for depth, (between, within, ratio) in expected.items():
            row = coset_dispersion_row(37, depth)
            self.assertAlmostEqual(row.between_variance, between, places=10)
            self.assertAlmostEqual(row.within_variance, within, places=10)
            self.assertAlmostEqual(row.between_within_ratio, ratio, places=12)

    def test_quotient_bound_does_not_reach_grh_scale(self) -> None:
        row = coset_dispersion_row(37, 5)
        self.assertGreater(row.quotient_to_grh_ratio, 1.0)
        self.assertEqual(row.dispersion_outcome, "quotient_improves_but_gap_remains")

    def test_measured_dispersion_is_below_quotient_candidate_bound(self) -> None:
        for depth in (2, 3, 4, 5):
            row = coset_dispersion_row(37, depth)
            self.assertLess(row.between_variance, row.quotient_candidate_bound)

    def test_falsification_classes_are_recorded(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "square-root scale",
            "stronger component",
            "does not improve Gate 1",
            "quotient_improves_but_gap_remains",
        ]:
            self.assertIn(token, text)

    def test_non_claims_are_present(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "does not prove RH",
            "does not prove GRH",
            "does not prove the Coset Variance Theorem",
            "does not prove a dispersion-method square-root bound",
            "does not close the square-root barrier",
        ]:
            self.assertIn(token, text)


if __name__ == "__main__":
    unittest.main()
