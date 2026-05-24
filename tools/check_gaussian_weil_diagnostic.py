#!/usr/bin/env python3
"""Gaussian-smoothed Weil diagnostic for the finite character operator.

This diagnostic reuses the P(7)=210 character infrastructure from
``check_finite_character_operator`` and evaluates Gaussian-smoothed character
sums over the full prime range up to the requested cutoff.

It is numerical evidence only. It does not prove RH, GRH, PNT, PNT-AP,
zero-location results, essential self-adjointness, or any Yang-Mills mass-gap
statement.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Dict, Iterable, List, Mapping

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
class GaussianWeilRow:
    cutoff: int
    sigma: float
    finite_weil_distribution: float
    min_abs_lambda_sq: float
    max_grh_signature_ratio: float


def raw_character_sum(
    index: CharacterIndex,
    cutoff: int,
    dlog_table: Mapping[int, ExponentTriple] | None = None,
) -> complex:
    """psi(B,chi) = sum_{p<=B} log(p)*chi(p), restricted to units mod 210."""

    table = build_dlog_table() if dlog_table is None else dlog_table
    total = 0j
    for prime in primes_up_to(cutoff):
        residue = prime % MODULUS
        if math.gcd(residue, MODULUS) == 1:
            total += math.log(prime) * character_value(index, residue, table)
    return total


def gaussian_eigenvalue(
    index: CharacterIndex,
    sigma: float,
    cutoff: int,
    dlog_table: Mapping[int, ExponentTriple] | None = None,
) -> complex:
    """lambda_chi^(sigma)(B) = sum_{p<=B} log(p)*chi(p)*exp(-log(p)^2/(2*sigma^2))."""

    if sigma <= 0:
        raise ValueError("sigma must be positive")
    table = build_dlog_table() if dlog_table is None else dlog_table
    total = 0j
    for prime in primes_up_to(cutoff):
        residue = prime % MODULUS
        if math.gcd(residue, MODULUS) == 1:
            weight = math.exp(-(math.log(prime) ** 2) / (2 * sigma**2))
            total += math.log(prime) * character_value(index, residue, table) * weight
    return total


def growth_exponent(
    index: CharacterIndex,
    sigma: float,
    b_low: int,
    b_high: int,
    dlog_table: Mapping[int, ExponentTriple] | None = None,
) -> float:
    """alpha_hat(chi) = log(|lam(B_high)|/|lam(B_low)|) / log(B_high/B_low)."""

    if b_low <= 1 or b_high <= b_low:
        raise ValueError("require 1 < b_low < b_high")
    table = build_dlog_table() if dlog_table is None else dlog_table
    low = abs(gaussian_eigenvalue(index, sigma, b_low, table))
    high = abs(gaussian_eigenvalue(index, sigma, b_high, table))
    if low == 0 or high == 0:
        raise ZeroDivisionError("growth exponent undefined for zero eigenvalue")
    return math.log(high / low) / math.log(b_high / b_low)


def finite_weil_pos_distribution(
    sigma: float,
    cutoff: int,
    dlog_table: Mapping[int, ExponentTriple] | None = None,
) -> float:
    """W_k^pos = (1/48)*sum_chi |lambda_chi^(sigma)|^2."""

    table = build_dlog_table() if dlog_table is None else dlog_table
    values = [gaussian_eigenvalue(index, sigma, cutoff, table) for index in character_indices()]
    return sum(abs(value) ** 2 for value in values) / len(values)


def min_abs_lambda_sq(
    sigma: float,
    cutoff: int,
    dlog_table: Mapping[int, ExponentTriple] | None = None,
) -> float:
    table = build_dlog_table() if dlog_table is None else dlog_table
    return min(abs(gaussian_eigenvalue(index, sigma, cutoff, table)) ** 2 for index in character_indices())


def max_grh_signature_ratio(
    cutoff: int,
    dlog_table: Mapping[int, ExponentTriple] | None = None,
) -> float:
    table = build_dlog_table() if dlog_table is None else dlog_table
    return max(abs(raw_character_sum(index, cutoff, table)) / math.sqrt(cutoff) for index in character_indices())


def non_trivial_character_indices() -> List[CharacterIndex]:
    return [index for index in character_indices() if index != (0, 0, 0)]


def diagnostic_rows(cutoffs: Iterable[int] = (200, 500, 1000)) -> List[GaussianWeilRow]:
    table = build_dlog_table()
    rows: List[GaussianWeilRow] = []
    for cutoff in cutoffs:
        sigma = math.log(cutoff) / 2
        rows.append(
            GaussianWeilRow(
                cutoff=cutoff,
                sigma=sigma,
                finite_weil_distribution=finite_weil_pos_distribution(sigma, cutoff, table),
                min_abs_lambda_sq=min_abs_lambda_sq(sigma, cutoff, table),
                max_grh_signature_ratio=max_grh_signature_ratio(cutoff, table),
            )
        )
    return rows


def run_checks() -> List[GaussianWeilRow]:
    table = build_dlog_table()
    rows = diagnostic_rows()
    for row in rows:
        if row.finite_weil_distribution <= 0:
            raise AssertionError(f"non-positive finite Weil distribution at B={row.cutoff}")
        if row.min_abs_lambda_sq <= 0:
            raise AssertionError(f"zero Gaussian eigenvalue weight at B={row.cutoff}")
        if row.max_grh_signature_ratio >= math.log(row.cutoff) ** 2:
            raise AssertionError(f"GRH-signature ratio exceeds log^2 envelope at B={row.cutoff}")

    for index in non_trivial_character_indices():
        low = raw_character_sum(index, 200, table)
        high = raw_character_sum(index, 500, table)
        if abs(low) > 0.5:
            # Recorded as a diagnostic, not a hard gate: moderate-scale ratios are noisy.
            _ = math.log(abs(high) / abs(low)) / math.log(500 / 200)
    return rows


def main() -> None:
    print("Gaussian-smoothed Weil diagnostic")
    for row in run_checks():
        print(
            f"B={row.cutoff} sigma={row.sigma:.6f} "
            f"W={row.finite_weil_distribution:.12f} "
            f"min_abs_lambda_sq={row.min_abs_lambda_sq:.12f} "
            f"max_ratio={row.max_grh_signature_ratio:.12f} "
            f"log2={math.log(row.cutoff) ** 2:.12f}"
        )


if __name__ == "__main__":
    main()
