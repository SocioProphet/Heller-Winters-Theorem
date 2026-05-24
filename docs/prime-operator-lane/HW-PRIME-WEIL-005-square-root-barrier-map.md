# HW-PRIME-WEIL-005 — Square-Root Barrier Map

Status: barrier map / theorem-candidate ledger.  
Claim class: method-grade analytic diagnosis; theorem-candidate equivalence conditional on windowed Omega.  
Lane: prime/operator lane, Weil-positivity / fixed-modulus Richter-window variance route.  
Depends on: `HW-PRIME-WEIL-003`, `HW-PRIME-WEIL-004`, `HW-OPEN-008`, finite Parseval variance identity.

## Purpose

This document records the precise barrier exposed by the Richter-window Parseval variance route.

The prior proof-attempt surface `HW-PRIME-WEIL-004` shows why the direct contradiction route is circular: it compares an off-line-zero lower bound against a GRH-conditional upper bound. This document isolates the correct contribution:

1. the fixed-modulus variance identity gives an exact computable surface;
2. GRH predicts the critical-line variance scale;
3. an off-line zero predicts a larger Omega-scale variance lower bound;
4. all currently standard unconditional tools stop at the square-root barrier;
5. any unconditional critical-scale variance bound would be GRH-strength.

This is a precise reformulation and barrier map, not a proof of RH or GRH.

## Exact finite surface

For fixed primorial modulus `P`, finite character group `G_P`, and Richter window `W_K`, the exact Parseval variance identity is:

```text
Var_P(W_K) = (1 / |G_P|) sum_{chi != 1} |psi_{W_K}(chi)|^2.
```

This is unconditional and finite.

The object is computable directly from primes in the window and residue classes modulo `P`.

## Critical-scale variance theorem-candidate

The expected critical-scale statement is:

```text
Var_P(W_K) = O_P(10^K K^A)
```

for some fixed polynomial exponent `A`.

In the current normalization used by the lane, the GRH-shaped bound is written:

```text
Var_P(W_K) = O_P(10^K K^4).
```

## Theorem-candidate equivalence

Candidate statement:

```text
GRH for all nontrivial L(s, chi), chi in hat(G_P)
  <=>
Var_P(W_K) = O_P(10^K K^4)
```

where `W_K` is the Richter window family and the implied constant may depend on the fixed modulus `P`.

### Forward direction

If all zeros of all relevant `L(s, chi)` lie on `Re(s)=1/2`, the explicit formula gives:

```text
psi_{W_K}(chi) = O(10^(K/2) K^2)
```

for each nontrivial character, hence the Parseval identity yields:

```text
Var_P(W_K) = O_P(10^K K^4).
```

This is the GRH-to-variance direction.

### Reverse direction

The reverse direction requires a windowed Omega implication:

```text
if L(s, chi) has a zero rho_0 with Re(rho_0)=sigma_0>1/2,
then psi_{W_K}(chi) = Omega(10^(K sigma_0))
```

along the Richter windows, at least on an infinite subsequence of `K`.

If this windowed Omega implication holds, then Parseval gives:

```text
Var_P(W_K) = Omega(10^(2K sigma_0))
```

along that subsequence, contradicting:

```text
Var_P(W_K) = O_P(10^K K^4)
```

because:

```text
2 sigma_0 > 1.
```

Thus the reverse direction is theorem-candidate status until the windowed Omega implication is supplied for the exact Richter-window family.

## Barrier table

The following table records the scale comparison for individual character sums and the induced variance scale.

| Method | Per-character scale | Variance scale | Status |
|---|---|---|---|
| Brun-Titchmarsh / trivial fixed-window control | `O(10^K / K)` in count scale, squared into `O(10^(2K) / K^2)` | `O_P(10^(2K) / K^2)` | unconditional, too large |
| Siegel-Walfisz fixed-modulus distribution | `O(10^K exp(-c sqrt(K)))` | `O_P(10^(2K) exp(-2c sqrt(K))) = O_P(10^(2K) / K^A)` for any fixed `A` | unconditional, still too large |
| GRH explicit formula | `O(10^(K/2) K^2)` | `O_P(10^K K^4)` | conditional |
| Off-line zero | `Omega(10^(K(1/2+delta)))` | `Omega(10^(K(1+2delta)))` | conditional on windowed Omega |

