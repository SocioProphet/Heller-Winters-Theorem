# TOC — Synthesis v3 (complete) — prepublication

Synthesis target: keep the v0 book container while importing v2 rigor/governance language and preserving explicit Phase Operator commitments (incl. 90/11, ablations, cross-base/window survival). (Full v3 text to be pasted here next pass if not already present in repo.)

## Chapter 0 (added) — Claims Ledger / Notation / Reproducibility

Canonical text lives at:
`manuscript/part-ii-technical-core/chapters/chapter-00-claims-ledger-notation-and-the-reproducibility-standard/`

This chapter governs:
- A/B/C/D claim tagging
- reproducibility contract
- null models + stress tests
- per-chapter claims ledger discipline

## Chapters 00–01 (repo-integrated)

- Chapter 00: `manuscript/part-ii-technical-core/chapters/chapter-00-claims-ledger-notation-and-the-reproducibility-standard/`
- Chapter 01: `manuscript/part-ii-technical-core/chapters/chapter-01-phase-definitions-from-the-log-line-to-the-circle/`

## 1. Introduction (paper-ready)

<!-- BEGIN INTRO 1.1-1.7 (FROM V2) -->

1.1. Historical arc: primes as structure amid apparent randomness
Prime numbers are among the oldest and most stubborn invariants of mathematics. The Euclidean insight that primes are inexhaustible established, at the dawn of formal mathematics, that the integers contain an irreducible “atomic” substrate whose global organization is not captured by finite patterning. Across centuries, the subject evolved from explicit constructions and factorization techniques into the modern view: primes behave like a sparse, irregular set in value space, yet exhibit profound regularity once we adopt the correct asymptotic coordinates and averaging procedures. That duality—local irregularity paired with global law—is the permanent engine of number theory’s development.
In the classical era, identities and divisibility rules served as the main tools: explicit congruences, factorization patterns, and arithmetic symmetries. In the analytic era, beginning in earnest with Euler’s manipulation of infinite products and sums, primes were connected to transcendental functions and continuous approximations. This bridge created an enduring methodological split: the “discrete” view, emphasizing constructive and combinatorial constraints, and the “analytic” view, emphasizing smooth approximations and oscillatory error terms. Modern number theory is the ongoing attempt to reconcile these views without losing the power of either.

1.2. The analytic turning point: Riemann’s spectral encoding of prime irregularity
Riemann’s 1859 memoir introduced the explicit link between prime distribution and the complex zeros of the zeta function. The prime number theorem (proved later by Hadamard and de la Vallée Poussin) made precise that prime density is governed, at leading order, by a logarithmic law: primes thin out like (1/\ln x). What remained—and remains—difficult is the fluctuation structure around that mean field. In modern language, the zeta zeros act like a spectral set that generates log-periodic oscillations in the residual. The Riemann Hypothesis (RH) is then most naturally interpreted as an envelope constraint: it asserts that the spectral contributors have real part 1/2, pinning the growth rate of fluctuation terms to a precise hyperbolic scaling regime.
A key conceptual point for this paper is that RH does not say “primes occur at a fixed cosine value.” Rather, it constrains the envelope exponent of log-harmonic oscillations in prime-counting residuals. In the log coordinate u=\ln x, the relevant periodicity is periodicity in u, i.e. multiplicative scale in x. This aligns prime distribution with a two-channel decomposition: a circular (phase) channel given by harmonics in u, and a hyperbolic (envelope) channel governed by exponential scaling in u.

1.3. The combinatorial turning point: sieve theory and constraint-first reasoning
In parallel with analytic developments, sieve methods matured into a systematic technology for removing structured composite mass. From early inclusion–exclusion reasoning to modern sieves, the core principle is constraint-first: before attempting to detect primes, one removes provable composites by modular restrictions. This paper treats sieve logic not merely as an algorithmic preprocessing step, but as a policy layer—a formal set of admissibility constraints that defines the feasible state space prior to any spectral inference.
Our construction begins with hard bounding (e.g., the guaranteed existence of a prime in (n,2n)), proceeds through wheel admissibility (\gcd(n,M)=1), and then adds symmetric offset shells (difference-of-squares factorization witnesses) as structured composite certificates. These layers are deterministic and auditable: they do not “guess” primes, they only remove impossibilities and organize the residual search space.

