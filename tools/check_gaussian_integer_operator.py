#!/usr/bin/env python3
"""Gaussian-integer finite character-operator diagnostic for P(7)=210.

This diagnostic lifts split rational primes q=a^2+b^2 into unit Gaussian
phases (a+i b)/sqrt(q), aggregates those phases by residue class modulo 210,
and evaluates the resulting finite character transform on G_210.

It is finite arithmetic scaffolding only. It does not prove RH, GRH, PNT,
zero-location, Hilbert-Polya theorem-grade realization, conductor equality,
or Yang-Mills mass gap.
"""

from __future__ import annotations

import cmath
import math
import sys
from pathlib import Path
from typing import Dict, Mapping, Optional, Tuple

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.check_finite_character_operator import (
    ALPHA,
    BETA,
    GAMMA,
    MODULUS,
    PRIME_CUTOFF,
    build_dlog_table,
    character_value,
    eigenvalue_for_character,
    raw_prime_residue_kernel,
    reduced_residues,
)

PHI_111_INDEX = (1, 1, 1)


def _is_prime(n: int) -> bool:
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


def gaussian_integer_for_prime(prime: int) -> Optional[Tuple[int, int]]:
    """Return canonical a,b>=0 with a^2+b^2=prime for split primes."""

    if prime == 2:
        return (1, 1)
    if prime % 4 != 1:
        return None
    limit = math.isqrt(prime)
    for a in range(1, limit + 1):
        b2 = prime - a * a
        b = math.isqrt(b2)
        if b * b == b2:
            return (max(a, b), min(a, b))
    return None


def gaussian_phase(a: int, b: int) -> complex:
    norm = math.sqrt(a * a + b * b)
    return complex(a / norm, b / norm)


def gaussian_integer_kernel(cutoff: int = PRIME_CUTOFF, modulus: int = MODULUS) -> Dict[int, complex]:
    """Aggregate log(q)*(a+i b)/sqrt(q) by q mod modulus for split primes."""

    kernel = {h: 0j for h in reduced_residues(modulus)}
    raw = raw_prime_residue_kernel(cutoff, modulus)
    for q in range(2, cutoff + 1):
        if not _is_prime(q):
            continue
        residue = q % modulus
        if math.gcd(residue, modulus) != 1:
            continue
        pair = gaussian_integer_for_prime(q)
        if pair is None:
            continue
        a, b = pair
        kernel[residue] += math.log(q) * gaussian_phase(a, b)
    if set(kernel) != set(raw):
        raise AssertionError("gaussian kernel support diverged from raw residue support")
    return kernel


def gaussian_eigenvalue(index, kernel: Mapping[int, complex], dlog_table) -> complex:
    return eigenvalue_for_character(index, kernel, dlog_table)


def combined_generator(modulus: int = MODULUS) -> int:
    return (ALPHA * BETA * GAMMA) % modulus


def zeta2() -> complex:
    return -1 + 0j


def zeta4() -> complex:
    return 1j


def zeta6() -> complex:
    return cmath.exp(1j * math.pi / 3)


def chi_111_at_combined_generator() -> complex:
    dlog_table = build_dlog_table()
    return character_value(PHI_111_INDEX, combined_generator(), dlog_table)


def chi_111_zeta_product() -> complex:
    return zeta2() * zeta4() * zeta6()


def su2_j_half_casimir() -> float:
    j = 0.5
    return j * (j + 1.0)


def catalan_singularity_from_j_half() -> float:
    j = 0.5
    return 1.0 / (2.0 * (2.0 * j + 1.0))


def base_imaginary_half() -> complex:
    return 1.0 / (2.0 * 1j)


def run_checks():
    dlog_table = build_dlog_table()
    kernel = gaussian_integer_kernel(PRIME_CUTOFF, MODULUS)
    eigenvalue = gaussian_eigenvalue(PHI_111_INDEX, kernel, dlog_table)

    if len(kernel) != 48:
        raise AssertionError("expected 48 residue slots for G_210")
    if abs(chi_111_at_combined_generator() - chi_111_zeta_product()) > 1e-12:
        raise AssertionError("chi_111(g*) must equal zeta2*zeta4*zeta6")
    if abs(chi_111_at_combined_generator().imag + 0.5) > 1e-12:
        raise AssertionError("Im chi_111(g*) must be -1/2")
    if abs(abs(chi_111_at_combined_generator()) ** 2 - 1.0) > 1e-12:
        raise AssertionError("character value must have unit norm")
    spin_component = chi_111_at_combined_generator().imag
    if abs(spin_component * spin_component + 0.5 - su2_j_half_casimir()) > 1e-12:
        raise AssertionError("spin-component Casimir relation failed")
    if abs(catalan_singularity_from_j_half() - 0.25) > 1e-12:
        raise AssertionError("j=1/2 Catalan singularity relation failed")
    if abs(base_imaginary_half() ** 2 + catalan_singularity_from_j_half()) > 1e-12:
        raise AssertionError("(1/(2i))^2 = -rho_2 relation failed")

    return eigenvalue


def main() -> None:
    eigenvalue = run_checks()
    chi = chi_111_at_combined_generator()
    print("gaussian integer character operator checks passed")
    print(f"modulus: {MODULUS}")
    print(f"prime cutoff: {PRIME_CUTOFF}")
    print(f"combined generator g*: {combined_generator()}")
    print(f"chi_111(g*): {chi.real:.12f}{chi.imag:+.12f}i")
    print(f"Im chi_111(g*): {chi.imag:.12f}")
    print(f"j=1/2 Casimir: {su2_j_half_casimir():.12f}")
    print(f"Catalan rho_2 from j=1/2: {catalan_singularity_from_j_half():.12f}")
    print(f"phi_111 gaussian eigenvalue: {eigenvalue.real:.12f}{eigenvalue.imag:+.12f}i")


if __name__ == "__main__":
    main()
