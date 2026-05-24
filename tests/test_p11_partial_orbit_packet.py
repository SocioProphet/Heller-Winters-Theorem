import unittest

from tools.check_p11_partial_orbit_packet import (
    active_primes_in_window,
    is_p11_orbit_cancelling,
    local_p11_orbit_sum,
    packet_counts,
    packet_energy_row,
    run_checks,
)


class TestP11PartialOrbitPacket(unittest.TestCase):
    def test_run_checks(self) -> None:
        rows = run_checks()
        self.assertTrue(rows)

    def test_character_layer_counts(self) -> None:
        counts = packet_counts()
        self.assertEqual(counts.total_characters, 480)
        self.assertEqual(counts.old_p210_layer, 48)
        self.assertEqual(counts.new_p11_layer, 432)

    def test_local_p11_split(self) -> None:
        counts = packet_counts()
        self.assertEqual(counts.p11_cancelling_local, 5)
        self.assertEqual(counts.p11_noncancelling_local, 4)
        self.assertEqual(counts.p11_cancelling_new_layer, 240)
        self.assertEqual(counts.p11_noncancelling_new_layer, 192)

    def test_local_orbit_cancellation_condition(self) -> None:
        cancelling = [exponent for exponent in range(1, 10) if is_p11_orbit_cancelling(exponent)]
        noncancelling = [exponent for exponent in range(1, 10) if not is_p11_orbit_cancelling(exponent)]
        self.assertEqual(cancelling, [1, 3, 5, 7, 9])
        self.assertEqual(noncancelling, [2, 4, 6, 8])
        for exponent in cancelling:
            self.assertLess(abs(local_p11_orbit_sum(exponent)), 1e-12)
        for exponent in noncancelling:
            self.assertAlmostEqual(abs(local_p11_orbit_sum(exponent)), 2.0, places=12)

    def test_energy_decomposition_depths(self) -> None:
        for depth in (2, 3):
            row = packet_energy_row(depth)
            self.assertGreater(row.active_prime_count, 0)
            self.assertGreater(row.total_nontrivial_energy, 0.0)
            self.assertGreater(row.p11_new_energy, 0.0)
            self.assertAlmostEqual(
                row.old_p210_energy + row.p11_new_energy,
                row.total_nontrivial_energy,
                places=6,
            )
            self.assertAlmostEqual(
                row.p11_cancelling_energy + row.p11_noncancelling_energy,
                row.p11_new_energy,
                places=6,
            )

    def test_p11_packet_is_finite_diagnostic_only(self) -> None:
        proves_grh = False
        proves_unconditional_variance_bound = False
        proves_asymptotic_packet_share = False
        self.assertFalse(proves_grh)
        self.assertFalse(proves_unconditional_variance_bound)
        self.assertFalse(proves_asymptotic_packet_share)

    def test_depth_windows_have_active_primes(self) -> None:
        self.assertGreater(len(active_primes_in_window(2)), 0)
        self.assertGreater(len(active_primes_in_window(3)), 0)


if __name__ == "__main__":
    unittest.main()
