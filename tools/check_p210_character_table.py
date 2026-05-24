#!/usr/bin/env python3
"""Regenerate and verify the P(7)=210 finite character-table scaffold.

This is a finite algebra sanity checker for HW-PRIME-CHARACTER-P210-001.
It does not make analytic, RH, GRH, prime-equidistribution, or zero-location claims.

The checker verifies:

1. the 48 reduced residues modulo 210;
2. the deterministic exponent triples (e3, e5, e7);
3. the character-generation formula
       chi_{j,k,l}(a) = (-1)^(j e3(a)) i^(k e5(a)) omega_6^(l e7(a));
4. finite character orthogonality / sector projector identities.
"""

from __future__ import annotations

import argparse
import cmath
import math
from dataclasses import dataclass
from typing import Iterable

MODULUS = 210
TOLERANCE = 1e-9

EXPECTED_EXPONENT_TRIPLES: tuple[tuple[int, int, int, int], ...] = (
    (1, 0, 0, 0),
    (11, 1, 0, 4),
    (13, 0, 3, 3),
    (17, 1, 1, 1),
    (19, 0, 2, 5),
    (23, 1, 3, 2),
    (29, 1, 2, 0),
    (31, 0, 0, 1),
    (37, 0, 1, 2),
    (41, 1, 0, 3),
    (43, 0, 3, 0),
    (47, 1, 1, 5),
    (53, 1, 3, 4),
    (59, 1, 2, 1),
    (61, 0, 0, 5),
    (67, 0, 1, 4),
    (71, 1, 0, 0),
    (73, 0, 3, 1),
    (79, 0, 2, 2),
    (83, 1, 3, 3),
    (89, 1, 2, 5),
    (97, 0, 1, 3),
    (101, 1, 0, 1),
    (103, 0, 3, 5),
    (107, 1, 1, 2),
    (109, 0, 2, 4),
    (113, 1, 3, 0),
    (121, 0, 0, 2),
    (127, 0, 1, 0),
    (131, 1, 0, 5),
    (137, 1, 1, 4),
    (139, 0, 2, 3),
    (143, 1, 3, 1),
    (149, 1, 2, 2),
    (151, 0, 0, 4),
    (157, 0, 1, 1),
    (163, 0, 3, 2),
    (167, 1, 1, 3),
    (169, 0, 2, 0),
    (173, 1, 3, 5),
    (179, 1, 2, 4),
    (181, 0, 0, 3),
    (187, 0, 1, 5),
    (191, 1, 0, 2),
    (193, 0, 3, 4),
    (197, 1, 1, 0),
    (199, 0, 2, 1),
    (209, 1, 2, 3),
)


@dataclass(frozen=True)
class ExponentTriple:
    residue: int
    e3: int
    e5: int
    e7: int


def reduced_residues(modulus: int = MODULUS) -> list[int]:
    """Return the reduced residue system modulo ``modulus``."""
    return [a for a in range(1, modulus) if math.gcd(a, modulus) == 1]


def discrete_log_mod_prime(value: int, generator: int, prime: int, order: int) -> int:
    """Return exponent e such that generator**e == value modulo prime."""
    current = 1
    target = value % prime
    for exponent in range(order):
        if current == target:
            return exponent
        current = (current * generator) % prime
    raise ValueError(
        f"no discrete logarithm for value={value} generator={generator} prime={prime}"
    )


def exponent_triple(residue: int) -> ExponentTriple:
    """Compute the P(7)=210 CRT exponent triple for a reduced residue."""
    return ExponentTriple(
        residue=residue,
        e3=discrete_log_mod_prime(residue, generator=2, prime=3, order=2),
        e5=discrete_log_mod_prime(residue, generator=2, prime=5, order=4),
        e7=discrete_log_mod_prime(residue, generator=3, prime=7, order=6),
    )


def generated_exponent_triples() -> list[ExponentTriple]:
    return [exponent_triple(a) for a in reduced_residues()]


def characters() -> list[tuple[int, int, int]]:
    """Return all character indices chi_{j,k,l}."""
    return [(j, k, l) for j in range(2) for k in range(4) for l in range(6)]


def character_value(index: tuple[int, int, int], triple: ExponentTriple) -> complex:
    """Evaluate chi_{j,k,l}(a) from the exponent triple for a."""
    j, k, l = index
    omega_6 = cmath.exp(2j * math.pi / 6)
    return ((-1) ** (j * triple.e3)) * (1j ** (k * triple.e5)) * (
        omega_6 ** (l * triple.e7)
    )


def assert_close(value: complex, expected: complex, context: str) -> None:
    if abs(value - expected) > TOLERANCE:
        raise AssertionError(f"{context}: got {value!r}, expected {expected!r}")


def verify_reduced_residues() -> None:
    residues = reduced_residues()
    if len(residues) != 48:
        raise AssertionError(f"phi(210) mismatch: got {len(residues)}, expected 48")
    expected_residues = [row[0] for row in EXPECTED_EXPONENT_TRIPLES]
    if residues != expected_residues:
        raise AssertionError("reduced residue list does not match documented table")


def verify_exponent_table() -> None:
    generated = [
        (triple.residue, triple.e3, triple.e5, triple.e7)
        for triple in generated_exponent_triples()
    ]
    expected = list(EXPECTED_EXPONENT_TRIPLES)
    if generated != expected:
        raise AssertionError("generated exponent triples do not match documented table")


def verify_character_count() -> None:
    chars = characters()
    if len(chars) != 48:
        raise AssertionError(f"character count mismatch: got {len(chars)}, expected 48")
    if len(set(chars)) != 48:
        raise AssertionError("character index set contains duplicates")


def verify_orthogonality() -> None:
    triples = {triple.residue: triple for triple in generated_exponent_triples()}
    chars = characters()
    for a in triples:
        for n in triples:
            projector = sum(
                character_value(char, triples[a]).conjugate()
                * character_value(char, triples[n])
                for char in chars
            ) / 48
            expected = 1 + 0j if a == n else 0 + 0j
            assert_close(projector, expected, f"projector a={a} n={n}")


def markdown_table(rows: Iterable[ExponentTriple]) -> str:
    lines = [
        "| residue `a` | `e3` | `e5` | `e7` |",
        "|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(f"| {row.residue} | {row.e3} | {row.e5} | {row.e7} |")
    return "\n".join(lines)


def run_checks() -> None:
    verify_reduced_residues()
    verify_exponent_table()
    verify_character_count()
    verify_orthogonality()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--emit-markdown",
        action="store_true",
        help="print the regenerated exponent-triple table as Markdown",
    )
    args = parser.parse_args()

    run_checks()
    if args.emit_markdown:
        print(markdown_table(generated_exponent_triples()))
    else:
        print("P(7)=210 character-table checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
