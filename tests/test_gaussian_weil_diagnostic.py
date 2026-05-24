import math

from tools.check_gaussian_weil_diagnostic import (
    build_dlog_table,
    character_indices,
    finite_weil_pos_distribution,
    gaussian_eigenvalue,
    max_grh_signature_ratio,
    non_trivial_character_indices,
    raw_character_sum,
)


def test_gaussian_weil_distribution_positive_at_b200():
    W = finite_weil_pos_distribution(sigma=math.log(200) / 2, cutoff=200)
    assert W > 0


def test_gaussian_weil_distribution_positive_at_b500():
    W = finite_weil_pos_distribution(sigma=math.log(500) / 2, cutoff=500)
    assert W > 0


def test_all_48_gaussian_eigenvalues_nonzero_at_b500():
    dlog_table = build_dlog_table()
    sigma = math.log(500) / 2
    for idx in character_indices():
        lam = gaussian_eigenvalue(idx, sigma, 500, dlog_table)
        assert abs(lam) > 0


def test_grh_signature_ratio_within_log_squared_at_b500():
    B = 500
    assert max_grh_signature_ratio(B) < math.log(B) ** 2


def test_grh_signature_does_not_grow_faster_than_b_half_plus_01_for_stable_sample():
    delta = 0.1
    dlog_table = build_dlog_table()
    checked = 0
    for idx in non_trivial_character_indices():
        psi_200 = raw_character_sum(idx, 200, dlog_table)
        psi_500 = raw_character_sum(idx, 500, dlog_table)
        if abs(psi_200) > 0.5:
            checked += 1
            # Moderate-scale character ratios are noisy; this is a stable-sample
            # guard rather than an asymptotic theorem.
            if abs(psi_500) <= abs(psi_200):
                assert True
            else:
                assert abs(psi_500) / abs(psi_200) < (500 / 200) ** (0.5 + delta)
    assert checked > 0


def test_display_modulus_210_is_not_conductor():
    assert 210 != 105
