# Spectral Zeta Regularization Lane

Status: programme-lane scoping document.

## Purpose

This lane supplies the spectral invariant channel for the Heller–Winters Programme. Its role is to turn operator spectra into regularized finite readouts, determinant-gradient signals, and spectral currents that can enter the unified coherence objective.

## Maturity

Mathematical baseline with theorem-candidate channel.

## Load-bearing prerequisites

- A declared operator family, usually positive elliptic in the compact Riemannian baseline.
- A zeta determinant convention: `log det_zeta L = -zeta_L'(0)`.
- Trace-class, heat-kernel, or analytic-continuation assumptions sufficient for the stated variation.
- A declared handling of sector projections, especially when the operator does not commute with vertical or archetype projections.
- A strict separation between spectral zeta on operators and analogies with the Riemann zeta function.

## Admissible claims

This lane may support claims of the following form:

- regularized spectral data can define finite invariant readouts;
- determinant variation supplies a spectral-current or gradient signal under declared assumptions;
- round-sphere baselines can be computed explicitly and used as regression targets.

## Non-claims

This lane does not claim:

- that Lorentzian cases follow automatically from compact Riemannian cases;
- that sectorized zeta traces are archetype spectra unless commutation or smoothing assumptions are declared;
- that formal analogy with the Riemann zeta proves number-theoretic content;
- that determinant gradients are physically meaningful without the operator family and metric choice being fixed.

## Interfaces

This lane interfaces with:

- gravitational information bounds, by providing compressed finite spectral readouts;
- octonionic Hopf geometry, when apex geometry defines or perturbs the operator family;
- descent/topos semantics, by requiring spectral data to be compared only through declared invariant channels;
- information-geometric learning dynamics, by providing gradients or regularity penalties for the coherence objective.

## Proof and falsification obligations

Before this lane can become theorem-track, it must specify:

1. the operator family and domain;
2. the regulator and determinant convention;
3. the differentiability assumptions for the operator path;
4. the proof of the variational formula in the selected setting;
5. regression baselines, such as the round `S^15` Dirac-spectrum calculation;
6. failure cases where the determinant or sector interpretation is invalid.

## Adversarial notes

The main failure mode is illicit transfer: importing rigor from standard zeta determinant theory into settings where the operator is no longer positive elliptic, the projection does not commute, or the Lorentzian regulator has not been specified. This lane is powerful only when the analytic setting is explicit.
