# Table of Contents
## The Heller–Winters Theorem
### A Policy-Enforced, Multiscale Construction for Prime Localization and Log-Harmonic Residual Analysis

---

## Front Matter
* Title Page
* Copyright
* Dedication
    * To Dahl Winters, to truth/light/love, and to Atle Selberg
* Epigraph
* Acknowledgments
* Author Contributions Ledger
* Notation, Conventions, and Operator Legend
* Reader’s Map
    * What is proven, what is definitional, what is empirical, what is conjectural

---

## Preface
1. Zero First
    * Placeholder → number → coordinate system
2. Primes as Atoms and as Weather
3. Why the Old Tools Still Matter
    * Sieve, residues, bounds, zeta, zeros
4. The Human Layer
    * Hardy–Ramanujan (creation + cost)
    * Erdős–Selberg (truth + credit)

---

## Part I — The Ancestry of Constraints
1. The Discovery of Zero and the Birth of Representation
2. Euclid, Eratosthenes, and the First Prime Machines
3. Euler’s Product and the Analytic Doorway
4. Gauss, Legendre, Density, and the Mean-Field Law
5. Dirichlet and the Symmetry of Residue Classes
6. Chebyshev and the First Universal Enclosure
7. Riemann, Zeta Zeros, and Log-Scale Oscillation
8. Hardy–Littlewood and the Additive/Harmonic Arsenal
9. Ramanujan and the Tragic Speed of Genius
10. Sieves, Averages, and Modern Breakthroughs
* (This part ends by naming the operator inheritance: enclosures, residues, sieves, explicit-formula residuals.)

---

## Part II — The Heller–Winters Construction
(23-chapter technical core; each chapter has 10 subtopics in the full manuscript outline.)

11. Purpose and Thesis
* Mean-field vs residual
* Volume (log) vs distance (linear)
* Policy enforcement vs brute search
* Signal vs artifact (base, window, aliasing)
* Determinism and governance
* Operator falsifiability
* Scope and non-claims
* Canonical notation
* Alignment to classical theorems
* Full pipeline roadmap

12. Canonical Coordinate System
* (u=\ln x) as primary coordinate
* Multiplicative windows and log-length
* Change-of-base as rescaling
* Volume element and normalization
* Anchor windows (2, 10)
* Irrational windows (metallic/plastic) as probes
* Index vs value vs policy state space
* Nesting and multiresolution schedules
* Boundary effects
* Invariance rules

13. Prime Density Mean-Field Model
* (\pi(x)\sim x/\ln x) baseline
* Local intensity (\sim 1/\ln x)
* Window expectation (\int dt/\ln t)
* Gap scale (\sim \ln x)
* Regimes and drift
* Variance intuition
* Coverage language
* Residual definition
* Stability checks
* Mean-field guardrails

14. Boundedness Layer
* Bertrand/Chebyshev enclosure ((n,2n))
* Next-prime enclosure ((p,2p))
* Complexity baseline
* Bound-sensitive scoring
* Nested internal windows
* Log-cell representation
* Metric definitions
* Failure modes
* Operator ordering implications
* Practical evaluation harness

15. Wheel Sieve Layer
* Modulus design
* Reduced residues
* Survivor density (\varphi(M)/M)
* Residue state machines
* Depth vs cost
* Base resonance hazards
* Lattice-safe symmetry constraints
* Deterministic eliminator rules
* Residue signatures as features
* Cross-window invariants

16. Symmetric Offset Algebra
* Difference of squares
* Neighbor shells (n^2-1)
* General shells (n^2-k^2)
* Factor-pair ↔ additive geometry
* Parity constraints
* Composite certificates
* Shell density scaling
* Shell statistics in log windows
* Wheel + shell interaction
* Structural noise removal

17. Figurate Number Lattices
* Triangular, square, polygonal scaffolds
* Second differences and curvature
* Index/value conversion discipline
* Predictable counts per log-volume
* Offset maps from anchors
* Trapezoidal and higher families
* Residue intersections
* Congruence constraints
* Density contrasts
* Audit-friendly summaries

18. Base-(b) Compartmentalization
* Digit orbits and carry coupling
* Decimal vs binary vs hex partitions
* Repeating expansions of (1/n) and modular order
* Base invariance as a signal criterion
* Wheel resonance control
* Window alignment hazards
* Cross-base consensus scoring
* Artifact tests
* Feature extraction
* Base-agnostic representations

19. (p)-Adic Structure Layer
* Valuations (v_p(\cdot))
* (p)-Adic neighborhoods
* Depth schedules
* Filter vs feature roles
* Lifting logic
* Interaction with wheels and shells
* Compartment consensus
* Quotient conditioning
* Drift and artifact control
* Practical computation patterns

20. Quotient Functions and Normalization
* Windowed quotients vs raw counts
* Li / Chebyshev-type residual normalizations
* Conditioned quotients (residue/base/(p)-adic)
* Robust denominators
* Schedule stability
* Outlier handling
* Boundary correction integration
* Aggregation rules
* Comparative baselines
* Diagnostic plots (ledger-ready)

21. Euler–Mascheroni Calibration
* (\gamma) as discrete-continuous offset
* Harmonic sums vs logs
* Why (\gamma) belongs in the ledger
* Error floors
* Window calibration
* Misuse prevention
* Quotient alignment
* Cross-scale stability
* Interpretation discipline
* Where it stops helping

