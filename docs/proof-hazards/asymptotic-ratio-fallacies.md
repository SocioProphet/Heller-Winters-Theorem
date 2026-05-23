# Asymptotic Ratio Fallacies

Status: proof-hazard note  
Scope: prime/operator, HPHD, residual, empirical, and spectral-zeta lanes

## Core warning

Ratio convergence is not equality of residuals.

The implication

```text
A_N / B_N -> 1
```

does not imply

```text
A_N - B_N = 0.
```

Under suitable nonzero denominator hypotheses, it usually implies only

```text
A_N - B_N = o(B_N).
```

That is an asymptotic relative-smallness statement, not a vanishing theorem.

## False inference pattern

Invalid:

```text
A_N -> k
B_N -> k
|A_N| / |B_N| -> 1
therefore k = 0
```

Counterexample:

```text
A_N = 2 + 1/N
B_N = 2 + 2/N
```

Then

```text
A_N -> 2
B_N -> 2
A_N / B_N -> 1
```

but

```text
k = 2 != 0.
```

## Heller-Winters risk surfaces

This hazard is especially relevant when prose discusses:

- prime-counting ratios;
- local-to-global density normalization;
- residual amplitude quotients;
- major/minor arc dominance ratios;
- empirical phase-gate survival rates;
- finite-window null comparisons;
- zeta regularization remainders;
- quotient-normalized operator scores.

## Required distinction

Use the strongest statement actually justified.

| Observed or proved relation | Permitted conclusion | Forbidden conclusion |
|---|---|---|
| `A_N/B_N -> 1` | relative error tends to zero, under hypotheses | `A_N = B_N` |
| `A_N - B_N -> 0` | absolute error tends to zero | exact equality for finite `N` |
| `R_N = o(B_N)` | residual is asymptotically smaller than baseline | residual vanishes identically |
| finite-window ratio near `1` | empirical agreement in tested window | asymptotic theorem |
| null-model survival | failure to falsify in run scope | proof of structural law |

## Reviewer instruction

If a proof or empirical claim uses a ratio, require the author to state:

1. denominator nonzero conditions;
2. convergence mode;
3. whether the claim is pointwise, uniform, averaged, or finite-window;
4. whether the result is exact equality, absolute asymptotic, relative asymptotic, or empirical observation;
5. whether any residual term is being set to zero rather than bounded.

## Safe Heller-Winters language

Use:

```text
The normalized discrepancy is asymptotically small relative to the baseline under the stated hypotheses.
```

Do not use:

```text
The residual disappears.
```

unless the proof establishes exact vanishing or a separately stated zero theorem.