#!/usr/bin/env python3
from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Iterable, Tuple


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


def primes_up_to(limit: int) -> Tuple[int, ...]:
    return tuple(n for n in range(2, limit + 1) if is_prime(n))


def order_mod_10(p: int) -> int | None:
    if math.gcd(10, p) != 1:
        return None
    x = 1
    for k in range(1, p):
        x = (x * 10) % p
        if x == 1:
            return k
    raise RuntimeError(p)


def local_noncancelling_count(p: int) -> int:
    order = order_mod_10(p)
    return 0 if order is None else (p - 1) // order - 1


def phi_of_primes(primes: Iterable[int]) -> int:
    out = 1
    for p in primes:
        out *= p - 1
    return out


def cumulative_noncancelling_count(primes: Iterable[int]) -> int:
    total = 0
    phi_prev = 1
    for p in primes:
        total += phi_prev * local_noncancelling_count(p)
        phi_prev *= p - 1
    return total


@dataclass(frozen=True)
class NonCancellingRow:
    p: int
    order: int | None
    local_noncancelling: int
    phi_previous: int
    contribution: int
    phi_prefix: int
    cumulative_noncancelling: int
    cumulative_fraction: float


def noncancelling_rows(limit: int = 37) -> Tuple[NonCancellingRow, ...]:
    rows = []
    phi_prev = 1
    cumulative = 0
    for p in primes_up_to(limit):
        local = local_noncancelling_count(p)
        contribution = phi_prev * local
        cumulative += contribution
        phi_prefix = phi_prev * (p - 1)
        rows.append(
            NonCancellingRow(
                p=p,
                order=order_mod_10(p),
                local_noncancelling=local,
                phi_previous=phi_prev,
                contribution=contribution,
                phi_prefix=phi_prefix,
                cumulative_noncancelling=cumulative,
                cumulative_fraction=cumulative / (phi_prefix - 1) if phi_prefix > 1 else 0.0,
            )
        )
        phi_prev = phi_prefix
    return tuple(rows)


def run_checks() -> Tuple[NonCancellingRow, ...]:
    rows = noncancelling_rows(37)
    by_p = {row.p: row for row in rows}
    expected_local = {2: 0, 3: 1, 5: 0, 7: 0, 11: 4, 13: 1, 17: 0, 19: 0, 23: 0, 29: 0, 31: 1, 37: 11}
    for p, expected in expected_local.items():
        assert by_p[p].local_noncancelling == expected, (p, by_p[p], expected)
    expected_cumulative = {7: 1, 11: 193, 13: 673, 17: 673, 19: 673, 23: 673, 29: 673, 31: 1_021_870_753, 37: 338_238_997_153}
    for p, expected in expected_cumulative.items():
        assert by_p[p].cumulative_noncancelling == expected, (p, by_p[p], expected)
    assert by_p[29].cumulative_noncancelling == 673
    assert by_p[31].cumulative_noncancelling > 1_000_000_000
    assert by_p[37].cumulative_noncancelling > 300_000_000_000
    return rows


def main() -> None:
    for row in run_checks():
        print(row)


if __name__ == "__main__":
    main()
