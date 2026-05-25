from pathlib import Path
import unittest

from tools.check_cayley_spectral_gap import (
    cayley_spectral_gap_row,
    quotient_size,
    run_checks,
    support_generates_quotient,
    quotient_prime_weights,
)


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "prime-operator-lane" / "HW-PRIME-WEIL-020-cayley-spectral-gap.md"


class TestCayleySpectralGap(unittest.TestCase):
    def test_document_exists_and_is_finite_diagnostic(self) -> None:
        self.assertTrue(DOC.exists())
        text = DOC.read_text(encoding="utf-8")
        self.assertIn("HW-PRIME-WEIL-020", text)
        self.assertIn("Cayley Quotient Spectral Gap Diagnostic", text)
        self.assertIn("finite spectral-gap diagnostic", text)

    def test_run_checks(self) -> None:
        rows = run_checks()
        self.assertEqual([row.depth for row in rows], [2, 3, 4, 5])

    def test_q37_quotient_size_and_support_generation(self) -> None:
        self.assertEqual(quotient_size(37), 12)
        for depth in (2, 3, 4, 5):
            weights = quotient_prime_weights(37, depth)
            self.assertEqual(len(weights), 12)
            self.assertTrue(support_generates_quotient(weights))
            self.assertAlmostEqual(sum(weights), 1.0, places=12)

    def test_q37_exact_spectral_gap_values(self) -> None:
        expected = {
            2: (11, 0.1738538617608776, 0.8261461382391224, 0.602247443323792),
            3: (12, 0.079165278069826, 0.920834721930174, 0.2742365676245137),
            4: (12, 0.015439950573328871, 0.9845600494266711, 0.05348555771871564),
            5: (12, 0.004696017888982491, 0.9953039821110176, 0.016267483153940037),
        }
        for depth, (support_size, lambda_star, gap, l2_bound) in expected.items():
            row = cayley_spectral_gap_row(37, depth)
            self.assertEqual(row.support_size, support_size)
            self.assertAlmostEqual(row.lambda_star, lambda_star, places=12)
            self.assertAlmostEqual(row.spectral_gap, gap, places=12)
            self.assertAlmostEqual(row.one_step_l2_bound, l2_bound, places=12)

    def test_gap_improves_in_measured_windows(self) -> None:
        rows = [cayley_spectral_gap_row(37, depth) for depth in (2, 3, 4, 5)]
        self.assertLess(rows[1].lambda_star, rows[0].lambda_star)
        self.assertLess(rows[2].lambda_star, rows[1].lambda_star)
        self.assertLess(rows[3].lambda_star, rows[2].lambda_star)

    def test_non_claims_are_present(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "does not prove RH",
            "does not prove GRH",
            "does not prove the Coset Variance Theorem",
            "does not prove a uniform spectral gap as `K -> infinity`",
            "does not close the square-root barrier",
        ]:
            self.assertIn(token, text)


if __name__ == "__main__":
    unittest.main()
