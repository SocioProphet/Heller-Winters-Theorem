# Interlude A — Adopted Terminology

This file records the canonical glossary terms that have been adopted into prose across
the manuscript. It is generated and maintained by `bin/glossary_construction.py`.

Source of truth: `manuscript/part-ii-technical-core/chapters/chapter-00-claims-ledger-notation-and-the-reproducibility-standard/sections/0.10-glossary-core-terms.md`

---

## Adopted Terms

### Log-circle phase map

**Definition**: The map p ↦ θ(p) = (ln p mod 2π) embedding primes onto the unit circle via
logarithmic phase.

**First adopted in**: Chapter 1 (purpose and thesis), Chapter 2 analytics section.

**Usage note**: This is the primary coordinate transformation. Always write θ(p) when
referring to the phase of prime p on the unit circle. Do not write "angle of ln p" without
first defining this map.

---

### Traversal index k(p)

**Definition**: The integer k(p) = floor(ln p / 2π), counting how many full revolutions
ln p has completed.

**First adopted in**: Chapter 1, Chapter 2 analytics.

**Usage note**: k(p) tracks which "lap" the prime p occupies in the log-spiral unwinding.
Always pair with the phase θ(p) when discussing the coordinate decomposition.

---

### Identity-coupled feature map

**Definition**: A feature representation in which the coordinate system is fixed by the
mathematical object's identity (prime index or value), not by exogenous tuning.

**First adopted in**: Chapter 1 (reproducibility covenant section).

**Usage note**: The defining property is that no free parameter governs the map — the
coordinate is derived from the mathematical identity of the prime alone.

---

### Wheel sieve generator

**Definition**: The periodic sequence of wheel-admissible residues mod M = p_1·p_2·…·p_r
that generates candidate positions for primes without redundant multiples.

**First adopted in**: Chapter 2 (wheel section, M=30 micro-example).

**Usage note**: Always specify M when referencing a particular generator. The default
manuscript wheel uses M = 30 in historical examples and M = 210 (Q = 7) in experiments.

---

### Certified window + sieve policy layer

**Definition**: The combination of a bounded prime window [x, x+H] with a deterministic
elimination policy, yielding a certified set of prime candidates.

**First adopted in**: Chapter 2 (Eratosthenes section), Chapter 1 (thesis statement).

**Usage note**: "Certified" has a precise meaning here — every non-prime in the window
carries an explicit elimination certificate (divisor). The term must not be weakened to
mean "approximately correct."

---

### Ablation-first validation protocol

**Definition**: The experimental discipline of testing each component of a model in
isolation before combining, to attribute effects unambiguously.

**First adopted in**: Chapter 1 (reproducibility covenant), Chapter 2 analytics.

**Usage note**: This protocol is a hard methodological commitment. Any experiment that
combines components without first ablating them individually violates the protocol and
must be flagged in the claims ledger.

---

## Term Adoption Command Pattern

To record adoption of a new term, use the glossary construction tool:

```bash
python3 bin/glossary_construction.py --term "Term Name" --chapter "chapter-identifier"
```

Or to rebuild the full adoption file from scratch:

```bash
python3 bin/glossary_construction.py --rebuild
```

See `CONTRIBUTING.md` for the full term adoption workflow.

---

*Last updated: 2026-01-04*
