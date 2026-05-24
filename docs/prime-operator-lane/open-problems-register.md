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

## Register non-claim

This register does not assert progress toward any Clay problem. It records open problems, current scaffolding, and the precise finite/infinite boundary of the prime/operator-lane program.