1.4. Calibration constants: Euler–Mascheroni and Euler–Maclaurin as discrete–continuous glue
Any program that mixes discrete counts with continuous approximations must confront systematic offsets between sums and integrals. The Euler–Mascheroni constant \gamma is the canonical example: it is the stable offset between the harmonic sum and the logarithm, \gamma=\lim(H_n-\ln n). Euler–Maclaurin summation generalizes this phenomenon, decomposing sums into integrals plus boundary and curvature corrections. In this paper, these objects are not decorative historical references: they provide the formal grammar by which “volume laws” (integral terms) and “index regularity” (correction terms) are separated. That separation is essential if we want residual signals to be interpretable rather than merely numerical artifacts.

1.5. Identity channels: Euclidean and hyperbolic projections as denoising operators
A second calibration principle is geometric: the decomposition of behavior into channels that satisfy exact identities. Circular identities (\sin^2+\cos^2=1) define unit-magnitude phase objects, while hyperbolic identities (\cosh^2-\sinh^2=1) define growth/decay envelopes. We use these as identity channels: projections that force modeled components back onto their invariant manifolds, with the residual interpreted as off-channel noise or structural mismatch. This provides a disciplined mechanism for “cutting noise” without collapsing the signal into arbitrary smoothing.

1.6. Multiscale schedules and governance: why metallic/plastic/φ appear, and why 60/90 are not “mystical”
A persistent hazard in prime experimentation is aliasing: artifacts introduced by base representation, fixed periodic partitions, or windowing choices can masquerade as structure. To counter this, we introduce incommensurate scaling schedules—metallic ratios, the plastic constant, and a φ/Fibonacci ladder—as window dilation factors in log-volume. The objective is not to claim that primes are “generated by ratios,” but to use irrational scalings as a de-aliasing test: true arithmetic structure should be stable across many incompatible window schedules, while digit-period artifacts should fracture.
Separately, periodic compartments (wheel residue classes, base-(b) digit compartments) are governed as periodic-lattice objects; sector quantizations used as backbone invariants are restricted to lattice-safe rotational orders (2/3/4/6). This prevents us from smuggling in phase discretizations that only “work” because we tuned them after the fact.

1.7. Contributions and claims of this work
This paper contributes:
1. A strict operator ordering that separates hard admissibility constraints (boundedness, wheel, symmetric shells) from soft spectral scoring and from window schedule design.
2. A unified coordinate model in which number line growth is treated as log-volume, making multiplicative windows the canonical units of analysis.
3. Quotient-normalized observables that align discrete counts with continuous expectations, using Euler–Maclaurin logic to define what is “mean field” versus “residual.”
4. A two-channel (circular/hyperbolic) identity framework for residual analysis, consistent with the RH interpretation as an envelope constraint.
5. A multiscale de-aliasing protocol using metallic/plastic/φ schedules to test invariance and isolate base- and period-dependent artifacts.
6. A deterministic phase-gate formalism (derived from the cosine construction) that is meaningful only when its indices are policy-derived rather than freely tuned.
7. A governance boundary between periodic backbone compartments (lattice-safe sectoring) and aperiodic probes (de-aliasing schedules and alternative encodings such as Fibonacci/Zeckendorf), so that we can distinguish invariants from artifacts.

Crucially, we do not claim an unconditional proof of RH or an unconditional closed-form next-prime formula at this stage. We claim a testable, falsifiable construction that can be evaluated by stability under scaling, base change, and residual-envelope diagnostics, and by performance relative to baseline primality search strategies.

2. Related Work and Intellectual Lineage (short bridge paragraph we can expand)
The work sits at the intersection of Euclid–Euler–Gauss style arithmetic structure, sieve methods (Erdős and the modern combinatorial tradition), and the analytic zeta program (Riemann and the development through Weil’s structural viewpoint in arithmetic geometry). Ramanujan’s legacy is relevant not because of mystique but because he repeatedly found unexpected identities and asymptotic relations linking discrete arithmetic objects to analytic expansions—exactly the kind of bridge we formalize via quotient functions and Euler–Maclaurin calibration. Wilson’s theorem represents the canonical “tight” primality identity, serving as a reference point for what it means for a condition to be logically equivalent to primality. Bertrand’s postulate (Chebyshev) provides the first hard boundedness layer that makes next-prime localization a finite policy domain.
<!-- END INTRO 1.1-1.7 (FROM V2) -->

