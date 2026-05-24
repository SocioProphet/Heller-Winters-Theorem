#!/usr/bin/env python3
from __future__ import annotations

import math
from dataclasses import dataclass
from functools import lru_cache
from typing import Iterable, Tuple


@dataclass(frozen=True)
class QuotientLargeSieveRow:
    q: int
    depth: int
    orbit_size: int
    quotient_index: int
    noncancelling_count: int
    window_size: int
    prime_log_square_sum: float
    standard_bound: float
    quotient_candidate_bound: float
    improvement_factor: float
    grh_packet_scale: float
    quotient_to_grh_ratio: float
    asymptotic_gap_factor: float


def ord10(q: int) -> int:
    if math.gcd(q, 10) != 1:
        raise ValueError("q must be coprime to 10")
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


def prime_log_square_sum(depth: int) -> float:
    return sum(math.log(p) ** 2 for p in primes_in_window(depth))


def quotient_large_sieve_row(q: int, depth: int) -> QuotientLargeSieveRow:
    d = ord10(q)
    i = (q - 1) // d
    nc = i - 1
    n = 10**depth
    s2 = prime_log_square_sum(depth)
    standard = (n + q**2) * s2
    quotient = ((n / i) + i) * s2 / d
    improvement = standard / quotient
    grh_packet = max(nc, 1) * n * math.log(n) ** 4
    quotient_to_grh = quotient / grh_packet
    asymptotic_gap = n / max((q - 1) * max(nc, 1) * math.log(n) ** 2, 1.0)
    return QuotientLargeSieveRow(
        q=q,
        depth=depth,
        orbit_size=d,
        quotient_index=i,
        noncancelling_count=nc,
        window_size=n,
        prime_log_square_sum=s2,
        standard_bound=standard,
        quotient_candidate_bound=quotient,
        improvement_factor=improvement,
        grh_packet_scale=grh_packet,
        quotient_to_grh_ratio=quotient_to_grh,
        asymptotic_gap_factor=asymptotic_gap,
    )


def quotient_large_sieve_rows(qs: Iterable[int] = (11, 13, 37), depths: Iterable[int] = (3, 4, 5)) -> Tuple[QuotientLargeSieveRow, ...]:
    return tuple(quotient_large_sieve_row(q, depth) for q in qs for depth in depths)


def run_checks() -> Tuple[QuotientLargeSieveRow, ...]:
    rows = quotient_large_sieve_rows()
    by_qd = {(row.q, row.depth): row for row in rows}
    assert by_qd[(11, 5)].improvement_factor > 9.0
    assert by_qd[(13, 5)].improvement_factor > 11.0
    assert by_qd[(37, 5)].improvement_factor > 35.0
    assert by_qd[(11, 5)].quotient_to_grh_ratio > 1.0
    assert by_qd[(13, 5)].quotient_to_grh_ratio > 1.0
    assert by_qd[(37, 5)].quotient_to_grh_ratio > 1.0
    assert quotient_large_sieve_row(37, 10).asymptotic_gap_factor > quotient_large_sieve_row(37, 5).asymptotic_gap_factor
    return rows


if __name__ == "__main__":
    for row in run_checks():
        print(row)
