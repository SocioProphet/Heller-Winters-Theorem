# A1 Gate Minimality Proof Note v2

Status: conditional proof note and reference target for the Catalan A1 harness. This document does not claim a general singularity-class theorem. It fixes the A1 algebraic isolated case under the declared convention and records the scope boundaries that downstream work must respect.

## Convention

Default convention:

```text
A1-sauzin-normalization-v0
```

Local coordinate:

```text
t = 1 - 4x
```

The local A1 model is the square-root branch structure `sqrt(t)`. One circuit around the branch point sends `sqrt(t)` to `-sqrt(t)`. In the Catalan generating function

```text
C(x) = (1 - sqrt(1-4x))/(2x)
```

the normalized discontinuity in the `t` coordinate has leading coefficient `-4` under the chosen lateral convention.

## T1 — admissible A1 gate data

An admissible A1 gate datum consists of:

1. an algebraic isolated A1 singularity with local square-root coordinate;
2. a faithful spatial spin-frame action

```text
rho_spatial: G -> Spin(3) ~= SU(2)
```

with the underlying orientation action obtained by composition with the canonical cover `Spin(3) -> SO(3)`;
3. a non-abelian active-set action on the A1 active sector;
4. a central order-2 element `zeta_G in G` realizing the Spin-lift of the nontrivial loop class;
5. polarization compatibility: the active-set pairing `Q_A` is the transported symplectic form from the A1 source data.

## T2 — A1 minimality claim

Within the above admissible A1 class, the minimal single-group realization is the spin group

```text
G = Spin(3) ~= SU(2)
```

with active sector the defining two-dimensional spinor representation and central element

```text
zeta = -I in SU(2).
```

This is a conditional, scope-bound statement: it is about the A1 square-root case with a two-dimensional complex active set and symplectic pairing. It is not a theorem for `A_n`, `D_n`, `E_n`, non-algebraic, non-isolated, orthogonal, higher-rank, Spin^c, or noncompact real-form cases.

## Proof skeleton

### Step 1 — A1 monodromy supplies a Z/2 sign

The A1 square-root local model has nontrivial monodromy `sqrt(t) -> -sqrt(t)`. Under `A1-sauzin-normalization-v0`, the Catalan reference model realizes this as hard multiplier `-1` and normalized jump coefficient of absolute value `4`.

### Step 2 — faithful spatial action must land in Spin(3)

A map into `SO(3)` alone loses the central sign because the kernel of the cover

```text
Spin(3) -> SO(3)
```

is `{+I,-I}`. The A1 datum requires the sign to remain a group element, so the faithful target in condition (ii) is `Spin(3) ~= SU(2)`, not merely `SO(3)`.

### Step 3 — SO(3) is excluded by the faithful-spin condition

`SO(3)` carries the orientation action but not the central spin element acting as `-1` on the active spinor sector. Under v2, `SO(3)` is excluded directly by condition (ii), not by the polarization condition alone.

### Step 4 — U(1) is excluded by non-abelian active action

`U(1)` can represent an order-2 sign as a group element and can sit as a maximal torus inside `SU(2)`. It is excluded only by condition (iii): the active-set action must be non-abelian.

### Step 5 — SU(2) realizes all A1 requirements

The defining representation of `SU(2)` is two-dimensional, irreducible, faithful into `Spin(3)`, symplectic, and carries the central element `-I`. The Pauli matrices provide a concrete non-abelian active-set witness.

## Harness obligations

The reference implementation for this note is:

```text
harness/catalan_a1_harness.py
```

The harness verifies eight predicates:

1. Catalan coefficient enumeration;
2. Stokes multiplier `-1`;
3. Catalan jump coefficient `4` up to sign convention;
4. symplectic pairing preservation;
5. non-abelian commutator witness;
6. spin-lift provenance with `zeta=-I`;
7. faithful spatial spin-frame action;
8. irreducible filtration of the defining representation.

The committed reference report is:

```text
harness/reference_reports/catalan_a1_report.json
```

Hash-chain head:

```text
0e8469cc953d2e340b2eda0e929e1e143bde041e82479948c4784801e13b7075
```

## Non-claims

This proof note does not claim:

- a general ADE minimality theorem;
- a result for `A_n` with `n >= 2`;
- a result for orthogonal active pairings;
- a result for `SO(3)` as a single-group substitute for `Spin(3)`;
- a result for non-isolated or non-algebraic singularities;
- a proof of P vs NP or any Clay problem;
- an empirical validation of Lawful Learning.

## Open subclaims

C-1. Categorical universal property: restate minimality as a terminal or initial object in the appropriate category of A1 admissible gate data.

C-2. Pair theorem: formulate the `(G_spatial, G_active) = (SO(3), SU(2))` alternative when the single-group framing is relaxed.

C-3. Boundary witnesses: add expected-fail harness rows for out-of-scope cases.

C-4. Spin^c extension: study U(1)-extended spin lifts.

C-5. Real-form variants: study noncompact real forms such as `SL(2,R)` under explicitly changed polarization conditions.
