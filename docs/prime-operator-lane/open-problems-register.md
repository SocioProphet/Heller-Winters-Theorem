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

Non-claim: the finite operators do not prove RH, do not identify zero ordinates, and do not construct a Hilbert-Pólya operator.

## HW-OPEN-002 — Puiseux coefficient general pattern

Established finite inputs:

- At `p=2`, the coefficient side records the `1/2` component.
- At `p=3`, the coefficient side records the `sqrt(3)/2` component.
- These two components satisfy the complementary unit-circle identity

```math
\left(\frac12\right)^2+\left(\frac{\sqrt3}{2}\right)^2=1.
```

Problem: verify the next case and prove the general Puiseux coefficient pattern. The falsifiable next prediction is that the `p=5` coefficient should satisfy

```math
c_5^2=1-\rho_5.
```

Open: verify the `p=5` case directly and prove the general formula

```math
c_p^2=1-\rho_p.
```

Boundary note: the `p=2` and `p=3` observations are not yet a general theorem. The general theorem belongs in Heller-Godel once the encoding hypothesis is promoted from method-grade assembly to theorem-grade claim.

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

## Register non-claim

This register does not assert progress toward any Clay problem. It records open problems, current scaffolding, and the precise finite/infinite boundary of the prime/operator-lane program.
