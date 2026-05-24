# Prime Operator Lane Open-Problems Register

Status: open-problems register  
Claim class: governance / finite-infinite boundary tracking  
Mathematical content added by this document: none beyond problem statements and boundary accounting

This register records open problems exposed by the finite prime/operator-lane scaffolding. It does not assert progress toward any Clay problem. It records the precise finite/infinite boundary of the current scaffolding.

## HW-OPEN-001 — Hilbert-Pólya finite extension

Finite scaffolding:

- `HW-PRIME-FINITE-OPERATOR-001`
- `HW-PRIME-ANTISYM-OPERATOR-001`
- `HW-PRIME-GAUSSIAN-INT-001`

Problem: construct a self-adjoint operator on a natural infinite-dimensional Hilbert space extending the finite character-operator scaffold whose eigenvalues equal the nontrivial zeros of `zeta(s)` for `Re(s)=1/2`.

Current boundary: the finite `P(7)=210` character-operator eigenvalues approximate finite cutoff character sums. The antisymmetric operator `-iC_{K^-}` gives spectral-coordinate approximations to imaginary parts in the finite model. The gap between finite approximation and actual zero location is the entire open content.

Stieltjes tower refinement. The gap between the finite operator eigenvalue `lambda_chi(B)` approximating spectral data at cutoff `B` and the actual zero ordinate is governed by the Stieltjes constants. The `n`-th order correction to the eigenvalue approximation involves `gamma_n` — the `n`-th moment of the accumulated discrete-to-continuous error between the finite prime sum and its integral approximation. The full tower `{gamma_n}` would need to be controlled to close the gap between the finite operator eigenvalue and the actual spectral data. This is the analytic content of `HW-OPEN-001` stated precisely. The finite program approximates the leading correction; the full tower is not computable from the finite operator alone.

Weil-positivity attack surface. `HW-PRIME-WEIL-001` records the Gaussian-smoothed finite Weil positivity strategy, the GRH-signature growth-rate measurement `|psi(B,chi)|/sqrt(B) < log(B)^2`, and the conditional theorem target separating finite positivity from the open weak-convergence and growth-exponent conditions. This is a cross-reference only: it does not close `HW-OPEN-001` and does not promote the finite diagnostic to a Hilbert-Pólya construction.

Non-claim: the finite operators do not prove RH, do not identify zero ordinates, and do not construct a Hilbert-Pólya operator.

## HW-OPEN-002 — Puiseux coefficient general pattern

Established finite inputs:

For the arity-`p` algebraic generating function

```text
C_p(x)=1+x C_p(x)^p,
```

the critical data are

```text
y_p = p/(p-1),
rho_p = (p-1)^(p-1) / p^p.
```

The principal square-root expansion has raw coefficient `A_p` defined by

```text
C_p(x)=y_p - A_p sqrt(1-x/rho_p) + b_p(1-x/rho_p) + O((1-x/rho_p)^(3/2)).
```

Direct expansion gives the exact leading formula

```text
A_p^2 = 2p/(p-1)^3.
```

The next coefficient is

```text
b_p = (p y_p^(p-1) - binom(p,3)y_p^(p-3)A_p^2)
      / (2 binom(p,2)y_p^(p-2)).
```

Checked values:

| `p` | `rho_p` | `A_p` | `A_p^2` | `b_p` |
| ---: | ---: | ---: | ---: | ---: |
| 2 | `1/4` | `2` | `4` | `2` |
| 3 | `4/27` | `sqrt(3)/2` | `3/4` | `2/3` |
| 5 | `256/3125` | `sqrt(10)/8` | `5/32` | `1/4` |
| 7 | `6^6/7^7` | `sqrt(7/108)` | `7/108` | `4/27` |
| 11 | `10^10/11^11` | `sqrt(11/1000)` | `11/1000` | `2/25` |

Correction: the earlier candidate pattern

```text
c_p^2 = 1 - rho_p
```

is false for the raw Puiseux coefficient normalization.

The falsifiable `p=5` prediction is now algebraically accounted for:

```text
A_5^2 = 5/32,
A_5 = sqrt(10)/8,
b_5 = 1/4.
```

The corresponding Heller-Godel preflight candidate is `HG-MTH-P5 — p=5 Puiseux Preflight`.

Open: determine whether the observed coincidence

```text
b_7 = rho_3 = 4/27
```

has structural meaning or is only a low-depth arithmetic coincidence.

