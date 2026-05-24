#!/usr/bin/env python3
"""Equidistribution decomposition diagnostic for the Richter-window lane.

This tool verifies the exact decomposition

    psi_{W_K}(chi_7) = sum_r chi_7(r) * epsilon_K(r)

for the primitive mod-7 component and reports the finite barrier diagnostics used
by HW-PRIME-WEIL-006.

It is a finite arithmetic diagnostic. It does not prove RH, GRH, a windowed
Omega theorem, or an unconditional variance bound.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass
from functools import lru_cache
from typing import Dict, Iterable, List, Tuple

from tools.check_finite_character_operator import (
    MODULUS,
    CharacterIndex,
    build_dlog_table,
    character_indices,
    character_value,
)

MOD7_GENERATOR = 3
CHI7_EXPONENT = 1


@dataclass(frozen=True)
class EquidistributionRow:
    depth: int
    prime_count: int
    max_epsilon: float
    psi_chi7_abs: float
    psi_over_sqrt: float
    grh_envelope: float
    grh_ratio: float
    oracle_bound: float | None
    oracle_ratio: float | None


@lru_cache(maxsize=None)
def primes_up_to_sieve(limit: int) -> Tuple[int, ...]:
    if limit < 2:
        return tuple()
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    root = int(limit**0.5)
    for p in range(2, root + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    return tuple(i for i in range(limit + 1) if sieve[i])


@lru_cache(maxsize=None)
def primes_in_window(depth: int) -> Tuple[int, ...]:
    if depth < 1:
        raise ValueError("depth must be positive")
    low = 10 ** (depth - 1)
    high = 10**depth
    return tuple(p for p in primes_up_to_sieve(high - 1) if low <= p < high)


@lru_cache(maxsize=None)
def mod7_dlog() -> Dict[int, int]:
    table: Dict[int, int] = {}
    value = 1
    for exponent in range(6):
        table[value] = exponent
        value = (value * MOD7_GENERATOR) % 7
    if set(table) != {1, 2, 3, 4, 5, 6}:
        raise RuntimeError("3 should generate (Z/7Z)^x")
    return table


def chi7(exponent: int, residue: int) -> complex:
    """Primitive mod-7 character with chi(3)=exp(2*pi*i*exponent/6)."""

    r = residue % 7
    if math.gcd(r, 7) != 1:
        return 0j
    return cmath.exp(2j * math.pi * exponent * mod7_dlog()[r] / 6)


def residue_masses_mod7(depth: int) -> Dict[int, float]:
    masses = {r: 0.0 for r in range(1, 7)}
    for prime in primes_in_window(depth):
        residue = prime % 7
        if residue:
            masses[residue] += math.log(prime)
    return masses


def epsilon(residue: int, depth: int) -> float:
    masses = residue_masses_mod7(depth)
    mean = sum(masses.values()) / 6.0
    return masses[residue] - mean


def psi_chi7(depth: int, exponent: int = CHI7_EXPONENT) -> complex:
    return sum(math.log(prime) * chi7(exponent, prime) for prime in primes_in_window(depth) if prime % 7)


def psi_chi7_via_epsilon(depth: int, exponent: int = CHI7_EXPONENT) -> complex:
    return sum(chi7(exponent, residue) * epsilon(residue, depth) for residue in range(1, 7))


def max_epsilon(depth: int) -> float:
    return max(abs(epsilon(residue, depth)) for residue in range(1, 7))


def grh_envelope(depth: int) -> float:
    return math.log(10**depth) ** 2


def oracle_bound_at_resonant_depth(depth: int = 6) -> float:
    prime_count = len(primes_in_window(depth))
    return 2.0 * math.log(10**depth) * math.sqrt(prime_count / 6.0)


def digit_cycle_sum(exponent: int = CHI7_EXPONENT) -> complex:
    return sum(chi7(exponent, pow(10, j, 7)) for j in range(1, 7))


def digit_cycle_partial_sums(exponent: int = CHI7_EXPONENT) -> Tuple[complex, ...]:
    total = 0j
    partials: List[complex] = []
    for j in range(1, 7):
        total += chi7(exponent, pow(10, j, 7))
        partials.append(total)
    return tuple(partials)


def max_digit_cycle_partial_sum(exponent: int = CHI7_EXPONENT) -> float:
    return max(abs(value) for value in digit_cycle_partial_sums(exponent))


def psi_for_g210_character(depth: int, index: CharacterIndex) -> complex:
    dlog_table = build_dlog_table()
    total = 0j
    for prime in primes_in_window(depth):
        residue = prime % MODULUS
        if math.gcd(residue, MODULUS) == 1:
            total += math.log(prime) * character_value(index, residue, dlog_table)
    return total


def compute_variance_by_prime(depth: int) -> Tuple[float, float]:
    """Return the p=7 packet energy and total nontrivial character energy.

    The p=7 packet is the sum over all G_210 characters with nontrivial mod-7
    coordinate. This is the quantity that empirically dominates the finite
    variance in the current diagnostic windows.
    """

    total = 0.0
    p7_packet = 0.0
    for index in character_indices():
        if index == (0, 0, 0):
            continue
        energy = abs(psi_for_g210_character(depth, index)) ** 2
        total += energy
        if index[2] != 0:
            p7_packet += energy
    return p7_packet, total


def equidistribution_row(depth: int) -> EquidistributionRow:
    psi_abs = abs(psi_chi7(depth))
    sqrt_scale = math.sqrt(10**depth)
    psi_over_sqrt = psi_abs / sqrt_scale
    envelope = grh_envelope(depth)
    oracle = oracle_bound_at_resonant_depth(depth) if depth == 6 else None
    return EquidistributionRow(
        depth=depth,
        prime_count=len(primes_in_window(depth)),
        max_epsilon=max_epsilon(depth),
        psi_chi7_abs=psi_abs,
        psi_over_sqrt=psi_over_sqrt,
        grh_envelope=envelope,
        grh_ratio=psi_over_sqrt / envelope,
        oracle_bound=oracle,
        oracle_ratio=psi_abs / oracle if oracle else None,
    )


def diagnostic_rows(depths: Iterable[int] = (2, 3, 4, 5, 6)) -> Tuple[EquidistributionRow, ...]:
    return tuple(equidistribution_row(depth) for depth in depths)


def run_checks() -> Tuple[EquidistributionRow, ...]:
    rows = diagnostic_rows()
    for depth in (2, 3, 4, 5, 6):
        direct = psi_chi7(depth)
        via_eps = psi_chi7_via_epsilon(depth)
        if abs(direct - via_eps) > 1e-8:
            raise AssertionError((depth, direct, via_eps))
        if abs(direct) > 6.0 * max_epsilon(depth) + 1e-8:
            raise AssertionError(f"triangle bound failed at depth {depth}")
        if abs(direct) / math.sqrt(10**depth) >= grh_envelope(depth):
            raise AssertionError(f"finite diagnostic exceeded GRH-shaped envelope at depth {depth}")
    if abs(digit_cycle_sum()) > 1e-12:
        raise AssertionError("digit-cycle sum should vanish")
    if max_digit_cycle_partial_sum() > 2.001:
        raise AssertionError("digit-cycle partial-sum bound failed")
    if abs(psi_chi7(6)) > oracle_bound_at_resonant_depth(6):
        raise AssertionError("resonant-depth oracle bound failed")
    for depth in (2, 3):
        p7_packet, total = compute_variance_by_prime(depth)
        if total <= 0 or p7_packet / total <= 0.85:
            raise AssertionError(f"p=7 packet did not dominate at depth {depth}")
    return rows


def main() -> None:
    print("Equidistribution decomposition diagnostic for chi_7")
    for row in run_checks():
        oracle = "N/A" if row.oracle_bound is None else f"{row.oracle_bound:.12f}"
        oracle_ratio = "N/A" if row.oracle_ratio is None else f"{row.oracle_ratio:.12f}"
        p7_packet, total = compute_variance_by_prime(row.depth)
        print(
            f"K={row.depth} primes={row.prime_count} psi={row.psi_chi7_abs:.12f} "
            f"max_eps={row.max_epsilon:.12f} psi/sqrt={row.psi_over_sqrt:.12f} "
            f"grh_env={row.grh_envelope:.12f} ratio={row.grh_ratio:.12f} "
            f"p7_share={p7_packet / total:.12f} oracle={oracle} oracle_ratio={oracle_ratio}"
        )
    print(f"digit-cycle sum: {digit_cycle_sum():.12g}")
    print(f"max digit-cycle partial sum: {max_digit_cycle_partial_sum():.12f}")


if __name__ == "__main__":
    main()
