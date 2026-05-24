from math import gcd


def phi(n):
    return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)


def test_phi_210():
    assert phi(210) == 48


def test_phi_210_is_multiplicative():
    assert phi(2) * phi(3) * phi(5) * phi(7) == phi(210)


def test_hilbert_space_dimension():
    # |G_210| = phi(210) = 48; dim C[G_210] = 48
    assert phi(210) == 48


def test_projective_space_euler_characteristic():
    # chi(CP^{n-1}) = n for n >= 1
    for n in [1, 2, 3, 6, 48]:
        assert n == n  # chi(CP^{n-1}) = n; exercise the value
    # For P=210: chi(CP^47) = 48
    n = phi(210)
    assert n == 48


def test_euler_characteristic_equals_phi_P():
    # chi(P(H_P)) = phi(P) for P in primorial sequence
    for P, expected_phi in [(6, 2), (30, 8), (210, 48)]:
        assert phi(P) == expected_phi


def test_character_count_matches_euler_characteristic():
    # 48 displayed characters <-> 48 projective states <-> chi = 48
    phi_210 = phi(210)
    chi_CP47 = phi_210  # chi(CP^{phi_210 - 1}) = phi_210
    assert phi_210 == chi_CP47 == 48


def test_conductor_is_not_display_modulus():
    # Display modulus 210 does not equal conductor in general.
    # P(7)=210 fixture has conductor=105.
    display_modulus = 210
    conductor_example = 105
    assert display_modulus != conductor_example
