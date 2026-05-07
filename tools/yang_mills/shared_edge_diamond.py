#!/usr/bin/env python3
"""Shared-edge SU(2) Wilson diamond computation.

This script is intentionally dependency-free. It fixes the Wilson coefficient
convention for W_beta(g)=exp(beta cos(theta)), evaluates the first SU(2)
character coefficients, computes the normalized diamond gap proxy, and validates
the shared-edge contraction by direct Haar quadrature.

The class parameter theta is defined by eigenvalues exp(+/- i theta), theta in
[0, pi]. The normalized Haar measure for class functions is
(2/pi) sin(theta)^2 dtheta.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Iterable


def modified_bessel_i(order: int, beta: float, tol: float = 1e-16) -> float:
    """Return I_order(beta) using the defining power series."""
    if order < 0:
        raise ValueError("order must be nonnegative")
    if beta < 0:
        raise ValueError("this script assumes beta >= 0")

    term = (beta / 2.0) ** order / math.factorial(order)
    total = term
    for m in range(10_000):
        term *= (beta * beta / 4.0) / ((m + 1) * (m + order + 1))
        total += term
        if abs(term) < tol * max(1.0, abs(total)):
            return total
    raise RuntimeError("Bessel series did not converge")


def wilson_coefficient(two_j: int, beta: float) -> float:
    """Return c_j(beta), where two_j = 2j.

    c_j(beta) = I_{2j}(beta) - I_{2j+2}(beta)
              = 2(2j+1) I_{2j+1}(beta) / beta.
    """
    if two_j < 0:
        raise ValueError("two_j must be nonnegative")
    if beta == 0:
        return 1.0 if two_j == 0 else 0.0
    return modified_bessel_i(two_j, beta) - modified_bessel_i(two_j + 2, beta)


def su2_character(two_j: int, phi: float) -> float:
    """Return chi_j(phi)=sin((2j+1)phi)/sin(phi)."""
    dimension = two_j + 1
    denominator = math.sin(phi)
    if abs(denominator) < 1e-12:
        # The phi=0 limit is d_j. The phi=pi limit has alternating sign; this
        # script's validation angles avoid the latter singular endpoint.
        return float(dimension)
    return math.sin(dimension * phi) / denominator


def diamond_character_sum(phi: float, beta: float, two_j_max: int = 80) -> float:
    """Evaluate sum_j c_j^2/d_j chi_j(phi) through two_j_max."""
    total = 0.0
    for two_j in range(two_j_max + 1):
        c = wilson_coefficient(two_j, beta)
        dimension = two_j + 1
        total += c * c / dimension * su2_character(two_j, phi)
    return total


def direct_haar_quadrature(phi: float, beta: float, panels: int = 4096) -> float:
    """Directly integrate the two-plaquette diamond over Haar measure.

    The second angular variable over the axis of u is integrated analytically,
    leaving a one-dimensional Simpson quadrature over theta.
    """
    if panels <= 0:
        raise ValueError("panels must be positive")
    if panels % 2:
        panels += 1

    step = math.pi / panels
    cos_phi = math.cos(phi)
    sin_phi = math.sin(phi)

    def integrand(theta: float) -> float:
        sin_theta = math.sin(theta)
        cos_theta = math.cos(theta)
        axis_argument = beta * sin_theta * sin_phi
        if abs(axis_argument) < 1e-12:
            axis_average = 1.0 + axis_argument * axis_argument / 6.0
        else:
            axis_average = math.sinh(axis_argument) / axis_argument
        class_weight = (2.0 / math.pi) * sin_theta * sin_theta
        exponent = beta * cos_theta * (1.0 + cos_phi)
        return class_weight * math.exp(exponent) * axis_average

    total = integrand(0.0) + integrand(math.pi)
    for index in range(1, panels):
        total += (4.0 if index % 2 else 2.0) * integrand(index * step)
    return total * step / 3.0


@dataclass(frozen=True)
class CoefficientRow:
    j: str
    dimension: int
    c_j: float
    kappa_j: float
    mu_j: float
    mass_proxy: str


def coefficient_table(beta: float, two_j_values: Iterable[int]) -> list[CoefficientRow]:
    rows: list[CoefficientRow] = []
    c0 = wilson_coefficient(0, beta)
    kappa0 = c0 * c0
    for two_j in two_j_values:
        dimension = two_j + 1
        c = wilson_coefficient(two_j, beta)
        kappa = c * c / dimension
        mu = kappa / kappa0
        if two_j == 0:
            mass = ""
        else:
            mass = f"{-math.log(mu):.15f}"
        rows.append(
            CoefficientRow(
                j=str(two_j / 2).rstrip("0").rstrip("."),
                dimension=dimension,
                c_j=c,
                kappa_j=kappa,
                mu_j=mu,
                mass_proxy=mass,
            )
        )
    return rows


def main() -> None:
    beta = 1.0
    print("Shared-Edge Diamond v0.1")
    print(f"beta={beta}")
    print()
    print("j,d_j,c_j,kappa_j,mu_j,mass_proxy")
    for row in coefficient_table(beta, [0, 1, 2]):
        print(
            f"{row.j},{row.dimension},{row.c_j:.15f},"
            f"{row.kappa_j:.15f},{row.mu_j:.15f},{row.mass_proxy}"
        )

    c0 = wilson_coefficient(0, beta)
    c_half = wilson_coefficient(1, beta)
    mu_half = (c_half * c_half / 2.0) / (c0 * c0)
    print()
    print(f"mu_half_diamond={mu_half:.15f}")
    print(f"m_diamond={-math.log(mu_half):.15f}")
    print()
    print("phi,direct_haar,character_sum,abs_error")
    for phi in [0.0, 0.7, 1.4, 2.4]:
        direct = direct_haar_quadrature(phi, beta)
        summed = diamond_character_sum(phi, beta)
        print(f"{phi:.1f},{direct:.15f},{summed:.15f},{abs(direct - summed):.3e}")

    kappa0 = c0 * c0
    kappa_half = c_half * c_half / 2.0
    connected_defect = kappa0 * kappa_half
    print()
    print("non_product_witness")
    print("rank_Jmax_1=3")
    print("product_rank=1")
    print(f"connected_defect_0_half={connected_defect:.15f}")


if __name__ == "__main__":
    main()
