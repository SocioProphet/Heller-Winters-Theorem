# Chapter 4 Figures (Draft Archive)

This file stores the Chapter 4 render queue/specs as text-first objects.
When we generate PNG/SVGs, they must match these declared axes, labels, and baselines.

---

## Render Queue — Chapter 4

1) **Fig 4.1: π(x) vs comparators (step + smooth)**
   - Plot range: a moderate range that is readable (e.g., x ≤ 10^5) and a second range if needed.
   - Curves:
     - π(x) as a step function.
     - x/ln x as a baseline curve (clearly marked as rough).
     - Li(x) as the mean-field comparator.
   - Axis discipline:
     - x-axis linear for the moderate range plot.
     - Optionally a second figure with log-x if we want to emphasize scaling.

2) **Fig 4.2: Local intensity λ(x) = 1/ln x**
   - Same x-range as Fig 4.1.
   - Single curve showing thinning.
   - Explicit label: λ(x)=1/ln x.

3) **Fig 4.3: Window expectation as area under the intensity curve**
   - Show the curve 1/ln t.
   - Shade the region between a and b.
   - Label the shaded area: ∫_a^b dt/ln t.
   - This is the “mean-field coverage operator.”

4) **Fig 4.4: Micro-example panel for [100,200]**
   - Text + simple annotation:
     - actual count: π(200)−π(100)=21
     - mean-field estimate: ∫_100^200 dt/ln t ≈ 100/ln(150) ≈ 19.96
   - Goal: tactile verification without machinery.

---

## Notes

- We keep **mean-field vs residual** explicit. When residual appears, we include a zero baseline.
- Any computed figure must record its method (how π(x) was computed; how Li(x) was approximated) and be stored with a ledger tag.

---

## v3 (resynth) locked list — bridge-to-Riemann instrument panel

These are the *non-optional* visuals implied by the resynthesized draft:

1. **Overlay (global):** \(\pi(x)\) vs \(\operatorname{Li}(x)\) vs \(x/\ln x\) on log-x (or dual x/u=ln x) over a range large enough to show global agreement + local deviation (target: \(x\le 10^5\) or \(10^6\)).
2. **Residual (bridge):** \(R(x)=\pi(x)-\operatorname{Li}(x)\) over the same range with a clearly drawn zero-line.
3. **Intensity:** \(1/\ln x\) across the same range to visualize thinning (mark 2–3 windows).
4. **Window-as-area schematic:** shade the area under \(1/\ln t\) from \(a\) to \(b\), label as expected prime count.
5. **Calibration panel:** \([100,200]\) “actual = 21” vs “mean-field ≈ 20,” explicitly labeled as calibration (not evidence).

