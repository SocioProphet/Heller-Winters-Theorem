from __future__ import annotations
from pathlib import Path

ROOT = Path("manuscript")

def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

PREFACE_V1 = """# Preface
## A historical restatement of the study of primes (as the backbone of our paper)

Prime numbers enter mathematics first as irreducible multiplicative atoms: integers (>1) that admit no nontrivial factorization. The earliest “theory of primes” is therefore inseparable from the earliest theory of proof about divisibility, because primes are not an empirical category (like “large numbers”) but a logical category (defined by universal negation over divisors). From the beginning, the subject has been a tension between local discreteness (each prime is a stubborn individual) and global law (their distribution exhibits stable large-scale structure).

### 1) Antiquity: existence, infinitude, and the first algorithmic lens
The classical starting point is Euclid’s proof that there are infinitely many primes, which is the first decisive statement that primes are not a finite “resource” but an inexhaustible phenomenon of the integers. The proof is constructive in spirit: from any finite list of primes, we build a number that forces a new prime divisor, guaranteeing perpetual novelty. This is not only a theorem about primes; it is a theorem about the structure of arithmetic itself—an early instance of “no finite policy can close the world of integers.”

In the same era of thought, the sieve of Eratosthenes provides the first systematic computational view: rather than seeking primes directly, we iteratively eliminate composites. This “negative definition” viewpoint—prime as “not killed by any small divisor”—will eventually mature into modern sieve theory. The key motif already appears here: primes are understood by constraining the composite phase space.

### 2) Early modern arithmetic: congruence, identities, and tests
As number theory expands, primes become the organizing units of congruences and modular arithmetic. Fermat’s and Euler’s work (and the later refinement into group-theoretic language) treats primes as the moduli where multiplicative structure becomes clean. Along this line, Wilson’s theorem crystallizes a sharp equivalence:
\\[
p\\ \\text{prime} \\iff (p-1)!\\equiv -1 \\pmod p.
\\]
Its significance is conceptual: it sets a gold standard for exact characterization, while exposing the practical barrier (factorial growth) that forces layered policy constraints before expensive certification.

### 3) The empirical-to-asymptotic transition: Gauss and Legendre’s prime-density conjectures
By the late 18th century, attention shifts from “what primes are” to “how many primes lie below x.” Gauss and Legendre converge on the idea that prime density is controlled by logarithms. The logarithmic integral \\(\\mathrm{Li}(x)\\) becomes a natural candidate for \\(\\pi(x)\\), marking the birth of the “mean-field + fluctuation” mindset.

This phase matters for our paper because it introduces the essential coordinate change: primes are sparse in \\(x\\)-space but become more regular in logarithmic coordinates. That coordinate change is the ancestor of our log-harmonic language: multiplicative phenomena often linearize in \\(\\log x\\).

### 4) Analytic number theory begins: Dirichlet, Chebyshev, and the first distribution laws beyond “all primes”
Dirichlet’s theorem on primes in arithmetic progressions establishes that primes obey a fairness principle across admissible residue classes modulo \\(m\\). Chebyshev then obtains robust upper/lower bounds showing the correct order of growth for \\(\\pi(x)\\), even without the full limit—demonstrating how far inequality-driven policy can go before deep analytic machinery is required.

### 5) Riemann’s 1859 revolution: primes as a spectral phenomenon of zeros
Riemann links prime distribution to the complex-analytic behavior of \\(\\zeta(s)\\). Two ingredients dominate the modern worldview: (i) the Euler product (primes encoded multiplicatively) and (ii) the zeros of \\(\\zeta(s)\\) (fluctuations encoded spectrally). The explicit-formula viewpoint turns “prime irregularity” into “spectral interference.”

This is where our architecture naturally lives: once primes are understood as “mean field + oscillatory residual,” it becomes meaningful to talk about identity channels: a logarithmic coordinate for the mean field, and harmonic components in \\(\\log x\\) for fluctuations. RH reads as an envelope constraint on those oscillations—not as a naïve periodicity claim.

### 6) 1896: the Prime Number Theorem is proved (Hadamard; de la Vallée Poussin)
The Prime Number Theorem formalizes Gauss/Legendre’s asymptotic insight:
\\[
\\pi(x)\\sim \\frac{x}{\\log x}.
\\]
For us, PNT is the baseline: any “localization” method is judged against density \\(1/\\log x\\), and any policy layer must respect asymptotic geometry.

### 7) Early 20th century: sieve theory, conjectural constellations, and probabilistic structure
Hardy–Littlewood propose quantitative heuristics for constellations (twin primes and general \\(k\\)-tuples). Brun’s theorem introduces sieve methods as a mature technique with genuinely nontrivial outcomes. Erdős and probabilistic number theory legitimize distributional diagnostics—exactly the lens we use when we compartmentalize by base, residue, and schedule.

### 8) Mid-century structural expansion: zeta functions beyond \\(\\zeta(s)\\)
Weil’s program generalizes the “counting ↔ zeta ↔ zeros ↔ error terms” paradigm far beyond primes. This matters here as methodological permission: treating localization as disciplined interplay between discrete counting and spectral constraints is historically consistent with number theory’s most successful expansions.

### 9) Late 20th to 21st century: computation, combinatorics, and modern breakthroughs
Selberg–Erdős elementary proofs of PNT demonstrate that deep asymptotics can arise without complex analysis—by identities and inequalities. Green–Tao and bounded-gap breakthroughs show modern “optimized policy operators” in action (sieve weights extracting global structure from admissibility). AKS clarifies the computational boundary: primality is checkable in polynomial time; localization/prediction is the hard part.

## Minimal bibliography pointers (full URLs, unshortened)
(Stored in manuscript/references/URLS.md)
"""

