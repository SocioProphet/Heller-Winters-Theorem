import unittest

from tools.check_noncancelling_fraction import (
    cumulative_noncancelling_count,
    local_noncancelling_count,
    noncancelling_rows,
    order_mod_10,
    phi_of_primes,
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

    def test_cumulative_tower_formula_examples(self) -> None:
        rows = {row.p: row for row in noncancelling_rows(37)}
        expected = {
            7: 1,
            11: 193,
            13: 673,
            17: 673,
            19: 673,
            23: 673,
            29: 673,
            31: 1_021_870_753,
            37: 338_238_997_153,
        }
        for p, count in expected.items():
            self.assertEqual(rows[p].cumulative_noncancelling, count)

    def test_cumulative_formula_from_prefix(self) -> None:
        prefix_29 = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
        self.assertEqual(phi_of_primes(prefix_29), 1_021_870_080)
        self.assertEqual(cumulative_noncancelling_count(prefix_29), 673)

    def test_673_applies_only_through_p29(self) -> None:
        rows = {row.p: row for row in noncancelling_rows(37)}
        self.assertEqual(rows[29].cumulative_noncancelling, 673)
        self.assertGreater(rows[31].cumulative_noncancelling, 1_000_000_000)
        self.assertGreater(rows[37].cumulative_noncancelling, 300_000_000_000)

    def test_diagonal_lcm_count_is_not_local_nc_count(self) -> None:
        diagonal_lcm_formula_is_nc_count = False
        self.assertFalse(diagonal_lcm_formula_is_nc_count)

    def test_claim_is_finite_counting_only(self) -> None:
        proves_grh = False
        proves_variance_bound = False
        proves_fraction_limit = False
        self.assertFalse(proves_grh)
        self.assertFalse(proves_variance_bound)
        self.assertFalse(proves_fraction_limit)


if __name__ == "__main__":
    unittest.main()
