from tools.check_antisymmetric_character_operator import (
    MODULUS,
    PRIME_CUTOFF,
    antisymmetric_kernel,
    kernel_is_antisymmetric,
    self_adjoint_antisymmetric_eigenvalues,
    spectrum_is_symmetric_about_zero,
)
from tools.check_finite_character_operator import (
    TOLERANCE,
    build_dlog_table,
    inversion_symmetric_kernel,
    raw_prime_residue_kernel,
    reduced_residues,
    spectrum_summary,
)


def test_antisymmetric_kernel_satisfies_inversion_condition():
    kernel = antisymmetric_kernel(PRIME_CUTOFF, MODULUS)

    assert kernel_is_antisymmetric(kernel, MODULUS, TOLERANCE)
    for h in reduced_residues(MODULUS):
        assert abs(kernel[h] + kernel[pow(h, -1, MODULUS)]) <= TOLERANCE


def test_antisymmetric_kernel_is_pure_imaginary_on_diagonal_elements():
    kernel = antisymmetric_kernel(PRIME_CUTOFF, MODULUS)

    self_inverse_elements = [
        h for h in reduced_residues(MODULUS) if (h * h) % MODULUS == 1
    ]
    assert self_inverse_elements

    for h in self_inverse_elements:
        assert abs(kernel[h]) <= TOLERANCE


def test_all_48_antisymmetric_eigenvalues_are_real():
    dlog_table = build_dlog_table()
    kernel = antisymmetric_kernel(PRIME_CUTOFF, MODULUS)
    values = self_adjoint_antisymmetric_eigenvalues(kernel, dlog_table)

    assert len(values) == 48
    assert all(abs(value.imag) < 1e-8 for value in values)


def test_antisymmetric_spectrum_is_symmetric_about_zero():
    dlog_table = build_dlog_table()
    kernel = antisymmetric_kernel(PRIME_CUTOFF, MODULUS)
    values = self_adjoint_antisymmetric_eigenvalues(kernel, dlog_table)

    assert spectrum_is_symmetric_about_zero(values, tolerance=1e-6)
    summary = spectrum_summary(values)
    assert summary.min_real < 0
    assert summary.max_real > 0
    assert abs(summary.min_real + summary.max_real) < 1e-6


def test_antisymmetric_and_symmetric_kernels_are_orthogonal_decomposition():
    raw = raw_prime_residue_kernel(PRIME_CUTOFF, MODULUS)
    symmetric = inversion_symmetric_kernel(PRIME_CUTOFF, MODULUS)
    antisymmetric = antisymmetric_kernel(PRIME_CUTOFF, MODULUS)

    for h in reduced_residues(MODULUS):
        inverse = pow(h, -1, MODULUS)
        assert abs(symmetric[h] + antisymmetric[h] - raw[h]) <= TOLERANCE
        assert abs(symmetric[h] - antisymmetric[h] - raw[inverse]) <= TOLERANCE


def test_display_modulus_210_is_not_conductor():
    assert 210 != 105
