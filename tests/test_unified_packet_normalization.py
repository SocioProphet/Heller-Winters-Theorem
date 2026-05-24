import unittest

from tools.check_unified_packet_normalization import (
    PACKET_COUNTS,
    energy_per_character,
    run_checks,
    unified_packet_row,
)


class TestUnifiedPacketNormalization(unittest.TestCase):
    def test_packet_counts_partition_nontrivial_family(self) -> None:
        self.assertEqual(PACKET_COUNTS["inert_p235"], 7)
        self.assertEqual(PACKET_COUNTS["p7_full"], 40)
        self.assertEqual(PACKET_COUNTS["p11_cancel"], 240)
        self.assertEqual(PACKET_COUNTS["p11_noncancel"], 192)
        self.assertEqual(sum(PACKET_COUNTS.values()), 479)

    def test_run_checks(self) -> None:
        rows = run_checks()
        self.assertEqual([row.depth for row in rows], [2, 3, 4])

    def test_depth_2_values(self) -> None:
        per = energy_per_character(2)
        self.assertAlmostEqual(per["inert_p235"], 43.97548578691933, places=12)
        self.assertAlmostEqual(per["p7_full"], 202.30156826531112, places=12)
        self.assertAlmostEqual(per["p11_cancel"], 295.27846503367005, places=12)
        self.assertAlmostEqual(per["p11_noncancel"], 295.27846503367033, places=12)

    def test_depth_3_values(self) -> None:
        per = energy_per_character(3)
        self.assertAlmostEqual(per["inert_p235"], 912.6281970745762, places=12)
        self.assertAlmostEqual(per["p7_full"], 1575.7596578353377, places=12)
        self.assertAlmostEqual(per["p11_cancel"], 3923.0976633164673, places=12)
        self.assertAlmostEqual(per["p11_noncancel"], 4214.224918349286, places=12)

    def test_depth_4_values(self) -> None:
        per = energy_per_character(4)
        self.assertAlmostEqual(per["inert_p235"], 881.487346082066, places=12)
        self.assertAlmostEqual(per["p7_full"], 12236.765876957472, places=12)
        self.assertAlmostEqual(per["p11_cancel"], 31698.31204139129, places=12)
        self.assertAlmostEqual(per["p11_noncancel"], 37149.28844831745, places=12)

    def test_observed_ordering(self) -> None:
        for depth in (2, 3, 4):
            row = unified_packet_row(depth)
            self.assertLess(row.inert_p235_per_character, row.p7_full_per_character)
            self.assertLess(row.p7_full_per_character, row.p11_cancel_per_character)
            self.assertLessEqual(row.p11_cancel_per_character, row.p11_noncancel_per_character + 1e-9)
        self.assertAlmostEqual(unified_packet_row(2).p11_noncancel_over_p11_cancel, 1.0, places=12)
        self.assertGreater(unified_packet_row(3).p11_noncancel_over_p11_cancel, 1.0)
        self.assertGreater(
            unified_packet_row(4).p11_noncancel_over_p11_cancel,
            unified_packet_row(3).p11_noncancel_over_p11_cancel,
        )

    def test_claim_is_finite_diagnostic_only(self) -> None:
        proves_grh = False
        proves_asymptotic_ordering = False
        proves_unconditional_variance_bound = False
        self.assertFalse(proves_grh)
        self.assertFalse(proves_asymptotic_ordering)
        self.assertFalse(proves_unconditional_variance_bound)


if __name__ == "__main__":
    unittest.main()