Boundary note: this entry is a finite arithmetic diagnostic. The general theorem belongs in Heller-Godel only after the relevant encoding and Puiseux-normalization surfaces are promoted with explicit normalization conventions.

## HW-OPEN-003 — Eisenstein integer carry

Current state: `HG-FND-007` records a carry mechanism at the current normalized level. In the present finite arithmetic layer, the carry is treated as degree-0 / scalar-valued carry data.

Problem: generalize the carry mechanism to `Z[omega]`-valued carry at `p=3`, where the carry takes values in Eisenstein integers.

Prerequisite: the `p=3` encoding hypothesis must become theorem-grade in Heller-Godel before this can be used as more than a finite arithmetic diagnostic.

Non-claim: this register entry does not assert that the Eisenstein carry construction exists, proves any zero-location statement, or supplies a Yang-Mills mass gap.

## HW-OPEN-004 — Cardinality gap and continuum completion

Finite scaffolding:

- `HW-PRIME-FINITE-OPERATOR-001`
- `HW-PRIME-ANTISYM-OPERATOR-001`
- `HW-PRIME-GAUSSIAN-INT-001`

Problem: the finite operator `T_210` lives on a 48-dimensional complex Hilbert space — finite, therefore countable. The Hilbert-Pólya operator, if it exists, must live on an infinite-dimensional Hilbert space over `R` whose eigenvalues are the Riemann zero ordinates. That target object requires continuum completion.

The gap between finite and continuum is not merely one of dimension. It is a cardinality and completion jump from finite/countable scaffolding to continuum analysis. No countable tower of corrections — including the full Stieltjes tower `{gamma_n}` — bridges this gap by itself. The continuum requires distributional completion. The Hilbert-Pólya operator, if it exists, lives in a space of tempered distributions or a similar analytic completion, not in the bare inductive limit of the finite operators.

This is why the problem is hard: it is not an approximation problem with a convergent sequence of finite corrections. It is a completion problem requiring a fundamentally different construction.

Current boundary: the finite program builds the best computable finite approximation to the spectral structure. The cardinality/completion gap between the finite approximation and the actual spectral problem is not closeable by adding more primes to the cutoff or enlarging `G_P`. It requires a different mathematical object.

Non-claim: this entry does not assert that the Hilbert-Pólya operator does not exist. It records precisely why the finite arithmetic scaffolding cannot construct it directly.

## HW-OPEN-005 — Profinite inductive limit and essential self-adjointness

Finite scaffolding:

- `HW-PRIME-FINITE-OPERATOR-001`
- `HW-PRIME-ANTISYM-OPERATOR-001`
- `HW-PRIME-GAUSSIAN-INT-001`
- `HW-PRIME-PROFINITE-001`

The primorial operators `T_{P_k}` form a compatible inductive system. Their natural analytic completion is

```text
L^2(Z_hat^x, d mu_Haar),
```

the `L^2` space of the profinite completion of the multiplicative group under Haar measure. This is a separable infinite-dimensional Hilbert space canonically defined from the arithmetic structure.

The formal limit operator `T_infinity` on `L^2(Z_hat^x)` has character-indexed eigenvalue data governed by the regularized logarithmic derivative of the corresponding Dirichlet `L`-function. The finite operators `T_{P_k}` approximate this limit surface with error governed by the Stieltjes tower (`HW-OPEN-001`).

Open problem: is the naive convolution operator `T_infinity` essentially self-adjoint on the dense domain formed by the union of the finite Hilbert spaces?

Essential self-adjointness requires controlling the `L^2(Z_hat^x)` growth of the limit kernel `K_infinity`. This growth is governed by the same Stieltjes tower that controls the finite operator eigenvalue approximation. If the Stieltjes tower is Borel summable in the scoped sense of the Yang-Mills Lane VIII Borel-Stieltjes surface, essential self-adjointness becomes plausible, but not established.

The cardinality gap from `HW-OPEN-004` is resolved at the arithmetic-completion level: `L^2(Z_hat^x)` lives at `2^{aleph_0}` but is canonically defined from the arithmetic inductive system via profinite Haar measure, without requiring Osterwalder-Schrader distributional machinery or gauge theory. It is the natural completion of the finite program.

Non-claim: this entry does not assert that `T_infinity` is essentially self-adjoint, that its spectrum matches the target zero-ordinate surface, or that this construction proves RH.

## HW-OPEN-006 — Multi-base error space representation

The choice of base encodes what is treated as the fundamental unit of measurement. Different bases make different aspects of the discrete-to-continuous gap legible. The prime-operator lane has identified the following natural bases, one per level of the `HG-DOC-002` embedding stack:

