# HW-PRIME-WEIL-017 — Quotient Large-Sieve Diagnostic

Status: analytic-bound diagnostic / quotient-large-sieve target.  
Claim class: method-grade diagnostic, not theorem-grade analytic progress.  
Lane: prime/operator lane, quotient-character / coset-variance surface.  
Depends on: `HW-OPEN-014`, `HW-PRIME-WEIL-016`.

## Purpose

This document tests the first analytic tool native to the coset-variance framework: applying a large-sieve-style estimate only to quotient characters of

```text
G_q / <10>.
```

These quotient characters are exactly the local non-cancelling characters. The goal is to determine whether the orbit/coset restriction improves the standard large-sieve scale enough to approach the GRH-scale packet bound.

## Setup

Let:

```text
G_q = (Z/qZ)^x,
H_q = <10>,
d_q = |H_q| = ord_q(10),
I_q = [G_q:H_q] = (q-1)/d_q.
```

The non-cancelling local characters are the nontrivial characters of the quotient:

```text
G_q / H_q.
```

Their count is:

```text
n_nc(q) = I_q - 1.
```

The quotient restriction is meaningful because it discards all characters that see within-coset oscillation and keeps only characters that see between-coset mass imbalance.

## Standard large-sieve scale

A standard large-sieve comparison gives the model scale:

```text
B_standard(q,K) = (10^K + q^2) * sum_{p in W_K} (log p)^2.
```

This is a comparison scale, not a sharp theorem for this exact finite packet.

## Quotient candidate scale

The quotient-coset heuristic replaces the full unit group by the quotient size `I_q` and divides by the orbit size `d_q`:

```text
B_quotient(q,K) = (10^K / I_q + I_q) * sum_{p in W_K} (log p)^2 / d_q.
```

This captures the hoped-for gain from using the orbit structure.

The quotient gain relative to the standard comparison is:

```text
B_standard / B_quotient.
```

For fixed q and large K, this gain is approximately:

```text
q - 1.
```

up to lower-order terms. This is a real finite structural improvement, but it is still a constant-factor improvement at fixed q.

## GRH packet scale comparison

A GRH-shaped packet scale for the non-cancelling local packet is:

```text
B_GRH(q,K) = n_nc(q) * 10^K * (log 10^K)^4.
```

The quotient diagnostic compares:

```text
B_quotient(q,K) / B_GRH(q,K).
```

If this ratio remains greater than 1 and grows with K, the quotient-large-sieve restriction has not crossed the square-root barrier.

## Finite diagnostic results

The diagnostic implementation is:

```text
tools/check_quotient_large_sieve.py
```

It evaluates q in:

```text
11, 13, 37
```

and depths:

```text
K = 3,4,5.
```

The CI guards require:

- quotient improvement over the standard comparison for q=11,13,37;
- quotient candidate scale still above the GRH packet scale at tested depths;
- asymptotic gap factor increasing from K=5 to K=10 for q=37.

## Result

The quotient restriction gives a real structural improvement, but it does not close the GRH-scale gap.

In the fixed-q regime, the gain is essentially a constant-factor gain from orbit/coset compression. The remaining obstruction still grows with the window scale.

Thus the quotient large-sieve diagnostic supports the central conclusion of `HW-OPEN-014`:

```text
coset structure isolates the right packet,
but standard large-sieve technology does not prove the Coset Variance Theorem.
```

## What would be needed to improve this

A proof-closing result would need more than quotient restriction. It would need one of:

1. a large-sieve inequality with a genuine square-root saving for fixed quotient packets;
2. a dispersion estimate exploiting arithmetic structure of the cosets beyond quotient size;
3. a cancellation theorem for coset mass imbalance across Richter windows;
4. an explicit-formula tail bound that avoids assuming GRH;
5. a new structural input not present in the standard large-sieve framework.

## Non-claims

This document does not prove RH.

This document does not prove GRH.

This document does not prove the Coset Variance Theorem.

This document does not prove an unconditional variance bound.

This document does not prove the quotient candidate inequality as a sharp theorem.

This document does not claim that quotient large sieve crosses the square-root barrier.

This document does not close `HW-OPEN-014` or `HW-PRIME-WEIL-016`.
