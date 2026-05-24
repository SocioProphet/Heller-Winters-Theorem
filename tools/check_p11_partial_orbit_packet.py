#!/usr/bin/env python3
"""p=11 partial-orbit packet diagnostic for the Prime-Weil lane.

This tool extends the finite character-packet diagnostics from P=210 to
P=2310 = 2*3*5*7*11 and isolates the p=11 partial-orbit layer.

It is a finite diagnostic. It does not prove RH, GRH, Artin's conjecture,
or an unconditional variance bound.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass
from functools import lru_cache
from typing import Dict, Iterable, List, Tuple

MODULUS_2310 = 2310
FACTORS = (3, 5, 7, 11)
GENERATOR_BY_FACTOR = {3: 2, 5: 2, 7: 3, 11: 2}
ORDER_BY_FACTOR = {3: 2, 5: 4, 7: 6, 11: 10}

CharacterIndex2310 = Tuple[int, int, int, int]
ExponentTuple2310 = Tuple[int, int, int, int]


@dataclass(frozen=True)
class PacketCounts:
    total_characters: int
    old_p210_layer: int
    new_p11_layer: int
    p11_cancelling_local: int
    p11_noncancelling_local: int
    p11_cancelling_new_layer: int
    p11_noncancelling_new_layer: int


@dataclass(frozen=True)
class PacketEnergyRow:
    depth: int
    active_prime_count: int
    total_nontrivial_energy: float
    old_p210_energy: float
    p11_new_energy: float
    p11_cancelling_energy: float
    p11_noncancelling_energy: float

    @property
    def p11_share(self) -> float:
        return self.p11_new_energy / self.total_nontrivial_energy if self.total_nontrivial_energy else 0.0

    @property
    def p11_noncancelling_share_of_new(self) -> float:
        return self.p11_noncancelling_energy / self.p11_new_energy if self.p11_new_energy else 0.0


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
    low = 10 ** (depth - 1)
    high = 10**depth
    return tuple(p for p in primes_up_to_sieve(high - 1) if low <= p < high)


@lru_cache(maxsize=None)
def active_primes_in_window(depth: int) -> Tuple[int, ...]:
    return tuple(p for p in primes_in_window(depth) if math.gcd(p, MODULUS_2310) == 1)


def multiplicative_order(a: int, modulus: int) -> int:
    if math.gcd(a, modulus) != 1:
        raise ValueError(f"{a} is not a unit modulo {modulus}")
    value = 1
    for order in range(1, modulus + 1):
        value = (value * a) % modulus
        if value == 1:
            return order
    raise RuntimeError(f"order not found for {a} modulo {modulus}")


@lru_cache(maxsize=None)
def dlog_table_mod_prime(prime: int) -> Dict[int, int]:
    generator = GENERATOR_BY_FACTOR[prime]
    order = ORDER_BY_FACTOR[prime]
    table: Dict[int, int] = {}
    value = 1
    for exponent in range(order):
        table[value] = exponent
        value = (value * generator) % prime
    if len(table) != order:
        raise RuntimeError(f"bad discrete log table modulo {prime}")
    return table


def residue_exponents(residue: int) -> ExponentTuple2310:
    return tuple(dlog_table_mod_prime(p)[residue % p] for p in FACTORS)  # type: ignore[return-value]


def character_indices() -> Tuple[CharacterIndex2310, ...]:
    return tuple(
        (e3, e5, e7, e11)
        for e3 in range(2)
        for e5 in range(4)
        for e7 in range(6)
        for e11 in range(10)
    )


def character_value(index: CharacterIndex2310, residue: int) -> complex:
    exponents = residue_exponents(residue)
    angle = sum(i * e / o for i, e, o in zip(index, exponents, (2, 4, 6, 10)))
    return cmath.exp(2j * math.pi * angle)


def window_character_sum(index: CharacterIndex2310, depth: int) -> complex:
    return sum(math.log(p) * character_value(index, p % MODULUS_2310) for p in active_primes_in_window(depth))


def local_p11_orbit_sum(exponent: int) -> complex:
    # <10> mod 11 = {10, 1}; generator 2 has 10 = 2^5, so chi(10)=(-1)^exponent.
    return 1.0 + ((-1) ** exponent)


def is_p11_orbit_cancelling(exponent: int) -> bool:
    return exponent % 2 == 1


def packet_counts() -> PacketCounts:
    total = len(character_indices())
    old = sum(1 for index in character_indices() if index[3] == 0)
    new = sum(1 for index in character_indices() if index[3] != 0)
    local_cancelling = sum(1 for exponent in range(1, 10) if is_p11_orbit_cancelling(exponent))
    local_noncancelling = sum(1 for exponent in range(1, 10) if not is_p11_orbit_cancelling(exponent))
    cancelling_new = sum(1 for index in character_indices() if index[3] != 0 and is_p11_orbit_cancelling(index[3]))
    noncancelling_new = sum(1 for index in character_indices() if index[3] != 0 and not is_p11_orbit_cancelling(index[3]))
    return PacketCounts(
        total_characters=total,
        old_p210_layer=old,
        new_p11_layer=new,
        p11_cancelling_local=local_cancelling,
        p11_noncancelling_local=local_noncancelling,
        p11_cancelling_new_layer=cancelling_new,
        p11_noncancelling_new_layer=noncancelling_new,
    )


def packet_energy_row(depth: int) -> PacketEnergyRow:
    total = 0.0
    old = 0.0
    p11_new = 0.0
    p11_cancel = 0.0
    p11_noncancel = 0.0
    for index in character_indices():
        if index == (0, 0, 0, 0):
            continue
        energy = abs(window_character_sum(index, depth)) ** 2
        total += energy
        if index[3] == 0:
            old += energy
        else:
            p11_new += energy
            if is_p11_orbit_cancelling(index[3]):
                p11_cancel += energy
            else:
                p11_noncancel += energy
    return PacketEnergyRow(
        depth=depth,
        active_prime_count=len(active_primes_in_window(depth)),
        total_nontrivial_energy=total,
        old_p210_energy=old,
        p11_new_energy=p11_new,
        p11_cancelling_energy=p11_cancel,
        p11_noncancelling_energy=p11_noncancel,
    )


def packet_energy_rows(depths: Iterable[int] = (2, 3)) -> Tuple[PacketEnergyRow, ...]:
    return tuple(packet_energy_row(depth) for depth in depths)


def run_checks() -> Tuple[PacketEnergyRow, ...]:
    counts = packet_counts()
    if counts.total_characters != 480:
        raise AssertionError(counts)
    if counts.old_p210_layer != 48:
        raise AssertionError(counts)
    if counts.new_p11_layer != 432:
        raise AssertionError(counts)
    if (counts.p11_cancelling_local, counts.p11_noncancelling_local) != (5, 4):
        raise AssertionError(counts)
    if (counts.p11_cancelling_new_layer, counts.p11_noncancelling_new_layer) != (240, 192):
        raise AssertionError(counts)

    for exponent in range(1, 10):
        total = local_p11_orbit_sum(exponent)
        if is_p11_orbit_cancelling(exponent) and abs(total) > 1e-12:
            raise AssertionError((exponent, total))
        if not is_p11_orbit_cancelling(exponent) and abs(total - 2.0) > 1e-12:
            raise AssertionError((exponent, total))

    rows = packet_energy_rows()
    for row in rows:
        if row.total_nontrivial_energy <= 0:
            raise AssertionError(row)
        if row.p11_new_energy <= 0:
            raise AssertionError(row)
        if abs((row.old_p210_energy + row.p11_new_energy) - row.total_nontrivial_energy) > 1e-6:
            raise AssertionError(row)
        if abs((row.p11_cancelling_energy + row.p11_noncancelling_energy) - row.p11_new_energy) > 1e-6:
            raise AssertionError(row)
    return rows


def main() -> None:
    counts = packet_counts()
    print("p=11 partial-orbit packet diagnostic for P=2310")
    print(counts)
    for row in run_checks():
        print(
            f"K={row.depth} active_primes={row.active_prime_count} "
            f"total={row.total_nontrivial_energy:.12f} old_p210={row.old_p210_energy:.12f} "
            f"p11_new={row.p11_new_energy:.12f} p11_share={row.p11_share:.12f} "
            f"p11_cancel={row.p11_cancelling_energy:.12f} "
            f"p11_noncancel={row.p11_noncancelling_energy:.12f} "
            f"noncancel_share_new={row.p11_noncancelling_share_of_new:.12f}"
        )


if __name__ == "__main__":
    main()
