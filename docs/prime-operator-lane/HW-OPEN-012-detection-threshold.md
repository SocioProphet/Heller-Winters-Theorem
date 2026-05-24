# HW-OPEN-012 — Off-Line Zero Detection Threshold

Status: open diagnostic threshold problem.  
Claim class: finite-diagnostic / explicit-formula threshold surface, not theorem-grade analytic progress.  
Lane: prime/operator lane, Richter-window / renormalized packet-energy surface.  
Depends on: `HW-PRIME-WEIL-005`, `HW-PRIME-WEIL-011`.

## Purpose

This document records the detection-threshold problem exposed by the `K=5` extension of `HW-PRIME-WEIL-011`.

The count-normalized `p=11` cancelling and non-cancelling energies remain bounded after division by `10^K` for the tested depths `K=2,3,4,5`. The non-cancelling/cancelling ratio also inverts at `K=5`, showing finite prime-race fluctuation rather than monotone growth.

This is consistent with GRH-scale behavior at the tested depths. It is not evidence for RH or GRH, and it is not evidence against a hypothetical off-line zero at depths beyond current computation.

## Observed finite scale

For the `p=11` cancelling and non-cancelling sublayers, the tested values of:

```text
E_C(K) / 10^K
```

remain bounded in the finite computed range:

| K | `E_cancel(K)/10^K` | `E_non(K)/10^K` |
|---:|---:|---:|
| 2 | `2.952784650337` | `2.952784650337` |
| 3 | `3.923097663316` | `4.214224918349` |
| 4 | `3.169831204139` | `3.714928844832` |
| 5 | `3.578881287026` | `3.051196916722` |

No exponential growth is visible at these depths.

## Ratio inversion

The finite ratio:

```text
E_non(K) / E_cancel(K)
```

is:

| K | ratio |
|---:|---:|
| 2 | `1.000000000000` |
| 3 | `1.074208515825` |
| 4 | `1.171964248437` |
| 5 | `0.852556056493` |

The inversion at `K=5` is a finite prime-race / residue-bias diagnostic. It shows that the count-normalized p11 sublayer statistic is sensitive to window-level residue fluctuations.

This document does not promote the inversion to a theorem-grade Littlewood or Chebyshev-bias statement.

## Detection-threshold model

A hypothetical off-critical zero with:

```text
rho = 1/2 + delta + i t,
```

would contribute a growth factor of the form:

```text
10^(2 delta K)
```

to squared-energy scale after normalization by the critical-line baseline.

A crude detectability heuristic compares:

```text
10^(2 delta K) / K^2
```

against an `O(1)` finite noise floor.

For example, if:

```text
delta = 0.1,
```

then at `K=5`:

```text
10^(2 delta K) / K^2 = 10^1 / 25 = 0.4,
```

which remains below an `O(1)` finite diagnostic floor. At `K=20`:

```text
10^(2 delta K) / K^2 = 10^4 / 400 = 25,
```

which would exceed such a crude threshold.

This is only a heuristic detection threshold. It is not a theorem and does not account for phase cancellation, zero multiplicity, explicit-formula truncation, or the actual finite variance noise model.

## Computational barrier

Direct prime enumeration to depth `K=20` would require windows up to:

```text
10^20,
```

which is infeasible for the present direct enumeration diagnostics.

Thus the next analytic problem is not direct computation, but an explicit-formula surrogate for the renormalized packet-energy statistic at larger depths.

## Open problem

Can the explicit formula be used to estimate or bound the count-normalized packet-energy ratios at depths beyond direct enumeration, while preserving the finite packet decomposition used in `HW-PRIME-WEIL-011`?

Concrete subproblems:

1. derive an explicit-formula expression for the p11 cancelling and non-cancelling packet energies;
2. quantify the finite noise floor for the normalized packet-energy ratio;
3. determine the depth at which a hypothetical off-critical contribution of size `delta` would become detectable;
4. distinguish genuine off-line-zero growth from finite prime-race sign changes;
5. state a non-circular criterion that does not assume GRH to rule out large-depth growth.

## Non-claims

This document does not prove RH.

This document does not prove GRH.

This document does not prove an off-line zero exists.

This document does not rule out off-line zeros.

This document does not prove a Littlewood sign-change theorem or a Chebyshev-bias theorem.

This document does not prove the explicit-formula surrogate exists.

This document does not prove an unconditional variance bound.

This document does not close the square-root barrier.