The unconditional rows stop near the square of the main term. The GRH row is the square-root cancellation row.

The missing factor is roughly:

```text
10^K / K^A
```

between the best fixed-modulus unconditional scale and the GRH scale.

## Route 1 — Large sieve: wrong averaging axis

The large sieve is designed to average over moduli:

```text
sum_{q <= Q} sum_{chi mod q} |sum_n a_n chi(n)|^2
  <= (N + Q^2) sum_n |a_n|^2.
```

For a single fixed modulus `P`, this is the wrong averaging axis. It does not exploit the fixed finite character group strongly enough to cross the square-root barrier.

Applied to a Richter window with prime weights, the resulting fixed-modulus estimate remains at a `10^(2K)`-scale after squaring and summing. It is not a route to:

```text
O_P(10^K K^A).
```

Conclusion: useful as a diagnostic comparison, not a closing method for fixed `P`.

## Route 2 — Sieve theory: square-root barrier

For fixed modulus, classical unconditional distribution estimates such as Siegel-Walfisz give:

```text
psi(x; P, g) - x / phi(P) = O(x exp(-c sqrt(log x))).
```

On Richter windows this yields an unconditional scale of the form:

```text
Var_P(W_K) = O_P(10^(2K) exp(-2c sqrt(K)))
```

or, for every fixed `A`,

```text
Var_P(W_K) = O_P(10^(2K) / K^A).
```

This is far above the GRH scale:

```text
O_P(10^K K^4).
```

Conclusion: sieve theory reaches strong logarithmic savings but does not supply square-root cancellation in individual fixed-modulus character sums.

## Route 3 — Spectral/operator route: gap equals GRH-strength input

The finite variance is the squared Hilbert-Schmidt norm of the nontrivial character component:

```text
Var_P(W_K) = (1 / |G_P|) sum_{chi != 1} |lambda_chi(W_K)|^2.
```

A spectral-radius bound of the form:

```text
max_{chi != 1} |lambda_chi(W_K)| <= C 10^(K/2) K^A
```

would imply the critical-scale variance bound.

But `lambda_chi(W_K)` is exactly the character sum `psi_{W_K}(chi)` in this lane's finite operator model. Therefore proving the spectral-radius bound is equivalent to proving the same square-root cancellation estimate for all nontrivial characters.

Conclusion: the operator language packages the problem cleanly, but the spectral gap is not an independent input unless the operator theory supplies a genuinely new positivity/self-adjointness mechanism.

## Correct frontier

The missing lemma is:

```text
Var_P(W_K) <= C(P) 10^K K^A
```

for fixed primorial `P` and some finite exponent `A`, unconditionally.

Such a lemma would immediately rule out off-critical zeros through the Parseval/Omega mechanism, assuming the windowed Omega implication is available.

This missing lemma is GRH-strength. It is not a routine analytic estimate.

## What would constitute progress

Progress is any new method that supplies one of the following without assuming GRH:

1. a fixed-modulus square-root cancellation estimate for all nontrivial characters;
2. an unconditional critical-scale variance bound for the Richter windows;
3. an operator-theoretic spectral gap for the nontrivial character component not equivalent by definition to the desired character-sum bound;
4. a windowed Omega theorem plus an independent unconditional variance bound below the off-line zero scale;
5. a structural reduction showing that the Richter-window variance bound follows from a weaker-than-GRH statement that is independently approachable.

## Actual contribution of the programme

The current contribution is not a proof of RH.

The contribution is a finite, computable, CI-testable encoding of the GRH obstruction as a variance problem:

```text
finite Parseval identity + Richter windows + explicit formula scale separation.
```

This makes the square-root barrier visible in a concrete arithmetic observable.

## Non-claims

This document does not prove RH.

This document does not prove GRH.

This document does not prove the windowed Omega implication.

This document does not prove the unconditional critical-scale variance bound.

This document does not claim that large sieve, sieve theory, or the existing finite operator model crosses the square-root barrier.

This document does not close `HW-OPEN-001` or construct a Hilbert-Polya operator.

This document does not promote the prime/operator lane to a completed theorem.
