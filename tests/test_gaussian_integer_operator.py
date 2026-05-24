import cmath
import math

from tools.check_finite_character_operator import (
    ALPHA,
    BETA,
    GAMMA,
    MODULUS,
    PRIME_CUTOFF,
    build_dlog_table,
    character_value,
    reduced_residues,
)
from tools.check_gaussian_integer_operator import (
    PHI_111_INDEX,
    base_imaginary_half,
    catalan_singularity_from_j_half,
    chi_111_at_combined_generator,
    chi_111_zeta_product,
    combined_generator,
    gaussian_eigenvalue,
    gaussian_integer_for_prime,
    gaussian_integer_kernel,
    gaussian_phase,
    su2_j_half_casimir,
    zeta2,
    zeta4,
    zeta6,
)


def test_gaussian_integer_split_prime_examples():
    assert gaussian_integer_for_prime(2) == (1, 1)
    assert gaussian_integer_for_prime(5) == (2, 1)
    assert gaussian_integer_for_prime(13) == (3, 2)
    assert gaussian_integer_for_prime(17) == (4, 1)
    assert gaussian_integer_for_prime(3) is None
    assert gaussian_integer_for_prime(7) is None


def test_gaussian_phase_has_unit_norm():
    for pair in [(1, 1), (2, 1), (3, 2), (4, 1)]:
        phase = gaussian_phase(*pair)
        assert abs(abs(phase) - 1.0) < 1e-12


def test_gaussian_kernel_has_full_residue_support_shape():
    kernel = gaussian_integer_kernel(PRIME_CUTOFF, MODULUS)

    assert set(kernel) == set(reduced_residues(MODULUS))
    assert len(kernel) == 48
    assert any(abs(value) > 0 for value in kernel.values())


def test_combined_generator_and_chi_111_value():
    dlog_table = build_dlog_table()
    g_star = combined_generator()
    chi = character_value(PHI_111_INDEX, g_star, dlog_table)

    assert g_star == (ALPHA * BETA * GAMMA) % MODULUS
    assert abs(chi - chi_111_at_combined_generator()) < 1e-12
    assert abs(chi - chi_111_zeta_product()) < 1e-12
    assert abs(chi - cmath.exp(-1j * math.pi / 6)) < 1e-12
    assert abs(chi.imag + 0.5) < 1e-12


def test_chi_111_casimir_relation():
    chi_111_gstar = zeta2() ** 1 * zeta4() ** 1 * zeta6() ** 1

    assert abs(abs(chi_111_gstar) ** 2 - 1.0) < 1e-12
    assert abs(chi_111_gstar.imag + 0.5) < 1e-12

    j = 0.5
    spin_component = chi_111_gstar.imag
    assert abs(spin_component * spin_component + j - j * (j + 1)) < 1e-12
    assert abs(su2_j_half_casimir() - 0.75) < 1e-12


def test_catalan_singularity_from_j_half():
    j = 0.5
    rho_2 = 1 / (2 * (2 * j + 1))

    assert abs(rho_2 - 0.25) < 1e-12
    assert abs(catalan_singularity_from_j_half() - 0.25) < 1e-12

    base_squared = (1 / (2 * 1j)) ** 2
    assert abs(base_squared + rho_2) < 1e-12
    assert abs(base_imaginary_half() ** 2 + rho_2) < 1e-12


def test_phi_111_gaussian_eigenvalue_is_computable():
    dlog_table = build_dlog_table()
    kernel = gaussian_integer_kernel(PRIME_CUTOFF, MODULUS)
    eigenvalue = gaussian_eigenvalue(PHI_111_INDEX, kernel, dlog_table)

    assert isinstance(eigenvalue, complex)
    assert abs(eigenvalue) > 0


def test_display_modulus_210_is_not_conductor():
    assert 210 != 105
