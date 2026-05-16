# Formal Claims, Guardrails, and Conjectural Objects

Status: Draft v0.1  
Lane: HPHD / zeta mirror-lattice / formal claim boundary  
Purpose: Convert the HPHD zeta mirror-lattice intuition into typed definitions, lemmas, conjectures, and admissible research claims.

## 1. Core objects

### Definition 1: Zeta mirror lattice

The zeta mirror lattice is:

```math
\mathcal M^-_{\zeta}=\{-2n:n\in\mathbb N\}.
```

It is the set of trivial zeros of the Riemann zeta function.

### Definition 2: Non-trivial zeta fluctuation spectrum

The non-trivial zeta spectrum is:

```math
Z_{\mathrm{nt}}
=
\{\rho\in\mathbb C:\zeta(\rho)=0,\ 0<\Re(\rho)<1\}.
```

The Riemann hypothesis asserts:

```math
\rho\in Z_{\mathrm{nt}}\Rightarrow \Re(\rho)=\frac12.
```

HPHD does not assume RH as proven. HPHD may study the consequences of the critical-line hypothesis as a conditional branch.

### Definition 3: Regularized density value

A divergent series `S` may be assigned a zeta-regularized value only when a specified analytic-continuation procedure assigns such a value.

We write:

```math
S\overset{\zeta\text{-reg}}{=}a
```

to distinguish this from ordinary convergence.

### Definition 4: HPHD mirror domain

An HPHD mirror domain is a transformed negative-side structure induced by continuation, completion, reflection, or renormalization from a positive arithmetic source domain.

For the base zeta function, the canonical first example is:

```math
\mathcal M^-_{\zeta}.
```

### Definition 5: Admissible density comparison

A density comparison between two spectra or lattices is admissible only when the measure, coordinate, and transformation are explicit.

For example, one may define:

```math
\mu_{\mathrm{triv}}=\sum_{n\ge1}\delta_{-2n}
```

and:

```math
\mu_{\mathrm{nt}}=\sum_{\rho\in Z_{\mathrm{nt}}}\delta_{\rho}.
```

A comparison requires a named transformation such as:

```math
\Phi_*\mu_{\mathrm{triv}}\sim\mu_{\mathrm{nt}}.
```

Without such a transformation, a claim of "same density" is not admissible.

## 2. Lemmas

### Lemma 1: Trivial zeros are not ordinary negative primes

The trivial zeros of `zeta(s)` occur at negative even integers:

```math
-2,-4,-6,\ldots
```

The negatives of the positive primes are:

```math
-2,-3,-5,-7,-11,\ldots
```

Therefore:

```math
\mathcal M^-_{\zeta}\neq\{-p:p\in\mathbb P\}.
```

The phrase "negative primes" is therefore inadmissible as a literal theorem. It may be retained only as a clearly typed metaphor for a negative mirror-lattice counterpart to positive-prime harmonic structure.

### Lemma 2: Raw density mismatch

The trivial-zero lattice and the non-trivial-zero spectrum do not have the same ordinary counting density.

The trivial-zero counting function has linear growth:

```math
N_{\mathrm{triv}}(R)\sim\frac{R}{2}.
```

The non-trivial-zero counting function has asymptotic growth:

```math
N_{\mathrm{nt}}(T)
\sim
\frac{T}{2\pi}\log\frac{T}{2\pi}
-
\frac{T}{2\pi}.
```

Therefore any HPHD claim that the two are density-correspondent requires an explicit embedding, reparameterization, or pushforward measure.

### Lemma 3: Zeta-regularized equality is not ordinary equality

The expression:

```math
1+1+1+\cdots
```

diverges as an ordinary series.

The statement:

```math
1+1+1+\cdots\overset{\zeta\text{-reg}}{=}-\frac12
```

is a regularized assignment, not a statement of ordinary convergence.

Therefore HPHD must preserve the distinction between:

```math
=
```

