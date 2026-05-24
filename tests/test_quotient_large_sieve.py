from pathlib import Path
import unittest

from tools.check_quotient_large_sieve import (
    quotient_large_sieve_row,
    run_checks,
)


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "prime-operator-lane" / "HW-PRIME-WEIL-017-quotient-large-sieve.md"


class TestQuotientLargeSieve(unittest.TestCase):
    def test_document_exists_and_is_diagnostic(self) -> None:
        self.assertTrue(DOC.exists())
        text = DOC.read_text(encoding="utf-8")
        self.assertIn("HW-PRIME-WEIL-017", text)
        self.assertIn("Quotient Large-Sieve Diagnostic", text)
        self.assertIn("method-grade diagnostic", text)

    def test_run_checks(self) -> None:
        rows = run_checks()
        self.assertTrue(rows)

    def test_orbit_constants(self) -> None:
        row11 = quotient_large_sieve_row(11, 5)
        row13 = quotient_large_sieve_row(13, 5)
        row37 = quotient_large_sieve_row(37, 5)
        self.assertEqual((row11.orbit_size, row11.quotient_index, row11.noncancelling_count), (2, 5, 4))
        self.assertEqual((row13.orbit_size, row13.quotient_index, row13.noncancelling_count), (6, 2, 1))
        self.assertEqual((row37.orbit_size, row37.quotient_index, row37.noncancelling_count), (3, 12, 11))

    def test_quotient_improves_standard_comparison(self) -> None:
        for q in (11, 13, 37):
            row = quotient_large_sieve_row(q, 5)
            self.assertGreater(row.improvement_factor, 1.0)
            self.assertLess(row.quotient_candidate_bound, row.standard_bound)

    def test_quotient_bound_still_above_grh_packet_scale(self) -> None:
        for q in (11, 13, 37):
            row = quotient_large_sieve_row(q, 5)
            self.assertGreater(row.quotient_to_grh_ratio, 1.0)

    def test_gap_grows_with_depth_for_fixed_q37(self) -> None:
        row5 = quotient_large_sieve_row(37, 5)
        row10 = quotient_large_sieve_row(37, 10)
        self.assertGreater(row10.asymptotic_gap_factor, row5.asymptotic_gap_factor)

    def test_non_claims_are_present(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in [
            "does not prove RH",
            "does not prove GRH",
            "does not prove the Coset Variance Theorem",
            "does not prove an unconditional variance bound",
            "does not claim that quotient large sieve crosses the square-root barrier",
        ]:
            self.assertIn(token, text)


if __name__ == "__main__":
    unittest.main()
