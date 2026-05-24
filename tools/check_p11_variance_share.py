#!/usr/bin/env python3
"""p=11 non-cancelling variance-share diagnostic.

This tool compares the finite p=11 non-cancelling energy share against the
local character-count baseline 4/9 in the P=2310 packet.

It is a finite diagnostic. It does not prove an asymptotic law, RH, GRH,
Artin's conjecture, or an unconditional variance bound.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Tuple

from tools.check_p11_partial_orbit_packet import PacketEnergyRow, packet_energy_row

LOCAL_NONCANCELLING_BASELINE = 4.0 / 9.0
FULL_NONTRIVIAL_COUNT_BASELINE = 192.0 / 479.0
NEW_LAYER_COUNT_BASELINE = 432.0 / 479.0


@dataclass(frozen=True)
class P11VarianceShareRow:
    depth: int
    total_nontrivial_energy: float
    p11_new_energy: float
    p11_noncancelling_energy: float
    p11_new_share_total: float
    p11_noncancelling_share_new: float
    p11_noncancelling_share_total: float
    deviation_from_local_baseline: float


def variance_share_row(depth: int) -> P11VarianceShareRow:
    row: PacketEnergyRow = packet_energy_row(depth)
    p11_new_share_total = row.p11_new_energy / row.total_nontrivial_energy
    p11_noncancelling_share_new = row.p11_noncancelling_energy / row.p11_new_energy
    p11_noncancelling_share_total = row.p11_noncancelling_energy / row.total_nontrivial_energy
    return P11VarianceShareRow(
        depth=depth,
        total_nontrivial_energy=row.total_nontrivial_energy,
        p11_new_energy=row.p11_new_energy,
        p11_noncancelling_energy=row.p11_noncancelling_energy,
        p11_new_share_total=p11_new_share_total,
        p11_noncancelling_share_new=p11_noncancelling_share_new,
        p11_noncancelling_share_total=p11_noncancelling_share_total,
        deviation_from_local_baseline=p11_noncancelling_share_new - LOCAL_NONCANCELLING_BASELINE,
    )


def variance_share_rows(depths: Iterable[int] = (2, 3, 4)) -> Tuple[P11VarianceShareRow, ...]:
    return tuple(variance_share_row(depth) for depth in depths)


def run_checks() -> Tuple[P11VarianceShareRow, ...]:
    rows = variance_share_rows()
    for row in rows:
        if not 0.0 <= row.p11_new_share_total <= 1.0:
            raise AssertionError(row)
        if not 0.0 <= row.p11_noncancelling_share_new <= 1.0:
            raise AssertionError(row)
        if not 0.0 <= row.p11_noncancelling_share_total <= 1.0:
            raise AssertionError(row)
    # Finite observed values for depths 2..4 stay close to the local 4/9 count baseline.
    if abs(rows[0].p11_noncancelling_share_new - LOCAL_NONCANCELLING_BASELINE) > 1e-10:
        raise AssertionError(rows[0])
    if abs(rows[1].p11_noncancelling_share_new - LOCAL_NONCANCELLING_BASELINE) > 0.03:
        raise AssertionError(rows[1])
    if abs(rows[2].p11_noncancelling_share_new - LOCAL_NONCANCELLING_BASELINE) > 0.05:
        raise AssertionError(rows[2])
    return rows


def main() -> None:
    print("p=11 variance-share diagnostic")
    print(f"local non-cancelling baseline: {LOCAL_NONCANCELLING_BASELINE:.12f}")
    print(f"full nontrivial count baseline: {FULL_NONTRIVIAL_COUNT_BASELINE:.12f}")
    print(f"new layer count baseline: {NEW_LAYER_COUNT_BASELINE:.12f}")
    for row in run_checks():
        print(
            f"K={row.depth} p11_new/total={row.p11_new_share_total:.12f} "
            f"p11_non/new={row.p11_noncancelling_share_new:.12f} "
            f"p11_non/total={row.p11_noncancelling_share_total:.12f} "
            f"deviation={row.deviation_from_local_baseline:.12f}"
        )


if __name__ == "__main__":
    main()
