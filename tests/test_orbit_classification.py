import unittest

from tools.check_orbit_classification import (
    classify_prime,
    digit_cycle_partial_sums,
    orbit_character_sum,
    orbit_mod_prime,
    primitive_root_primes,
    run_checks,
)


class TestOrbitClassification(unittest.TestCase):
    def test_run_checks(self) -> None:
        rows = run_checks()
        self.assertTrue(rows)

    def test_terminating_primes(self) -> None:
        for prime in (2, 5):
            row = classify_prime(prime)
            self.assertEqual(row.category, "terminating")
            self.assertIsNone(row.period)
            self.assertEqual(row.orbit, tuple())

    def test_degenerate_prime_three(self) -> None:
        row = classify_prime(3)
        self.assertEqual(row.category, "degenerate")
        self.assertEqual(row.period, 1)
        self.assertEqual(row.orbit, (1,))
        self.assertEqual(row.noncancelling_nontrivial_characters, 1)

    def test_partial_orbit_prime_eleven(self) -> None:
        row = classify_prime(11)
        self.assertEqual(row.category, "partial")
        self.assertEqual(row.period, 2)
        self.assertEqual(row.orbit, (10, 1))
        self.assertEqual(row.cancelling_nontrivial_characters, 5)
        self.assertEqual(row.noncancelling_nontrivial_characters, 4)

    def test_full_orbit_primes(self) -> None:
        for prime in (7, 19):
            row = classify_prime(prime)
            self.assertEqual(row.category, "full")
            self.assertEqual(row.period, prime - 1)
            self.assertEqual(len(row.orbit), prime - 1)
            self.assertEqual(row.cancelling_nontrivial_characters, prime - 2)
            self.assertEqual(row.noncancelling_nontrivial_characters, 0)

    def test_p19_orbit_matches_expected_order(self) -> None:
        self.assertEqual(
            orbit_mod_prime(10, 19),
            (10, 5, 12, 6, 3, 11, 15, 17, 18, 9, 14, 7, 13, 16, 8, 4, 2, 1),
        )

    def test_full_orbit_character_sums_cancel(self) -> None:
        for prime in (7, 19):
            for exponent in range(1, prime - 1):
                self.assertLess(abs(orbit_character_sum(prime, exponent)), 1e-9)

    def test_partial_orbit_character_sums_do_not_all_cancel(self) -> None:
        nonzero = [exponent for exponent in range(1, 10) if abs(orbit_character_sum(11, exponent)) > 1e-9]
        zero = [exponent for exponent in range(1, 10) if abs(orbit_character_sum(11, exponent)) <= 1e-9]
        self.assertEqual(len(nonzero), 4)
        self.assertEqual(len(zero), 5)

    def test_artin_prime_prefix_for_base_10(self) -> None:
        self.assertEqual(primitive_root_primes(100, 10), [7, 17, 19, 23, 29, 47, 59, 61, 97])

    def test_digit_cycle_partial_sums_for_full_orbit(self) -> None:
        partials = digit_cycle_partial_sums(19, 1)
        self.assertEqual(len(partials), 18)
        self.assertLess(abs(partials[-1]), 1e-9)
        self.assertGreater(max(abs(value) for value in partials[:-1]), 0.0)

    def test_finite_to_asymptotic_transition_remains_open(self) -> None:
        finite_to_asymptotic_transition_proved = False
        self.assertFalse(finite_to_asymptotic_transition_proved)


if __name__ == "__main__":
    unittest.main()
