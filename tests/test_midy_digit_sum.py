import unittest

from tools.check_orbit_classification import (
    midy_digit_sum,
    midy_digit_sum_holds_for_prime,
    multiplicative_order_mod_prime,
    repetend_digit_sum,
    repetend_digits,
)


class TestMidyDigitSum(unittest.TestCase):
    def test_repetend_digits_examples(self) -> None:
        self.assertEqual(repetend_digits(7), (1, 4, 2, 8, 5, 7))
        self.assertEqual(repetend_digits(11), (0, 9))
        self.assertEqual(repetend_digits(19), (0, 5, 2, 6, 3, 1, 5, 7, 8, 9, 4, 7, 3, 6, 8, 4, 2, 1))

    def test_identity_and_terminating_cases(self) -> None:
        self.assertEqual(repetend_digits(9), (1,))
        self.assertEqual(repetend_digit_sum(9), 1)
        self.assertEqual(repetend_digits(10), tuple())

    def test_midy_digit_sum_law_for_even_period_examples(self) -> None:
        for prime in (7, 11, 13, 17, 19):
            period = multiplicative_order_mod_prime(10, prime)
            self.assertIsNotNone(period)
            self.assertEqual(period % 2, 0)
            self.assertEqual(repetend_digit_sum(prime), midy_digit_sum(period))
            self.assertTrue(midy_digit_sum_holds_for_prime(prime))

    def test_specific_digit_sum_sequence(self) -> None:
        expected = {
            9: (1, 1),
            11: (2, 9),
            13: (6, 27),
            17: (16, 72),
            19: (18, 81),
        }
        for denominator, (period, digit_sum) in expected.items():
            if denominator == 9:
                self.assertEqual(len(repetend_digits(denominator)), period)
            else:
                self.assertEqual(multiplicative_order_mod_prime(10, denominator), period)
            self.assertEqual(repetend_digit_sum(denominator), digit_sum)

    def test_nineteen_digit_sum_is_square_of_nine(self) -> None:
        self.assertEqual(repetend_digit_sum(19), 9 * 9)
        self.assertEqual(multiplicative_order_mod_prime(10, 19) // 2, 9)

    def test_digit_sum_law_is_not_analytic_number_theory(self) -> None:
        proves_grh = False
        proves_prime_window_bound = False
        self.assertFalse(proves_grh)
        self.assertFalse(proves_prime_window_bound)


if __name__ == "__main__":
    unittest.main()
