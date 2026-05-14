# Corrected A₂ minimality sketch

**Status:** controlled correction note.  
**Scope:** replaces the withdrawn cubic-invariant A₂ sketch.  
**Boundary:** sketch-level only; not a theorem, not a proof of A₂ gate-minimality, and not a continuum Yang--Mills claim.

## 1. Correction

The earlier A₂ sketch used an incorrect invariant claim:

> SU(3) preserves a unique cubic invariant on the fundamental representation `V_A = C^3`.

That statement is false. It conflates the adjoint representation with the fundamental representation.

Correct invariant facts for the fundamental representation `V = C^3` are:

| Form on `V = C^3` | SU(3)-invariant? | Note |
|---|---:|---|
| Hermitian form `H(v,w) = v†w` | yes | unitary structure |
| Symmetric bilinear form `v^T w` | no | would imply an orthogonal branch |
| Alternating volume `epsilon(v,w,u) = det(v,w,u)` | yes | determinant-one structure |
| Symmetric trilinear in `Sym^3 V*` | no | no trivial summand in `Sym^3 V*` |
| `d^{abc}` cubic tensor | yes on adjoint | lives on the `8`-dimensional adjoint, not `C^3` |

Therefore the cubic-invariant version of the A₂ sketch is withdrawn.

## 2. Corpus convention: lattice tower, not free path choice

The program uses `A_1, A_2, D_4, E_8` in the lattice / Lie-algebra tower sense.

The intended tower is:

```text
A_1  <-> rank-1 root system       <-> sl(2) / SU(2) <-> mu_2
A_2  <-> Eisenstein / A2 lattice  <-> sl(3) / SU(3) <-> mu_3
D_4  <-> Hurwitz quaternion lane  <-> Spin(8) triality
E_8  <-> octonion / Cayley lane   <-> E8 structure
```

Accordingly, the corrected A₂ default is not a choice between unrelated paths. It follows the `A_n <-> sl(n+1)` rule:

```text
G_{A2} = SU(3)
V_A    = C^3
zeta   = omega I_3, where omega = exp(2 pi i / 3)
```

## 3. Dimension correction

`SU(3)` has no faithful two-dimensional complex representation. The smallest non-trivial irreducible representations are:

```text
3      fundamental
bar 3  antifundamental
8      adjoint
```

Therefore an A₁ setup with `dim V_A = 2` cannot extend to A₂ with the same `dim V_A` and faithful `SU(3)` action. The minimal faithful A₂ choice is `V_A = C^3` with the fundamental representation.

## 4. Corrected polarization compatibility

For A₂ the polarization compatibility should be stated as two clauses.

### (v_A2) Preserved Hermitian and volume structures

The active representation preserves:

```text
H_A : V_A x conjugate(V_A) -> C
epsilon_A in wedge^3 V_A^*
```

These are the Hermitian form and alternating volume form on `C^3`.

### (v_A2') No additional symmetric bilinear structure

The active representation does **not** preserve any symmetric bilinear form on `V_A`.

This exclusion is necessary because `SO(3) < SU(3)` can preserve both a Hermitian form and an alternating volume form through the complexified standard representation. It is distinguished by preserving an additional symmetric bilinear form. The A₂ branch must exclude that orthogonal structure explicitly.

## 5. Corrected A₂ minimality conjecture

> **Corrected sketch conjecture `T_A2`.** Under the A₂ lattice-tower convention, with `(i)--(iv)` restated for `mu_3` monodromy and a central element of order `3`, and with `(v_A2)` plus `(v_A2')`, the admissible A₂ class has a unique minimal representative up to isomorphism:
>
> ```text
> (SU(3), rho_def),    V_A = C^3,    zeta = omega I_3.
> ```
>
> This is a sketch target, not a theorem.

## 6. Open Spin-target issue

The A₂ spatial / spin-frame target is not fixed by this correction note.

Open candidates include:

```text
SU(3) itself
SU(4) ~= Spin(6)
A2 -> D4 lattice-tower embedding
```

This correction note does not select among those targets. It only corrects the A₂ representation-theoretic invariant data and prevents the false cubic-on-fundamental claim from propagating.

## 7. Product structure with A₁

The `mu_6 = Z[omega]^x` structure suggests that the combined A₁/A₂ gate should be treated as a product of the `mu_2` and `mu_3` components:

```text
A1 component: SU(2), center element -I
A2 component: SU(3), center element omega I_3
combined order: lcm(2, 3) = 6
candidate product: SU(2) x SU(3)
representation surface: C^2 tensor C^3 = C^6
```

This is a future product-gate target. It is not established by the corrected A₂ sketch.

## 8. Non-claims

This note does not claim:

- that A₂ minimality is proved;
- that the A₂ Spin-target has been selected;
- that a cubic invariant exists on the SU(3) fundamental representation;
- that adjoint `d^{abc}` data may be used as a fundamental-representation invariant;
- that the A₁ proof transfers automatically to A₂;
- that the `SU(2) x SU(3)` product gate is proved;
- that any continuum Yang--Mills mass-gap consequence follows from this sketch.

## 9. Implementation consequence

Any downstream A₂ note or issue must use:

```text
Hermitian + alternating volume + no symmetric bilinear
```

not:

```text
Hermitian + cubic d-symbol on C^3
```

The adjoint `d`-symbol remains valid adjoint-representation data, but it is not the A₂ fundamental-representation polarization.
