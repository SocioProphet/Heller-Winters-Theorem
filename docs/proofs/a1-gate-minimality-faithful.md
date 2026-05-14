# A1 Gate Minimality: Faithful Triad Action Version

Status: draft v1, faithful-triad branch  
Claim class: theorem-candidate proof note  
Location: `docs/proofs/a1-gate-minimality-faithful.md`

## 0. Purpose

This note records the faithful-triad version of the A1 gate-minimality result.

It is parallel to the non-faithful branch. The two branches answer different questions:

- **T2:** non-faithful triad action; the spin data is bundled into `G = SU(2)` and the central `-I` is an element of `G`.
- **T2':** faithful triad action; `G = SO(3)` acts faithfully on the spatial triad and the central `-I` lives in an auxiliary `Spin(3)`-structure on `V_A`, not in `G`.

Under T2', the minimal connected compact Lie group acting faithfully on the triad is `SO(3)`, equipped with canonical auxiliary spinor data on the two-dimensional polarization space.

## 1. Categorical setup

Let `A'_1` denote the category whose objects are tuples

```text
(G, rho_spatial, V_A, Q_A, S, gamma)
```

where:

- `G` is a connected compact Lie group;
- `rho_spatial: G -> SO(3)` is faithful and nontrivial;
- `V_A` is a two-dimensional complex vector space carrying a non-degenerate symplectic form `Q_A`;
- `S` is an auxiliary `Spin(3)`-structure on `V_A`, represented by a homomorphism `sigma: Spin(3) -> Sp(V_A, Q_A) = SL(2,C)`;
- `gamma` is the distinguished nontrivial loop class in `pi_1(SO(3)) = Z/2`.

The compatibility requirement is that the faithful spatial action of `G` on the triad, pulled through `rho_spatial`, has a projective action on `P(V_A)` whose linear lift is carried by the auxiliary `Spin(3)`-structure.

Morphisms preserve the group action, spatial representation, auxiliary spin structure, symplectic form, and distinguished loop class.

The key ontological distinction is that `V_A` is not a linear representation of `G` in this category. It carries auxiliary `Spin(3)` symmetry. The group `G` acts through compatibility with that auxiliary structure.

## 2. T1': admissibility under faithfulness

An object of `A'_1` realizes the A1 gate semantics when the following conditions hold:

1. **Lie regularity.** `G` is a connected compact Lie group.
2. **Faithful triad action.** `rho_spatial: G -> SO(3)` is faithful and nontrivial.
3. **Non-abelian active set.** The action induced on the polarization space through the auxiliary spin structure is non-abelian.
4. **Coherent loop class.** The generator `gamma in pi_1(SO(3)) = Z/2` lifts through the auxiliary `Spin(3)`-structure to the central element `-I`.
5. **Polarization compatibility.** The auxiliary representation `sigma: Spin(3) -> SL(V_A, Q_A)` preserves `Q_A`, and the induced action on `P(V_A)` factors through the projective quotient.

## 3. T2': minimality under faithfulness

The category `A'_1` has a unique minimal object up to isomorphism:

```text
(SO(3), id, C^2, epsilon, sigma_spinor, gamma_can)
```

where `sigma_spinor: Spin(3) -> SL(2,C)` is the canonical spinor representation and `gamma_can` generates `pi_1(SO(3))`.

In this faithful version, the central element `-I` is not an element of `G = SO(3)`. It is the image of the lifted loop endpoint under the auxiliary spinor structure on `V_A`.

## 4. Proof sketch

### Step 1: Reduce candidates by faithfulness

The connected compact subgroups of `SO(3)` are, up to conjugacy:

```text
{e}, SO(2), SO(3)
```

Faithfulness requires `G` to inject into `SO(3)`. Nontriviality excludes `{e}`. Thus the only candidates are `SO(2)` and `SO(3)`.

### Step 2: Eliminate `SO(2)`

`SO(2)` is abelian. Any induced image through the projective auxiliary spin structure remains abelian. Therefore condition (iii), non-abelian active set, fails.

Thus `G = SO(3)` is the only connected faithful candidate.

### Step 3: Verify `SO(3)` is admissible

For `G = SO(3)`:

- `SO(3)` is connected, compact, and Lie;
- the identity map into `SO(3)` is faithful;
- the spinor representation of `Spin(3) = SU(2)` on `C^2` is non-abelian;
- the generator of `pi_1(SO(3))` lifts to the nontrivial central element of `Spin(3)`;
- the canonical spinor representation preserves the symplectic form `epsilon`.

Therefore the canonical tuple is admissible.

### Step 4: Necessity and uniqueness of the auxiliary spin structure

`SO(3)` has no faithful two-dimensional complex linear representation. Its irreducible complex representations are integer-spin representations of dimensions `2l + 1`, hence odd-dimensional. A reducible two-dimensional representation is a sum of trivial representations and cannot be faithful.

Therefore the two-dimensional symplectic action on `V_A` cannot be a faithful linear representation of `SO(3)`. It must be represented projectively, and the linear lift is supplied by the auxiliary `Spin(3)`-structure.

Given two auxiliary spin structures inducing the same projective action, Schur uniqueness for the irreducible spinor representation implies that they differ by a scalar. Preservation of `Q_A` forces the scalar to be `+1` or `-1`, and the coherent loop condition fixes the canonical branch by requiring the lifted generator to terminate at `-I`.

### Step 5: Minimality

Steps 1 and 2 force `G = SO(3)`. Step 4 forces the auxiliary spin structure to be canonical up to the central branch fixed by the loop condition. The remaining data are canonical. Hence the faithful admissible category has a unique minimal object up to isomorphism.

## 5. Counterexample witnesses when conditions are removed

- Remove non-abelianness: `SO(2)` is faithful and connected but abelian.
- Remove polarization compatibility: `SO(3)` acting only on its standard real triad lacks the two-dimensional symplectic spinor witness.
- Remove loop coherence: the wrong central branch lifts the distinguished loop to `+I` instead of `-I`.
- Remove faithfulness: the non-faithful theorem returns `SU(2)` with kernel `{+I,-I}` in the map to `SO(3)`.
- Remove connectedness: finite non-abelian subgroups and their binary covers enter, but they fail the connected Lie-group condition.

## 6. Harness interpretation under T2'

The Catalan A1 harness predicates keep the same numerical values under T2 and T2'. What changes is the witness object.

Under T2':

- the `zeta = -I` predicate tests the auxiliary spin structure, not an element of `G`;
- pairing preservation tests that `sigma` lands in `SL(V_A) = Sp(V_A, Q_A)`;
- Stokes and jump checks witness the abstract `Z/2` monodromy;
- the commutator predicate witnesses non-abelianness through the auxiliary spin algebra, while the Lie algebra isomorphism with `so(3)` preserves the numerical value.

## 7. Structural note

Under T2', `Spin(3)` is auxiliary data on `V_A`. Its identification with the universal cover of `SO(3)` is specific to A1 and should not be built into the general definition. In higher Ak cases, the auxiliary group may differ from the universal cover of the spatial-symmetry group.

## 8. Summary

T2' states that, under faithful action on the spatial triad, the minimal connected compact Lie group is `SO(3)`, with the A1 sign data carried by an auxiliary `Spin(3)`-structure on `V_A`.

T2 and T2' are not competing theorems. They allocate the spin data differently.
