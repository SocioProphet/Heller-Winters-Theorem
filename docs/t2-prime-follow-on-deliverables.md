# T2' Follow-On Deliverables

Status: bounded downstream patch plan  
Scope: gate-minimality language, scope-singularity framing, Catalan harness interpretation, categorical C-1', and A2 scoping boundary  
Claim class: theorem-follow-on discipline, not a new proof claim

## 0. Purpose and notation guard

This document records the downstream changes required once **T2'** is the committed theorem framing.

The source notes for this tranche contained several inline mathematical symbols that were not recoverable in plain text. This document therefore names the mathematical roles explicitly rather than inventing missing notation. Any later formalization may replace the prose names with the canonical symbols once the notation table is locked.

Execution order:

1. apply the gate-minimality patch v2;
2. apply the scope-singularity patch v2;
3. add a predicate-interpretation table for the Catalan harness;
4. add C-1' as the categorical formulation under the broadened category;
5. keep A2 scoping separated as new research territory.

The first four items are mechanical or bounded. The fifth is not mechanical and must not be treated as a direct extension of T2'.

---

## 1. Gate-minimality patch v2

### 1.1 Required framing

The v1 language used the phrase:

```text
faithful into Spin(3)
```

That phrase is ambiguous. It can be read as either:

1. `G` is a faithful subgroup of `Spin(3)`, which collapses the framing toward the T2 reading; or
2. `G` acts faithfully through the `Spin(3)` cover, which blurs the distinction between T2 and T2'.

Under T2', the unambiguous replacement is:

```text
faithful into SO(3); the auxiliary Spin(3)-structure lives on V_A
```

### 1.2 Load-bearing distinction

The auxiliary `Spin(3)`-structure is data about `V_A`. It is not data about `G`.

For the A1 case, the auxiliary `Spin(3)`-structure is incidentally isomorphic to the universal cover of the connected spatial symmetry group. That coincidence must not be promoted into the definition of gate-minimality, because it is not expected to survive the A2 transition.

### 1.3 Search-and-replace table

| v1 phrase | T2' replacement | Reason |
| --- | --- | --- |
| faithful into `Spin(3)` | faithful into `SO(3)` | `G` is constrained at the spatial-symmetry level. |
| `G` acts faithfully through `Spin(3)` | `G` acts faithfully as a closed connected subgroup of `SO(3)` | Avoids conflating the group action with the auxiliary cover. |
| `Spin(3)` is the gate-minimal group | `SO(3)` is the maximal connected admissible spatial group; `Spin(3)` is auxiliary structure on `V_A` | Separates spatial symmetry from vector-space structure. |
| the cover witnesses gate minimality | the auxiliary structure witnesses the form on `V_A` | The witness belongs to the representation data. |
| universal cover of `G` | auxiliary `Spin(3)`-structure on `V_A` | Prevents accidental T2/T2' collapse. |

### 1.4 Patch rule

Every document invoking A1 gate-minimality must state which theorem fragment it uses:

- **T2:** the stricter reading where the group-level cover is treated as the object of interest;
- **T2':** the committed reading where `G` is faithful into `SO(3)` and the auxiliary `Spin(3)`-structure lives on `V_A`;
- **fragment-only:** a document may use only a numerical or harness fragment, but must then avoid group-level claims.

---

## 2. Scope-singularity patch v2

### 2.1 Required scope declaration

Any document invoking A1 gate-minimality must include a scope declaration:

```text
A1 gate-minimality scope: T2 | T2' | fragment-only
```

A document with no declaration is not eligible for theorem-level reuse.

### 2.2 Boundary table under T2'

| Row | Boundary item | T2' effect | Failure mode if not patched |
| ---: | --- | --- | --- |
| 1 | Group-action target | revised | Treating `Spin(3)` as the target of the faithful group action collapses T2' back into T2 ambiguity. |
| 2 | Auxiliary structure | revised | Treating auxiliary `Spin(3)` as data about `G` rather than data about `V_A`. |
| 3 | Numerical Catalan predicates | unchanged | Numerical results are unaffected by T2/T2' semantics. |
| 4 | Stokes and jump predicates | unchanged | These remain harness-level predicates unless promoted by interpretation metadata. |
| 5 | Predicate interpretation | revised | The same number may witness different theoretical content under T2 versus T2'. |
| 6 | External analytic scope | unchanged | External analytic claims remain outside gate-minimality. |
| 7 | Continuum or mass-gap scope | unchanged | No continuum or Yang-Mills mass-gap claim is introduced by T2'. |
| 8 | A2 generalization | unchanged as blocker | A2 remains a new research problem, not a mechanical corollary. |
| 9 | Categorical formulation | revised | The category must be broadened before the universal-property claim has non-trivial content. |

