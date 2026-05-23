# Auxiliary Intersection Fallacy

Status: proof-hazard note  
Scope: all Heller-Winters Programme lanes

## Definition

The auxiliary intersection fallacy occurs when a passage proves a statement on an intersection

```text
X ∩ A
```

but states or implies the statement on the full source class

```text
X.
```

Equivalently, it proves

```text
X and A -> Y
```

but claims

```text
X -> Y
```

without proving

```text
X -> A.
```

## Why it matters

The Heller-Winters Programme uses filters, envelopes, residual channels, mirror-lattice encodings, operator constraints, and finite-window empirical gates. These are useful instruments, but they can silently narrow the domain.

A result over a narrowed domain is not wrong. The error is dropping the narrowing premise while preserving theorem-strength language.

## Canonical bad pattern

```text
Let X be the classical condition.
Let A be an auxiliary model condition.
We show that X and A force Y.
Therefore every X satisfies Y.
```

This is invalid unless the proof also establishes `X -> A`.

## Correct forms

Conditional form:

```text
For every object satisfying X and A, Y holds.
```

Bridge form:

```text
For every object satisfying X, A holds. Since X and A imply Y, every X satisfies Y.
```

Equivalence form:

```text
X and A define the same class. Therefore results over A transfer to X.
```

## Heller-Winters examples to guard

| Source class `X` | Auxiliary condition `A` | Unsafe promotion |
|---|---|---|
| prime events | localization-cell membership | all primes satisfy a claim proved only for selected cells |
| von Mangoldt signal | residual-envelope condition | exact arithmetic behavior inferred from envelope membership |
| zeta-zero data | mirror-lattice or oscillator constraint | zero-location claim inferred from an auxiliary zero condition |
| admissible tuple class | positive singular-series heuristic | existence claim inferred from admissibility alone |
| empirical phase gate | finite-window survival | asymptotic theorem inferred from finite-window survival |

## Reviewer instruction

When reading a theorem-strength passage, mark every premise. If a premise appears before the proof but disappears from the conclusion, require one of:

1. a bridge lemma;
2. a cited classical theorem;
3. a downgrade to conditional/conjectural/heuristic status;
4. a narrowed conclusion retaining the auxiliary premise.

## Safe verdict language

Use:

```text
The result holds inside the auxiliary model under the stated bridge assumptions.
```

Do not use:

```text
The auxiliary model proves the classical theorem.
```

unless the bridge has already been discharged.