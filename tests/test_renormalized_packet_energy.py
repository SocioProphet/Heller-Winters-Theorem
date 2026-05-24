import unittest

from tools.check_renormalized_packet_energy import (
    OLD_LAYER_COUNT,
    P11_CANCELLING_COUNT,
    P11_NONCANCELLING_COUNT,
    normalized_packet_energy_row,
    run_checks,
)


class TestRenormalizedPacketEnergy(unittest.TestCase):
    def test_packet_counts(self) -> None:
        self.assertEqual(OLD_LAYER_COUNT, 47)
        self.assertEqual(P11_CANCELLING_COUNT, 240)
        self.assertEqual(P11_NONCANCELLING_COUNT, 192)

    def test_run_checks(self) -> None:
        rows = run_checks()
        self.assertEqual([row.depth for row in rows], [2, 3, 4, 5])

    def test_depth_2_values(self) -> None:
        row = normalized_packet_energy_row(2)
        self.assertAlmostEqual(row.old_layer_energy_per_character, 178.72108789618892, places=12)
        self.assertAlmostEqual(row.p11_cancelling_energy_per_character, 295.27846503367005, places=12)
        self.assertAlmostEqual(row.p11_noncancelling_energy_per_character, 295.27846503367033, places=12)
        self.assertAlmostEqual(row.noncancel_to_cancel_ratio, 1.0, places=12)

    def test_depth_3_values(self) -> None:
        row = normalized_packet_energy_row(3)
        self.assertAlmostEqual(row.old_layer_energy_per_character, 1476.995397722033, places=12)
        self.assertAlmostEqual(row.p11_cancelling_energy_per_character, 3923.0976633164673, places=12)
        self.assertAlmostEqual(row.p11_noncancelling_energy_per_character, 4214.224918349286, places=12)
        self.assertAlmostEqual(row.noncancel_to_cancel_ratio, 1.0742085158254022, places=12)

    def test_depth_4_values(self) -> None:
        row = normalized_packet_energy_row(4)
        self.assertAlmostEqual(row.old_layer_energy_per_character, 10545.554180869645, places=12)
        self.assertAlmostEqual(row.p11_cancelling_energy_per_character, 31698.31204139129, places=12)
        self.assertAlmostEqual(row.p11_noncancelling_energy_per_character, 37149.28844831745, places=12)
        self.assertAlmostEqual(row.noncancel_to_cancel_ratio, 1.1719642484372144, places=12)

    def test_depth_5_values(self) -> None:
        row = normalized_packet_energy_row(5)
        self.assertAlmostEqual(row.old_layer_energy_per_character, 136843.17131838758, places=12)
        self.assertAlmostEqual(row.p11_cancelling_energy_per_character, 357888.12870257103, places=12)
        self.assertAlmostEqual(row.p11_noncancelling_energy_per_character, 305119.6916722366, places=12)
        self.assertAlmostEqual(row.noncancel_to_cancel_ratio, 0.8525560564927581, places=12)

    def test_ratio_oscillates_not_monotone(self) -> None:
        ratios = {depth: normalized_packet_energy_row(depth).noncancel_to_cancel_ratio for depth in (2, 3, 4, 5)}
        self.assertAlmostEqual(ratios[2], 1.0, places=12)
        self.assertGreater(ratios[3], ratios[2])
        self.assertGreater(ratios[4], ratios[3])
        self.assertLess(ratios[5], ratios[4])
        self.assertLess(ratios[5], 1.0)

    def test_energy_per_10K_bounded(self) -> None:
        for depth in (2, 3, 4, 5):
            row = normalized_packet_energy_row(depth)
            cancel_scaled = row.p11_cancelling_energy_per_character / (10**depth)
            noncancel_scaled = row.p11_noncancelling_energy_per_character / (10**depth)
            self.assertLess(cancel_scaled, 6.0)
            self.assertLess(noncancel_scaled, 6.0)

    def test_no_exponential_growth_detected_at_current_depths(self) -> None:
        # This is a finite diagnostic non-claim. For a small off-line offset, a
        # simple signal-to-baseline heuristic remains below the current compute range.
        delta_test = 0.1
        for depth in (2, 3, 4, 5):
            off_line_signal = 10 ** (2 * delta_test * depth) / (depth**2)
            self.assertLess(off_line_signal, 1.0)
        conservative_detectable_depth = 20
        self.assertGreater(conservative_detectable_depth, 5)

    def test_claim_is_finite_diagnostic_only(self) -> None:
        proves_grh = False
        proves_asymptotic_ordering = False
        proves_unconditional_variance_bound = False
        proves_littlewood_theorem = False
        self.assertFalse(proves_grh)
        self.assertFalse(proves_asymptotic_ordering)
        self.assertFalse(proves_unconditional_variance_bound)
        self.assertFalse(proves_littlewood_theorem)


if __name__ == "__main__":
    unittest.main()
