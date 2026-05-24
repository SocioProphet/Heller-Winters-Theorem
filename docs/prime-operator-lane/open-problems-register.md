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

## HW-OPEN-006 — Multi-base error-space representation

Finite scaffolding:

- `HW-PRIME-WINDOW-001`
- `HW-PRIME-PROFINITE-001`
- `HW-OPEN-001`
- `HW-OPEN-005`

Different algebraic and transcendental bases make different aspects of the discrete-to-continuous gap legible. The choice of base determines which structure is treated as the fundamental unit of measurement.

In this program, the natural bases for the embedding-stack levels are:

| Base | Natural unit | What becomes legible | Embedding-stack location |
| --- | --- | --- | --- |
| `zeta_p` | cyclotomic unit | finite character values and general `p` Puiseux structure | Levels 0-1 |
| `1/(2i)` | branch-cut unit | analytic / singular decomposition at `p=2` | Levels 2-3 |
| `omega` | Eisenstein unit | `p=3` Puiseux structure and Eisenstein carry | Level 4 / HW-OPEN-003 |
| `gamma` | error unit | discrete-to-continuous gap and Stieltjes tower | finite / infinite boundary |
| `1/gamma` | inverse error unit | zero ordinates as resonances in accumulated-error coordinates | spectral open-problem surface |
| `e` | natural growth | RG flow, coupling running, and `Lambda_YM` scaling | Yang-Mills Levels 7-8 |
| `pi` | periodicity | zero spacing and oscillatory correction terms | continuum spectral surface |
| `i` | rotation | real/imaginary decomposition and `K^+` / `K^-` splitting | Gaussian-integer operator lane |

The Euler-Mascheroni constant `gamma` is the accumulated rectangular error between the discrete harmonic sum and the continuous logarithm:

```text
gamma = lim_{N -> infinity} (sum_{n=1}^N 1/n - log N).
```

Using `gamma` as the base means measuring analytic objects in units of the discrete-to-continuous error itself.

The Laurent expansion

```text
zeta(s) = 1/(s-1) + sum_{n>=0} (-1)^n gamma_n (s-1)^n / n!
```

becomes, after the rescaling `s = 1 + gamma t`,

```text
zeta(1 + gamma t) = 1/(gamma t)
  + gamma_0
  - gamma_1 gamma t
  + gamma_2 gamma^2 t^2 / 2
  - ...
```

This expresses the Stieltjes tower as the Taylor correction structure in the error-unit coordinate.

In this coordinate system, the critical-line form of the zero problem becomes a statement about whether the spectral resonances occur as purely imaginary frequencies in the accumulated-error coordinate. This is a restatement of the zero-location question, not a proof.

Open problem: formalize this multi-base representation as a typed bridge between the finite arithmetic program and analytic continuation. The bridge would need to specify which base changes are algebraic, which are transcendental coordinate changes, and which claims are invariant under the change of base.

Non-claim: this entry does not prove RH, does not identify zero ordinates, does not construct a Hilbert-Pólya operator, and does not transfer proof from arithmetic to Yang-Mills.

## Register non-claim

This register does not assert progress toward any Clay problem. It records open problems, current scaffolding, and the precise finite/infinite boundary of the prime/operator-lane program.
