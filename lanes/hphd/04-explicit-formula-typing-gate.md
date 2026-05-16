# Explicit Formula + Typing Gate (HPHD)

Status: Draft v0.1  
Lane: HPHD / zeta mirror-lattice  
Purpose: Provide a manuscript-grade *gate* that justifies (i) “background vs oscillations” claims via an explicit formula, and (ii) “negative / regularized density” language via strict typing rules.

---

## 1. Why this file exists

HPHD wants to say:

- Trivial zeros behave like a *rigid negative mirror lattice* (regular cancellation scaffold).
- Non-trivial zeros behave like a *fluctuation spectrum* (prime irregularity signal).
- Certain divergent positive densities admit finite *regularized* negative invariants.

This is admissible only if we tether the metaphors to a formula-level decomposition and forbid category errors with a typing system.

---

## 2. Explicit formula bridge (one equation; each term typed)

Define the Chebyshev function

```math
\psi(x) := \sum_{n\le x} \Lambda(n),
```

where the von Mangoldt function is

```text
Λ(n) = log p  if n = p^k
Λ(n) = 0      otherwise.
```

A canonical explicit-formula representation (for `x>1`, with the usual midpoint convention at discontinuities) is:

```math
\psi(x)
=
 x
-\sum_{\rho}\frac{x^{\rho}}{\rho}
-\log(2\pi)
-\frac12\log\bigl(1-x^{-2}\bigr).
```

Interpretation term-by-term:

1) **Main growth** `x`  
Source: the pole of `ζ(s)` at `s=1` (residue).  
HPHD role: *smooth baseline*.

2) **Non-trivial zero spectrum** `- Σ_ρ x^ρ/ρ`  
Source: non-trivial zeros `ρ` of `ζ(s)` in `0<Re(ρ)<1`.  
HPHD role: *oscillatory fluctuation spectrum* driving prime-counting irregularity.

If RH holds, `ρ = 1/2 + iγ`, so

```math
x^{\rho}=x^{1/2}\,e^{i\gamma\log x},
```

which is an oscillation in `log x` with amplitude scale `x^{1/2}`.

3) **Trivial-zero mirror lattice correction** `-(1/2) log(1-x^{-2})`  
Source: trivial zeros at `-2,-4,-6,...`.  
HPHD role: *rigid negative mirror-lattice correction (regular, non-mysterious).*

The mirror-lattice structure is exposed by expansion:

```math
-\frac12\log(1-x^{-2})
=
\frac12\sum_{n\ge 1}\frac{x^{-2n}}{n}.
```

4) **Completion normalization** `-log(2π)`  
Source: completed zeta normalization; equivalently `ζ'(0)/ζ(0)=\log(2\pi)` so the constant matches the completion layer.  
HPHD role: *completion constant; not prime signal.*

### Manuscript-safe synthesis

The explicit formula implements:

```text
prime-power density  = smooth baseline  + (non-trivial oscillations) + (trivial-lattice/completion corrections).
```

So the “bassline vs prime music” metaphor is permitted only as shorthand for the explicit decomposition above.

---

## 3. Typing rules (so we never lie with “=”)

HPHD uses the following type system.

### Rule T1: Convergent equality vs regularized assignment

If `Σ a_n` diverges, we do not write `Σ a_n = c`. We write a typed assignment:

```math
\Bigl(\sum_{n\ge1} a_n\Bigr)_{\zeta\text{-reg}} := c.
```

or the compact notation already used in this repo:

```math
\sum_{n\ge1} a_n \overset{\zeta\text{-reg}}{=} c.
```

### Rule T2: Regularization is a functional, not a limit claim

A regularized value does **not** assert partial sums converge. It asserts the regularization functional assigns a value compatible with analytic continuation.

### Rule T3: “Negative” must be typed

Whenever HPHD says “negative,” it must be declared as one of:

- **(Sign)**: algebraic sign inside ordinary arithmetic.
- **(Dual/renormalized)**: analytic continuation / subtraction of divergences / regularized invariant.

### Rule T4: Density comparisons require an explicit measure layer

Claims like “same density” are inadmissible unless we explicitly name:

- coordinate choice;
- measure (counting measure, spectral measure, kernel-weighted measure);
- embedding / pushforward map.

### Rule T5: “Negative primes” is never literal

If the phrase is used, it is an HPHD *operator name* for the mirror-lattice structure and must be defined as such. No statement may assert “trivial zeros are primes.”

### Rule T6: Metaphor gating

Metaphors are permitted only when they can be backed by:

- an explicit formula decomposition; or
- a clearly declared transform/kernel that yields the intended comparison.

---

## 4. Minimal checklist before promoting an HPHD claim

Every candidate statement must be tagged as one of:

- definition
- lemma
- conjecture
- analogy
- computational experiment
- theorem (external citation)

If it is an analogy, it must reference the explicit-formula decomposition or a declared transform/measure.

---

## 5. Immediate follow-ons (research lanes)

1) Pick HPHD’s default embedding/kernel for comparing mirror-lattice measures with non-trivial-zero measures.
2) Extend the “mirror lattice” notion from `ζ(s)` to Dirichlet `L(s,χ)` where completion/parity alters trivial-zero structure.
3) Implement explicit-formula experiments that numerically separate:
   - main term,
   - non-trivial oscillations,
   - trivial/completion correction terms.