### 2.3 Patch rule

Rows 1, 2, 5, and 9 must be revised wherever the older scope-singularity table appears. Rows 3, 4, 6, 7, and 8 remain materially unchanged.

---

## 3. Catalan harness interpretation update

### 3.1 Numerical content unchanged

The five-predicate numerical harness content does not change under T2'. The same computed predicate values remain valid as numerical statements.

What changes is the interpretation layer.

### 3.2 Predicate interpretation shift

Under T2, the spin predicate may be read as testing a group-level object directly.

Under T2', the same check is interpreted as testing the auxiliary spin structure on `V_A`. That auxiliary structure is representation data, not a faithful group-action target.

### 3.3 Required metadata addition

The Catalan harness should remain version-agnostic by adding a predicate-interpretation table reference to the harness metadata:

```json
{
  "predicateInterpretationTable": "registry/t2-prime-predicate-interpretation.v0.1.json",
  "gateMinimalityScope": "T2'"
}
```

This changes the hash-chain head exactly once when the interpretation table is added. It should not change again unless the harness source or predicate interpretation table changes.

### 3.4 Predicate interpretation table shape

The table must include:

- predicate identifier;
- numerical value or result reference;
- T2 interpretation;
- T2' interpretation;
- claim class;
- downstream reuse rule.

Minimum claim discipline:

```text
same number, different witness object
```

The harness proves the numerical predicate. The interpretation table states what that predicate is allowed to witness under each theorem framing.

---

## 4. C-1': categorical formulation

### 4.1 Why C-1 needed revision

The strict category used by the earlier C-1 formulation collapses the universal-property claim too far. Under strict morphisms, the connected A1 formulation becomes effectively singleton-shaped, so terminality risks becoming tautological.

C-1' restores non-trivial content by broadening the category to admit disconnected admissible groups.

### 4.2 Recommended two-clause statement

C-1' should be stated in two clauses:

```text
SO(3) is the maximal connected admissible spatial group.
The terminal admissible group is the broadened disconnected admissible group carrying the corresponding auxiliary structure.
```

When the terminal object is written with its final canonical notation, the relation must state:

```text
SO(3) is the identity component of the terminal admissible group.
```

This keeps both statements mathematically meaningful:

1. the connected result preserves the T2' gate-minimality content;
2. the broadened result gives the universal-property formulation non-trivial shape.

### 4.3 Proof method

The proof uses the same Schur-uniqueness argument used in Step 4b of T2'. The uniqueness is attached to the admissible action and auxiliary structure, not to an accidental identification of `G` with an auxiliary cover.

### 4.4 Claim boundary

C-1' is a categorical restatement of the T2' downstream structure. It is not a new analytic theorem and does not promote A2.

---

## 5. A2 scoping boundary

### 5.1 Structural template

The T2' template generalizes only as a template:

```text
spatial-symmetry group + auxiliary group preserving the form on V_A
```

The central element of the auxiliary group should lift the relevant loop class.

### 5.2 A2 difference

For A2, the loop class is expected to involve a third root of unity rather than the A1 involutive class. The auxiliary group is conjecturally of SU(3)-type, with center of Z3-type. The form on `V_A` is conjecturally Hermitian rather than symplectic.

This is a conjectural scoping statement only.

### 5.3 Open research question

The spatial-symmetry group for A2 is not identified in this patch.

Resolving it requires understanding the topology of the A2 Milnor base. That is the substantive A2 work and must not be represented as a mechanical extension of T2'.

---

## 6. Required downstream artifacts

The next mechanical tranche should add or update:

1. `registry/t2-prime-predicate-interpretation.v0.1.json`;
2. harness metadata pointing to that table;
3. any prior gate-minimality text containing ambiguous `Spin(3)` group-action language;
4. any prior scope-singularity table lacking a T2/T2' declaration;
5. C-1' as a half-page categorical appendix once canonical notation is available.

---

## 7. Completion status for this patch

This document completes the follow-on framing and patch instructions.

It does not claim that all downstream source files have already been rewritten. It is the controlling patch document for the T2' transition.
