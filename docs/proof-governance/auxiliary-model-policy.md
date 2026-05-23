# Auxiliary Model Proof Policy

Status: governance scaffold  
Scope: Heller-Winters Programme, all lanes  
Purpose: prevent auxiliary constructions from being promoted into theorem-strength claims without an explicit bridge obligation.

## Rule

An auxiliary model may organize, visualize, filter, or generate candidate structure. It does not transfer theorem status from the model to the classical object unless the required bridge is declared and proved or cited.

In symbols, proving

```text
X and A -> Y
```

must not be stated as

```text
X -> Y
```

unless the repository also carries a bridge proving

```text
X -> A
```

or an equivalence proving

```text
X <-> A.
```

Here `X` is the classical source condition, `A` is the auxiliary condition, and `Y` is the target claim.

## Required bridge labels

Every theorem-strength use of an auxiliary object must label the bridge type as one of the following.

| Bridge label | Meaning | Permitted theorem-strength use |
|---|---|---|
| `definition` | auxiliary object is only notation for the classical object | yes, after definition is explicit |
| `source_to_auxiliary` | `X -> A` is proved or cited | yes for conclusions requiring `A` |
| `auxiliary_to_source` | `A -> X` is proved or cited | no for all-`X` claims unless paired with reverse direction |
| `equivalence` | `X <-> A` is proved or cited | yes |
| `conditional` | bridge holds under named hypotheses | only with hypotheses retained |
| `computational` | finite-window support only | no unconditional theorem promotion |
| `heuristic` | organizing analogy or candidate generator | no theorem promotion |
| `unknown` | bridge has not been established | no theorem promotion |
| `rejected` | attempted bridge is known invalid | no claim support |

## Heller-Winters application

The policy applies to all lanes, including:

- prime/operator candidate filters;
- residual and envelope diagnostics;
- zeta mirror-lattice methods;
- spectral-zeta analogies;
- geometric, descent, and coherence-objective surrogates;
- empirical phase-gate and finite-window measurements.

A localization operator, harmonic envelope, oscillator variable, mirror-lattice representation, or residual diagnostic is proof-bearing only to the extent that its bridge status is declared.

## Forbidden promotion pattern

The following pattern is disallowed in theorem-strength prose:

```text
1. Introduce auxiliary condition A.
2. Prove X and A imply Y.
3. Conclude X implies Y.
```

The valid statement is instead:

```text
X and A imply Y.
```

To promote the result, add and prove one of:

```text
X -> A
X <-> A
```

with all hypotheses preserved.

## Review checklist

Before a claim is marked `Proven`, `Lemma`, `Theorem`, or `Corollary`, reviewers must ask:

1. What is the classical source object?
2. What auxiliary object or condition was introduced?
3. Is the auxiliary condition still present in the conclusion?
4. If not, where is the bridge that allowed it to be dropped?
5. Does the bridge hold for all objects in scope or only for a filtered subsystem?
6. Are finite-window or asymptotic observations being promoted beyond their status?

## Negative-control source

This policy is motivated by a common false-proof archetype in zeta and prime-distribution work: solving an auxiliary zero-set intersection and then presenting the result as a theorem over the full classical zero set.

The repository should treat such examples as proof-safety fixtures, not as mathematical evidence.