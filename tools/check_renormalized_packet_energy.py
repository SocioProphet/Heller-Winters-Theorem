#!/usr/bin/env python3
"""Count-normalized packet-energy diagnostic for the Prime-Weil lane.

This tool removes raw character-count growth by computing energy per character
for the old P=210 layer, the p=11 cancelling sublayer, and the p=11
non-cancelling sublayer.

It is a finite diagnostic. It does not prove RH, GRH, an asymptotic packet law,
or an unconditional variance bound.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Tuple

from tools.check_p11_partial_orbit_packet import packet_energy_row

OLD_LAYER_COUNT = 47
P11_CANCELLING_COUNT = 240
P11_NONCANCELLING_COUNT = 192


@dataclass(frozen=True)
class NormalizedPacketEnergyRow:
    depth: int
    old_layer_energy_per_character: float
    p11_cancelling_energy_per_character: float
    p11_noncancelling_energy_per_character: float
    noncancel_to_cancel_ratio: float
    noncancel_to_old_ratio: float
    cancel_to_old_ratio: float


def normalized_packet_energy_row(depth: int) -> NormalizedPacketEnergyRow:
    row = packet_energy_row(depth)
    old_per = row.old_p210_energy / OLD_LAYER_COUNT
    cancel_per = row.p11_cancelling_energy / P11_CANCELLING_COUNT
    noncancel_per = row.p11_noncancelling_energy / P11_NONCANCELLING_COUNT
    return NormalizedPacketEnergyRow(
        depth=depth,
        old_layer_energy_per_character=old_per,
        p11_cancelling_energy_per_character=cancel_per,
        p11_noncancelling_energy_per_character=noncancel_per,
        noncancel_to_cancel_ratio=noncancel_per / cancel_per,
        noncancel_to_old_ratio=noncancel_per / old_per,
        cancel_to_old_ratio=cancel_per / old_per,
    )


def normalized_packet_energy_rows(depths: Iterable[int] = (2, 3, 4, 5)) -> Tuple[NormalizedPacketEnergyRow, ...]:
    return tuple(normalized_packet_energy_row(depth) for depth in depths)


def run_checks() -> Tuple[NormalizedPacketEnergyRow, ...]:
    rows = normalized_packet_energy_rows()
    for row in rows:
        if row.old_layer_energy_per_character <= 0:
            raise AssertionError(row)
        if row.p11_cancelling_energy_per_character <= 0:
            raise AssertionError(row)
        if row.p11_noncancelling_energy_per_character <= 0:
            raise AssertionError(row)
        if row.noncancel_to_cancel_ratio <= 0:
            raise AssertionError(row)
    if abs(rows[0].noncancel_to_cancel_ratio - 1.0) > 1e-12:
        raise AssertionError(rows[0])
    if rows[1].noncancel_to_cancel_ratio <= 1.0:
        raise AssertionError(rows[1])
    if rows[2].noncancel_to_cancel_ratio <= rows[1].noncancel_to_cancel_ratio:
        raise AssertionError(rows[2])
    if rows[3].noncancel_to_cancel_ratio >= rows[2].noncancel_to_cancel_ratio:
        raise AssertionError(rows[3])
    if rows[3].noncancel_to_cancel_ratio >= 1.0:
        raise AssertionError(rows[3])
    return rows


def main() -> None:
    print("Count-normalized packet-energy diagnostic")
    for row in run_checks():
        cancel_scaled = row.p11_cancelling_energy_per_character / (10**row.depth)
        noncancel_scaled = row.p11_noncancelling_energy_per_character / (10**row.depth)
        print(
            f"K={row.depth} old_per={row.old_layer_energy_per_character:.12f} "
            f"p11_cancel_per={row.p11_cancelling_energy_per_character:.12f} "
            f"p11_non_per={row.p11_noncancelling_energy_per_character:.12f} "
            f"non/cancel={row.noncancel_to_cancel_ratio:.12f} "
            f"non/old={row.noncancel_to_old_ratio:.12f} "
            f"cancel/old={row.cancel_to_old_ratio:.12f} "
            f"cancel/10^K={cancel_scaled:.12f} non/10^K={noncancel_scaled:.12f}"
        )


if __name__ == "__main__":
    main()
