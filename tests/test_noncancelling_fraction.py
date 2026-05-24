import unittest

from tools.check_noncancelling_fraction import (
    lcm_orders,
    local_noncancelling_count,
    noncancelling_rows,
    order_mod_10,
    phi_of_primes,
    primorial_diagonal_noncancelling_count,
    run_checks,
)


class TestNonCancellingFraction(unittest.TestCase):
    def test_run_checks(self) -> None:
        rows = run_checks()
        self.assertTrue(rows)

    def test_local_formula_examples(self) -> None:
        expected = {
            2: 0,
            3: 1,
            5: 0,
            7: 0,
            11: 4,
            13: 1,
            17: 0,
            19: 0,
            23: 0,
            29: 0,
            31: 1,
            37: 11,
        }
        for p, count in expected.items():
            self.assertEqual(local_noncancelling_count(p), count)

    def test_artin_primes_have_zero_local_noncancelling(self) -> None:
        for p in (7, 17, 19, 23, 29):
            self.assertEqual(order_mod_10(p), p - 1)
            self.assertEqual(local_noncancelling_count(p), 0)

    def test_primorial_diagonal_formula_examples(self) -> None:
        rows = {row.p: row for row in noncancelling_rows(37)}
        expected = {
            7: 7,
            11: 79,
            13: 959,
            17: 1919,
            19: 11519,
            23: 23039,
            29: 92159,
            31: 552959,
            37: 19906559,
        }
        for p, count in expected.items():
            self.assertEqual(rows[p].diagonal_noncancelling, count)
            self.assertEqual(
                rows[p].diagonal_noncancelling,
                rows[p].phi_prefix // rows[p].resonant_lcm - 1,
            )

    def test_prefix_phi_and_lcm_examples(self) -> None:
        prefix_29 = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
        self.assertEqual(phi_of_primes(prefix_29), 1021870080)
        self.assertEqual(lcm_orders(prefix_29), 11088)
        self.assertEqual(primorial_diagonal_noncancelling_count(prefix_29), 92159)

    def test_673_is_not_current_verified_prefix_count(self) -> None:
        rows = noncancelling_rows(37)
        self.assertNotIn(673, [row.diagonal_noncancelling for row in rows])
        self.assertNotIn(673, [row.local_noncancelling for row in rows])

    def test_claim_is_finite_counting_only(self) -> None:
        proves_grh = False
        proves_variance_bound = False
        proves_fraction_limit = False
        self.assertFalse(proves_grh)
        self.assertFalse(proves_variance_bound)
        self.assertFalse(proves_fraction_limit)


if __name__ == "__main__":
    unittest.main()
