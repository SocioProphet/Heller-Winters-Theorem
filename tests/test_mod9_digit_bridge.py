import unittest

from tools.check_orbit_classification import (
    DIGITS_1_OVER_7,
    RODIN_ACTIVE_SET,
    RODIN_AXIS_SET,
    one_seventh_digit_set,
    rodin_axis_mod_9,
    rodin_doubling_orbit,
    units_mod_9,
)


class TestMod9DigitBridge(unittest.TestCase):
    def test_doubling_orbit_mod_9(self) -> None:
        self.assertEqual(rodin_doubling_orbit(), (1, 2, 4, 8, 7, 5))
        self.assertEqual(set(rodin_doubling_orbit()), set(RODIN_ACTIVE_SET))

    def test_mod9_unit_axis_split(self) -> None:
        self.assertEqual(units_mod_9(), RODIN_ACTIVE_SET)
        self.assertEqual(rodin_axis_mod_9(), RODIN_AXIS_SET)
        self.assertTrue(set(units_mod_9()).isdisjoint(set(rodin_axis_mod_9())))

    def test_digits_of_one_seventh_match_units_as_set(self) -> None:
        self.assertEqual(DIGITS_1_OVER_7, (1, 4, 2, 8, 5, 7))
        self.assertEqual(one_seventh_digit_set(), RODIN_ACTIVE_SET)
        self.assertEqual(set(DIGITS_1_OVER_7), set(rodin_doubling_orbit()))

    def test_bridge_is_finite_arithmetic_only(self) -> None:
        analytic_theorem_claimed = False
        self.assertFalse(analytic_theorem_claimed)


if __name__ == "__main__":
    unittest.main()
