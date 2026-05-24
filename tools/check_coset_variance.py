#!/usr/bin/env python3
from __future__ import annotations

import math
from dataclasses import dataclass
from functools import lru_cache
from typing import Dict, Iterable, Tuple

Q = 37
BASE = 10


@dataclass(frozen=True)
class CosetVarianceRow:
    q: int
    depth: int
    coset_count: int
    orbit_size: int
    theta_active: float
    between_variance: float
    within_variance: float
    ratio: float


@lru_cache(maxsize=None)
def primes_upto(limit: int) -> Tuple[int, ...]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    return tuple(i for i in range(limit + 1) if sieve[i])


@lru_cache(maxsize=None)
def primes_in_window(depth: int) -> Tuple[int, ...]:
    low = 10 ** (depth - 1)
    high = 10**depth
    return tuple(p for p in primes_upto(high - 1) if low <= p < high)


def ord_mod(base: int, q: int) -> int:
    if math.gcd(base, q) != 1:
        raise ValueError("base must be a unit")
    x = 1
    for k in range(1, q):
        x = (x * base) % q
        if x == 1:
            return k
    raise RuntimeError(q)


def subgroup_h(q: int = Q, base: int = BASE) -> Tuple[int, ...]:
    h = []
    x = 1
    for _ in range(ord_mod(base, q)):
        h.append(x)
        x = (x * base) % q
    return tuple(h)


def unit_residues(q: int = Q) -> Tuple[int, ...]:
    return tuple(r for r in range(1, q) if math.gcd(r, q) == 1)


def cosets(q: int = Q, base: int = BASE) -> Tuple[Tuple[int, ...], ...]:
    h = set(subgroup_h(q, base))
    seen = set()
    out = []
    for r in unit_residues(q):
        if r in seen:
            continue
        c = tuple(sorted((r * x) % q for x in h))
        out.append(c)
        seen.update(c)
    return tuple(out)


def residue_masses(q: int, depth: int) -> Dict[int, float]:
    masses = {r: 0.0 for r in unit_residues(q)}
    for p in primes_in_window(depth):
        residue = p % q
        if residue != 0:
            masses[residue] += math.log(p)
    return masses


def theta_active(q: int, depth: int) -> float:
    return sum(math.log(p) for p in primes_in_window(depth) if p % q != 0)


def coset_masses(q: int, depth: int) -> Tuple[float, ...]:
    masses = residue_masses(q, depth)
    return tuple(sum(masses[r] for r in c) for c in cosets(q))


def between_coset_variance(q: int, depth: int) -> float:
    values = coset_masses(q, depth)
    mean = sum(values) / len(values)
    return sum((v - mean) ** 2 for v in values)


def within_coset_variance(q: int, depth: int) -> float:
    masses = residue_masses(q, depth)
    total = 0.0
    for c in cosets(q):
        mean = sum(masses[r] for r in c) / len(c)
        total += sum((masses[r] - mean) ** 2 for r in c)
    return total


def coset_variance_row(depth: int, q: int = Q) -> CosetVarianceRow:
    between = between_coset_variance(q, depth)
    within = within_coset_variance(q, depth)
    return CosetVarianceRow(
        q=q,
        depth=depth,
        coset_count=len(cosets(q)),
        orbit_size=len(subgroup_h(q)),
        theta_active=theta_active(q, depth),
        between_variance=between,
        within_variance=within,
        ratio=between / within if within else float("inf"),
    )


def coset_variance_rows(depths: Iterable[int] = (2, 3, 4, 5)) -> Tuple[CosetVarianceRow, ...]:
    return tuple(coset_variance_row(depth) for depth in depths)


def run_checks() -> Tuple[CosetVarianceRow, ...]:
    assert len(subgroup_h(Q)) == 3
    assert len(cosets(Q)) == 12
    assert sum(len(c) for c in cosets(Q)) == 36
    rows = coset_variance_rows()
    for row in rows:
        assert row.between_variance >= 0
        assert row.within_variance >= 0
        assert row.theta_active > 0
    return rows


if __name__ == "__main__":
    for row in run_checks():
        print(row)
