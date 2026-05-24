from math import comb, gcd
from fractions import Fraction


def v_p(n, p):
    """p-adic valuation of nonzero integer n."""
    if n == 0:
        return float("inf")
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def digit_sum_base_p(n, p):
    """Sum of digits of n in base p."""
    s = 0
    while n > 0:
        s += n % p
        n //= p
    return s


def fc(n, p):
    """Fuss-Catalan number FC_n^(p) = C(pn,n)/((p-1)n+1)."""
    return comb(p * n, n) // ((p - 1) * n + 1)


def witt_carry(a, b, p):
    """Degree-0 Witt vector carry at prime p."""
    return (a + b - (a + b) % p) // p


def teichmuller_mod_p_sq(a, p):
    """Teichmuller lift omega_p(a) mod p^2."""
    for x in range(a, p * p, p):
        if pow(x, p - 1, p * p) == 1:
            return x
    return None


def test_padic_carry_matches_hg_fnd_007():
    for p in [2, 3, 5]:
        for a in range(p):
            for b in range(p):
                carry = witt_carry(a, b, p)
                assert carry in (0, 1)
                assert carry == int((a + b) >= p)


def test_negative_one_in_padic_base():
    for p in [2, 3, 5, 7]:
        for k in range(1, 8):
            partial = sum((p - 1) * p**j for j in range(k))
            assert partial % p**k == p**k - 1
            assert (partial + 1) % p**k == 0


def test_fuss_catalan_padic_valuation():
    for p in [2, 3]:
        for n in range(1, 6):
            # Kummer: v_p(C(pn,n)) = s_p((p-1)n)/(p-1).
            # The Legendre expression ((p-1)n - s_p((p-1)n))/(p-1)
            # instead computes v_p(((p-1)n)!), not this binomial valuation.
            kummer_val = digit_sum_base_p((p - 1) * n, p) // (p - 1)
            binom_val = v_p(comb(p * n, n), p)
            assert kummer_val == binom_val


def test_teichmuller_lift_is_multiplicative():
    p = 5
    for a in range(1, p):
        for b in range(1, p):
            wa = teichmuller_mod_p_sq(a, p)
            wb = teichmuller_mod_p_sq(b, p)
            wab = teichmuller_mod_p_sq((a * b) % p, p)
            assert (wa * wb) % (p * p) == wab


def test_teichmuller_reduces_to_character():
    for p in [3, 5, 7]:
        for a in range(1, p):
            w = teichmuller_mod_p_sq(a, p)
            assert w % p == a


def test_profinite_crt_decomposition():
    P = 30
    primes = [2, 3, 5]
    for n in range(P):
        residues = tuple(n % p for p in primes)
        reconstructed = 0
        for p, r in zip(primes, residues):
            Mi = P // p
            inv = pow(Mi, -1, p)
            reconstructed += r * Mi * inv
        assert reconstructed % P == n % P


def test_euler_product_partial_at_trivial_character():
    import math

    primes = [p for p in range(2, 50) if all(p % d != 0 for d in range(2, p))]
    s = 2
    partial_product = 1.0
    for p in primes:
        partial_product *= 1 - p ** (-s)
    expected = 6 / math.pi**2
    assert abs(partial_product - expected) < 0.1