URLS = """# URLs (unshortened)

Euclid, Elements, Book IX, Prop. 20:
https://aleph0.clarku.edu/~djoyce/java/elements/bookIX/propIX20.html

Selberg (1949) “An elementary proof of the prime-number theorem” (PDF):
https://www.math.lsu.edu/~mahlburg/teaching/handouts/2014-7230/Selberg-ElemPNT1949.pdf

Prime Number Theorem historical notes (PDF):
https://www.math.ucdavis.edu/~tracy/courses/math205A/PNT_Petersen.pdf

Riemann explicit formula (overview):
https://en.wikipedia.org/wiki/Explicit_formulae_for_L-functions

Brun’s theorem overview:
https://en.wikipedia.org/wiki/Brun%27s_theorem

Green–Tao (Annals paper PDF):
https://annals.math.princeton.edu/wp-content/uploads/annals-v167-n2-p03.pdf

Zhang bounded gaps (AIM news summary):
https://aimath.org/news/primegaps70m/

Maynard “Small gaps between primes” (Annals PDF):
https://annals.math.princeton.edu/wp-content/uploads/annals-v181-n1-p07-p.pdf

AKS primality test overview:
https://en.wikipedia.org/wiki/AKS_primality_test

Weil conjectures course notes (PDF):
https://pagine.dm.unipi.it/tamas/Weil.pdf
"""

