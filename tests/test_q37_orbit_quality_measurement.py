import unittest

from tools.check_q37_orbit_quality_measurement import (
    cancelling_exponents,
    noncancelling_exponents,
    predicted_ratio,
    q37_row,
    run_checks,
)


class TestQ37OrbitQualityMeasurement(unittest.TestCase):
    def test_run_checks(self) -> None:
        rows = run_checks()
        self.assertEqual([row.depth for row in rows], [2, 3, 4, 5])

    def test_packet_counts(self) -> None:
        self.assertEqual(len(noncancelling_exponents()), 11)
        self.assertEqual(len(cancelling_exponents()), 24)

    def test_preregistered_prediction(self) -> None:
        self.assertAlmostEqual(predicted_ratio(), 1.1146333333333333, places=12)

    def test_measured_values(self) -> None:
        expected = {
            2: (189.49027875773587, 114.7290336687584, 0.6054613166485441),
            3: (1024.1588360911671, 1848.8296994837428, 1.805217739994352),
            4: (20069.659764608412, 9407.435842493238, 0.4687391790807865),
            5: (150781.37488886353, 103834.7376381514, 0.6886443217186798),
        }
        for depth, (cancel, noncancel, ratio) in expected.items():
            row = q37_row(depth)
            self.assertAlmostEqual(row.cancel_per_character, cancel, places=12)
            self.assertAlmostEqual(row.noncancel_per_character, noncancel, places=12)
            self.assertAlmostEqual(row.ratio, ratio, places=12)

    def test_model_is_falsified_at_finite_depths(self) -> None:
        row = q37_row(5)
        self.assertLess(row.ratio, 1.0)
        self.assertGreater(abs(row.ratio - predicted_ratio()), 0.1)

    def test_claim_is_finite_diagnostic_only(self) -> None:
        proves_grh = False
        proves_asymptotic_law = False
        proves_orbit_quality_irrelevant = False
        self.assertFalse(proves_grh)
        self.assertFalse(proves_asymptotic_law)
        self.assertFalse(proves_orbit_quality_irrelevant)


if __name__ == "__main__":
    unittest.main()