| Base | Natural unit | Stack level | What becomes legible |
| --- | --- | --- | --- |
| `p` (p-adic) | p-adic valuation | Level 0 | integrality of `FC` numbers, Teichmuller lifts, Euler factors |
| `zeta_p` | cyclotomic root | Level 1 | character values, finite Fourier modes |
| `1/(2i)` | branch-cut unit | Levels 2-3 | analytic / singular decomposition at `p=2` |
| `omega=zeta_3` | Eisenstein unit | Level 4 | `p=3` monodromy, Eisenstein carry |
| `i` | imaginary rotation | operator level | `K^+` / `K^-` real-imaginary splitting |
| `e` | natural growth | Levels 7-8 | RG flow, coupling running, `Lambda_YM` |
| `pi` | periodicity | Level 9 | zero spacing, oscillatory corrections |
| `gamma` | error unit | Gap 6-7 | discrete-to-continuous error, Stieltjes tower |
| `1/gamma` | inverse error unit | Gap 6-7 | zero ordinates as resonances in error space |

The p-adic base is foundational: every other base derives from it or is compared against it through a completion surface. The cyclotomic roots `zeta_p` are roots of unity visible in local p-adic / cyclotomic structures. The imaginary unit `i=zeta_4` is the cyclotomic unit governing the Gaussian-integer operator split. The transcendental bases `e`, `pi`, and `gamma` are completion coordinates modeled through rational approximations and adelic comparison surfaces.

The key insight: base `gamma` is the natural coordinate for the gap between Level 6, the finite carry cocycle, and Level 7, the lattice Hilbert space, because `gamma` is precisely the accumulated error when crossing from discrete harmonic summation to continuous logarithmic integration.

In base `1/gamma` coordinates, the zero-location problem can be restated as a resonance problem in the accumulated-error coordinate. This is a restatement, not a proof, but it identifies a natural coordinate system for the spectral problem.

The Euler product

```text
L(s,chi) = product_p (1 - chi(p)p^(-s))^(-1)
```

is the character-indexed spectral data of `T_infinity` expressed as a product of p-adic local factors: one factor per prime, one p-adic base per factor.

Open: formalize this base hierarchy as a typed bridge connecting the finite arithmetic program, Levels 0-6 with p-adic and cyclotomic bases, to the continuum spectral problem, Levels 9-10 with periodic and transcendental bases, with the `gamma`-base gap precisely identified as the finite/infinite boundary.

Non-claim: this entry does not assert that any base yields a proof of RH, GRH, or Yang-Mills mass gap. It records natural coordinate systems for each level and the open bridge problem between them.

## HW-OPEN-007 — Prime residue oracle and repeating-decimal sieve

Finite scaffolding:

- `HW-PRIME-WINDOW-001`
- `HW-PRIME-FINITE-OPERATOR-001`
- `HW-PRIME-WEIL-001`
- `HW-PRIME-WEIL-002`

Problem: formalize the digit-cycle / residue-class oracle that connects repeating decimal structure, repunit resonances, and prime-window residue transitions.

The candidate oracle surface has three finite components:

1. a repeating-decimal sieve, where the cycle of `1/q` identifies residue-period information through `ord_q(10)`;
2. a first-digit / terminal-digit admissibility bound, where base-10 prime candidates are restricted to `{1,3,7,9}` at the terminal digit, giving the `2/5` admissibility density among digits `0..9`;
3. a residue-transition oracle, where the next-prime candidate transition is constrained by the current residue class, the repunit resonance cycle, and the finite character orbit.

The polynomial orbit analysis from `HW-PRIME-WINDOW-001` is a test surface for this oracle. For `n^2+1`, the orbit in `G_210` has size `16` out of `48`; all even-`n` prime candidates are `1 mod 4`; primes `3 mod 4` never divide values of `n^2+1`; and the gap sequence between even-`n` candidates is an arithmetic progression with common difference `8`.

Open: determine whether the oracle is merely a finite sieve description or whether it yields a reusable bound on Richter-window character sums for polynomial thin sets.

Non-claim: this entry does not predict the next prime, prove infinitude of primes of the form `n^2+1`, prove Landau's fourth problem, prove RH/GRH, or construct a Hilbert-Pólya operator.

## Register non-claim

This register does not assert progress toward any Clay problem. It records open problems, current scaffolding, and the precise finite/infinite boundary of the prime/operator-lane program.
