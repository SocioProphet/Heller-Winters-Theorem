#!/usr/bin/env python3
from __future__ import annotations

import cmath
import math
from dataclasses import dataclass
from functools import lru_cache
from typing import Dict, Iterable, Tuple

Q = 37
BASE = 10


@dataclass(frozen=True)
class CayleySpectralGapRow:
    q: int
    depth: int
    orbit_size: int
    quotient_size: int
    support_size: int
    support_generates: bool
    lambda_star: float
    spectral_gap: float
    one_step_l2_bound: float
    grh_claimed: bool


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


@lru_cache(maxsize=None)
def primes_upto(limit: int) -> Tuple[int, ...]:
    return tuple(n for n in range(2, limit + 1) if is_prime(n))


@lru_cache(maxsize=None)
def primes_in_window(depth: int) -> Tuple[int, ...]:
    low = 10 ** (depth - 1)
    high = 10**depth
    return tuple(p for p in primes_upto(high - 1) if low <= p < high)


def multiplicative_order(a: int, q: int) -> int:
    if math.gcd(a, q) != 1:
        raise ValueError("a must be a unit modulo q")
    x = 1
    for k in range(1, q):
        x = (x * a) % q
        if x == 1:
            return k
    raise RuntimeError(q)


def primitive_generator(q: int) -> int:
    for g in range(2, q):
        if multiplicative_order(g, q) == q - 1:
            return g
    raise RuntimeError(q)


@lru_cache(maxsize=None)
def dlog_table(q: int) -> Dict[int, int]:
    g = primitive_generator(q)
    table: Dict[int, int] = {}
    x = 1
    for exponent in range(q - 1):
        table[x] = exponent
        x = (x * g) % q
    return table


def orbit_size(q: int = Q, base: int = BASE) -> int:
    return multiplicative_order(base, q)


def quotient_size(q: int = Q, base: int = BASE) -> int:
    return (q - 1) // orbit_size(q, base)


def quotient_coordinate(residue: int, q: int = Q, base: int = BASE) -> int:
    if residue % q == 0:
        raise ValueError("residue must be a unit")
    return dlog_table(q)[residue % q] % quotient_size(q, base)


def quotient_prime_weights(q: int, depth: int, base: int = BASE) -> Tuple[float, ...]:
    size = quotient_size(q, base)
    weights = [0.0 for _ in range(size)]
    for p in primes_in_window(depth):
        if p % q == 0:
            continue
        weights[quotient_coordinate(p, q, base)] += math.log(p)
    total = sum(weights)
    if total <= 0:
        raise RuntimeError("empty active prime mass")
    return tuple(w / total for w in weights)


def support_generates_quotient(weights: Tuple[float, ...]) -> bool:
    size = len(weights)
    support = [i for i, w in enumerate(weights) if w > 0 and i != 0]
    if not support:
        return False
    g = size
    for s in support:
        g = math.gcd(g, s)
    return g == 1


def quotient_eigenvalues(weights: Tuple[float, ...]) -> Tuple[complex, ...]:
    size = len(weights)
    values = []
    for m in range(size):
        values.append(sum(w * cmath.exp(2j * math.pi * m * a / size) for a, w in enumerate(weights)))
    return tuple(values)


def spectral_gap(weights: Tuple[float, ...]) -> Tuple[float, float]:
    eigenvalues = quotient_eigenvalues(weights)
    lambda_star = max(abs(v) for v in eigenvalues[1:])
    return lambda_star, 1.0 - lambda_star


def cayley_spectral_gap_row(q: int, depth: int) -> CayleySpectralGapRow:
    weights = quotient_prime_weights(q, depth)
    lam, gap = spectral_gap(weights)
    qsize = quotient_size(q)
    return CayleySpectralGapRow(
        q=q,
        depth=depth,
        orbit_size=orbit_size(q),
        quotient_size=qsize,
        support_size=sum(1 for w in weights if w > 0),
        support_generates=support_generates_quotient(weights),
        lambda_star=lam,
        spectral_gap=gap,
        one_step_l2_bound=math.sqrt(qsize) * lam,
        grh_claimed=False,
    )


def cayley_spectral_gap_rows(q: int = Q, depths: Iterable[int] = (2, 3, 4, 5)) -> Tuple[CayleySpectralGapRow, ...]:
    return tuple(cayley_spectral_gap_row(q, depth) for depth in depths)


def run_checks() -> Tuple[CayleySpectralGapRow, ...]:
    rows = cayley_spectral_gap_rows()
    assert orbit_size(Q) == 3
    assert quotient_size(Q) == 12
    for row in rows:
        assert row.quotient_size == 12
        assert row.support_generates
        assert 0.0 <= row.lambda_star < 1.0
        assert row.spectral_gap > 0.0
        assert row.grh_claimed is False
    return rows


if __name__ == "__main__":
    for row in run_checks():
        print(row)
