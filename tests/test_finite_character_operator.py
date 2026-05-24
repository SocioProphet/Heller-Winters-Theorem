import cmath
import math

from tools.check_finite_character_operator import (
    ALPHA,
    BETA,
    GAMMA,
    MODULUS,
    PRIME_CUTOFF,
    TOLERANCE,
    build_dlog_table,
    character_indices,
    crt_generators,
    eigenvalues,
    group_exponent,
    inversion_symmetric_kernel,
    kernel_is_inversion_symmetric,
    multiplicative_order,
    phi,
    spectrum_summary,
)


def test_phi_210():
    assert phi(210) == 48


def test_exp_g_210_from_actual_element_orders():
    assert group_exponent(210) == 12


def test_crt_generators_are_fixed_values():
    assert crt_generators() == (71, 127, 31)
    assert (ALPHA, BETA, GAMMA) == (71, 127, 31)
    assert multiplicative_order(ALPHA) == 2
    assert multiplicative_order(BETA) == 4
    assert multiplicative_order(GAMMA) == 6


def test_dlog_table_spans_full_group():
    dlog_table = build_dlog_table()

    assert len(dlog_table) == phi(MODULUS) == 48


def test_kernel_inversion_symmetry_holds_for_all_elements():
    kernel = inversion_symmetric_kernel(PRIME_CUTOFF, MODULUS)

    assert len(kernel) == 48
    assert kernel_is_inversion_symmetric(kernel)
    for h, value in kernel.items():
        assert abs(value - kernel[pow(h, -1, MODULUS)]) <= TOLERANCE


def test_all_48_character_eigenvalues_are_real_to_tolerance():
    dlog_table = build_dlog_table()
    kernel = inversion_symmetric_kernel(PRIME_CUTOFF, MODULUS)
    values = eigenvalues(kernel, dlog_table)

    assert len(values) == len(character_indices()) == 48
    assert all(abs(value.imag) <= TOLERANCE for value in values)


def test_cos_pi_over_three_real_part_is_one_half():
    assert abs(cmath.exp(1j * math.pi / 3).real - 0.5) < 1e-12


def test_spectrum_is_not_generically_symmetric_about_zero():
    dlog_table = build_dlog_table()
    kernel = inversion_symmetric_kernel(PRIME_CUTOFF, MODULUS)
    summary = spectrum_summary(eigenvalues(kernel, dlog_table))

    assert summary.eigenvalue_count == 48
    assert summary.min_real < 0
    assert summary.max_real > 0
    assert abs(summary.min_real + summary.max_real) > 1.0


def test_display_modulus_210_is_not_conductor():
    display_modulus = 210
    conductor_example = 105

    assert display_modulus != conductor_example
