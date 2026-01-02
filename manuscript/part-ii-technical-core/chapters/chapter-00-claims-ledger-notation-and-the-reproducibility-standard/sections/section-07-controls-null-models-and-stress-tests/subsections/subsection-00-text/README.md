# 0.7 Controls, Null Models, and Stress Tests

A pattern must survive at least these tests:

**Null N1: Random-phase baseline**  
Replace \theta(p) with i.i.d. uniform angles. If our figure looks the same, our mapping isn’t doing anything.

**Null N2: Random odd integers**  
Apply the same \theta(\cdot) to odd integers (or wheel-filtered integers) instead of primes. If the structure persists unchanged, we’re seeing an artifact of the function, not primes.

**Stress S1: Window expansion**  
Re-run at [n_a,n_b], then at [n_a, 10n_b]. Real structure should tighten or stabilize; fake structure drifts.

**Stress S2: Subsampling**  
Take every k-th prime, or random 10% subsample. If the structure depends on a fragile ordering accident, it collapses.

**Stress S3: Perturbation of constants**  
If constants are used, perturb them slightly. If the “signal” disappears instantly, it may be numerology rather than structure.
