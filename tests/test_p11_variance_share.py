import math
import unittest

from tools.check_p11_variance_share import (
    FULL_NONTRIVIAL_COUNT_BASELINE,
    LOCAL_NONCANCELLING_BASELINE,
    NEW_LAYER_COUNT_BASELINE,
    run_checks,
    variance_share_row,
)


class TestP11VarianceShare(unittest.TestCase):
    def test_baselines_are_exact_counts(self) -> None:
        self.assertAlmostEqual(LOCAL_NONCANCELLING_BASELINE, 4.0 / 9.0, places=15)
        self.assertAlmostEqual(FULL_NONTRIVIAL_COUNT_BASELINE, 192.0 / 479.0, places=15)
        self.assertAlmostEqual(NEW_LAYER_COUNT_BASELINE, 432.0 / 479.0, places=15)

    def test_run_checks(self) -> None:
        rows = run_checks()
        self.assertEqual([row.depth for row in rows], [2, 3, 4])

    def test_depth_2_values_match_computation(self) -> None:
        row = variance_share_row(2)
        self.assertAlmostEqual(row.p11_new_share_total, 0.9382180088664248, places=12)
        self.assertAlmostEqual(row.p11_noncancelling_share_new, 0.4444444444444449, places=12)
        self.assertAlmostEqual(row.p11_noncancelling_share_total, 0.4169857817184115, places=12)

    def test_depth_3_values_match_computation(self) -> None:
        row = variance_share_row(3)
        self.assertAlmostEqual(row.p11_new_share_total, 0.9618597686152422, places=12)
        self.assertAlmostEqual(row.p11_noncancelling_share_new, 0.46218250579118775, places=12)
        self.assertAlmostEqual(row.p11_noncancelling_share_total, 0.4445547580783247, places=12)

    def test_depth_4_values_match_computation(self) -> None:
        row = variance_share_row(4)
        self.assertAlmostEqual(row.p11_new_share_total, 0.967468868352348, places=12)
        self.assertAlmostEqual(row.p11_noncancelling_share_new, 0.4838899868953186, places=12)
        self.assertAlmostEqual(row.p11_noncancelling_share_total, 0.4681484980286464, places=12)

    def test_non_cancelling_share_is_near_local_baseline(self) -> None:
        for depth in (2, 3, 4):
            row = variance_share_row(depth)
            self.assertLess(abs(row.p11_noncancelling_share_new - LOCAL_NONCANCELLING_BASELINE), 0.05)

    def test_document_claim_is_finite_diagnostic_only(self) -> None:
        proves_grh = False
        proves_unconditional_variance_bound = False
        proves_asymptotic_packet_share = False
        self.assertFalse(proves_grh)
        self.assertFalse(proves_unconditional_variance_bound)
        self.assertFalse(proves_asymptotic_packet_share)


if __name__ == "__main__":
    unittest.main()
