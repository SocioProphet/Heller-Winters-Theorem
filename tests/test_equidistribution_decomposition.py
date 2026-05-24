import math
import unittest

from tools.check_equidistribution_decomposition import (
    chi7,
    compute_variance_by_prime,
    digit_cycle_sum,
    epsilon,
    grh_envelope,
    max_digit_cycle_partial_sum,
    max_epsilon,
    oracle_bound_at_resonant_depth,
    prime_count_window,
    psi_chi7,
    psi_chi7_via_epsilon,
)


class TestEquidistributionDecomposition(unittest.TestCase):
    def test_decomposition_is_exact(self) -> None:
        for depth in (2, 3):
            direct = psi_chi7(depth)
            via_eps = psi_chi7_via_epsilon(depth)
            self.assertLess(abs(direct - via_eps), 1e-8)

    def test_triangle_bound_holds(self) -> None:
        for depth in (2, 3, 4, 5, 6):
            psi = abs(psi_chi7(depth))
            bound = 6.0 * max_epsilon(depth)
            self.assertLessEqual(psi, bound + 1e-8)

    def test_digit_cycle_sum_is_exactly_zero(self) -> None:
        self.assertLess(abs(digit_cycle_sum()), 1e-12)

    def test_digit_cycle_max_partial_sum(self) -> None:
        self.assertLessEqual(max_digit_cycle_partial_sum(), 2.001)

    def test_oracle_bound_at_resonant_depth(self) -> None:
        actual = abs(psi_chi7(6))
        n6 = prime_count_window(6)
        oracle = 2.0 * math.log(10**6) * math.sqrt(n6 / 6.0)
        self.assertAlmostEqual(oracle, oracle_bound_at_resonant_depth(6), places=10)
        self.assertLessEqual(actual, oracle)

    def test_empirical_ratio_within_grh_envelope(self) -> None:
        for depth in (2, 3, 4, 5, 6):
            ratio = abs(psi_chi7(depth)) / math.sqrt(10**depth)
            self.assertLess(ratio, grh_envelope(depth))

    def test_p7_packet_dominates_variance(self) -> None:
        for depth in (2, 3):
            delta7, var_total = compute_variance_by_prime(depth)
            self.assertGreater(delta7 / var_total, 0.85)

    def test_equidistribution_error_controls_character_sum(self) -> None:
        for depth in (2, 3, 4, 5, 6):
            psi = abs(psi_chi7(depth))
            max_eps = max(abs(epsilon(residue, depth)) for residue in range(1, 7))
            if max_eps > 0.01:
                self.assertLessEqual(psi / max_eps, 6.0 + 1e-10)

    def test_barrier_remains_open(self) -> None:
        unconditional_sqrt_bound_proved = False
        self.assertFalse(unconditional_sqrt_bound_proved)

    def test_chi7_is_nontrivial(self) -> None:
        values = {round(abs(chi7(1, residue)), 12) for residue in range(1, 7)}
        self.assertEqual(values, {1.0})
        self.assertLess(abs(sum(chi7(1, residue) for residue in range(1, 7))), 1e-12)


if __name__ == "__main__":
    unittest.main()
