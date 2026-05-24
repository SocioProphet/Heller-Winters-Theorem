from math import gcd


def dr(n: int) -> int:
    return 1 + (n - 1) % 9 if n > 0 else 0


def repunit(k: int) -> int:
    return (10**k - 1) // 9


def test_repunit_additive_sum_produces_digit_sequence() -> None:
    assert 1 + 11 + 111 == 123

    # R_1 + ... + R_n produces digits 1,2,...,n for n <= 9.
    for n in range(1, 10):
        total = sum(repunit(k) for k in range(1, n + 1))
        digits = [int(d) for d in str(total)]
        assert digits == list(range(1, n + 1))


def test_digital_root_of_repunit_is_k_mod_9() -> None:
    for k in range(1, 20):
        assert dr(repunit(k)) == dr(k)


def test_digital_root_sum_equals_triangular_digital_root() -> None:
    def triangular(n: int) -> int:
        return n * (n + 1) // 2

    for n in range(1, 10):
        total = sum(repunit(k) for k in range(1, n + 1))
        assert dr(total) == dr(triangular(n))


def test_coprimality_fingerprint_at_n_equals_3() -> None:
    def phi(n: int) -> int:
        return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)

    assert dr(123) == 6
    assert phi(9) == 6
    assert dr(123) == phi(9)


def ord10(p: int) -> int:
    order = 1
    x = 10 % p
    while x != 1:
        x = (x * 10) % p
        order += 1
    return order


def test_repunit_resonance_condition() -> None:
    # p divides R_k iff ord_p(10) divides k for primes p not dividing 10.
    for p in [7, 11, 13, 37, 41, 101]:
        order = ord10(p)
        for k in range(1, 13):
            assert (repunit(k) % p == 0) == (k % order == 0)
