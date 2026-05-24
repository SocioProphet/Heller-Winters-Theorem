#!/usr/bin/env python3
"""Non-cancelling character fraction diagnostics for the Prime-Weil lane.

This tool verifies two finite facts:

1. Local theorem for prime p: non-cancelling local characters for the base-10
   orbit <10> in (Z/pZ)^x have count (p-1)/ord_p(10)-1.
2. Primorial diagonal theorem: non-cancelling characters for the simultaneous
   diagonal base-10 orbit in G_P have count phi(P)/lcm_p ord_p(10)-1.

It is finite arithmetic. It does not prove RH, GRH, Artin's conjecture, or an
unconditional variance bound.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from functools import reduce
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
    value = 1
    for k in range(1, p):
        value = (value * 10) % p
        if value == 1:
            return k
    raise RuntimeError(f"order not found modulo {p}")


def local_noncancelling_count(p: int) -> int:
    order = order_mod_10(p)
    if order is None:
        return 0
    return (p - 1) // order - 1


def phi_of_primes(primes: Iterable[int]) -> int:
    result = 1
    for p in primes:
        result *= p - 1
    return result


def lcm_orders(primes: Iterable[int]) -> int:
    result = 1
    for p in primes:
        order = order_mod_10(p)
        if order is not None:
            result = math.lcm(result, order)
    return result


def primorial_diagonal_noncancelling_count(primes: Iterable[int]) -> int:
    ps = tuple(primes)
    return phi_of_primes(ps) // lcm_orders(ps) - 1


@dataclass(frozen=True)
class NonCancellingRow:
    p: int
    order: int | None
    local_noncancelling: int
    phi_prefix: int
    resonant_lcm: int
    diagonal_noncancelling: int
    diagonal_fraction: float


def noncancelling_rows(limit: int = 37) -> Tuple[NonCancellingRow, ...]:
    rows = []
    prefix = []
    for p in primes_up_to(limit):
        prefix.append(p)
        phi_prefix = phi_of_primes(prefix)
        lcm = lcm_orders(prefix)
        diagonal = primorial_diagonal_noncancelling_count(prefix)
        fraction = diagonal / (phi_prefix - 1) if phi_prefix > 1 else 0.0
        rows.append(
            NonCancellingRow(
                p=p,
                order=order_mod_10(p),
                local_noncancelling=local_noncancelling_count(p),
                phi_prefix=phi_prefix,
                resonant_lcm=lcm,
                diagonal_noncancelling=diagonal,
                diagonal_fraction=fraction,
            )
        )
    return tuple(rows)


def run_checks() -> Tuple[NonCancellingRow, ...]:
    rows = noncancelling_rows(37)
    by_p = {row.p: row for row in rows}
    expected_local = {
        2: 0,
        3: 1,
        5: 0,
        7: 0,
        11: 4,
        13: 1,
        17: 0,
        19: 0,
        23: 0,
        29: 0,
        31: 1,
        37: 11,
    }
    for p, expected in expected_local.items():
        if by_p[p].local_noncancelling != expected:
            raise AssertionError((p, by_p[p], expected))
    expected_diagonal = {
        7: 7,
        11: 79,
        13: 959,
        17: 1919,
        19: 11519,
        23: 23039,
        29: 92159,
        31: 552959,
        37: 19906559,
    }
    for p, expected in expected_diagonal.items():
        if by_p[p].diagonal_noncancelling != expected:
            raise AssertionError((p, by_p[p], expected))
    if any(row.diagonal_noncancelling == 673 for row in rows):
        raise AssertionError("673 is not produced by the verified prefix table through p<=37")
    return rows


def main() -> None:
    print("Non-cancelling character fraction diagnostics")
    for row in run_checks():
        print(
            f"p={row.p} ord={row.order} local_nc={row.local_noncancelling} "
            f"phi_prefix={row.phi_prefix} lcm={row.resonant_lcm} "
            f"diag_nc={row.diagonal_noncancelling} fraction={row.diagonal_fraction:.12g}"
        )


if __name__ == "__main__":
    main()
