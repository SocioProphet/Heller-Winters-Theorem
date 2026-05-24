#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

VERIFIED_HEIGHT = 3e12


@dataclass(frozen=True)
class TruncationHeightRow:
    depth: int
    t_needed: float
    verified_height: float
    feasible: bool
    status: str


TRUNCATION_ROWS = (
    TruncationHeightRow(5, 4e4, VERIFIED_HEIGHT, True, "yes"),
    TruncationHeightRow(10, 5e7, VERIFIED_HEIGHT, True, "yes"),
    TruncationHeightRow(20, 2e13, VERIFIED_HEIGHT, False, "borderline/no"),
    TruncationHeightRow(50, 1e29, VERIFIED_HEIGHT, False, "no"),
    TruncationHeightRow(11088, 10.0**5544, VERIFIED_HEIGHT, False, "impossible"),
)


def truncation_height_rows() -> Tuple[TruncationHeightRow, ...]:
    return TRUNCATION_ROWS


def run_checks() -> Tuple[TruncationHeightRow, ...]:
    rows = truncation_height_rows()
    assert rows[0].feasible is True
    assert rows[1].feasible is True
    assert rows[2].feasible is False
    assert rows[-1].depth == 11088
    assert rows[-1].feasible is False
    return rows


if __name__ == "__main__":
    for row in run_checks():
        print(row)
