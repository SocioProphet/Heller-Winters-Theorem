from pathlib import Path
import re

ROOT = Path("manuscript")
PREFACE = ROOT / "preface"
CORE = ROOT / "part-ii-technical-core"

def slugify(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s

def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")

# ----------------------------
# Preface: store v1 + cleaned v2 + synthesis lane (no push)
# ----------------------------
preface_v1 = r"""# Preface
## A historical restatement of the study of primes (as the backbone of our paper)

Prime numbers enter mathematics first as irreducible multiplicative atoms: integers (>1) that admit no nontrivial factorization. The earliest “theory of primes” is therefore inseparable from the earliest theory of proof about divisibility, because primes are not an empirical category (like “large numbers”) but a logical category (defined by universal negation over divisors). From the beginning, the subject has been a tension between local discreteness (each prime is a stubborn individual) and global law (their distribution exhibits stable large-scale structure).

1) Antiquity: existence, infinitude, and the first algorithmic lens
The classical starting point is Euclid’s proof that there are infinitely many primes, which is the first decisive statement that primes are not a finite “resource” but an inexhaustible phenomenon of the integers. The proof is constructive in spirit: from any finite list of primes, we build a number that forces a new prime divisor, guaranteeing perpetual novelty. This is not only a theorem about primes; it is a theorem about the structure of arithmetic itself—an early instance of “no finite policy can close the world of integers.” (Aleph Zero)
In the same era of thought, the sieve of Eratosthenes provides the first systematic computational view: rather than seeking primes directly, we iteratively eliminate composites. This “negative definition” viewpoint—prime as “not killed by any small divisor”—will eventually mature into modern sieve theory. The key historical motif already appears here: primes are understood by constraining the composite phase space.

2) Early modern arithmetic: congruence, identities, and tests
As number theory expands, primes become the organizing units of congruences and modular arithmetic. Fermat’s and Euler’s work (and the later refinement into group-theoretic language) treats primes as the moduli where multiplicative structure becomes clean. Along this line, Wilson’s theorem crystallizes a sharp equivalence:
p prime iff (p-1)! ≡ -1 (mod p),
a kind of “perfect but expensive” primality witness. Wilson’s theorem’s significance is conceptual: it sets a gold standard for what it means to characterize primes exactly, while simultaneously exposing the practical barrier (factorial growth) that forces other approaches. (Wikipedia)
This era also teaches a structural lesson we reuse in our work: identities can be logically complete but computationally intractable; the enduring strategy is therefore to develop policy layers (constraints) that eliminate impossibilities cheaply before any expensive certification.

3) The empirical-to-asymptotic transition: Gauss and Legendre’s prime-density conjectures
By the late 18th century, attention shifts from “what primes are” to “how many primes lie below x.” Gauss (as a teenager, by his later recollection) and Legendre converge on the idea that prime density is controlled by logarithms—an astonishing step because it replaces exact arithmetic with smooth approximation. The logarithmic integral Li(x) becomes a natural candidate for π(x), the prime-counting function, marking the birth of the modern “mean-field + fluctuation” mindset. (Mathematical Association of America)
This phase matters for our paper because it introduces the essential coordinate change: primes are sparse in x-space but become more regular in logarithmic coordinates. That coordinate change is exactly the philosophical ancestor of our “log-harmonic signature” language: multiplicative phenomena often linearize in log x.

4) Analytic number theory begins: Dirichlet, Chebyshev, and the first distribution laws beyond “all primes”
Dirichlet’s 1837 theorem on primes in arithmetic progressions establishes that primes are not merely infinite as a set, but equidistributed across congruence classes that are not obstructed by a common factor. This is the first decisive theorem that primes obey a deep fairness principle modulo m, proven via what are now called Dirichlet L-functions—opening the analytic portal. (MIT Mathematics)
Chebyshev then builds strong partial progress toward the prime number theorem by proving that if π(x) behaves like x/log x, then the limiting constant must be 1, and by obtaining robust upper/lower bounds that establish the correct order of growth even without a full limit proof. This is a foundational precursor because it shows how far one can go using relatively elementary inequalities and careful bounding, a template that later reappears in sieve and elementary-proof traditions. (Williams College)

5) Riemann’s 1859 revolution: primes as a spectral phenomenon of zeros
Riemann’s 1859 memoir changes the subject permanently by linking prime distribution to the complex-analytic behavior of ζ(s). Two ingredients dominate the modern worldview: (i) the Euler product (primes encoded multiplicatively), and (ii) the zeros of ζ(s) (fluctuations encoded spectrally). Riemann sketches an explicit-formula relationship between prime counting (in a smoothed sense) and sums over zeros, thereby turning “prime irregularity” into “spectral interference.” (Wikipedia)
This is where our paper’s architecture naturally lives: once primes are understood as “mean field + oscillatory residual,” it becomes mathematically meaningful to talk about channels: a logarithmic base coordinate for the mean field, and harmonic components in log x for fluctuations. The Riemann Hypothesis (RH) then reads as an envelope constraint on those oscillations (real part 1/2 for nontrivial zeros), rather than as a mystical statement about primes themselves. (WIRED)

6) 1896: the Prime Number Theorem is proved (Hadamard; de la Vallée Poussin)
The Prime Number Theorem (PNT) formalizes Gauss/Legendre’s asymptotic insight: π(x) ~ x/log x. Hadamard and de la Vallée Poussin prove it in 1896 using complex analysis and, critically, the non-vanishing of ζ(s) on the line Re(s)=1. This is the canonical victory of analytic number theory: a global counting law extracted from complex-analytic control. (Mathematics Department at UC Davis)
For our purposes, PNT is not “the end of the story” but the establishment of a baseline: any refined prime-localization method is judged against the fact that density is 1/log x at leading order, and any proposed “policy enforcement layer” must respect that asymptotic geometry.

7) Early 20th century: sieve theory, conjectural constellations, and probabilistic structure
With PNT in hand, the field bifurcates into (a) proving deeper distribution results and (b) developing tools to carve out prime-like sets. Hardy and Littlewood propose conjectures on prime constellations (including twin primes and general k-tuples), giving a quantitative heuristic superstructure for patterns beyond single primes. (Wikipedia)
Viggo Brun’s 1919 theorem—showing the sum of reciprocals of twin primes converges—introduces sieve methods as a mature technique with genuinely nontrivial outcomes. (Wikipedia)
Erdős then helps open probabilistic number theory (e.g., Erdős–Kac). (Queen's Math & Stats)

8) Mid-century structural expansion: “zeta functions” beyond ζ(s) (Weil and algebraic geometry)
Weil’s 1949 conjectures (now theorems) generalize “counting ↔ zeta ↔ zeros ↔ error terms” beyond primes. (Pagine)

9) Late 20th to 21st century: computation, combinatorics, and major modern breakthroughs
Selberg/Erdős elementary PNT proofs (1949) legitimize constraint-first architectures. (LSU Math)
Green–Tao (2004) and Zhang/Maynard (2013/2015) exemplify optimized sieve-policy operators. (Annals; AIM)
AKS (2002) grounds the algorithmic benchmark: deterministic polynomial-time primality. (Wikipedia)
"""

preface_v2 = r"""# Preface
## A historical restatement of the study of primes (as the backbone of our paper)

Prime numbers enter mathematics as irreducible multiplicative atoms: integers greater than 1 admitting no nontrivial factorization. From the start, “prime theory” is inseparable from proof about divisibility, because “prime” is a logical category rather than an empirical one: it is defined by a universal negation over divisors. The field has always lived in a productive tension between local discreteness (each prime as an individual event) and global law (stable large-scale behavior in their distribution). We inherit that tension deliberately: our work treats primes as mean-field structure plus residual fluctuations, and it treats inference as an auditable composition of constraints rather than a single miracle formula.

### 1) Antiquity: infinitude and the first algorithmic lens
Euclid’s proof of infinitely many primes is the first decisive statement that primes are not a finite resource but an inexhaustible phenomenon of the integers.[^euclid] The proof is constructive in spirit: from any finite list of primes, one builds an integer that forces a new prime divisor, guaranteeing perpetual novelty. In parallel, the sieve of Eratosthenes supplies the earliest computational posture: rather than seeking primes directly, we iteratively eliminate composites. That “elimination-first” viewpoint is the ancestor of modern sieve theory, and it foreshadows the policy style we adopt: constrain the composite phase space until what remains is forced to be small and testable.

### 2) Early modern arithmetic: congruence, identities, and exact-but-expensive witnesses
As number theory expands, primes become the organizing units of congruence and modular arithmetic. Fermat’s and Euler’s work (later reframed in group-theoretic language) treats primes as moduli where multiplicative structure becomes clean and diagnostics become sharp. Wilson’s theorem then crystallizes an exact equivalence,
\[
p\ \text{prime}\iff (p-1)!\equiv -1\pmod p,
\]
which is conceptually perfect but computationally prohibitive at scale.[^wilson] The methodological lesson endures: some identities are logically complete yet practically unusable, so the winning strategy is to introduce cheaper constraint layers that eliminate impossibilities before invoking any expensive certification.

### 3) The empirical-to-asymptotic transition: Gauss, Legendre, and logarithmic density
By the late 18th century, attention shifts from “what primes are” to “how many primes lie below x.” Gauss and Legendre converge on the striking idea that prime density is governed by logarithms, and that the logarithmic integral offers a natural approximation to the prime-counting function.[^pntnotes] This is the conceptual birth of “mean field + fluctuation”: replace exact arithmetic with a smooth baseline and reserve scrutiny for residual structure. For our paper, this is also the origin of a decisive coordinate change: primes are sparse in x-space but become more regular in log x, a fact that directly motivates our log-volume and log-harmonic language.

### 4) Distribution laws beyond “all primes”: Dirichlet and Chebyshev
Dirichlet’s theorem on primes in arithmetic progressions establishes that primes are not merely infinite as a set; they are equidistributed among admissible residue classes modulo m.[^dirichlet] This is the first decisive “fairness principle” in prime distribution and the portal into analytic number theory via L-functions. Chebyshev’s bounds and associated arguments then show how far one can go with inequalities and careful bounding even without complete asymptotics.[^pntnotes] That bounding lineage matters for us: it validates constraint-first architectures as mathematically serious rather than merely heuristic.

### 5) Riemann: primes as a spectral phenomenon of zeros
Riemann’s 1859 memoir permanently changes the subject by tying prime distribution to the analytic behavior of ζ(s), pairing the Euler product (primes encoded multiplicatively) with the zero set (fluctuations encoded spectrally). In explicit-formula form, prime-counting behavior is related—after smoothing—to oscillatory contributions indexed by zeros, turning “prime irregularity” into something like spectral interference.[^explicit] This is precisely the historical root of our channel language: a smooth baseline in log coordinates plus oscillatory residual structure that is naturally expressed as harmonics in log x. In this framing, RH functions as an envelope constraint on those oscillations rather than as a generator of primes; it governs what kinds of residual growth are permitted.

### 6) 1896: the Prime Number Theorem as baseline geometry
The Prime Number Theorem formalizes the Gauss/Legendre insight:
\[
\pi(x)\sim \frac{x}{\log x}.
\]
Hadamard and de la Vallée Poussin prove it in 1896 using complex analysis and, critically, control of ζ(s) near the line Re(s)=1.[^pntnotes] For our purposes, PNT is not the end of the story but the baseline geometry: any prime-localization or candidate-reduction method must respect the leading-order density 1/log x, and any scoring layer that violates that geometry is ipso facto suspect.

### 7) Early 20th century: sieves, constellations, and probabilistic diagnostics
With PNT established, the field bifurcates into deeper distribution theorems and increasingly powerful methods for carving out prime-like sets. Hardy–Littlewood’s k-tuple heuristics supply a quantitative conjectural superstructure for constellations beyond single primes.[^hl] Brun’s theorem (1919) inaugurates mature sieve technique with nontrivial outcomes, showing that sieve methods can rigorously control densities even when they cannot settle infinitude questions outright.[^brun] Erdős’s probabilistic number theory lens then legitimizes distributional diagnostics for multiplicative statistics, which aligns with our use of compartmentalized, stress-tested observables rather than single-base, single-window anecdotes.[^erdoskac]

### 8) Mid-century expansion: zeta functions beyond ζ(s)
A parallel deepening occurs when zeta functions are generalized to count solutions of equations over finite fields. Weil’s conjectures (now theorems) demonstrate that “counting ↔ zeta ↔ zeros ↔ error terms” is a recurring organizing principle across arithmetic geometry, not an accident of the integers.[^weil] For us, this is methodological permission: it supports treating residual structure and spectral constraints as first-class, disciplined tools rather than decorative metaphor.

### 9) Late 20th to 21st century: computation, combinatorics, and modern policy operators
Modern number theory is shaped by three reinforcing currents. First, Selberg’s elementary proof of PNT shows that deep asymptotics can emerge from combinatorial identities and inequalities without complex analysis, strengthening the legitimacy of constraint-first architectures.[^selberg] Second, additive-combinatoric breakthroughs (e.g., Green–Tao) and bounded-gap results (Zhang; Maynard) exemplify “optimized policy operators”: carefully engineered sieve weights and structural constraints that extract global regularity from local admissibility.[^greentao][^zhang][^maynard] Third, algorithmic primality milestones such as AKS clarify the computational boundary conditions: primality can be decided deterministically in polynomial time, so the scientific target shifts from “can we test?” to “what can we infer, localize, and audit before we test?”[^aks]

**Bridge to our construction.** This history gives us two validated rails: elimination-first constraint systems (Eratosthenes → Brun/Maynard) and mean-field-plus-residual spectral thinking in log coordinates (Gauss/Legendre → Riemann). Our construction sits at their intersection: a governed stack of operators whose job is to prune, score, and diagnose candidates while remaining falsifiable under cross-scale, cross-window, and cross-representation stress tests.

---

## Notes (endnotes)
[^euclid]: Euclid, *Elements*, Book IX, Proposition 20: https://aleph0.clarku.edu/~djoyce/java/elements/bookIX/propIX20.html
[^wilson]: Wilson’s theorem (standard reference): https://en.wikipedia.org/wiki/Wilson%27s_theorem
[^dirichlet]: Dirichlet theorem notes (MIT): https://math.mit.edu/~drew/18.785/lecture1.pdf
[^explicit]: Explicit formula overview (for L-functions): https://en.wikipedia.org/wiki/Explicit_formulae_for_L-functions
[^pntnotes]: Historical notes on the PNT (Petersen, UC Davis-hosted PDF): https://www.math.ucdavis.edu/~tracy/courses/math205A/PNT_Petersen.pdf
[^selberg]: Selberg (1949) “An elementary proof of the prime-number theorem” (PDF): https://www.math.lsu.edu/~mahlburg/teaching/handouts/2014-7230/Selberg-ElemPNT1949.pdf
[^hl]: Hardy–Littlewood k-tuple conjectures (overview): https://en.wikipedia.org/wiki/Hardy%E2%80%93Littlewood_prime_k-tuple_conjecture
[^brun]: Brun’s theorem (overview): https://en.wikipedia.org/wiki/Brun%27s_theorem
[^erdoskac]: Erdős–Kac theorem (overview): https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Kac_theorem
[^weil]: Weil conjectures course notes (PDF): https://pagine.dm.unipi.it/tamas/Weil.pdf
[^greentao]: Green–Tao (Annals PDF): https://annals.math.princeton.edu/wp-content/uploads/annals-v167-n2-p03.pdf
[^zhang]: Zhang bounded gaps (AIM summary): https://aimath.org/news/primegaps70m/
[^maynard]: Maynard “Small gaps between primes” (Annals PDF): https://annals.math.princeton.edu/wp-content/uploads/annals-v181-n1-p07-p.pdf
[^aks]: AKS primality test (overview): https://en.wikipedia.org/wiki/AKS_primality_test
"""

preface_biblio = r"""# Preface — Sources (pointer list)

This file is the “source index” for Preface versions. Prefer primary papers and institutional PDFs; Wikipedia links are allowed as navigational indexes, not as sole authorities.

- Euclid, *Elements*, IX.20: https://aleph0.clarku.edu/~djoyce/java/elements/bookIX/propIX20.html
- Selberg (1949) elementary PNT proof (PDF): https://www.math.lsu.edu/~mahlburg/teaching/handouts/2014-7230/Selberg-ElemPNT1949.pdf
- PNT historical notes (PDF): https://www.math.ucdavis.edu/~tracy/courses/math205A/PNT_Petersen.pdf
- Dirichlet theorem notes (MIT): https://math.mit.edu/~drew/18.785/lecture1.pdf
- Green–Tao (Annals PDF): https://annals.math.princeton.edu/wp-content/uploads/annals-v167-n2-p03.pdf
- Zhang bounded gaps (AIM): https://aimath.org/news/primegaps70m/
- Maynard bounded gaps (Annals PDF): https://annals.math.princeton.edu/wp-content/uploads/annals-v181-n1-p07-p.pdf
- Weil conjectures notes (PDF): https://pagine.dm.unipi.it/tamas/Weil.pdf
- (Index links used sparingly) explicit formula / Wilson / HL / Brun / Erdős–Kac / AKS: Wikipedia entries
"""

preface_readme = """# Preface

This node holds versioned Preface drafts and the running synthesis.

## Structure
- `versions/` — immutable snapshots (v1, v2, …)
- `synthesis/` — merge target (“best-of” aggregator)
- `toc/` — local table of contents for this node
- `notes/` — meta notes that must not leak into publication text

## Version policy
- We do not overwrite old versions; we add vN+1.
- We keep citations clean in v2+ (endnotes preferred).
"""

preface_toc = """# TOC — Preface

## Versions
- `versions/preface-v1.md` — raw imported draft (as received)
- `versions/preface-v2.md` — cleaned, endnoted, publication-ready narrative
- `versions/preface-sources.md` — source index (pointers)

## Synthesis
- `synthesis/preface-synthesis-v0.md` — merge-target scaffold
"""

preface_compare = """# Preface comparison — v1 vs v2

## v1
- Strong historical arc and clear linkage to our method.
- Mixed-quality in-text citations (“(Wikipedia)”/“(WIRED)”) inside narrative.
- Several claims are correct but not citation-disciplined.

## v2
- Same arc, tighter prose, explicit bridge into our construction.
- Removes casual parentheticals; uses endnotes instead.
- Downgrades Wikipedia to index-role (navigation), keeping primary PDFs where possible.
"""

preface_synth = """# Preface — Synthesis (v0)

## Goal
Merge the strongest features across Preface versions while keeping publication text clean.

## Merge checklist
- [ ] keep “two rails” bridge: elimination-first + log-spectral residual
- [ ] keep narrative cadence (no bibliography clutter in body)
- [ ] ensure every major historical claim is endnoted (v2 standard)
- [ ] add/remove milestones only if they strengthen the backbone of Part II

## Candidate carryovers
- v1 opening tension (discrete vs law)
- v2 bridge paragraph (Preface → Part II operator stack)
"""

write(PREFACE / "README.md", preface_readme)
write(PREFACE / "toc" / "TOC.md", preface_toc)
write(PREFACE / "versions" / "preface-v1.md", preface_v1)
write(PREFACE / "versions" / "preface-v2.md", preface_v2)
write(PREFACE / "versions" / "preface-sources.md", preface_biblio)
write(PREFACE / "synthesis" / "preface-synthesis-v0.md", preface_synth)
write(PREFACE / "compare-v1-v2.md", preface_compare)

# ----------------------------
# Technical core scaffold: chapter -> section -> subsection folders
# ----------------------------
core_readme = """# Part II — Technical Core (Heller–Winters Construction)

We keep edits small and isolatable by enforcing a three-level lattice:

- `chapter-XX-*` — chapter scope
- `sections/NN-*` — section/subtopic scope
- `subsections/` — sub-subtopic scope (three default lanes):
  01-context, 02-formalism, 03-tests

Each node has:
- `README.md` (human-facing overview)
- `toc/TOC.md` (local navigation)
- optional `versions/`, `synthesis/`, `notes/` if needed later
"""
write(CORE / "README.md", core_readme)

chapters = {
  1: {
    "title": "Purpose and Thesis",
    "overview": "We situate primes as locally discrete but globally lawful, and we frame our contribution as a policy-enforced multiscale program rather than a single trick. We separate hard constraints (eliminators) from soft analytic layers (scorers and diagnostics). We define success as a disciplined, falsifiable pipeline that increases inference value and remains auditable in failure. We distinguish constructive localization from proof of RH, treating RH-consistency as an envelope constraint on residuals. We require a rigor contract: every operator is either theorem-backed, a coordinate change, or a labeled heuristic probe.",
    "sections": [
      "Mean-field vs fluctuation decomposition",
      "Volume not distance as central invariant",
      "Policy-enforced inference vs brute search",
      "Signal vs artifact",
      "Determinism vs fitted parameters",
      "Falsifiability criteria",
      "Scope limits and non-claims",
      "Notation and canonical coordinates",
      "Relationship to classical prime theorems",
      "Roadmap of the full stack",
    ],
  },
  2: {
    "title": "Canonical Coordinate System",
    "overview": "We formalize coordinate choices that make volume measurable and scale comparisons meaningful. We use u = ln x so multiplicative growth becomes additive translation and window schedules become fixed log-lengths. Base change becomes linear frequency rescaling in the log-harmonic picture, so cross-base persistence is a strong anti-artifact test. We separate index space, value space, and policy/state space to avoid category errors. We define normalization conventions so comparisons across scales are meaningful.",
    "sections": [
      "Log coordinate u = ln x",
      "Multiplicative windows and log-length L = ln r",
      "Change-of-base as frequency rescaling",
      "Volume element and expectation compatibility",
      "Octaves/decades as canonical windows",
      "Metallic/plastic windows as irrational scalings",
      "Index space vs value space vs policy space",
      "Window families and nesting",
      "Boundary effects and endcaps",
      "Units, normalization, invariance",
    ],
  },
  3: {
    "title": "Prime Density Mean-Field Model",
    "overview": "We restate the mean-field picture: density about 1/ln x and cumulative count about x/ln x. Any candidate reduction must preserve this baseline rather than hallucinate structure. We frame distribution as mean field plus residual; the residual is where spectral content lives. We use windowed expectations via ∫ dt/ln t rather than raw counts. This chapter sets guardrails for later operators.",
    "sections": [
      "pi(x) ~ x/ln x heuristic",
      "Local intensity ~ 1/ln x",
      "Window expectation integral",
      "Decade vs octave expectations",
      "Drift in 1/u in log coordinates",
      "Coverage interpretations",
      "Average gap ~ ln x",
      "Variance intuition",
      "Scaling regimes",
      "Mean-field invariants used by policy",
    ],
  },
  4: {
    "title": "Boundedness Layer",
    "overview": "We formalize the doubling bound guaranteeing a prime in (n,2n), giving a finite search interval for the next prime after p. This converts localization from unbounded to bounded policy space. We treat the bound as the outer enclosure that all other sieves act inside. In log-window language it becomes a fixed log-length cell L = ln 2 around u = ln p. The bound is scaffold, not solution, so we record its failure modes explicitly.",
    "sections": [
      "Bertrand/Chebyshev bound (n,2n)",
      "Specialization to next-prime window (p,2p)",
      "Implications for search complexity",
      "Interaction with wheel modulus selection",
      "Bounds as outer policy boundary",
      "Nested bounds across ratios",
      "Bounding in log coordinate",
      "Practical boundedness metrics",
      "Failure modes (trivial, degenerate)",
      "Bound-sensitive scoring rules",
    ],
  },
  5: {
    "title": "Wheel Sieve Layer",
    "overview": "We formalize wheel sieves as modular admissibility filters: candidates must be coprime to a chosen modulus M. Wheels eliminate composite volume cheaply and provide stable periodic structure via residue classes. We treat wheel selection as a policy decision balancing pruning power and overhead, including resonance risk with base partitions. Residue classes also serve as state labels for later symmetry governance. Wheel is deterministic elimination, not prediction, and we keep that separation explicit.",
    "sections": [
      "Modulus definition",
      "Reduced residue classes",
      "Candidate density phi(M)/M",
      "Residue graphs and transitions",
      "Wheel depth vs compute cost",
      "Interaction with base representations",
      "Compatibility with crystallographic partitioning",
      "Wheel as deterministic eliminator",
      "Wheel as feature generator",
      "Wheel invariants across windows",
    ],
  },
  6: {
    "title": "Symmetric Offset Algebra",
    "overview": "We formalize symmetric-offset identities (difference-of-squares and shell families) that yield composite certificates and connect factor pairs to additive geometry. Parity constraints determine when decompositions exist, providing cheap policy filters. Shell families can be analyzed statistically in log windows, producing both eliminators and features. Hyperbola geometry (ab=n) in rotated coordinates links naturally to hyperbolic identity-channel reasoning later. Shell enforcement is positioned as structural noise reduction.",
    "sections": [
      "Difference-of-squares identity",
      "Neighbor shell",
      "General offset shells",
      "Factor-pair to symmetric mapping",
      "Parity constraints",
      "Composite certificates",
      "Shell density vs scale",
      "Shell statistics in log windows",
      "Shell and wheel interaction",
      "Shells as structural noise reducers",
    ],
  },
}

# Minimal scaffolds for Chapters 7–23: titles + section lists only (overview short)
chapters_7_23 = {
  7: ("Figurate Number Lattices", ["Triangular structure","Polygonal families","Second differences","sqrt(X) counting law","Offsets","Trapezoidal sums","Scaffolds","Residue intersections","Congruence constraints","Density contrast"]),
  8: ("Base-(b) Compartmentalization", ["Digit orbits","Base-change invariance","Repeating expansions","Decimal/binary/hex","Base symmetries","Carry coupling","Wheel compatibility","Window alignment","Cross-base consensus","Base-invariant features"]),
  9: ("(p)-Adic Structure Layer", ["Valuations","p-adic balls","Multiplicative signatures","Separating digit artifacts","Lifting logic","Local constraints","Depth schedules","Wheel interaction","Quotient features","Triangulation with Zeckendorf"]),
 10: ("Quotient Functions and Normalization", ["Density quotient","Li quotient","Chebyshev residual","Window quotients","Residue-sector quotients","Base-conditioned","p-adic-conditioned","Robust normalization","Schedule stability","Quotient invariants"]),
 11: ("Euler–Mascheroni Constant (gamma)", ["Definition","Harmonic vs log","Calibration role","Summation corrections","Log-volume connection","Window calibration","Error floors","Quotient interactions","Ledger placement","Misuse prevention"]),
 12: ("Euler–Maclaurin Summation Bridge", ["Decomposition","Boundary terms","Bernoulli structure","Volume laws","Curvature regularity","Window approximations","Error narratives","Sampling vs density","Linking to gamma","Mean/residual separation"]),
 13: ("Ratio Families as Window Schedules", ["Ratio/log-length","Anchor windows","Metallic family","Golden/silver","Plastic constant","Continued fractions","Resonance avoidance","Multiresolution nesting","Ratio mixing","Consensus tests"]),
 14: ("Ordering and Governance of Ratio Application", ["Tier-0 lattice-safe","Tier-1 anchors","Tier-2 probes","Add/prune rules","Overfit avoidance","Cross-check logic","Conflict resolution","Aggregation","Sensitivity diagnostics","Ratios as knobs"]),
 15: ("Harmonic Signature Formalism", ["Harmonic coordinate","Log-harmonics","Cos/sin decomposition","Frequency resolution","Mode count","Coherence","Mixers","Window fingerprints","Base-invariant spectra","Mapping the gate"]),
 16: ("Identity Channels: Circular vs Hyperbolic", ["Circle identity","Euler form","Hyperbolic identity","Envelope/phase","Projections","Off-channel residual","Mixers","Diagnostics","Residual ledger","Anti-artifact rationale"]),
 17: ("RH-Consistent Envelope Constraint", ["rho=beta+i*gamma","Decomposition","Log-periodic oscillations","Hyperbolic envelope","RH policy","Envelope measurement","Scale stability","Failure signatures","Guidance for pruning/scoring","Not a proof"]),
 18: ("Cosine Phase-Gate Construction", ["Transcription","Parameter roles","60/90 quantization","Hit criteria","Wheel compatibility","Base compatibility","Schedule compatibility","No-free-knob governance","Circular-ledger integration","Falsification rules"]),
 19: ("Structural Sieves Beyond the Wheel", ["Squares shells","Small-factor constraints","Residue exclusion","Divisor-offset symmetry","Figurate exclusions","Digit exclusions","p-adic exclusions","Mixed ordering","Depth accounting","Conservatism tradeoffs"]),
 20: ("Optimization View: Policy as Constraint System", ["CSP framing","Hard vs soft","Multiobjective","Ratio regularizer","Base regularizer","p-adic regularizer","Residual objective","Window stability","Complexity budget","Interpretability objective"]),
 21: ("Classical Theorems as Policy Operators", ["Bertrand","Wilson","Fermat/Euler tests","Goldbach heuristics","Twin-prime operators","Gap inequalities","Quadratic residues","CRT combiner","Dirichlet/AP distribution","Misuse risks"]),
 22: ("Evidence Ledger and Falsification Protocol", ["Determinism requirement","Prediction events","FP/FN definitions","Scale drift","Base drift","p-adic drift","Residual thresholds","Ablation","Failure taxonomy","Novelty criteria"]),
 23: ("Consolidated Spec and Future Extensions", ["One-page spec","Data structures","Parameter governance","Ratio governance","Complexity accounting","Claims taxonomy","Constellations","Prime powers","psi-residuals / lattice counting","Research program map"]),
}

for k, (title, sections) in chapters_7_23.items():
    if k not in chapters:
        chapters[k] = {
            "title": title,
            "overview": "Scaffold chapter overview. (We will replace with the 4–6 sentence chapter overview from the TOC draft and keep the technical contract consistent.)",
            "sections": sections,
        }

def node_boiler(title: str) -> str:
    return f"""# {title}

## Purpose
(One paragraph: why this node exists in the operator stack.)

## Current status
- Draft: stub
- Owner: us
- Next edit scope: keep changes local to this node

## Notes
- This file is intentionally short; deeper material lives in subsections and versions/synthesis when needed.
"""

write(CORE / "toc" / "TOC.md", "# TOC — Part II Technical Core\n\n(Generated per-chapter TOCs live inside each chapter folder.)\n")

for ch_num in range(1, 24):
    ch = chapters[ch_num]
    ch_slug = f"chapter-{ch_num:02d}-{slugify(ch['title'])}"
    ch_dir = CORE / ch_slug
    write(ch_dir / "README.md", f"# Chapter {ch_num:02d} — {ch['title']}\n\n{ch['overview']}\n")
    toc_lines = [f"# TOC — Chapter {ch_num:02d}\n", "## Sections\n"]
    for i, sec in enumerate(ch["sections"], start=1):
        sec_slug = f"{i:02d}-{slugify(sec)}"
        sec_dir = ch_dir / "sections" / sec_slug
        write(sec_dir / "README.md", node_boiler(f"Section {ch_num:02d}.{i:02d} — {sec}"))
        write(sec_dir / "toc" / "TOC.md", f"# TOC — Section {ch_num:02d}.{i:02d}\n\n## Subsections\n- 01-context\n- 02-formalism\n- 03-tests\n")
        for j, sub in enumerate(["context", "formalism", "tests"], start=1):
            sub_dir = sec_dir / "subsections" / f"{j:02d}-{sub}"
            write(sub_dir / "README.md", node_boiler(f"Subsection {ch_num:02d}.{i:02d}.{j:02d} — {sub.title()}"))
            write(sub_dir / "toc" / "TOC.md", f"# TOC — Subsection {ch_num:02d}.{i:02d}.{j:02d}\n\n(Insert outline here.)\n")
        toc_lines.append(f"- {sec_slug}/  — {sec}\n")
    write(ch_dir / "toc" / "TOC.md", "".join(toc_lines))

print("OK: Preface v1/v2 stored; technical core scaffold created.")
