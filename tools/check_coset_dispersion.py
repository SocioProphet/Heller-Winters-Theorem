#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Tuple

from tools.check_coset_variance import between_coset_variance, within_coset_variance
from tools.check_quotient_large_sieve import quotient_large_sieve_row


@dataclass(frozen=True)
class CosetDispersionRow:
    q: int
    depth: int
    between_variance: float
    within_variance: float
    between_within_ratio: float
    quotient_candidate_bound: float
    grh_packet_scale: float
    measured_to_grh_ratio: float
    quotient_to_grh_ratio: float
    dispersion_outcome: str


def coset_dispersion_row(q: int, depth: int) -> CosetDispersionRow:
    between = between_coset_variance(q, depth)
    within = within_coset_variance(q, depth)
    qls = quotient_large_sieve_row(q, depth)
    measured_to_grh = between / qls.grh_packet_scale
    quotient_to_grh = qls.quotient_candidate_bound / qls.grh_packet_scale
    if qls.quotient_candidate_bound <= qls.grh_packet_scale:
        outcome = "square_root_scale_candidate"
    elif qls.quotient_candidate_bound < qls.standard_bound:
        outcome = "quotient_improves_but_gap_remains"
    else:
        outcome = "no_quotient_improvement"
    return CosetDispersionRow(
        q=q,
        depth=depth,
        between_variance=between,
        within_variance=within,
        between_within_ratio=between / within if within else float("inf"),
        quotient_candidate_bound=qls.quotient_candidate_bound,
        grh_packet_scale=qls.grh_packet_scale,
        measured_to_grh_ratio=measured_to_grh,
        quotient_to_grh_ratio=quotient_to_grh,
        dispersion_outcome=outcome,
    )


def coset_dispersion_rows(q: int = 37, depths: Iterable[int] = (2, 3, 4, 5)) -> Tuple[CosetDispersionRow, ...]:
    return tuple(coset_dispersion_row(q, depth) for depth in depths)


def run_checks() -> Tuple[CosetDispersionRow, ...]:
    rows = coset_dispersion_rows()
    assert [row.depth for row in rows] == [2, 3, 4, 5]
    for row in rows:
        assert row.between_variance > 0
        assert row.within_variance > 0
        assert row.between_within_ratio > 0
        assert row.quotient_candidate_bound > row.between_variance
    assert rows[-1].quotient_to_grh_ratio > 1.0
    assert rows[-1].dispersion_outcome == "quotient_improves_but_gap_remains"
    return rows


if __name__ == "__main__":
    for row in run_checks():
        print(row)
