# HW-PRIME-WEIL-020 — Cayley Quotient Spectral Gap Diagnostic

Status: finite spectral-gap diagnostic.  
Claim class: finite quotient-graph computation, not theorem-grade analytic progress.  
Lane: prime/operator lane, coset quotient / spectral-gap surface.  
Depends on: `HW-OPEN-014`, `HW-PRIME-WEIL-019`, `HW-PRIME-WEIL-018`.

## Purpose

This document tests a finite-group route to Gate 1: whether the quotient Cayley graph associated to

```text
G_q / <10>
```

has a spectral gap strong enough to explain mixing of prime cosets.

This is qualitatively different from the large-sieve and dispersion diagnostics. It studies the finite quotient random walk induced by prime residues in a Richter window.

## Setup

For `q=37`:

```text
G_q = (Z/37Z)^x,
H_q = <10>,
ord_37(10) = 3,
G_q / H_q has size 12.
```

For each Richter window `W_K`, define a log-weighted probability measure on the quotient:

```text
mu_K(aH_q) = (1 / theta_K) sum_{p in W_K, p mod q in aH_q} log p.
```

This gives a finite random walk on the quotient group. Its Fourier eigenvalues are:

```text
lambda_m(K) = sum_{a in G_q/H_q} mu_K(a) exp(2 pi i m a / |G_q/H_q|).
```

The finite spectral gap is:

```text
gap(K) = 1 - max_{m != 0} |lambda_m(K)|.
```

## Finite q=37 measured values

| K | support size | lambda_star | spectral gap | sqrt(12) lambda_star |
|---:|---:|---:|---:|---:|
| 2 | 11 | `0.173853861761` | `0.826146138239` | `0.602247443324` |
| 3 | 12 | `0.079165278070` | `0.920834721930` | `0.274236567625` |
| 4 | 12 | `0.015439950573` | `0.984560049427` | `0.053485557719` |
| 5 | 12 | `0.004696017889` | `0.995303982111` | `0.016267483154` |

The finite quotient graph is strongly mixing in the measured windows. The observed quotient spectral gap improves with depth in this finite range.

## Interpretation

The spectral gap shows that the observed prime-coset measure on `G_37/<10>` is very close to uniform at `K=5` in the quotient Fourier modes.

This explains why the measured between-coset variance can be small even when local non-cancelling characters exist.

However, this is a finite-window fact. It does not prove that the spectral gap remains bounded away from zero as `K -> infinity`, nor does it prove a square-root prime-distribution theorem.

## Relation to Gate 1

Gate 1 asks for an unconditional asymptotic bound on between-coset variance.

A finite spectral gap at measured windows suggests a possible route:

```text
uniform quotient expansion + prime-coset measure control => coset variance bound.
```

The missing theorem is to prove a lower bound on the quotient spectral gap, or a replacement mixing estimate, uniformly in the relevant depth/tower family.

## Boundary

A Cayley graph spectral gap is a property of a finite graph and a finite generator/measure set.

The prime distribution problem requires controlling how the prime-generated measure changes with `K`. The finite spectral gap of the observed measure does not by itself imply an asymptotic bound.

## Non-claims

This document does not prove RH.

This document does not prove GRH.

This document does not prove the Coset Variance Theorem.

This document does not prove a uniform spectral gap as `K -> infinity`.

This document does not prove an unconditional variance bound.

This document does not close the square-root barrier.
