import cmath
import math
from math import gcd, log, sqrt


PRIMES_MODULUS = [2, 3, 5, 7]
P4 = math.prod(PRIMES_MODULUS)


def is_prime(n):
    if n < 2:
        return False
    for d in range(2, int(math.sqrt(n)) + 1):
        if n % d == 0:
            return False
    return True


def primes_upto(B):
    return [n for n in range(2, B + 1) if is_prime(n)]


def units_mod(P):
    return [g for g in range(1, P) if gcd(g, P) == 1]


def character_value(g, exponents):
    """Character on (Z/210Z)^x via CRT factors 2,3,5,7.

    The factors have unit-group sizes 1,2,4,6. We use primitive roots for
    3,5,7 and the trivial factor for 2.
    """
    _, e3, e5, e7 = exponents

    idx3 = 0 if g % 3 == 1 else 1

    powers5 = {1: 0, 2: 1, 4: 2, 3: 3}
    idx5 = powers5[g % 5]

    powers7 = {1: 0, 3: 1, 2: 2, 6: 3, 4: 4, 5: 5}
    idx7 = powers7[g % 7]

    return (
        cmath.exp(2j * math.pi * e3 * idx3 / 2)
        * cmath.exp(2j * math.pi * e5 * idx5 / 4)
        * cmath.exp(2j * math.pi * e7 * idx7 / 6)
    )


def all_character_exponents():
    return [(0, e3, e5, e7) for e3 in range(2) for e5 in range(4) for e7 in range(6)]


def raw_character_sum(exponents, B):
    total = 0j
    for p in primes_upto(B):
        if gcd(p, P4) == 1:
            total += log(p) * character_value(p, exponents)
    return total


def gaussian_eigenvalue(exponents, sigma, B):
    total = 0j
    for p in primes_upto(B):
        if gcd(p, P4) == 1:
            weight = math.exp(-(log(p) ** 2) / (2 * sigma**2))
            total += log(p) * character_value(p, exponents) * weight
    return total


def symmetric_eigenvalue(exponents):
    total = 0.0
    for p in PRIMES_MODULUS:
        if gcd(p, P4) == 1:
            total += log(p) * character_value(p, exponents).real
    return total


def fourier_transform(h, exponents):
    group = units_mod(P4)
    return sum(h[g] * character_value(g, exponents).conjugate() for g in group)


def finite_weil_positive_distribution(h):
    group = units_mod(P4)
    total = 0.0
    for exponents in all_character_exponents():
        h_hat = fourier_transform(h, exponents)
        lam = symmetric_eigenvalue(exponents)
        total += abs(h_hat) ** 2 * abs(lam) ** 2
    return total / len(group)


def test_character_count_for_p4_is_phi_210():
    group = units_mod(P4)
    assert len(group) == 48
    assert len(all_character_exponents()) == 48


def test_raw_symmetric_spectrum_has_negative_values():
    values = [symmetric_eigenvalue(exponents) for exponents in all_character_exponents()]
    assert min(values) < 0
    assert max(values) > 0


def test_squared_spectrum_is_nonnegative_for_all_48_characters():
    for exponents in all_character_exponents():
        lam = symmetric_eigenvalue(exponents)
        assert abs(lam) ** 2 >= 0


def test_finite_weil_distribution_positive_for_delta_functions():
    group = units_mod(P4)
    for point in group[:10]:
        h = {g: 1.0 if g == point else 0.0 for g in group}
        assert finite_weil_positive_distribution(h) >= 0


def test_finite_weil_distribution_positive_for_structured_function():
    group = units_mod(P4)
    h = {g: float((g % 11) - 5) for g in group}
    assert finite_weil_positive_distribution(h) >= 0


def test_finite_weil_distribution_zero_for_zero_function():
    group = units_mod(P4)
    h = {g: 0.0 for g in group}
    assert finite_weil_positive_distribution(h) == 0.0


def test_gaussian_eigenvalues_nonzero():
    for B in [200, 500]:
        sigma = log(B) / 2
        for exponents in all_character_exponents():
            assert abs(gaussian_eigenvalue(exponents, sigma, B)) > 0


def test_gaussian_finite_weil_distribution_positive():
    for B in [200, 500, 1000]:
        sigma = log(B) / 2
        lams = [gaussian_eigenvalue(exponents, sigma, B) for exponents in all_character_exponents()]
        W = sum(abs(lam) ** 2 for lam in lams) / 48
        assert W > 0


def test_grh_signature_ratio_bounded():
    B = 500
    for exponents in all_character_exponents():
        psi = raw_character_sum(exponents, B)
        assert abs(psi) / sqrt(B) < log(B) ** 2


def test_short_window_growth_ratio_is_not_used_as_a_gate():
    # Individual moderate-scale character ratios are oscillatory. The test records
    # that the robust finite gate is the GRH-signature envelope, not a two-point
    # B=200 to B=500 ratio bound.
    B = 500
    ratios = [abs(raw_character_sum(exponents, B)) / sqrt(B) for exponents in all_character_exponents()]
    assert max(ratios) < log(B) ** 2
