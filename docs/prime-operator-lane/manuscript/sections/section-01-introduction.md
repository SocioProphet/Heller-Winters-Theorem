# Section 1 — Introduction

Status: manuscript draft section.  
Claim class: exposition only; no new theorem claim.  
Source outline: `docs/prime-operator-lane/manuscript/prime-weil-reformulation-outline.md`.  
Source synthesis: `HW-PRIME-WEIL-022`.

## 1.1 Motivation

The Riemann Hypothesis and its Dirichlet generalizations can be approached through the behavior of prime-counting error terms in arithmetic progressions. In the Prime-Weil lane, the object of study is a finite, computable version of that problem: the variance of Chebyshev-weighted prime mass across residue classes in Richter windows.

The guiding idea is simple. Fix a finite unit group

```text
G_P = (Z/PZ)^x
```

and a Richter window `W_K`. The distribution of primes in `W_K` across residue classes of `G_P` determines a finite function on `G_P`. Fourier analysis on the finite abelian group decomposes this function into Dirichlet character modes. The square-root cancellation expected under GRH becomes a finite family of character-sum bounds.

This produces a computable surface for the GRH barrier. It does not remove the barrier.

## 1.2 Contribution

This manuscript presents the Prime-Weil program as a finite arithmetic reformulation of the GRH square-root obstruction.

The contribution is not a proof of RH or GRH. The contribution is a structured package of finite theorem surfaces and diagnostics:

1. an exact finite Parseval variance identity;
2. a base-10 orbit classification of prime factors;
3. a theorem for local and cumulative non-cancelling character counts;
4. a packet-energy hierarchy at finite Richter depths;
5. a finite operator normality theorem for abelian convolution;
6. a three-gate map of the remaining proof obstruction.

The output is a mathematically controlled reformulation. It identifies exactly where several plausible proof routes fail: quotient large sieve, coset dispersion, Cayley quotient spectral gap, and explicit-formula truncation.

## 1.3 What is finite and what is asymptotic

The finite objects in this paper are theorem-grade when stated as finite algebra or finite computation. Examples include:

```text
sum_{h in <10>} chi(h) = 0 iff chi|_<10> is nontrivial,
```

```text
n_nc(p) = (p - 1) / ord_p(10) - 1,
```

and the finite normality of convolution operators on `l^2(G_P)`.

The asymptotic claims needed for RH or GRH are not proved. In particular, the finite packet decomposition does not prove that prime-window character sums obey square-root cancellation for all `K`.

The boundary between these two levels is load-bearing. This manuscript treats finite computations as evidence and structure, not as substitutes for asymptotic estimates.

## 1.4 Base-10 orbit packets

A distinctive feature of the Prime-Weil lane is the role of the base-10 orbit

```text
<10> subset (Z/pZ)^x.
```

For each prime `p`, this orbit determines which local characters cancel over the digit cycle and which do not. This creates a packet structure:

- terminating primes;
- degenerate primes;
- partial-orbit primes;
- full-orbit / Artin primes.

Full-orbit primes have complete local Fourier cancellation over the base-10 orbit. Partial-orbit primes leave non-cancelling quotient characters. These finite distinctions become the packet labels used throughout the manuscript.

The transfer from digit-cycle cancellation to prime-window cancellation remains open. The orbit structure organizes the problem; it does not solve the distribution of primes.

## 1.5 Three locked gates

The Prime-Weil program now has three named proof gates.

Gate 1 is the Coset Variance Theorem. It asks whether between-coset variance can be controlled relative to within-coset variance at polynomial scale in `K`.

Gate 2 is the explicit-formula packet-energy surrogate. It asks whether packet energies can be controlled through zero sums and truncation errors beyond the directly computable range.

Gate 3 is the operator spectral-radius bound. Finite abelian convolution is normal and character diagonalized, so the nontrivial operator norm is exactly the maximum nontrivial character sum. The missing estimate is still the square-root bound for that norm.

All three gates are open.

## 1.6 Non-claim boundary

This manuscript does not prove RH.

This manuscript does not prove GRH.

This manuscript does not construct an infinite Hilbert-Polya operator.

This manuscript does not prove an unconditional variance bound.

This manuscript does not claim that digit-cycle, Rodin, or Midy-type finite arithmetic proves prime-window equidistribution.

This manuscript does not claim that finite diagnostics establish asymptotic behavior.

The intended claim is narrower and stronger: the Prime-Weil framework provides a finite, computable, packet-decomposed reformulation of the GRH square-root barrier, with exact finite theorem surfaces and precisely identified remaining obstructions.
