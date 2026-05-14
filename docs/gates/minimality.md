# Gate Minimality — A1 Alignment

Status: aligned with `docs/proofs/a1-gate-minimality.md` v2.

This document records the gate-minimality conditions for the algebraic isolated `A_1` case under the convention:

```text
A1-sauzin-normalization-v0
```

It is not a general ADE theorem and does not extend to non-isolated, non-algebraic, orthogonal, higher-rank, Spin^c, or noncompact real-form cases without a separate extension declaration.

## Minimality conditions

### (ii) Spatial spin-frame action

The spatial action is:

```text
rho_spatial: G -> Spin(3) ~= SU(2)
```

and it must be a continuous faithful homomorphism. The underlying orientation action is obtained by composition with the canonical two-to-one cover:

```text
pi: Spin(3) -> SO(3).
```

This is deliberately a Spin target, not merely an `SO(3)` target. The central sign that matters in the A1 case lives in the spin cover.

## (iv) Z/2 loop class realized as a central element

There exists a central element

```text
zeta_G in G
```

of order two such that `rho_spatial(zeta_G)` is the nontrivial element of

```text
ker(Spin(3) -> SO(3)) = {+I,-I}.
```

Equivalently, the topological loop class in `pi_1(SO(3))` is realized inside the group datum as the order-two central element produced by the Spin lift built into condition (ii).

For `G = SU(2)`, the central element is:

```text
zeta = -I.
```

The bare statement “loop class in pi_1(G)” is not the right local condition here, because `pi_1(SU(2))=0`. The group-theoretic content is the spin-lifted central element, not a loop class internal to `SU(2)`.

## (v) Polarization compatibility

The active-sector pairing `Q_A` is preserved by:

```text
rho_active: G -> Sp(V_A, Q_A).
```

The pairing `Q_A` is the parallel transport of the source pairing from the A1 datum.

Under the A1 assumptions:

```text
dim_C V_A = 2
Q_A symplectic
rho_spatial faithful into Spin(3)
```

condition (v)'s bare invariance clause is automatic for the minimal candidate: the defining two-dimensional representation of `SU(2)` is symplectic.

The role of (v) is therefore not to exclude `SO(3)` at the bare group-selection level. Under v2, `SO(3)` is excluded by (ii). Condition (v) instead plays three structural roles.

### Source-active coherence

`Q_A` on `V_A` must match the transported source pairing. The active representation must preserve the actual A1 polarization, not an arbitrary bilinear form chosen after the fact.

### Branch selection

If one weakens both (ii) and (v), the orthogonal branch reappears as a competing minimal candidate. In Frobenius-Schur language, the A1 proof note fixes the spinor branch:

```text
epsilon = -1
```

rather than the orthogonal branch:

```text
epsilon = +1.
```

Condition (v) locks the framework to the spinor/symplectic branch.

### Forward compatibility

For non-A1 cases, higher Milnor number, different lattice signatures, and different pairings actively select between symplectic, orthogonal, and unitary branches. Condition (v) is the clause that carries that future data.

## U(1) status

`U(1)` can satisfy some of the A1 conditions:

- `U(1)` embeds in `SU(2)` as a maximal torus;
- it contains the order-two element `-I`;
- it can represent the `Z/2` sign as a group element;
- it can preserve a symplectic form on a two-dimensional eigenspace decomposition.

But `U(1)` is excluded by condition (iii): the active-set action must be non-abelian. This is the precise sense in which `U(1)` can carry the sign but cannot satisfy the active-set role.

## Local conclusion

For the in-scope A1 datum, the minimal single-group realization is:

```text
G = Spin(3) ~= SU(2)
```

with central element:

```text
zeta = -I.
```

This conclusion is scope-bound and convention-bound.

## Cross-references

- `docs/proofs/a1-gate-minimality.md`
- `docs/scope/singularity-classes.md`
- `harness/catalan_a1_harness.py`
- `harness/reference_reports/catalan_a1_report.json`
