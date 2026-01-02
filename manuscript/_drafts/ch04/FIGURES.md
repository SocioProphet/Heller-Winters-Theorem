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

5) **Fig 4.5: Large-window verification panel for [100000,200000]**
   - Text + simple annotation:
     - actual count: π(200000)−π(100000)=8392
     - mean-field estimate: ∫_100000^200000 dt/ln t ≈ 8406.243...
     - residual for the window: (actual − expected) ≈ −14.243...
   - Goal: show the same mean-field operator stays accurate at scale (removes any “cherry-picked toy window” objection).

---

## Notes

- We keep **mean-field vs residual** explicit. When residual appears, we include a zero baseline.
- Any computed figure must record its method (how π(x) was computed; how Li(x) was approximated) and be stored with a ledger tag.
