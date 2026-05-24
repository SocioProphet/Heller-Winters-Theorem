#!/usr/bin/env python3
from __future__ import annotations

import cmath
import math
from dataclasses import dataclass
from functools import lru_cache
from typing import Dict, Iterable, Tuple

Q = 37
GENERATOR = 2
MODEL_CONSTANT = 0.3439


@dataclass(frozen=True)
class Q37Row:
    depth: int
    prime_count: int
    cancel_per_character: float
    noncancel_per_character: float
    ratio: float
    predicted_ratio: float
    deviation: float


def predicted_ratio(q: int = Q) -> float:
    return 1.0 + MODEL_CONSTANT / ord10(q)


def ord10(q: int) -> int:
    x = 1
    for k in range(1, q):
        x = (x * 10) % q
        if x == 1:
            return k
    raise RuntimeError(q)


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


@lru_cache(maxsize=None)
def dlog_table(q: int = Q, generator: int = GENERATOR) -> Dict[int, int]:
    table: Dict[int, int] = {}
    value = 1
    for exponent in range(q - 1):
        table[value] = exponent
        value = (value * generator) % q
    if len(table) != q - 1:
        raise RuntimeError("generator did not generate unit group")
    return table


def chi_value(exponent: int, residue: int, q: int = Q) -> complex:
    r = residue % q
    if r == 0:
        return 0j
    k = dlog_table(q)[r]
    return cmath.exp(2j * math.pi * exponent * k / (q - 1))


def noncancelling_exponents(q: int = Q) -> Tuple[int, ...]:
    return tuple(e for e in range(1, q - 1) if abs(chi_value(e, 10, q) - 1) < 1e-9)


def cancelling_exponents(q: int = Q) -> Tuple[int, ...]:
    nc = set(noncancelling_exponents(q))
    return tuple(e for e in range(1, q - 1) if e not in nc)


def character_sum(exponent: int, depth: int, q: int = Q) -> complex:
    return sum(math.log(p) * chi_value(exponent, p, q) for p in primes_in_window(depth) if p % q)


def q37_row(depth: int) -> Q37Row:
    cancel = cancelling_exponents(Q)
    noncancel = noncancelling_exponents(Q)
    cancel_energy = sum(abs(character_sum(e, depth)) ** 2 for e in cancel) / len(cancel)
    noncancel_energy = sum(abs(character_sum(e, depth)) ** 2 for e in noncancel) / len(noncancel)
    pred = predicted_ratio(Q)
    ratio = noncancel_energy / cancel_energy
    return Q37Row(
        depth=depth,
        prime_count=len(primes_in_window(depth)),
        cancel_per_character=cancel_energy,
        noncancel_per_character=noncancel_energy,
        ratio=ratio,
        predicted_ratio=pred,
        deviation=ratio - pred,
    )


def q37_rows(depths: Iterable[int] = (2, 3, 4, 5)) -> Tuple[Q37Row, ...]:
    return tuple(q37_row(depth) for depth in depths)


def run_checks() -> Tuple[Q37Row, ...]:
    assert ord10(Q) == 3
    assert len(noncancelling_exponents(Q)) == 11
    assert len(cancelling_exponents(Q)) == 24
    rows = q37_rows()
    assert abs(predicted_ratio(Q) - 1.1146333333333333) < 1e-12
    assert rows[-1].ratio < 1.0
    assert abs(rows[-1].ratio - predicted_ratio(Q)) > 0.1
    return rows


if __name__ == "__main__":
    for row in run_checks():
        print(row)
