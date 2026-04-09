# Chapter 2 — Versions Index

- vA1 — Jeremiah 29:13 / Matthew 7:7 / Poincaré (1908)
  - Sieve as policy machine + Euclid contradiction + Euclid algorithm + sieve + wheel (concept-only)
- vA2 — Jeremiah 29:13 / Matthew 7:7 / Poincaré (1908)
  - Adds M=30 micro-example: R30 residues, phi(M)/M density, repeating gap cycle
- vA3 — Jeremiah 29:13 / Matthew 7:7 / Poincaré (1908)
  - Adds Figure 2.1 full layout spec (1–120 grid + wheel overlay) + figure justification section
- vA-inline — Jeremiah 29:13 / Matthew 7:7 / Poincaré (1908)
  - File: `vA-jer-matt-poincare-inline-figs.md` — chapter text with Figures 2.1–2.2 embedded inline (uses the sealed CANONICAL figure package)
- FIGURES_INLINE_RENDER — text-render of 1–120 grid + gap cycle + explanatory notes
- FIGURES (CANONICAL) — sealed Figure 2.1 + 2.2 package (rules + render + typesetting spec)
- vB — Psalm 111:1 / John 1:1 / Newton (Principia rules)
  - Narrative rewrite; same technical spine; includes figure notes and a split-figure recommendation

- v04 — 2026-01-09 (file: v04-ch02-prime-machines-20260109.md)
  - Euclid proof clarified: P need not be prime; has a factor NOT in list (Issue #10)
  - Sieve stopping rule: added explicit sqrt-factor justification (Issue #13)
  - Policy machine: added one-sentence definition (det. constraint rule-set + audit ledger) (Issue #12)
  - Wheel micro-inset M=30: reformatted as boxed example with residues + gap cycle (Issue #11)
  - Promoted? no

- v05 — 2026-01-09 (file: v05-ch02-analytics-additions-20260109.md)
  - Arithmetic null defined as wheel-admissible composites only, primes excluded (Issue #6)
  - Mean resultant length R: stated O(1/√N) scaling + reporting protocol (Issue #7)
  - Circular tests: Rayleigh, Kuiper, Watson U²; EDF retained as visualization only (Issue #5)
  - Wheel modulus sensitivity: declared Q=7 default, sweep Q∈{5,7,11} (Issue #8)
  - Promoted? no

Status:
- CURRENT: vA-inline (vA-jer-matt-poincare-inline-figs.md)
- PENDING MERGE: v04 (content fixes), v05 (analytics additions)
- Figures: CANONICAL is sealed in FIGURES.md; reproducible generator: `bin/gen_fig2_1.py`
