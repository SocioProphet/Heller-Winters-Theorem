#!/usr/bin/env python3
"""Antisymmetric finite character-operator diagnostic for P(7)=210.

Computes K^-(h) = (A(h) - A(h^{-1})) / 2 — the antisymmetric prime-residue
kernel. The raw convolution by K^- is skew-Hermitian; the diagnostic
self-adjoint operator is -i times that convolution and has real spectrum
symmetric about 0.

This is a finite arithmetic diagnostic only. Does not prove RH, GRH, PNT,
zero-location, or Yang-Mills mass gap.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, Iterable, Mapping

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.check_finite_character_operator import (
    MODULUS,
    PRIME_CUTOFF,
    TOLERANCE,
    build_dlog_table,
    character_indices,
    eigenvalue_for_character,
    inversion_symmetric_kernel,
    raw_prime_residue_kernel,
    reduced_residues,
    spectrum_summary,
)


def antisymmetric_kernel(cutoff: int = PRIME_CUTOFF, modulus: int = MODULUS) -> Dict[int, float]:
    """Return K^-(h)=(A(h)-A(h^-1))/2 for the prime-residue kernel A."""

    raw = raw_prime_residue_kernel(cutoff, modulus)
    return {h: 0.5 * (raw[h] - raw[pow(h, -1, modulus)]) for h in reduced_residues(modulus)}


def kernel_is_antisymmetric(
    kernel: Mapping[int, float],
    modulus: int = MODULUS,
    tol: float = TOLERANCE,
) -> bool:
    """Check K(h)+K(h^-1)=0 on every unit residue."""

    return all(abs(kernel[h] + kernel[pow(h, -1, modulus)]) <= tol for h in kernel)


def raw_antisymmetric_eigenvalue(index, kernel, dlog_table) -> complex:
    """Eigenvalue of raw convolution by K^-; skew-Hermitian, hence imaginary."""

    return eigenvalue_for_character(index, kernel, dlog_table)


def self_adjoint_antisymmetric_eigenvalue(index, kernel, dlog_table) -> complex:
    """Eigenvalue of -i times raw antisymmetric convolution; real diagnostic."""

    return -1j * raw_antisymmetric_eigenvalue(index, kernel, dlog_table)


def self_adjoint_antisymmetric_eigenvalues(
    kernel: Mapping[int, float],
    dlog_table,
) -> list[complex]:
    return [
        self_adjoint_antisymmetric_eigenvalue(index, kernel, dlog_table)
        for index in character_indices()
    ]


def spectrum_is_symmetric_about_zero(values: Iterable[complex], tolerance: float = 1e-6) -> bool:
    vals = list(values)
    remaining = vals.copy()
    for value in vals:
        match_index = None
        for idx, candidate in enumerate(remaining):
            if abs(candidate + value) <= tolerance:
                match_index = idx
                break
        if match_index is None:
            return False
        remaining.pop(match_index)
    return True


def run_checks():
    dlog_table = build_dlog_table()
    kernel = antisymmetric_kernel(PRIME_CUTOFF, MODULUS)

    if not kernel_is_antisymmetric(kernel, MODULUS, TOLERANCE):
        raise AssertionError("kernel is not inversion-antisymmetric")

    raw_values = [
        raw_antisymmetric_eigenvalue(index, kernel, dlog_table)
        for index in character_indices()
    ]
    if len(raw_values) != 48:
        raise AssertionError("expected 48 raw antisymmetric eigenvalues")
    if max(abs(value.real) for value in raw_values) > 1e-8:
        raise AssertionError("raw antisymmetric convolution spectrum is not imaginary")

    values = self_adjoint_antisymmetric_eigenvalues(kernel, dlog_table)
    summary = spectrum_summary(values)

    if summary.eigenvalue_count != 48:
        raise AssertionError("expected 48 self-adjoint antisymmetric eigenvalues")
    if summary.max_abs_imag > 1e-8:
        raise AssertionError(f"self-adjoint diagnostic eigenvalues not real: {summary.max_abs_imag}")
    if not spectrum_is_symmetric_about_zero(values, tolerance=1e-6):
        raise AssertionError("self-adjoint antisymmetric spectrum is not symmetric about 0")

    return summary


def main() -> None:
    summary = run_checks()
    print("antisymmetric finite character operator checks passed")
    print(f"modulus: {MODULUS}")
    print(f"prime cutoff: {PRIME_CUTOFF}")
    print("kernel condition: K^-(h) + K^-(h^-1) = 0")
    print("diagnostic operator: -i times raw antisymmetric convolution")
    print(f"eigenvalue count: {summary.eigenvalue_count}")
    print(f"min eigenvalue real part: {summary.min_real:.12f}")
    print(f"max eigenvalue real part: {summary.max_real:.12f}")
    print(f"max absolute imaginary part: {summary.max_abs_imag:.3e}")
    print("symmetric-spectrum confirmation: passed")


if __name__ == "__main__":
    main()