CH0 = """# CHAPTER 0 — Claims Ledger, Notation, and the Reproducibility Standard

Hebrew (עִבְרִית)  
בַּקְּשׁוּ אֶת־הָאֱמֶת וְאַל־תִּירְאוּ לִבְחֹן אֶת־דַּרְכֵּיכֶם׃  
Seek truth, and do not fear to test your ways.

Greek (Ἑλληνικά)  
ζητεῖτε τὴν ἀλήθειαν· τὸ δὲ δοκιμάζειν ἔργον ἀγάπης ἐστίν.  
Seek truth; and testing is the work of love.

English  
Truth that cannot be checked is only a story. Truth that can be checked becomes a tool.

---

## Introductory Visualization for Chapter 0
**Prime Ladder on the Log Line**  
A clean strip-plot of the first N primes on a logarithmic axis, with tick-marks at 10^k. The point is not beauty—it is orientation: primes are sparse, growth is nonlinear, and our “natural” linear intuition is the wrong ruler.

*Caption:* Before we build phase, circle, or spectrum, we set the scale: primes live most naturally on the log line.

---

## 0.1 Why This Chapter Exists
This chapter is the spine that prevents us from lying to ourselves. We separate what we define, what we prove, what we observe, and what we speculate. Nothing in this book is allowed to float between those categories.

---

## 0.2 The Four Bins
(A) **Definitions** — objects we define precisely.  
(B) **Theorems / Proofs** — statements proved deductively from stated assumptions.  
(C) **Empirical Regularities** — repeatable patterns in computation/plots (not proofs).  
(D) **Heuristics / Interpretations** — intuition-guides; never used as proof.

Every claim in the manuscript is tagged A/B/C/D at first appearance.

---

## 0.3 Minimal Notation
- \\(\\mathbb{P}\\): the set of primes  
- \\(p_n\\): the n-th prime  
- \\(\\log\\): natural logarithm  
- \\(S^1 = \\{e^{i\\theta}:\\theta\\in\\mathbb{R}\\}\\): unit circle  
- \\(\\theta\\bmod 2\\pi\\): angle wrapped to \\([0,2\\pi)\\)  
- \\(\\arg(z)\\): argument of a complex number \\(z\\)

We keep notation brutally consistent. If a symbol changes meaning, we rename it.

---

## 0.4 The Prime-to-Geometry Template
**Angle map:** \\(\\theta:\\mathbb{P}\\to\\mathbb{R}\\)  
**Circle embedding:** \\(\\Phi(p)=e^{i\\theta(p)}\\in S^1\\)  
**Wrapped phase:** \\(r(p)=\\theta(p)\\bmod 2\\pi\\)

Different chapters propose different \\(\\theta(p)\\). The whole game is whether \\(r(p)\\) behaves like noise, or whether structure survives controls.

---

## 0.5 What We Claim in This Book
**A-claims (definitions we commit to)**  
A1: Every plot corresponds to an explicit \\(\\theta(p)\\) and an explicit prime range.  
A2: Every figure can be reproduced from text alone.

**C-claims (empirical observations, not yet proofs)**  
C1: Certain log-circle embeddings produce stable geometric structure across large prime windows.  
C2: Certain phase constructions preserve non-random clustering under multiple controls.

**B-claims (what must be proved to earn theorem-status)**  
B1: Theorem-grade structure must be deduced from stated assumptions and survive counterexamples.  
B2: Any “regularity” must survive a null model and a stress test.

Not claimed: we do not claim naïve periodicity; we do not claim pictures are proofs; we do not claim an operator is meaningful unless it survives controls.

---

## 0.6 Reproducibility Contract
Every result must specify:
1) Prime selection: by value range \\([p_a,p_b]\\) or index range \\([n_a,n_b]\\)  
2) Transformation: exact formula for \\(\\theta(p)\\)  
3) Wrapping/normalization: exact \\(\\bmod 2\\pi\\), scaling, saturation  
4) Rendering: scatter vs density vs histogram vs cumulative

If any of the above are missing, the figure is an illustration—not evidence.

---

## 0.7 Controls, Null Models, and Stress Tests
Null N1: random-phase baseline (i.i.d. uniform angles).  
Null N2: random odd integers (or wheel-filtered integers) with the same range/cardinality.  
Stress S1: window expansion.  
Stress S2: subsampling (every k-th prime or random subset).  
Stress S3: perturb constants (small epsilon sweeps).

---

## 0.8 The Claims Ledger Table
Per chapter:
- Definition used (explicit formula)
- What it predicts
- Which tests it passes (N1/N2/S1/S2/S3)
- Status (A/B/C/D)

---

## 0.9 Transition
Next we stop framing and start doing: print equations → normalize units → plot → test controls → interpret.

Now we show the work.
"""

