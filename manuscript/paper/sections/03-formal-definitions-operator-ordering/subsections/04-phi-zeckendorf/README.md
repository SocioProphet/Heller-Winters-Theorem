# 03.4 Fibonacci / φ as the canonical irrational scale ladder and Zeckendorf as integer grammar

## 03.4.1 Continued fractions and the “best approximation ladder”
A canonical de-aliasing method is to use irrational dilation windows (x ↦ r x) and demand invariance across many incompatible r. The golden ratio φ is extremal in this sense because its continued fraction is maximally uniform: φ = [1;1,1,1,…]. The convergents are ratios of successive Fibonacci numbers F_{n+1}/F_n → φ, giving a deterministic scale-refinement ladder rather than ad hoc irrational sampling.

## 03.4.2 Zeckendorf representation as a third coordinate system on ℤ
Zeckendorf: Every positive integer N has a unique representation as a sum of nonconsecutive Fibonacci numbers. This yields a constraint-grammar encoding (“no consecutive ones”), and provides a third coordinate system alongside:
- base-(b) digits (periodic digit artifacts),
- p-adic valuations (multiplicative structure),
- Zeckendorf (additive structure under a nonpositional grammar).

Triangulation rule: any candidate “signal” we treat as real must survive cross-projection among these encodings; single-encoding-only structure is treated as a likely artifact until proven otherwise.

## 03.4.3 Deterministic irrational coverings (Beatty / Wythoff style partitions)
Golden-ratio partitions (e.g., floor(nφ), floor(nφ²)) give deterministic aperiodic coverings of ℕ. Here they are probes (anti-alias tests), not prime generators.
