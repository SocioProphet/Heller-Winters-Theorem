# Prime-Weil Reformulation Manuscript Outline

Status: manuscript outline / publication planning surface.  
Claim class: outline only; no new theorem claim.  
Source synthesis: `HW-PRIME-WEIL-022`.

## Working title

Prime-Window Variance, Base-10 Orbit Packets, and a Finite Operator Reformulation of the GRH Barrier

## Claim posture

This manuscript should present a finite, computable reformulation and diagnostic decomposition of the GRH square-root barrier.

It must not present the work as a proof of RH or GRH.

## Abstract target

We introduce a finite character-packet decomposition of prime-window variance over primorial residue groups. The construction organizes character sums by base-10 orbit structure, separating terminating, degenerate, partial-orbit, and full-orbit prime factors. We prove finite theorem-grade results including the non-cancelling character-count formula and finite normality of the associated abelian convolution operator. We show that several natural analytic attacks — quotient large sieve, coset dispersion, explicit-formula truncation, and quotient Cayley spectral gap — all localize the same square-root barrier without crossing it. The result is a computable reformulation of the GRH obstruction, not a proof.

## Section 1 — Introduction

Goals:

- motivate prime-window variance as a computable reformulation surface;
- explain why finite packet decomposition is useful;
- state clearly that RH/GRH remains open;
- position the contribution as barrier localization and finite theorem infrastructure.

Key non-claim:

```text
This paper does not prove RH or GRH.
```

## Section 2 — Prime-window variance and Parseval identity

Content:

- define Richter windows `W_K`;
- define character sums `psi_{W_K}(chi)`;
- state finite Parseval variance identity;
- explain the equivalence between GRH-scale bounds and square-root character-sum scale.

Deliverable theorem:

```text
Var_P(W_K) = (1/|G_P|) sum_{chi != 1} |psi_{W_K}(chi)|^2.
```

## Section 3 — Base-10 orbit classification

Content:

- define `<10> subset (Z/pZ)^x`;
- classify prime factors into terminating, degenerate, partial, full/Artin;
- explain finite Fourier cancellation over the orbit.

Deliverable theorem:

```text
sum_{h in <10>} chi(h) = 0 iff chi|_<10> is nontrivial.
```

## Section 4 — Non-cancelling characters

Content:

- prove local formula:

```text
n_nc(p) = (p - 1) / ord_p(10) - 1.
```

- prove cumulative tower formula:

```text
N_nc(P_k) = sum_j phi(P_{j-1}) * n_nc(p_j).
```

- include corrected 673 count:

```text
673 holds through p=29, not through p=37.
```

## Section 5 — Packet hierarchy at P=2310

Content:

- present packet partition:

```text
7 + 40 + 240 + 192 = 479.
```

- define energy per character;
- present K=3,4 hierarchy:

```text
inert < p7 full-orbit < p11 cancelling < p11 non-cancelling.
```

Boundary:

Finite diagnostic only, no asymptotic ordering claim.

## Section 6 — q=37 falsification and prime-race behavior

Content:

- describe pre-registered model:

```text
R(q) = 1 + 0.3439 / ord_q(10).
```

- show q=37 falsification;
- interpret ratio as finite prime-race / coset imbalance diagnostic rather than simple orbit-quality invariant.

## Section 7 — Three locked gates

Subsections:

### Gate 1 — Coset variance theorem

Target:

```text
Var_between(q,K) / Var_within(q,K) = O(K^A).
```

Discuss quotient large sieve, dispersion, Cayley quotient spectral gap.

### Gate 2 — Explicit formula surrogate

Discuss truncation height barrier.

### Gate 3 — Operator spectral radius

Target:

```text
||T_{P,K}^perp|| = O(10^(K/2) K^A).
```

## Section 8 — Finite operator normality

Content:

- define finite convolution operator;
- prove finite abelian convolution is normal;
- prove character diagonalization;
- derive norm identity:

```text
||T_A|| = max_chi |lambda_chi|.
```

Boundary:

This is finite operator theory, not an infinite Hilbert-Polya construction.

## Section 9 — Negative diagnostics and why they matter

Content:

- quotient large sieve: constant-factor improvement only;
- coset dispersion: same result class;
- Cayley spectral gap: finite abelian quotient restates character sums;
- explicit formula surrogate: finite verification only;
- Rodin/Midy/geometric chain: exact finite arithmetic, no proof claim.

## Section 10 — Conclusion and open problems

Main conclusion:

The Prime-Weil program yields a finite computable encoding of the GRH square-root barrier.

Open problems:

1. prove the Coset Variance Theorem;
2. build zero-table finite verification infrastructure;
3. formulate infinite operator completion;
4. seek a genuinely new mechanism for square-root cancellation.

## Appendix A — Test and CI inventory

List theorem surfaces and guard tests.

## Appendix B — Tables

Include:

- local non-cancelling table;
- cumulative tower table;
- P=2310 packet hierarchy;
- q=37 packet and coset tables;
- truncation-height table.

## Non-claims for manuscript

The manuscript must explicitly state:

- no RH proof;
- no GRH proof;
- no Hilbert-Polya construction;
- no unconditional variance bound;
- no claim that digit-cycle/Rodin geometry proves prime-window equidistribution;
- no claim that finite diagnostics establish asymptotic behavior.
