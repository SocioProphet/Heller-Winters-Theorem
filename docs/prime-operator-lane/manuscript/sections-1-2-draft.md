# Prime-Weil Reformulation Manuscript — Sections 1–2 Draft

Status: manuscript draft.  
Claim class: exposition of already-landed finite theorem surfaces; no new theorem claim.  
Source outline: `docs/prime-operator-lane/manuscript/prime-weil-reformulation-outline.md`.

## Section 1 — Introduction

The Riemann Hypothesis and its Dirichlet generalizations can be read as square-root cancellation statements for prime-counting error terms. In the classical formulation, this cancellation is expressed through the location of zeros of zeta and Dirichlet `L`-functions. The Prime-Weil program developed here does not alter that analytic fact. Instead, it gives a finite arithmetic surface on which the same obstruction can be computed, decomposed, and tested.

The basic object of study is a prime window, called a Richter window in the internal notation. For each depth `K`, the window `W_K` collects primes in a base-10 scale interval. Character sums over residue groups measure how prime mass distributes across finite arithmetic classes in that window. The associated variance is finite, computable, and exactly expressible by Parseval over the character group.

The contribution of this manuscript is not a proof of RH or GRH. The contribution is a finite packet decomposition of the GRH square-root barrier. The decomposition organizes Dirichlet character sums by the base-10 orbit structure of prime factors. It separates terminating, degenerate, partial-orbit, and full-orbit cases; proves exact finite character-count identities; measures packet energies at finite depths; and isolates three proof gates where the classical square-root barrier reappears.

The first theorem-grade finite ingredient is the non-cancelling fraction theorem. For a prime `p` coprime to `10`, the base-10 orbit subgroup

```text
H_p = <10> subset (Z/pZ)^x
```

controls which local characters cancel over a complete digit orbit. The number of nontrivial local characters that do not cancel is

```text
n_nc(p) = (p - 1) / ord_p(10) - 1.
```

This formula is elementary finite character theory, but it is structurally useful. It identifies exactly where orbit quality enters the character packet decomposition. It also shows that full-orbit, base-10 Artin primes have no local non-cancelling characters.

The second theorem-grade finite ingredient is the normality of finite abelian convolution operators. The prime-window operator on a finite residue group is a convolution operator. Since the group is finite abelian, characters diagonalize this operator. Hence the operator is normal and its norm is exactly the maximum absolute character eigenvalue. On the nontrivial subspace, this gives

```text
||T_{P,K}^perp|| = max_{chi != 1} |psi_{W_K}(chi)|.
```

This is a clean finite operator reformulation of the square-root barrier. It is not an infinite Hilbert-Polya construction and does not supply the required norm bound.

The third ingredient is diagnostic rather than theorem-grade. Several natural routes were tested: quotient large sieve, coset dispersion, Cayley quotient spectral gap, and an explicit-formula surrogate. Each route localizes the obstruction in a different language. None crosses it. This is not a failure of the finite framework; it is the expected behavior of a faithful reformulation of GRH. A reformulation that made the barrier disappear would be suspect. A useful reformulation should show exactly where the obstruction lives.

The manuscript therefore has a bounded claim posture. It establishes a finite, computable encoding of the GRH square-root barrier and a set of theorem-grade finite facts around that encoding. It does not claim RH, GRH, a zero-free region, a Hilbert-Polya operator, or an unconditional variance bound.

The rest of the paper proceeds as follows. Section 2 defines the prime-window variance and records the finite Parseval identity. Section 3 classifies base-10 orbit types. Section 4 proves the non-cancelling character-count formula. Section 5 records the finite packet hierarchy at `P=2310`. Section 6 explains the q=37 falsification of a naive orbit-quality model. Section 7 states the three locked gates. Section 8 records the finite operator normality theorem. Section 9 explains the negative diagnostics. Section 10 records the open problems and current stopping point.

## Section 2 — Prime-window variance and the Parseval identity

Let `P` be a squarefree modulus, typically a primorial prefix, and let

```text
G_P = (Z/PZ)^x
```

be its group of reduced residue classes. Let `W_K` denote the Richter prime window at depth `K`. The precise choice of window can be varied, but in this program the base-10 scale is fixed because the orbit classification later depends on multiplication by `10`.

For each residue class `g in G_P`, define the finite prime-window mass

```text
f_K(g) = sum_{p in W_K, p == g mod P} log p.
```

The average mass is

```text
mu_K = (1/|G_P|) sum_{g in G_P} f_K(g).
```

The finite variance of prime mass across reduced residue classes is

```text
Var_P(W_K) = sum_{g in G_P} |f_K(g) - mu_K|^2.
```

Equivalently, one may use a normalized variance by dividing by `|G_P|`; the distinction is only a convention and does not affect the structural statements below.

Let `hat(G_P)` denote the finite character group. For a character `chi`, define the prime-window character sum

```text
psi_{W_K}(chi) = sum_{p in W_K, gcd(p,P)=1} chi(p) log p.
```

The trivial character records the total prime mass in the window. Nontrivial characters record deviations from equidistribution across the finite residue group.

By finite Fourier inversion on `G_P`, the function

```text
f_K - mu_K
```

has no trivial-character component. Its Fourier coefficients are the nontrivial character sums `psi_{W_K}(chi)`, up to the chosen normalization convention. Parseval therefore gives the exact finite identity

```text
Var_P(W_K) = (1/|G_P|) sum_{chi != 1} |psi_{W_K}(chi)|^2
```

under the normalized convention used in the lane.

This identity is unconditional. It is finite linear algebra on the character group of `G_P`. No analytic hypothesis enters.

The analytic content enters when one asks for the size of the nontrivial character sums. A GRH-scale estimate has the form

```text
|psi_{W_K}(chi)| = O(10^(K/2) poly(K))
```

for all nontrivial characters in the relevant family. If such a bound holds uniformly, the variance lies at the square-root scale. Conversely, an off-critical zero in a Dirichlet `L`-function produces a character sum contribution with hyperbolic growth above the square-root line. Thus the variance identity does not prove GRH; it gives a finite observable whose growth is equivalent to the same square-root cancellation problem.

This is the central structural point. The Prime-Weil lane turns GRH into a computable variance problem over finite residue groups. The remaining difficulty is exactly the classical difficulty: prove square-root cancellation for the nontrivial character sums without assuming that all zeros lie on the critical line.

The rest of the construction refines the nontrivial character family into packets. Those packets are not arbitrary. They are induced by the base-10 orbit structure of the prime factors of `P`. This packetization makes the barrier more visible: some packets have exact finite digit-cycle cancellation, some are inert or degenerate, and some remain non-cancelling. But after all finite decomposition is performed, the unresolved analytic requirement remains the same: control the nontrivial character sums at square-root scale.

## Section 2 boundary

The Parseval identity is theorem-grade finite mathematics.

The equivalence between square-root character-sum bounds and GRH-scale behavior is an analytic reformulation, not a proof.

No assertion is made here that the required square-root bounds hold unconditionally.
