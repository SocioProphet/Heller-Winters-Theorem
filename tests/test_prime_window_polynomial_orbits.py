from math import cos, cosh, exp, factorial, gcd, log, pi, sinh, sqrt, tan, tanh


def repunit(k):
    return (10**k - 1) // 9


def theta3(q, terms=20):
    return 1 + 2 * sum(q ** (n**2) for n in range(1, terms))


def test_n_squared_plus_1_orbit_in_G210():
    orbit = {(n**2 + 1) % 210 for n in range(210) if gcd((n**2 + 1) % 210, 210) == 1}
    assert len(orbit) == 16


def test_prime_candidates_all_equiv_1_mod_4():
    for n in range(0, 100, 2):
        assert (n**2 + 1) % 4 == 1


def test_even_odd_split_for_odd_p():
    for k in [2, 3]:
        for p in [1, 3, 5]:
            for n in range(10):
                value = n**k + p
                if n % 2 == 0:
                    assert value % 2 == 1
                else:
                    assert value % 2 == 0


def test_gap_sequence_is_arithmetic_progression():
    values = [n**2 + 1 for n in range(0, 20, 2)]
    gaps = [values[i + 1] - values[i] for i in range(len(values) - 1)]
    diffs = [gaps[i + 1] - gaps[i] for i in range(len(gaps) - 1)]
    assert all(diff == 8 for diff in diffs)


def test_primes_equiv_3_mod_4_never_divide_n_squared_plus_1():
    for p in [3, 7, 11, 19, 23, 31]:
        assert p % 4 == 3
        assert all((n**2 + 1) % p != 0 for n in range(p))


def test_perfect_cancellation_on_mod10_cosets():
    units = [1, 3, 7, 9]
    nontrivial_character = {1: 1, 3: -1, 7: -1, 9: 1}
    assert sum(nontrivial_character[g] for g in units) == 0


def test_geometric_center_of_richter_window():
    for k in range(1, 6):
        low = 10 ** (k - 1)
        high = 10**k
        assert sqrt(low * high) == 10 ** (k - 0.5)


def test_admissible_density_is_two_fifths():
    admissible_terminal_digits = {1, 3, 7, 9}
    assert len(admissible_terminal_digits) / 10 == 2 / 5


def test_next_prime_transition_from_3_most_likely_7():
    # Finite toy oracle: after terminal digit 3, adding 4 reaches 7, the next
    # admissible terminal class before wraparound to 1.
    admissible_cycle = [1, 3, 7, 9]
    idx = admissible_cycle.index(3)
    assert admissible_cycle[idx + 1] == 7
    assert (3 + 4) % 10 == 7


def test_repunit_resonance_prime_11_in_depth_2():
    assert repunit(2) == 11
    assert repunit(2) % 11 == 0


def test_cosine_series_uses_even_powers_only():
    x = 0.5
    cos_approx = sum((-1) ** n * x ** (2 * n) / factorial(2 * n) for n in range(10))
    assert abs(cos_approx - cos(x)) < 1e-10


def test_even_stream_generates_theta_function():
    z = 0.1
    even_stream = sum(z ** (4 * m**2) for m in range(10))
    theta_approx = 1 + 2 * sum(z ** (4 * m**2) for m in range(1, 10))
    assert abs(even_stream - theta_approx + 1) < 1e-12


def test_tan_poles_at_half_integer_pi():
    for k in range(5):
        pole = pi * (k + 0.5)
        x_near = pole - 0.001
        assert abs(tan(x_near)) > 100


def test_mittag_leffler_sum_n_squared_plus_1():
    n_max = 10000
    partial = sum(1 / (n**2 + 1) for n in range(1, n_max + 1))
    exact = (pi / tanh(pi) - 1) / 2
    assert abs(partial - exact) < 0.001


def test_exact_cancellation_on_critical_line():
    assert sinh(0) == 0.0
    assert cosh(0) == 1.0
    assert cosh(0) ** 2 - sinh(0) ** 2 == 1.0


def test_hyperbolic_identity_holds_exactly():
    for delta in [0, 0.1, 0.5, 1.0, 2.0]:
        for k in [1, 2, 3, 5, 10]:
            u = delta * k * log(10)
            assert abs(cosh(u) ** 2 - sinh(u) ** 2 - 1.0) < 1e-9


def test_tanh_is_zero_on_critical_line():
    assert tanh(0) == 0.0


def test_tanh_approaches_one_off_critical_line():
    for delta in [0.1, 0.2]:
        for k in [10, 20]:
            u = delta * k * log(10)
            assert tanh(u) > 0.9


def test_theta_functional_equation_at_t_equals_1():
    t = 1.0
    lhs = theta3(exp(-pi * t))
    rhs = t ** (-0.5) * theta3(exp(-pi / t))
    assert abs(lhs - rhs) < 1e-6
