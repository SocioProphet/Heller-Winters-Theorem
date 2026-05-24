# HW-PRIME-WEIL-018 — Three Locked Gates: Current Status

Status: consolidated proof-gate status document.  
Claim class: barrier summary / roadmap, not theorem-grade RH progress.  
Lane: prime/operator lane, current-state synthesis.  
Depends on: `HW-OPEN-014`, `HW-PRIME-WEIL-016`, `HW-PRIME-WEIL-017`, `HW-OPEN-015`.

## Purpose

This document records the current state of the Prime-Weil route after the quotient large-sieve diagnostic, explicit-formula surrogate, and corrected operator-domain analysis.

The program has produced a precise finite reformulation and diagnostic apparatus. It has not produced a proof of RH or GRH.

The remaining proof problem is now organized as three locked gates.

## Gate 1 — Coset Variance Theorem

Target:

```text
Var_between(q,K) / Var_within(q,K) = O(K^A)
```

for the relevant coset quotient packets.

Current obstruction: between-coset variance must converge at square-root scale. This is the prime-race/coset-equidistribution obstruction.

Best current diagnostic: quotient large-sieve restriction. It gives a real orbit/coset improvement but does not cross the square-root barrier.

Summary:

| Item | Status |
|---|---|
| Surface | `HW-OPEN-014` |
| Tool tried | standard large sieve, quotient large sieve |
| Best gain | finite constant-factor quotient/orbit improvement |
| Remaining gap | grows with `K`; GRH-scale square-root cancellation not reached |
| Next tools | Selberg/dispersion over quotient packets; pretentious distance; coset prime-race analysis |

The quotient large sieve isolates the right packet, but standard large-sieve technology does not prove the Coset Variance Theorem.

## Gate 2 — Explicit Formula Packet-Energy Surrogate

Target:

```text
E_C(K) = (1/|C|) sum_{chi in C} |psi_{W_K}(chi)|^2
```

expressed through zero sums with controlled truncation error.

Current obstruction: truncation height grows too quickly.

Summary:

| K | Required height | Current verification scale | Status |
|---:|---:|---:|---|
| 5 | about `4e4` | about `3e12` | feasible |
| 10 | about `5e7` | about `3e12` | feasible |
| 20 | about `2e13` | about `3e12` | borderline/no |
| 50 | about `1e29` | about `3e12` | no |
| 11088 | about `10^5544` | about `3e12` | impossible |

The explicit-formula surrogate is useful for finite verification. It does not reach the resonant tower depth with current zero verification heights.

Next tools:

1. zero-table wiring for finite verification;
2. smoothed windows;
3. zero-density estimates;
4. off-diagonal cancellation bounds;
5. explicit tail estimates that do not assume GRH.

## Gate 3 — Operator Spectral Radius

Corrected finite operator fact: the raw finite convolution operator is normal, not necessarily self-adjoint.

For finite abelian `G_P`, characters diagonalize convolution:

```text
T_{P,K} chi = lambda_chi chi.
```

Therefore the finite operator is normal and the spectral theorem applies. The finite spectral radius is:

```text
||T_{P,K}^perp|| = max_{chi != 1} |psi_{W_K}(chi)|.
```

The correct Gate 3 target is the operator-norm / spectral-radius bound:

```text
||T_{P,K}^perp|| = O(10^(K/2) K^A).
```

This is exactly the character-sum square-root bound in operator language.

Summary:

| Item | Status |
|---|---|
| Surface | `HW-OPEN-015` |
| Finite operator | normal convolution operator on `l^2(G_P)` |
| Spectral theorem | applies in finite dimension |
| Obstruction | spectral-radius bound remains GRH-strength |
| Infinite target | define `T_infty` on `L^2(Z_hat^x, d mu_Haar)` or restricted completion |
| Next tools | domain/closure analysis; normality of closure; random matrix/GUE spectral heuristics; norm estimates |

Self-adjointness may be useful for a symmetrized operator, but it is not the core finite fact. The core finite fact is normality; the proof barrier is the spectral-radius estimate.

## Current conclusion

All three gates are precisely stated and remain locked.

1. Coset variance: quotient large sieve gives a real but insufficient gain.
2. Explicit formula: finite verification works only below the truncation barrier.
3. Operator route: finite normality is exact, but the spectral-radius bound is still GRH-strength.

The framework is a precise finite reformulation and diagnostic apparatus for the GRH barrier. It is not a proof.

## Non-claims

This document does not prove RH.

This document does not prove GRH.

This document does not prove the Coset Variance Theorem.

This document does not prove the explicit-formula surrogate closes the truncation barrier.

This document does not construct a Hilbert-Polya operator.

This document does not prove an operator-norm bound at GRH scale.

This document does not prove an unconditional variance bound.

This document does not close the square-root barrier.
