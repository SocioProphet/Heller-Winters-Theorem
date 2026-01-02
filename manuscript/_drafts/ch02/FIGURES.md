# Chapter 2 — Sealed Figure Package (Canonical)

## FIGURE 2.1 (CANONICAL)
1–120 Sieve Grid with {2,3,5} Elimination + 30-Wheel Overlay

Canonical rules
- Domain: integers 1 to 120, laid out in a 10×12 grid, increasing left→right, top→bottom.
- Sieve elimination set: {2,3,5}.
- Eliminated (×): any n with n<2, or n divisible by 2 or 3 or 5, except n∈{2,3,5}.
- Wheel-admissible (□): any n≥2 with gcd(n,30)=1, plus 2,3,5.
- Wheel modulus: M=30.
- Reduced residues:
  \mathcal R_{30}=\{1,7,11,13,17,19,23,29\}.
  (And operationally we treat {2,3,5} as admissible primes as stated.)

Canonical legend
- □ = wheel-admissible (candidate corridor)
- × = eliminated by the sieve layer {2,3,5}

Canonical text-render (each entry shown as n□ or n×)

  1×   2□   3□   4×   5□   6×   7□   8×   9×  10×
 11□  12×  13□  14×  15×  16×  17□  18×  19□  20×
 21×  22×  23□  24×  25×  26×  27×  28×  29□  30×
 31□  32×  33×  34×  35×  36×  37□  38×  39×  40×
 41□  42×  43□  44×  45×  46×  47□  48×  49□  50×
 51×  52×  53□  54×  55×  56×  57×  58×  59□  60×
 61□  62×  63×  64×  65×  66×  67□  68×  69×  70×
 71□  72×  73□  74×  75×  76×  77□  78×  79□  80×
 81×  82×  83□  84×  85×  86×  87×  88×  89□  90×
 91□  92×  93×  94×  95×  96×  97□  98×  99× 100×
101□ 102× 103□ 104× 105× 106× 107□ 108× 109□ 110×
111× 112× 113□ 114× 115× 116× 117× 118× 119□ 120×

What this figure proves visually (and why we insisted on it)
- Admissible ≠ prime. Example: 49□ survives {2,3,5} but is composite.
- The wheel is a correctness-preserving compressor: every × here is eliminated by a certified reason (divisible by 2, 3, or 5).
- The □ positions are exactly the “candidate corridor” the wheel hands to deeper operators.

Caption (canonical)
A sieve certifies composites by exclusion. A wheel certifies inadmissible residue classes in advance. Together they form the first deterministic prime engine: fewer candidates, same correctness, explicit reasons.

Typesetting spec (so the final graphic matches the canonical render exactly)
- Use a monospaced grid or drawn rectangles (10 columns × 12 rows).
- Put each integer centered in its cell.
- If n is eliminated, draw a diagonal slash from lower-left to upper-right.
- If n is wheel-admissible, draw an inner rectangle (halo) inset ~7% from the cell border.
- Legend must include the explicit list \mathcal R_{30}=\{1,7,11,13,17,19,23,29\} so the reader can audit instantly.

---

## FIGURE 2.2 (CANONICAL)
30-Wheel Reduced Residues and Repeating Gap Cycle

\mathcal R_{30}=(1,7,11,13,17,19,23,29)

Gap cycle (cyclic, mod 30):
(6,4,2,4,2,4,6,2)

Rendered:

R₃₀ = (1, 7, 11, 13, 17, 19, 23, 29)
gap = (6, 4,  2,  4,  2,  4,  6,  2)  repeating every 30

Caption (canonical)
Wheel generation is walking a periodic step pattern through admissible residues; it is compression without heuristics.
