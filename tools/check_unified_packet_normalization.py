#!/usr/bin/env python3
"""Unified count-normalized packet comparison for P=2310.

This diagnostic splits the P=2310 nontrivial character family into four
finite orbit classes:

1. inert/terminating/degenerate p=2,3,5 layer;
2. p=7 full-orbit layer;
3. p=11 partial-orbit cancelling layer;
4. p=11 partial-orbit non-cancelling layer.

It reports energy per character for each class. This is a finite diagnostic,
not an asymptotic theorem and not RH/GRH progress.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, Tuple

from tools.check_p11_partial_orbit_packet import character_indices, window_character_sum

PACKET_ORDER = ("inert_p235", "p7_full", "p11_cancel", "p11_noncancel")
PACKET_LABELS = {
    "inert_p235": "p=2,3,5 inert/degenerate layer",
    "p7_full": "p=7 full-orbit layer",
    "p11_cancel": "p=11 partial-orbit cancelling layer",
    "p11_noncancel": "p=11 partial-orbit non-cancelling layer",
}
PACKET_COUNTS = {
    "inert_p235": 7,
    "p7_full": 40,
    "p11_cancel": 240,
    "p11_noncancel": 192,
}


@dataclass(frozen=True)
class UnifiedPacketRow:
    depth: int
    inert_p235_per_character: float
    p7_full_per_character: float
    p11_cancel_per_character: float
    p11_noncancel_per_character: float
    p7_over_inert: float
    p11_cancel_over_p7: float
    p11_noncancel_over_p11_cancel: float


def classify_index(index: Tuple[int, int, int, int]) -> str:
    e3, e5, e7, e11 = index
    if index == (0, 0, 0, 0):
        return "trivial"
    if e11 != 0:
        return "p11_noncancel" if e11 % 2 == 0 else "p11_cancel"
    if e7 != 0:
        return "p7_full"
    return "inert_p235"


def packet_energies(depth: int) -> Dict[str, float]:
    energies = {name: 0.0 for name in PACKET_ORDER}
    counts = {name: 0 for name in PACKET_ORDER}
    for index in character_indices():
        packet = classify_index(index)
        if packet == "trivial":
            continue
        energies[packet] += abs(window_character_sum(index, depth)) ** 2
        counts[packet] += 1
    if counts != PACKET_COUNTS:
        raise AssertionError((counts, PACKET_COUNTS))
    return energies


def energy_per_character(depth: int) -> Dict[str, float]:
    energies = packet_energies(depth)
    return {packet: energies[packet] / PACKET_COUNTS[packet] for packet in PACKET_ORDER}


def unified_packet_row(depth: int) -> UnifiedPacketRow:
    per = energy_per_character(depth)
    return UnifiedPacketRow(
        depth=depth,
        inert_p235_per_character=per["inert_p235"],
        p7_full_per_character=per["p7_full"],
        p11_cancel_per_character=per["p11_cancel"],
        p11_noncancel_per_character=per["p11_noncancel"],
        p7_over_inert=per["p7_full"] / per["inert_p235"],
        p11_cancel_over_p7=per["p11_cancel"] / per["p7_full"],
        p11_noncancel_over_p11_cancel=per["p11_noncancel"] / per["p11_cancel"],
    )


def unified_packet_rows(depths: Iterable[int] = (2, 3, 4)) -> Tuple[UnifiedPacketRow, ...]:
    return tuple(unified_packet_row(depth) for depth in depths)


def run_checks() -> Tuple[UnifiedPacketRow, ...]:
    rows = unified_packet_rows()
    for row in rows:
        if not (
            row.inert_p235_per_character
            < row.p7_full_per_character
            < row.p11_cancel_per_character
            <= row.p11_noncancel_per_character + 1e-9
        ):
            raise AssertionError(row)
    if abs(rows[0].p11_noncancel_per_character - rows[0].p11_cancel_per_character) > 1e-9:
        raise AssertionError(rows[0])
    if rows[1].p11_noncancel_over_p11_cancel <= 1.0:
        raise AssertionError(rows[1])
    if rows[2].p11_noncancel_over_p11_cancel <= rows[1].p11_noncancel_over_p11_cancel:
        raise AssertionError(rows[2])
    return rows


def main() -> None:
    print("Unified count-normalized packet comparison")
    for row in run_checks():
        print(
            f"K={row.depth} inert={row.inert_p235_per_character:.12f} "
            f"p7_full={row.p7_full_per_character:.12f} "
            f"p11_cancel={row.p11_cancel_per_character:.12f} "
            f"p11_non={row.p11_noncancel_per_character:.12f} "
            f"p7/inert={row.p7_over_inert:.12f} "
            f"cancel/p7={row.p11_cancel_over_p7:.12f} "
            f"non/cancel={row.p11_noncancel_over_p11_cancel:.12f}"
        )


if __name__ == "__main__":
    main()
