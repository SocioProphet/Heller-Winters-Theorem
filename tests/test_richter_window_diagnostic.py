from tools.check_richter_window_diagnostic import (
    active_primes_in_window,
    diagnostic_rows,
    richter_weil_distribution,
    richter_window_row,
    window_character_sum,
)
from tools.check_finite_character_operator import build_dlog_table, character_indices


def test_depth_one_has_no_active_primes_for_modulus_210():
    assert active_primes_in_window(1) == []


def test_window_character_sums_defined_for_depths_2_to_5():
    table = build_dlog_table()
    for depth in [2, 3, 4, 5]:
        for index in character_indices():
            assert isinstance(window_character_sum(index, depth, table), complex)


def test_richter_window_rows_positive_after_depth_one():
    for row in diagnostic_rows([2, 3, 4, 5]):
        assert row.active_prime_count > 0
        assert row.max_window_sum > 0
        assert row.grh_scale > 0
        assert row.ratio > 0
        assert row.mean_normalized_square > 0


def test_richter_weil_distribution_positive_through_depth_five():
    assert richter_weil_distribution(5) > 0


def test_richter_depth_three_ratio_within_generous_envelope():
    row = richter_window_row(3)
    assert row.ratio < 30


def test_richter_rows_depth_ordering():
    rows = diagnostic_rows([1, 2, 3, 4, 5])
    assert [row.depth for row in rows] == [1, 2, 3, 4, 5]
    assert rows[0].max_richter_exponent is None
    assert all(row.max_richter_exponent is not None for row in rows[1:])
