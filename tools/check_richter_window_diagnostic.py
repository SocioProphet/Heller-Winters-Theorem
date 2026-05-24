#!/usr/bin/env python3
"""Richter-window diagnostic for finite character sums.

The diagnostic evaluates decimal digit-depth windows W_k=[10^(k-1),10^k)
for the 48-character family of (Z/210Z)^x and reports per-window growth
statistics tied to the Richter refinement of HW-PRIME-WEIL-001.

It is numerical evidence only. It does not prove RH, GRH, PNT, PNT-AP,
zero-location results, essential self-adjointness, or any Yang-Mills mass-gap
statement.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Iterable, List, Mapping

from tools.check_finite_character_operator import (
    MODULUS,
    CharacterIndex,
    ExponentTriple,
    build_dlog_table,
    character_indices,
    character_value,
    primes_up_to,
)


@dataclass(frozen=True)
class RichterWindowRow:
    depth: int
    prime_count: int
    active_prime_count: int
    max_window_sum: float
    grh_scale: float
    ratio: float
    max_richter_exponent: float | None
    mean_normalized_square: float


def primes_in_window(depth: int) -> List[int]:
    if depth < 1:
        raise ValueError("depth must be positive")
    low = 10 ** (depth - 1)
    high = 10**depth
    return [p for p in primes_up_to(high - 1) if low <= p < high]


def active_primes_in_window(depth: int) -> List[int]:
    return [p for p in primes_in_window(depth) if math.gcd(p % MODULUS, MODULUS) == 1]


def window_character_sum(
    index: CharacterIndex,
    depth: int,
    dlog_table: Mapping[int, ExponentTriple] | None = None,
) -> complex:
    """psi_{W_k}(chi)=sum_{p in W_k, p mod P in G_P} log(p)*chi(p)."""

    table = build_dlog_table() if dlog_table is None else dlog_table
    total = 0j
    for prime in active_primes_in_window(depth):
        total += math.log(prime) * character_value(index, prime % MODULUS, table)
    return total


def richter_exponent(
    index: CharacterIndex,
    depth: int,
    dlog_table: Mapping[int, ExponentTriple] | None = None,
) -> float | None:
    value = abs(window_character_sum(index, depth, dlog_table))
    if value == 0:
        return None
    return math.log(value) / math.log(math.sqrt(10**depth))


def normalized_window_square(
    index: CharacterIndex,
    depth: int,
    dlog_table: Mapping[int, ExponentTriple] | None = None,
) -> float:
    value = abs(window_character_sum(index, depth, dlog_table))
    return (value**2) / ((10**depth) * (depth**2))


def richter_weil_distribution(
    k_max: int,
    dlog_table: Mapping[int, ExponentTriple] | None = None,
) -> float:
    table = build_dlog_table() if dlog_table is None else dlog_table
    total = 0.0
    for depth in range(1, k_max + 1):
        for index in character_indices():
            total += normalized_window_square(index, depth, table)
    return total / len(character_indices())


def richter_window_row(depth: int, dlog_table: Mapping[int, ExponentTriple] | None = None) -> RichterWindowRow:
    table = build_dlog_table() if dlog_table is None else dlog_table
    values = [abs(window_character_sum(index, depth, table)) for index in character_indices()]
    nonzero_exponents = [
        exponent for index in character_indices() if (exponent := richter_exponent(index, depth, table)) is not None
    ]
    scale = depth * math.sqrt(10**depth)
    max_value = max(values)
    return RichterWindowRow(
        depth=depth,
        prime_count=len(primes_in_window(depth)),
        active_prime_count=len(active_primes_in_window(depth)),
        max_window_sum=max_value,
        grh_scale=scale,
        ratio=max_value / scale if scale else 0.0,
        max_richter_exponent=max(nonzero_exponents) if nonzero_exponents else None,
        mean_normalized_square=sum(normalized_window_square(index, depth, table) for index in character_indices())
        / len(character_indices()),
    )


def diagnostic_rows(depths: Iterable[int] = (1, 2, 3, 4, 5)) -> List[RichterWindowRow]:
    table = build_dlog_table()
    return [richter_window_row(depth, table) for depth in depths]


def run_checks() -> List[RichterWindowRow]:
    rows = diagnostic_rows()
    for row in rows:
        if row.depth == 1:
            if row.active_prime_count != 0:
                raise AssertionError("depth-1 window should have no active primes for modulus 210")
            continue
        if row.active_prime_count <= 0:
            raise AssertionError(f"no active primes at depth {row.depth}")
        if row.max_window_sum <= 0:
            raise AssertionError(f"zero max window sum at depth {row.depth}")
        if row.mean_normalized_square <= 0:
            raise AssertionError(f"non-positive mean normalized square at depth {row.depth}")
    if richter_weil_distribution(3) <= 0:
        raise AssertionError("Richter Weil distribution must be positive at k=3")
    return rows


def main() -> None:
    print("Richter-window diagnostic for (Z/210Z)^x")
    for row in run_checks():
        exponent = "N/A" if row.max_richter_exponent is None else f"{row.max_richter_exponent:.6f}"
        print(
            f"k={row.depth} primes={row.prime_count} active={row.active_prime_count} "
            f"max_sum={row.max_window_sum:.12f} scale={row.grh_scale:.12f} "
            f"ratio={row.ratio:.12f} max_exp={exponent} "
            f"mean_norm_sq={row.mean_normalized_square:.12f}"
        )


if __name__ == "__main__":
    main()
