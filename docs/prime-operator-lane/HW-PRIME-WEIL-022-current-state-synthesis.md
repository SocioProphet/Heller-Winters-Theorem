# HW-PRIME-WEIL-022 — Current-State Synthesis

Status: synthesis / manuscript-surface draft.  
Claim class: finite theorem and diagnostic synthesis; no RH/GRH proof.  
Lane: prime/operator lane, Prime-Weil current-state surface.  
Depends on: `HW-PRIME-WEIL-007` through `HW-PRIME-WEIL-021`, `HW-OPEN-010` through `HW-OPEN-015`.

## Purpose

This document consolidates the Prime-Weil tranche into a single current-state surface.

The result of the tranche is not a proof of RH or GRH. The result is a finite, computable, CI-tested reformulation of the GRH square-root barrier, with exact theorem-grade finite components and precisely diagnosed proof gates.

## Executive summary

The Prime-Weil lane now has:

1. an exact finite character-variance reformulation;
2. a base-10 orbit classification for prime factors;
3. a non-cancelling character-count theorem;
4. a packet-energy hierarchy at finite Richter depths;
5. an explicit coset-variance proof gate;
6. an explicit-formula surrogate proof gate;
7. a finite operator normality theorem;
8. a three-gate status map explaining why the proof remains open.

The square-root barrier remains intact.

## Theorem-grade finite results

### Non-cancelling fraction theorem

For a prime `p` coprime to `10`, let:

```text
H_p = <10> subset (Z/pZ)^x,
d_p = ord_p(10).
```

The number of nontrivial local characters that do not cancel over the base-10 orbit is:

```text
n_nc(p) = (p - 1) / ord_p(10) - 1.
```

For a primorial tower `P_k`, the cumulative local non-cancelling count is:

```text
N_nc(P_k) = sum_j phi(P_{j-1}) * n_nc(p_j).
```

The corrected count discipline matters: `673` is the cumulative count through `p=29`, not through `p=37`.

### Finite operator normality theorem

For finite abelian `G_P`, every convolution operator on `l^2(G_P)` is diagonalized by the character basis and is normal.

For a kernel `A`:

```text
(T_A f)(g) = sum_{h in G_P} A(h) f(g h).
```

Characters satisfy:

```text
T_A chi = lambda_chi chi,
lambda_chi = sum_h A(h) chi(h).
```

Hence:

```text
||T_A|| = max_chi |lambda_chi|.
```

For the nontrivial prime-window restriction:

```text
||T_{P,K}^perp|| = max_{chi != 1} |psi_{W_K}(chi)|.
```

This is finite theorem-grade linear algebra. It does not supply the GRH-scale bound.

### Base-10 orbit classification

For each prime `p`, the base-10 orbit of `<10>` in `(Z/pZ)^x` falls into one of the following classes:

| Class | Condition | Effect |
|---|---|---|
| terminating | `p | 10` | no unit orbit |
| degenerate | `ord_p(10)=1` | no nontrivial orbit cancellation |
| partial | `1 < ord_p(10) < p-1` | some characters cancel, some do not |
| full / Artin | `ord_p(10)=p-1` | all nontrivial local characters cancel over the digit orbit |

This classification is exact and finite. Its transfer to actual prime windows is the open analytic step.

### Packet hierarchy diagnostics

At `P=2310`, the nontrivial character family splits exactly into:

```text
7 + 40 + 240 + 192 = 479
```

corresponding to inert `p=2,3,5`, full-orbit `p=7`, p=11 cancelling, and p=11 non-cancelling packets.

The finite measured hierarchy at `K=3,4` is:

```text
inert < p7 full-orbit < p11 partial-cancelling < p11 partial-non-cancelling.
```

This is a finite diagnostic hierarchy, not an asymptotic theorem.

## Diagnostic results that did not close the proof

### q=37 orbit-quality model falsification

The pre-registered model:

```text
R(q) = 1 + 0.3439 / ord_q(10)
```

was falsified by the q=37 local packet measurement. The result showed that the non-cancelling/cancelling ratio is dominated by finite-window prime-race fluctuations, not by orbit period alone.

### Quotient large sieve

Restricting to quotient characters of `G_q/<10>` gives a real finite improvement, but only at the level of a constant-factor quotient/orbit gain. It does not reach GRH-scale square-root cancellation.

### Coset dispersion

The q=37 between/within coset dispersion diagnostic is correctly formulated and finite-tested. It confirms the same result class:

```text
quotient_improves_but_gap_remains.
```

### Cayley quotient spectral gap

The q=37 quotient graph has strong finite mixing at measured windows. But in the abelian quotient setting, the Cayley spectral gap is another expression of character-sum control. It does not by itself produce an asymptotic theorem.

### Explicit formula surrogate

The explicit formula packet-energy surrogate is useful for finite verification at small and moderate `K`, but the truncation-height requirement becomes impossible at resonant tower depth.

## The three locked gates

### Gate 1 — Coset variance theorem

Target:

```text
Var_between(q,K) / Var_within(q,K) = O(K^A).
```

Current obstruction: between-coset variance requires square-root-scale coset equidistribution.

Tried tools:

- quotient large sieve;
- dispersion;
- Cayley quotient spectral gap.

All localize the obstruction. None crosses it.

### Gate 2 — Explicit formula surrogate

Target: bound packet energies through zero sums and controlled truncation.

Current obstruction: truncation height. The resonant tower depth requires a height far beyond direct verification.

The surrogate is finite verification infrastructure, not a proof route by itself.

### Gate 3 — Operator spectral radius

Target:

```text
||T_{P,K}^perp|| = O(10^(K/2) K^A).
```

Current theorem: finite operator normality identifies the norm exactly.

Current obstruction: normality identifies the spectral radius but does not bound it. The bound is the same square-root character-sum barrier.

## Publication-grade framing

A correct external framing is:

```text
Prime-window variance and base-10 orbit packets give a finite computable reformulation of the GRH square-root barrier.
```

A correct internal framing is:

```text
Heller-Winters Prime-Weil Program: finite arithmetic encoding of the GRH square-root barrier.
```

Incorrect framings:

- a proof of RH;
- a proof of GRH;
- a Hilbert-Polya construction;
- a proof that orbit structure alone forces square-root cancellation;
- a proof that Rodin/digit-cycle geometry implies prime-window equidistribution.

## Current stopping point

This tranche is complete as a finite-reformulation and diagnostic package.

The next meaningful work should be one of:

1. write the manuscript version of this synthesis;
2. build zero-table infrastructure for finite verification;
3. attempt a genuinely new proof mechanism for Gate 1;
4. formalize the infinite operator completion as an independent open-problem program.

Opening more finite diagnostic branches without a new mechanism is unlikely to change the proof status.

## Non-claims

This document does not prove RH.

This document does not prove GRH.

This document does not prove the Coset Variance Theorem.

This document does not prove the explicit-formula surrogate closes the truncation barrier.

This document does not construct a Hilbert-Polya operator.

This document does not prove an operator-norm bound at GRH scale.

This document does not prove an unconditional variance bound.

This document does not close the square-root barrier.