22. Euler–Maclaurin Bridge
* Sum↔integral decomposition
* Boundary terms
* Curvature corrections
* Bernoulli structure (as needed)
* Windowed approximations
* Error accounting
* Sampling vs density
* Links to (\gamma)
* Mean/residual separation formalized
* Implementation notes

23. Ratio Families as Window Schedules
* Anchors: 2 and 10
* Irrational probes: golden/silver/plastic/metallic family
* De-aliasing rationale
* Continued fraction ladder intuition
* Nesting rules
* Ratio mixing constraints
* Consensus tests
* Sensitivity diagnostics
* Governance boundaries
* When ratios are banned

24. Ordering and Governance of Ratio Application
* Tier-0 lattice-safe
* Tier-1 interpretability anchors
* Tier-2 de-alias probes
* Add/prune rules
* Overfit prevention
* Conflict resolution
* Aggregators
* Stability thresholds
* Complexity budgeting
* Audit templates

25. Harmonic Signature Formalism
* Log-harmonics (e^{it\ln x})
* Cos/sin decomposition
* Mode count vs resolution
* Coherence measures
* Window fingerprints
* Mixer identities
* Feature selection rules
* Base invariance checks
* Residual ledger mapping
* What counts as “harmonic signal”

26. Identity Channels
* Circular channel (phase manifold)
* Hyperbolic channel (envelope manifold)
* Projection operators
* Off-channel residuals as diagnostics
* Mixer design constraints
* Artifact rejection
* Channel-consistent scoring
* Cross-window persistence tests
* Ledger specification
* Interpretation discipline

27. RH-Consistent Envelope Constraint
* (x^\rho = x^\beta e^{i\gamma\ln x}) decomposition
* What (\beta=1/2) actually constrains
* Envelope measurement operators
* Drift tests
* Stability across schedules
* Failure signatures
* Policy use (not “proof”)
* Comparisons to known bounds
* Residual interpretability
* How this guides operator ordering

28. Explicit Phase-Selection Operator
* Canonical transcription of the phase rule
* State-governed parameters (no free knobs)
* Sector quantization under lattice safety
* The (90/11) normalization component (documented and testable)
* Hit conditions and tolerances
* Ablations (on/off, tolerance sweeps)
* Cross-base survival requirement
* Cross-window survival requirement
* Integration into the circular channel
* Falsifiers and failure taxonomy

29. Structural Sieves Beyond the Wheel
* Shell exclusions
* Parity and residue exclusions
* Figurate exclusions
* Digit exclusions (carefully bounded)
* (p)-Adic exclusions
* Mixed sieve ordering
* Depth accounting
* Conservative vs aggressive modes
* Composite certificate logging
* Practical pruning benchmarks

30. Optimization View
* CSP framing: hard constraints + soft scores
* Multiobjective design
* Regularizers: cross-base, cross-schedule, cross-compartment
* Residual minimization objective
* Complexity budgets
* Interpretability budgets
* Robust aggregation
* Sensitivity analysis
* Failure surfaces
* Reproducible evaluation harness

31. Classical Theorems as Policy Operators
* Euclid, Dirichlet, Chebyshev as hard boundaries
* Wilson as certification benchmark
* Fermat/Euler tests as quick filters (carefully)
* CRT as compartment combiner
* Quadratic residues as structured features
* Goldbach/twin prime heuristics as influence operators (labeled heuristic)
* Gap inequalities as constraints
* Sieve theorems as priors
* Misuse warnings
* Operator ledger integration

32. Evidence Ledger and Falsification Protocol
* Prediction events
* FP/FN definitions
* Scale drift tests
* Base drift tests
* (p)-Adic drift tests
* Residual thresholds
* Ablation studies
* Failure taxonomy
* Novelty criteria
* Publication-grade audit trails

33. Consolidated Spec and Extensions
* One-page executable spec
* Data structures and state machines
* Parameter governance rules
* Ratio governance rules
* Complexity accounting
* Claims taxonomy (proven/empirical/conjectural)
* Prime constellations
* Prime powers and (\psi)-based residuals
* Lattice counting / Ehrhart modules
* Research program map

---

## Appendices
A. Prime Milestones Timeline (dates + one-line significance)
B. Toolbox Genealogy (each tool → operator role)
C. Operator Ledger Templates (tables ready for replication)
D. Glossary (terms: enclosure, policy operator, identity channel, aliasing, coherence, etc.)
E. Reproducibility Checklist
F. Index

---

## Self-critique and refinements
Strong: this TOC is readable as a book (front matter + narrative history + technical core + appendices) and still preserves the operator-stack structure we need for the theorem to feel like a machine rather than a vibe.
Weak: Part I might be too long as “chapters” if we want to get to the theorem quickly. Also, Chapters 11–33 are dense; without interludes, a reader can drown in operators.
Two better packaging options (tradeoffs):
1. Short preface + timeline appendix (fastest route to the theorem): compress Part I into the Preface and Appendix A, and start Part II immediately. Best for technical readers; less story.
2. Three-part structure (best pacing):
    * Part I: History + the operator inheritance (short)
    * Part II: The construction (core)
    * Part III: Experiments + falsification ledger (expanded, with examples)
This adds length, but it makes the work harder to misread and easier to reproduce.
If we keep the current structure, the one surgical improvement we should make is to add two “worked examples” chapters inside Part II (after Wheel/Shells and after Phase-Selection), so readers see the machine running before they’re asked to believe it.
