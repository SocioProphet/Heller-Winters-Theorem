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
C_p(x)=y_p - A_p sqrt(1-x/rho_p) + O(1-x/rho_p).
```

Direct expansion gives

```text
A_p^2 = 2p/(p-1)^3.
```

Checked values:

| `p` | `rho_p` | `A_p` | `A_p^2` |
| ---: | ---: | ---: | ---: |
| 2 | `1/4` | `2` | `4` |
| 3 | `4/27` | `sqrt(3)/2` | `3/4` |
| 5 | `256/3125` | `sqrt(10)/8` | `5/32` |

Correction: the earlier candidate pattern

```text
c_p^2 = 1 - rho_p
```

is false for the raw Puiseux coefficient normalization. It is not a valid next prediction for `p=5`.

Problem: determine whether there is a separately normalized unit-circle component behind the observed `p=2` / `p=3` complementarity, or whether the complementarity was a low-depth artifact. The raw coefficient pattern is now the concrete falsifiable target:

```text
A_p^2 = 2p/(p-1)^3.
```

Open: verify the `p=5` raw coefficient in Heller-Godel and then decide whether a normalized coefficient convention exists that preserves a unit-circle identity.

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

## Register non-claim

This register does not assert progress toward any Clay problem. It records open problems, current scaffolding, and the precise finite/infinite boundary of the prime/operator-lane program.
