# HW-PRIME-WEIL-016 — Explicit Formula Packet-Energy Surrogate

Status: explicit-formula surrogate target / finite verification boundary map.  
Claim class: analytic surrogate design surface, not theorem-grade RH progress.  
Lane: prime/operator lane, packet-energy / explicit-formula surface.  
Depends on: `HW-OPEN-012`, `HW-OPEN-014`, `HW-PRIME-WEIL-015`.

## Purpose

This document records the explicit-formula surrogate needed to replace direct prime enumeration at depths beyond the feasible Richter-window range.

The q=37 measurement falsified the first pre-registered orbit-quality model at finite depth. The next proof-gate question is whether packet energies can be estimated or bounded by explicit formula methods at larger depths without assuming GRH.

This document states the formula, the truncation-height barrier, and the current feasibility boundary.

## Section 1 — Packet energy formula

For a character packet `C`, define the count-normalized packet energy:

```text
E_C(K) = (1/|C|) sum_{chi in C} |psi_{W_K}(chi)|^2.
```

The explicit formula has the model form:

```text
psi_{W_K}(chi)
  = - sum_{rho: L(rho,chi)=0} (10^(K rho) - 10^((K-1)rho)) / rho + err_K(chi).
```

Therefore:

```text
E_C(K)
  = (1/|C|) sum_{chi in C}
      | sum_rho (10^(K rho) - 10^((K-1)rho)) / rho |^2
    + packet_error.
```

Expanding the square gives diagonal and off-diagonal zero interactions:

```text
E_C(K)
  = (1/|C|) sum_{chi in C} sum_{rho,rho'}
      A_K(rho) conjugate(A_K(rho'))
    + packet_error,
```

where:

```text
A_K(rho) = (10^(K rho) - 10^((K-1)rho)) / rho.
```

This is a surrogate target. It is not implemented as a zero-sum computation in this PR because zero tables are not yet wired into the repository.

## Section 2 — Diagonal term under GRH

If all zeros in the packet lie on the critical line:

```text
rho = 1/2 + i gamma,
```

then:

```text
|10^(K rho) - 10^((K-1)rho)| = O(10^(K/2)).
```

The diagonal contribution is therefore at the GRH-shaped packet scale, up to polynomial and logarithmic factors in `K`, after truncation and zero-density accounting.

The off-diagonal terms encode phase interaction between zeros and are not automatically negligible without additional cancellation or averaging input.

## Section 3 — Truncation height requirements

The finite diagnostics expose a practical truncation-height barrier. The current working table is:

| K | T needed for error below signal | Verified height for conductors <=37 | Feasible? |
|---:|---:|---:|---|
| 5 | about `4e4` | about `3e12` | yes |
| 10 | about `5e7` | about `3e12` | yes |
| 20 | about `2e13` | about `3e12` | borderline/no |
| 50 | about `1e29` | about `3e12` | no |
| 11088 | about `10^5544` | about `3e12` | impossible |

The `K=11088` line is the resonant-depth tower barrier. The required height is symbolic at repository scale and is represented by `inf` in the helper tool to avoid floating-point overflow.

The table is a feasibility map, not a theorem.

## Section 4 — Smoothed window improvement

One possible improvement is to replace the sharp Richter window by a smoothed window:

```text
W_K^phi(x) = phi((log x - K log 10) / log 10)
```

for a Schwartz test function `phi`.

Smoothing can improve truncation behavior because the transform of the test function decays. The resulting error depends on the decay of the transform and on the available zero-free region.

This may extend the feasible surrogate range, but it does not reach the resonant tower depth `K*=11088` with current zero verification heights.

## Section 5 — What this establishes

The explicit formula surrogate is a finite verification strategy for low and medium depths, not an infinite proof.

It can plausibly certify packet-energy behavior up to depths where the required truncation height is below the verified height. In the current table, that means roughly `K <= 10`, with `K=20` already beyond the clean verified range.

To turn the surrogate into a proof, one needs one of:

1. much higher verified zero heights;
2. an analytic remainder bound that does not assume GRH;
3. an off-diagonal cancellation theorem;
4. a smoothed-window theorem strong enough to control the missing tail;
5. a separate proof of the coset variance theorem from `HW-OPEN-014`.

None of these is supplied here.

## Non-claims

This document does not prove RH.

This document does not prove GRH.

This document does not implement a zero-table surrogate computation.

This document does not prove the diagonal approximation.

This document does not prove that off-diagonal zero interactions are negligible.

This document does not prove the smoothed window improvement reaches the resonant tower depth.

This document does not prove an unconditional variance bound.

This document does not close the square-root barrier.
