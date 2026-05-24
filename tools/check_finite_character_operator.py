#!/usr/bin/env python3
"""Finite character-operator diagnostic for P(7)=210.

This is a finite arithmetic diagnostic only. It constructs the unit group
G_210, its CRT character coordinates, an inversion-symmetric prime-residue
kernel with cutoff B=500, and the associated convolution operator on C[G_210].

It does not prove RH, GRH, PNT, PNT-AP, zero-location results, or any
Yang-Mills mass-gap statement.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass
from functools import reduce
from typing import Dict, Iterable, List, Mapping, Sequence, Tuple

MODULUS = 210
PRIME_CUTOFF = 500
TOLERANCE = 1e-9

ALPHA = 71
BETA = 127
GAMMA = 31

ExponentTriple = Tuple[int, int, int]
CharacterIndex = Tuple[int, int, int]
ComplexVector = Dict[int, complex]


@dataclass(frozen=True)
class SpectrumSummary:
    eigenvalue_count: int
    min_real: float
    max_real: float
    max_abs_imag: float


def phi(n: int) -> int:
    return sum(1 for k in range(1, n + 1) if math.gcd(k, n) == 1)


def reduced_residues(modulus: int = MODULUS) -> List[int]:
    return [a for a in range(1, modulus) if math.gcd(a, modulus) == 1]


def crt_residue(congruences: Sequence[Tuple[int, int]], modulus: int = MODULUS) -> int:
    for candidate in range(modulus):
        if all(candidate % m == r % m for m, r in congruences):
            return candidate
    raise ValueError(f"no CRT solution modulo {modulus}: {congruences!r}")


def crt_generators() -> Tuple[int, int, int]:
    """Return the fixed CRT generators alpha, beta, gamma for G_210."""

    alpha = crt_residue([(2, 1), (3, 2), (5, 1), (7, 1)])
    beta = crt_residue([(2, 1), (3, 1), (5, 2), (7, 1)])
    gamma = crt_residue([(2, 1), (3, 1), (5, 1), (7, 3)])
    return alpha, beta, gamma


def multiplicative_order(a: int, modulus: int = MODULUS) -> int:
    if math.gcd(a, modulus) != 1:
        raise ValueError(f"{a} is not a unit modulo {modulus}")
    value = 1
    for order in range(1, phi(modulus) + 1):
        value = (value * a) % modulus
        if value == 1:
            return order
    raise ValueError(f"failed to find order for {a} modulo {modulus}")


def group_exponent(modulus: int = MODULUS) -> int:
    return reduce(math.lcm, (multiplicative_order(a, modulus) for a in reduced_residues(modulus)), 1)


def build_dlog_table(
    alpha: int = ALPHA,
    beta: int = BETA,
    gamma: int = GAMMA,
    modulus: int = MODULUS,
) -> Dict[int, ExponentTriple]:
    """Build the CRT discrete-log table for C2 x C4 x C6 coordinates."""

    table: Dict[int, ExponentTriple] = {}
    for e3 in range(2):
        for e5 in range(4):
            for e7 in range(6):
                value = (pow(alpha, e3, modulus) * pow(beta, e5, modulus) * pow(gamma, e7, modulus)) % modulus
                if value in table:
                    raise ValueError(f"duplicate CRT coordinate for residue {value}")
                table[value] = (e3, e5, e7)
    residues = set(reduced_residues(modulus))
    if set(table) != residues:
        missing = sorted(residues - set(table))
        extra = sorted(set(table) - residues)
        raise ValueError(f"CRT generators do not span G_{modulus}; missing={missing}, extra={extra}")
    return table


def character_indices() -> List[CharacterIndex]:
    return [(j, k, ell) for j in range(2) for k in range(4) for ell in range(6)]


def character_value(index: CharacterIndex, residue: int, dlog_table: Mapping[int, ExponentTriple]) -> complex:
    j, k, ell = index
    e3, e5, e7 = dlog_table[residue]
    omega_6 = cmath.exp(2j * math.pi / 6)
    return ((-1) ** (j * e3)) * ((1j) ** (k * e5)) * (omega_6 ** (ell * e7))


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True


def primes_up_to(cutoff: int) -> List[int]:
    return [n for n in range(2, cutoff + 1) if is_prime(n)]


def raw_prime_residue_kernel(cutoff: int = PRIME_CUTOFF, modulus: int = MODULUS) -> Dict[int, float]:
    """Return A(h)=sum log(q) for primes q<=cutoff with q mod modulus = h."""

    kernel = {h: 0.0 for h in reduced_residues(modulus)}
    for prime in primes_up_to(cutoff):
        residue = prime % modulus
        if math.gcd(residue, modulus) == 1:
            kernel[residue] += math.log(prime)
    return kernel


def inversion_symmetric_kernel(cutoff: int = PRIME_CUTOFF, modulus: int = MODULUS) -> Dict[int, float]:
    raw = raw_prime_residue_kernel(cutoff, modulus)
    return {h: 0.5 * (raw[h] + raw[pow(h, -1, modulus)]) for h in reduced_residues(modulus)}


def kernel_is_inversion_symmetric(kernel: Mapping[int, float], modulus: int = MODULUS, tolerance: float = TOLERANCE) -> bool:
    return all(abs(kernel[h] - kernel[pow(h, -1, modulus)]) <= tolerance for h in kernel)


def eigenvalue_for_character(
    index: CharacterIndex,
    kernel: Mapping[int, float],
    dlog_table: Mapping[int, ExponentTriple],
) -> complex:
    return sum(kernel[h] * character_value(index, h, dlog_table) for h in kernel)


def eigenvalues(
    kernel: Mapping[int, float],
    dlog_table: Mapping[int, ExponentTriple],
) -> List[complex]:
    return [eigenvalue_for_character(index, kernel, dlog_table) for index in character_indices()]


def character_vector(index: CharacterIndex, dlog_table: Mapping[int, ExponentTriple], modulus: int = MODULUS) -> ComplexVector:
    return {g: character_value(index, g, dlog_table) for g in reduced_residues(modulus)}


def convolution_action(vector: Mapping[int, complex], kernel: Mapping[int, float], modulus: int = MODULUS) -> ComplexVector:
    result: ComplexVector = {}
    for g in reduced_residues(modulus):
        result[g] = sum(kernel[h] * vector[(g * h) % modulus] for h in kernel)
    return result


def max_character_eigen_error(
    kernel: Mapping[int, float],
    dlog_table: Mapping[int, ExponentTriple],
    modulus: int = MODULUS,
) -> float:
    worst = 0.0
    for index in character_indices():
        vector = character_vector(index, dlog_table, modulus)
        image = convolution_action(vector, kernel, modulus)
        eigenvalue = eigenvalue_for_character(index, kernel, dlog_table)
        for g in reduced_residues(modulus):
            worst = max(worst, abs(image[g] - eigenvalue * vector[g]))
    return worst


def spectrum_summary(values: Iterable[complex]) -> SpectrumSummary:
    vals = list(values)
    return SpectrumSummary(
        eigenvalue_count=len(vals),
        min_real=min(v.real for v in vals),
        max_real=max(v.real for v in vals),
        max_abs_imag=max(abs(v.imag) for v in vals),
    )


def run_checks() -> SpectrumSummary:
    alpha, beta, gamma = crt_generators()
    if (alpha, beta, gamma) != (ALPHA, BETA, GAMMA):
        raise AssertionError((alpha, beta, gamma))
    if (multiplicative_order(ALPHA), multiplicative_order(BETA), multiplicative_order(GAMMA)) != (2, 4, 6):
        raise AssertionError("unexpected CRT generator orders")
    if phi(MODULUS) != 48:
        raise AssertionError("phi(210) must be 48")
    if group_exponent(MODULUS) != 12:
        raise AssertionError("exp(G_210) must be 12")

    dlog_table = build_dlog_table()
    if len(dlog_table) != 48:
        raise AssertionError("CRT discrete-log table must span 48 residues")

    kernel = inversion_symmetric_kernel(PRIME_CUTOFF, MODULUS)
    if not kernel_is_inversion_symmetric(kernel):
        raise AssertionError("kernel is not inversion-symmetric")

    values = eigenvalues(kernel, dlog_table)
    summary = spectrum_summary(values)
    if summary.eigenvalue_count != 48:
        raise AssertionError("expected 48 character eigenvalues")
    if summary.max_abs_imag > TOLERANCE:
        raise AssertionError(f"eigenvalues not real to tolerance: {summary.max_abs_imag}")

    error = max_character_eigen_error(kernel, dlog_table)
    if error > 1e-8:
        raise AssertionError(f"character diagonalization error too large: {error}")

    return summary


def main() -> None:
    summary = run_checks()
    print("finite character operator checks passed")
    print(f"modulus: {MODULUS}")
    print(f"prime cutoff: {PRIME_CUTOFF}")
    print(f"phi(210): {phi(MODULUS)}")
    print(f"exp(G_210): {group_exponent(MODULUS)}")
    print(f"CRT generators: alpha={ALPHA}, beta={BETA}, gamma={GAMMA}")
    print(f"eigenvalue count: {summary.eigenvalue_count}")
    print(f"min eigenvalue real part: {summary.min_real:.12f}")
    print(f"max eigenvalue real part: {summary.max_real:.12f}")
    print(f"max absolute imaginary part: {summary.max_abs_imag:.3e}")


if __name__ == "__main__":
    main()
