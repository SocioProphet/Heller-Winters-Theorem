CHAPTER 2 — v05 — Analytics Additions

Supplementary sections for the Chapter 2 experiment layer
(Issues #5, #6, #7, #8)

These sections extend v04 with the statistical and experimental protocol required for the
log-phase circle experiment described in Part II. They are separated here because Part II
locks Chapter 2 before these sections are merged.

⸻

§A. Null hygiene: wheel-admissible composites only (Issue #6)

The arithmetic null must **exclude primes** from the wheel-admissible set.

**Definition.** For a window [x, y]:

    A_{[x,y]} = { n ∈ [x,y] : gcd(n, M) = 1 }     (wheel-admissible set)
    C_{[x,y]} = { m ∈ A_{[x,y]} : m composite }    (arithmetic null = composites only)

The null distribution uses C_{[x,y]}, not A_{[x,y]}.

**Rationale.** Including primes in the null contaminates the comparison. We already
compute primes for each window (to define the prime sample), so exclusion is computationally
free. All strict-mode comparisons must use C_{[x,y]}.

**Sensitivity check.** Report the δ between results using A_{[x,y]} vs C_{[x,y]} for each
window; this quantifies how much contamination matters.

⸻

§B. Mean resultant length R: calibration and scaling (Issue #7)

Let θ_1, …, θ_N ∈ [0, 2π) be the phases of N points on the unit circle. The mean
resultant length is:

    R = (1/N) · |Σ_{j=1}^{N} e^{i θ_j}|

**Uniform-angle baseline (Issue #7):** Under the uniform distribution on [0, 2π),
the expected value satisfies

    E[R] = 0   and   Var(R) = 1/(2N),

so R = O(1/√N). For large N, R ≪ 1 is expected from uniform data alone; a large R
indicates non-uniform angular concentration.

**Reporting requirement.** Chapter 2 must report R for each window alongside:
- The theoretical O(1/√N) scaling reference (plot as a dashed line),
- Optional: Monte Carlo confidence bands (e.g. 5th–95th percentile from 10,000 uniform
  samples of the same N).

⸻

§C. Circular statistics: replace linear CDF claims (Issue #5)

The empirical distribution function (EDF) on [0, 2π) depends on the choice of cut point
and is not invariant under cyclic rotation. It may be retained as a visualization overlay,
but no inferential claims may rest on it.

**Required circular tests (at least one per window):**

1. **Rayleigh test** — tests for unimodal concentration away from uniform.
   - Test statistic: z = N · R²
   - Under H₀ (uniform): z is approximately χ²(2) / 2 for large N.
   - Report: z-statistic, p-value.

2. **Kuiper test** — circular analogue of Kolmogorov–Smirnov; invariant under rotation.
   - Statistic: V = D⁺ + D⁻ (sum of max positive and negative deviations).
   - Report: V-statistic, critical value at α = 0.05.

3. **Watson U² test** — rotation-invariant distributional difference test.
   - Preferred over Kuiper when the alternative is not merely a shift.
   - Report: U²-statistic, critical value at α = 0.05.

**Protocol:** For each analysis window, report R plus the outcome of at least one
invariant circular test. The EDF overlay may appear in figures but must be labelled
"visualization only."

⸻

§D. Wheel modulus sensitivity: declare default Q and run sweep (Issue #8)

The wheel modulus M = ∏_{q ≤ Q} q depends on the primorial cutoff Q. Results must not be
sensitive to an unspecified Q.

**Default declaration:** Q = 7, giving M = 2 · 3 · 5 · 7 = 210 (primorial of primes ≤ 7).

**Sensitivity sweep:** Report results for Q ∈ {5, 7, 11}:

| Q | M = ∏_{q ≤ Q} q | φ(M)/M (density) | Notes |
|---|-----------------|-------------------|-------|
| 5 | 30              | 8/30 ≈ 26.7%      | minimal wheel |
| 7 | 210             | 48/210 ≈ 22.9%    | **default** |
| 11| 2310            | 480/2310 ≈ 20.8%  | extended wheel |

**Acceptance criterion:** The key experimental outcomes (prime-vs-null R differences,
circular test p-values) must be stable across Q ∈ {5, 7, 11}. If sensitivity is detected,
report which window sizes drive the difference.

⸻

v05 delta summary:
- §A: Defined arithmetic null as C_{[x,y]} = wheel-admissible composites only; excluded
  primes (Issue #6).
- §B: Stated R = O(1/√N) uniform baseline; required reporting of theoretical scaling and
  optional MC bands (Issue #7).
- §C: Replaced linear EDF inferential use with circular tests (Rayleigh, Kuiper, Watson
  U²); EDF retained as visualization only (Issue #5).
- §D: Declared default Q=7, M=210; required sensitivity sweep for Q ∈ {5, 7, 11}
  (Issue #8).
