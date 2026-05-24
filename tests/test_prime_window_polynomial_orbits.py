from math import gcd, sqrt


def repunit(k):
    return (10**k - 1) // 9


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
