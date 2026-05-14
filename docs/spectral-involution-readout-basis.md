# Spectral Involution / Readout-Basis Reference

Status: **thin cross-repo reference / empirical-protocol guardrail / not theorem content**.  
Canonical owner: `SocioProphet/systems-learning-loops`.  
Canonical pattern path:

```text
kb/patterns/coordinate-basis-vs-readout-basis-involution.md
```

## Purpose

This note attaches the coordinate-basis vs readout-basis involution pattern to the Heller-Winters Programme without promoting it into a theorem claim.

The local guardrail is:

```text
spectral involution is not spectral selectivity.
```

Eigenvalue sign symmetry, conjugation symmetry, and functional-equation symmetry are coordinate-level or operator-level involutions unless a specific arithmetic/geometric readout basis has been declared.

## Local interpretation

A spectral artifact must distinguish:

```text
operator basis
observation basis
readout basis
transform between them
```

before comparing finite-window residuals, phase gates, envelopes, or arithmetic interpretations.

If a sign symmetry or eigenvalue pairing is observed, that is not yet evidence for a theorem-candidate residual structure. It becomes useful only after the relevant eigenfunctions, windows, normalization, and arithmetic/geometric readout directions are declared.

## Protocol hook

Future empirical artifacts should include a readout-basis declaration:

```yaml
readout_basis:
  operator_basis: string
  observation_basis: string
  readout_basis: string
  transform_declared_before_observation: boolean
  normalization_conventions: list[string]
  finite_window_only: boolean
```

This complements the existing finite-window, null-model, alternate-substrate, and basis-consistency rules.

## Canonical KB backlink

Do not duplicate the full cross-repo argument here. Use:

```text
SocioProphet/systems-learning-loops/kb/patterns/coordinate-basis-vs-readout-basis-involution.md
```

## Nonclaims

This note does not claim:

- RH or GRH evidence;
- an asymptotic residual theorem;
- that a spectral sign symmetry identifies the arithmetic readout basis;
- that the Part B cipher experiment measures prime spectra;
- that any current Heller-Winters empirical artifact has crossed the empirical-to-analytic bridge.

It is a guardrail: involution is not selectivity, and readout-basis declaration is required before promotion.