CH1 = """# CHAPTER 1 — Phase Definitions: From the Log Line to the Circle

Hebrew (עִבְרִית)  
פִּתְחוּ לִי שַׁעֲרֵי־צֶדֶק; אָבֹא־בָם, אוֹדֶה יָהּ׃  
Open to us the gates of righteousness; we enter and give thanks.

Greek (Ἑλληνικά)  
ὁ λόγος ἐστὶν ἀρχή· καὶ ἡ ἀρχὴ ζητεῖ τάξιν.  
The Logos is beginning; and beginning seeks order.

English  
We do not guess our way into truth. We define. We compute. We test. Then we speak.

---

## Introductory Visualization for Chapter 1
**The Log-Circle Map of Primes**  
Plot each prime \\(p\\) on the unit circle using
\\[
\\Phi_{\\log}(p)=e^{i(\\log p \\bmod 2\\pi)}.
\\]
This is the base instrument: the simplest log-phase embedding. Everything else is refinement, control, or alternative phase choice.

*Caption:* The circle is not decoration—it is a phase instrument. The question is whether primes leave a fingerprint after wrapping.

---

## 1.1 The Phase Pipeline (canonical)
1) choose a scalar transform \\(x(p)\\)  
2) convert to an angle \\(\\theta(p)\\)  
3) wrap to \\([0,2\\pi)\\)  
4) embed on the circle \\(e^{i\\theta}\\)

Formally:
- scalar: \\(x:\\mathbb{P}\\to\\mathbb{R}\\)
- angle: \\(\\theta(p)=\\alpha x(p)+\\beta\\)
- wrapped: \\(r(p)=\\theta(p)\\bmod 2\\pi\\)
- embedding: \\(\\Phi(p)=e^{ir(p)}\\in S^1\\)

\\(\\alpha,\\beta\\) are explicit constants—not tunable knobs—unless declared as a tested parameter family.

---

## 1.2 Base Phase Families

### 1.2.1 Log phase (baseline)
\\(x(p)=\\log p\\), \\(\\Phi_{\\log}(p)=e^{i(\\log p\\bmod 2\\pi)}\\)

### 1.2.2 Double-log phase (slow phase)
\\(x(p)=\\log\\log p\\), \\(\\Phi_{\\log\\log}(p)=e^{i(\\log\\log p\\bmod 2\\pi)}\\)

### 1.2.3 Index phase (ordering control)
For \\(p_n\\) the n-th prime:
\\(\\Phi_{\\mathrm{idx}}(p_n)=e^{i(n\\bmod 2\\pi)}\\)

This is deliberately blunt: if “structure” survives under \\(\\log p\\) but not under \\(n\\), it is likelier tied to magnitude than enumeration.

---

## 1.3 Hyperbolic Coupling Layer (bridge operator) — **scaled to avoid blowup**
We sometimes pair a bounded phase channel with an unbounded amplitude channel. To keep this numerically meaningful, we **center in a window**.

Let \\(u(p)=\\log p\\). On a window \\(W=[n_a,n_b]\\), define
\\[
\\tilde u(p)=u(p)-\\mathrm{median}_W(u).
\\]
Then:
\\[
a(p)=\\cosh(\\tilde u(p)),\\quad b(p)=\\sinh(\\tilde u(p)),
\\quad
u_\\circ(p)=\\cos(r(p)),\\quad v_\\circ(p)=\\sin(r(p)).
\\]
Coupled probes:
\\[
I_1(p)=a(p)u_\\circ(p),\\qquad I_2(p)=b(p)v_\\circ(p).
\\]
These are **measuring tools**, not proof objects: they test whether the same transform carries coherent signal in bounded and envelope-like channels.

---

## 1.4 The Winters Log-Circle Instrument (credited visualization step) — **non-degenerate form**
The core log-circle instrument is:
\\[
r(p)=\\log p\\bmod 2\\pi,\\qquad \\Phi_{\\log}(p)=e^{ir(p)}.
\\]
A circle wrap discards scale information, so every serious use is **two-channel**: phase + a second scalar channel \\(s(p)\\) (window index, density bin, \\(\\log\\log p\\), or radial fraction).

Example (phase + radial fraction):
\\[
s(p)=\\operatorname{frac}\\Big(\\frac{\\log p}{2\\pi}\\Big),
\\]
and we render \\(\\Phi_{\\log}(p)\\) with density stratified by \\(s(p)\\) or by prime-index windows.

This is the point of the instrument: phase is the circle; windowing/density is where signal must survive controls.

---

## 1.5 The Explicit Phase Equation Slot (verbatim insertion point)
Reserved for the explicit phase equation as it appears in the original notes. Insert verbatim, then normalize into unit-clean form (radians, consistent wrapping, defined domain).

---

## 1.6 Validation Checklist (for every phase equation)
Domain validity; unit sanity; growth sanity; small-prime edge cases; wrap applied once; determinism (no hidden knobs); controls (random-phase + odd-integer/wheel baselines).

---

## 1.7 Immediate Experiments
For \\(\\Phi_{\\log},\\Phi_{\\log\\log},\\Phi_{\\mathrm{idx}}\\):
- circle scatter for a fixed window  
- angle histogram on \\([0,2\\pi)\\)  
- window expansion \\([n_a,n_b]\\to[n_a,10n_b]\\)  
- nulls: random phases + odd integers / wheel-filtered integers

Goal: establish what a real signal must survive.

---

## 1.8 Transition
Next chapter: insert the explicit phase equation, normalize it, and run it through the full contract: plots, nulls, stress tests, stability checks.

Now we show the work.
"""

def main() -> None:
    # Preface v1 + URLs
    write(ROOT / "preface" / "PREFACE-v1.md", PREFACE_V1)
    write(ROOT / "references" / "URLS.md", URLS)

    # Chapters 0 and 1 content
    ch0 = ROOT / "part-ii-technical-core"
    ch0_dir = next(ch0.glob("chapter-00-*"))
    ch1_dir = next(ch0.glob("chapter-01-*"))
    write(ch0_dir / "README.md", CH0)
    write(ch1_dir / "README.md", CH1)

if __name__ == "__main__":
    main()
