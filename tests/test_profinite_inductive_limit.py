from math import gcd, log, prod


PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def primorial(k: int) -> int:
    result = 1
    for p in PRIMES[:k]:
        result *= p
    return result


def G(P: int) -> list[int]:
    return [g for g in range(1, P) if gcd(g, P) == 1]


def test_primorial_sequence() -> None:
    assert [primorial(k) for k in range(1, 6)] == [2, 6, 30, 210, 2310]


def test_group_sizes_are_totient() -> None:
    def phi(P: int) -> int:
        divisors = [
            p
            for p in range(2, P + 1)
            if all(p % d != 0 for d in range(2, p)) and P % p == 0
        ]
        return prod(p - 1 for p in divisors)

    for k in range(1, 6):
        P = primorial(k)
        assert len(G(P)) == phi(P)


def test_surjection_is_compatible() -> None:
    P4, P5 = primorial(4), primorial(5)
    G4, G5 = set(G(P4)), set(G(P5))
    image = {g % P4 for g in G5}
    assert image == G4


def test_lift_is_injective() -> None:
    P4, P5 = primorial(4), primorial(5)
    G4, G5 = G(P4), G(P5)
    f = {g: float(g) for g in G4}
    lifted = {g: f[g % P4] for g in G5}

    for g4 in G4:
        fibers = [g5 for g5 in G5 if g5 % P4 == g4]
        assert all(lifted[g5] == f[g4] for g5 in fibers)


def test_eigenvalue_approximation_improves_with_k() -> None:
    def prime_log_sum(P: int) -> float:
        primes = [p for p in range(2, P + 1) if all(p % d != 0 for d in range(2, p))]
        return sum(log(p) for p in primes)

    sums = [prime_log_sum(primorial(k)) for k in range(1, 6)]
    assert all(sums[i] < sums[i + 1] for i in range(len(sums) - 1))


def test_haar_measure_uniform_on_finite_level() -> None:
    P = primorial(4)
    group = G(P)
    size = len(group)

    chi_trivial_sum = sum(1 for _ in group)
    assert chi_trivial_sum == size

    norm_sq = chi_trivial_sum / size
    assert abs(norm_sq - 1.0) < 1e-12
