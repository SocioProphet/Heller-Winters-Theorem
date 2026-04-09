# Chapter 1 — Purpose and Thesis

## Role in the manuscript

Chapter 1 is **purely foundational**. It establishes the thesis posture and the canonical
coordinate system. No experimental plots or claims appear here.

Experimental content (log-phase null comparisons, controls, ablation results) is deferred
to Chapter 2 and the Evidence Ledger chapter.

---

## §1. Thesis posture

The central claim of this book is structural: the distribution of primes, when viewed
through the lens of logarithmic phase embedding and wheel-sieve compression, exhibits
measurable regularities that can be certified, falsified, and extended by deterministic
policy operators.

We do not assert a proof of the Riemann Hypothesis. We assert a reproducible experimental
framework that makes the question of prime phase concentration formally tractable.

---

## §2. Canonical coordinate system

**Primary coordinate:** For a prime p, define

    u = ln x,    θ(p) = ln p mod 2π ∈ [0, 2π).

This is the **Log-circle phase map**: the map p ↦ θ(p) embeds primes on the unit circle
via logarithmic phase.

**Secondary index:** The **Traversal index k(p)** = floor(ln p / 2π) counts how many full
revolutions ln p has completed. It partitions primes into annular bands.

**Why these coordinates?** The coordinate system is fixed by the identity of the prime
itself—not by exogenous tuning. This is the **Identity-coupled feature map** principle:
representations must be anchored to the object, not to the analyst's choice.

**Displayed equations (at most two in Chapter 1):**

    u = ln x                              (log-line coordinate)
    θ(p) = u mod 2π = ln p mod 2π        (circle embedding — representation, not test)

The circle embedding is introduced here as a representation. It is not tested in Chapter 1.

---

## §3. Reproducibility covenant (Issue #4)

The following invariants are fixed for all experiments in this book.

### Fixed: Window schedule

Windows are drawn from the schedule [x, x+H] with H = floor(x / log x). No window is
selected after seeing the result; all windows are enumerated in advance and listed in the
Evidence Ledger.

### Fixed: Null definitions

Two null models are used throughout:
- **Uniform null:** phases drawn uniformly from [0, 2π).
- **Arithmetic null (Wheel sieve generator):** the set C_{[x,y]} of
  **Certified prime candidates** that are composite
  (wheel-admissible composites, i.e., gcd(n, M) = 1 and n composite).

Primes are excluded from the arithmetic null. Null definitions are not changed between
windows.

### Fixed: Random seed protocol

All Monte Carlo simulations use a fixed seed recorded in the Evidence Ledger table:

    seed = sha256(window_spec_string)[:8] interpreted as uint32.

This makes every random draw reproducible from the window specification alone.

### Fixed: Plotting pipeline

Figures are generated from the same pipeline script for every window. No manual
post-processing is applied to figures that carry claims.

### Explicit non-claims

- We do **not** claim that the phase distribution is provably non-uniform.
- We do **not** cherry-pick windows that show strong signals.
- We do **not** tune parameters inside an experiment (tuning, if any, is recorded
  in the backlog and disclosed).
- We do **not** interpret a single-window result as a general law.

---

## §4. What Chapter 1 does NOT contain

Per Issue #2:

- No experimental plots.
- No null comparison results.
- No circular test outcomes.
- No claims about R (mean resultant length).

These all appear first in Chapter 2, alongside the **Ablation-first validation protocol**.

---

## §5. Canonical glossary terms used in this chapter (Issue #3)

All terms match the canonical glossary spelling exactly
(`manuscript/.../sections/0.10-glossary-core-terms.md`):

- **Log-circle phase map** — introduced in §2.
- **Traversal index k(p)** — introduced in §2.
- **Identity-coupled feature map** — introduced in §2 (principle).
- **Wheel sieve generator** — referenced in §3 null definition.
- **Certified window + sieve policy layer** — referenced in §3 window schedule.
- **Ablation-first validation protocol** — referenced in §4 (deferred to Ch. 2).

No near-synonyms are introduced for these terms without an explicit alias definition.

---

## §6. Backlog note (Issue #20)

Chapter 1 TOC-consistent framing adjustments are deferred until Chapter 2 is locked.
Pending items:
- Ensure Chapter 1 does NOT treat the log-circle as the first experiment (that belongs in
  Chapter 2 with controls).
- Chapter 1 functions as Part II on-ramp: thesis posture + coordinate/window discipline.
- Experiment protocol remains centralized in Chapter 2 and the Evidence Ledger.

Track edits as issues; execute after Chapter 2 is stable.