and:

```math
\overset{\zeta\text{-reg}}{=}.
```

### Lemma 4: The mirror lattice is completion-induced

The negative-even vanishing of `zeta(s)` is not a free-standing arithmetic fact about primes. It is induced by the analytic-continuation and functional-equation architecture of the completed zeta system.

Therefore the mirror lattice belongs to the completion layer, not to ordinary prime enumeration.

## 3. Conjectures

### Conjecture 1: Mirror-spectral correspondence

There exists an HPHD embedding, spectral index, or pushforward measure:

```math
\Phi
```

such that the regular trivial-zero lattice:

```math
\mathcal M^-_{\zeta}
```

and the irregular non-trivial spectrum:

```math
Z_{\mathrm{nt}}
```

become comparable as complementary components of a completed harmonic arithmetic system.

This does not mean the two sets are equal. It means the trivial zeros and non-trivial zeros can be interpreted as different projections of a deeper completed structure:

```text
regular mirror cancellation <-> irregular prime fluctuation
```

The task for HPHD is to specify the correct embedding measure.

Candidate embedding families:

- logarithmic coordinate transforms;
- spectral counting maps;
- operator-theoretic spectra;
- residue-class harmonic decompositions;
- Dirichlet-character extensions.

### Conjecture 2: Character-dependent mirror lattices

For each completed Dirichlet L-function `L(s, chi)`, there exists a character-dependent mirror lattice:

```math
\mathcal M^-_{\chi}
```

whose structure is determined by the parity, conductor, Gamma factors, and functional equation of `L(s, chi)`.

The zeta mirror lattice:

```math
\mathcal M^-_{\zeta}=\{-2n:n\in\mathbb N\}
```

is the base case, not the universal case.

### Conjecture 3: Regularized density shadow principle

Certain divergent positive arithmetic densities admit finite negative regularized invariants after analytic continuation. HPHD interprets these values as density shadows, not ordinary sums.

General form:

```text
positive divergent accumulation -> analytic continuation -> finite regularized shadow
```

This principle should be tested against zeta, Dirichlet L-functions, spectral zeta functions, and heat-kernel/zeta regularization analogues.

## 4. Admissible claims

The following claims are admissible:

1. The trivial zeros form a negative mirror lattice of the completed zeta system.
2. The non-trivial zeros form a fluctuation spectrum tied to prime-distribution irregularity.
3. Zeta-regularized values are finite analytic shadows of divergent positive densities.
4. A density correspondence requires an explicit transformation, measure, or embedding.
5. Dirichlet L-functions likely require character-dependent mirror lattices rather than one universal negative lattice.

## 5. Inadmissible claims without further proof

The following claims are not admissible in literal form:

1. The trivial zeros are primes.
2. Negative even integers are negative primes.
3. Trivial zeros and non-trivial zeros have the same density without specifying a measure transformation.
4. `1+1+1+...=-1/2` as an ordinary summation identity.
5. HPHD proves RH.
6. HPHD proves BSD.

## 6. BSD-adjacent relevance boundary

This repository is BSD-adjacent because the same general analytic pattern appears across L-functions:

```text
arithmetic object -> L-function -> analytic continuation / functional equation -> special values / zeros / rank-like structure
```

However, this repository does not yet make a BSD theorem claim.

The disciplined route is:

1. Build the base zeta mirror-lattice formalism.
2. Extend to Dirichlet L-functions.
3. Extend to modular forms and elliptic-curve L-functions only after the character-dependent case is stable.
4. Treat order of vanishing, special values, regulators, and rank phenomena as later research lanes.

## 7. Operational guardrail

Every future claim should be classified as one of:

- definition;
- lemma;
- conjecture;
- analogy;
- computational experiment;
- theorem proved elsewhere;
- proposed theorem not yet proved;
- HPHD-specific interpretation.

No metaphor should be promoted to theorem without a proof object or external mathematical citation.
