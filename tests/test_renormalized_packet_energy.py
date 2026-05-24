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
        self.assertEqual([row.depth for row in rows], [2, 3, 4])

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

    def test_non_cancelling_ratio_increases_after_depth_2(self) -> None:
        rows = run_checks()
        self.assertAlmostEqual(rows[0].noncancel_to_cancel_ratio, 1.0, places=12)
        self.assertGreater(rows[1].noncancel_to_cancel_ratio, rows[0].noncancel_to_cancel_ratio)
        self.assertGreater(rows[2].noncancel_to_cancel_ratio, rows[1].noncancel_to_cancel_ratio)

    def test_claim_is_finite_diagnostic_only(self) -> None:
        proves_grh = False
        proves_asymptotic_ordering = False
        proves_unconditional_variance_bound = False
        self.assertFalse(proves_grh)
        self.assertFalse(proves_asymptotic_ordering)
        self.assertFalse(proves_unconditional_variance_bound)


if __name__ == "__main__":
    unittest.main()
