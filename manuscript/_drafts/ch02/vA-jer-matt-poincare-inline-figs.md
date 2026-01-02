
Got it. We’re rendering the diagrams now, inline, with the micro-annotation baked into the legend (the full 𝓡₃₀ list), so a reader can verify the wheel instantly without hunting.

Below, each entry is printed as:
    • □ = wheel-admissible (survives divisibility by 2,3,5)
    • × = eliminated by the sieve layer {2,3,5}
    • (For this specific wheel, anything not wheel-admissible is automatically eliminated by 2 or 3 or 5, except the primes 2,3,5 themselves.)

⸻

Figure 2.1 — 1–120 grid with sieve {2,3,5} + 30-wheel overlay

Legend (with the required micro-annotation):
    • slash/strike in the print version = × here
    • box/halo in the print version = □ here
    • M=30
    • 𝓡₃₀={1,7,11,13,17,19,23,29}
    • wheel-admissible rule: gcd(n,30)=1 (and we also keep 2,3,5 as primes)

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

What this figure proves visually (and why we insisted on it):
    • Admissible ≠ prime. Example: 49□ survives {2,3,5} but is composite.
    • The wheel is a correctness-preserving compressor: every × here is eliminated by a certified reason (divisible by 2, 3, or 5).
    • The □ positions are exactly the “candidate corridor” the wheel hands to deeper operators.

⸻

Figure 2.2 — the 30-wheel step cycle (reduced residues + repeating gaps)

𝓡₃₀=(1,7,11,13,17,19,23,29)

Compute forward cyclic gaps mod 30:
    • 7-1=6
    • 11-7=4
    • 13-11=2
    • 17-13=4
    • 19-17=2
    • 23-19=4
    • 29-23=6
    • 31-29=2 (wrap, since 31≡1 (mod 30))

So the repeating gap cycle is:

(6,4,2,4,2,4,6,2)

Rendered:

R₃₀ = (1, 7, 11, 13, 17, 19, 23, 29)
gap = (6, 4,  2,  4,  2,  4,  6,  2)  repeating every 30

This is the “wheel” in its purest mechanical form: candidate generation becomes “walk a repeating step pattern” rather than “scan every integer.”
