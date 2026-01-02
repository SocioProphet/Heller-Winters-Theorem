# CHAPTER 0 — Claims Ledger, Notation, and the Reproducibility Standard

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
- \(\mathbb{P}\): the set of primes  
- \(p_n\): the n-th prime  
- \(\log\): natural logarithm  
- \(S^1 = \{e^{i\theta}:\theta\in\mathbb{R}\}\): unit circle  
- \(\theta\bmod 2\pi\): angle wrapped to \([0,2\pi)\)  
- \(\arg(z)\): argument of a complex number \(z\)

We keep notation brutally consistent. If a symbol changes meaning, we rename it.

---

## 0.4 The Prime-to-Geometry Template
**Angle map:** \(\theta:\mathbb{P}\to\mathbb{R}\)  
**Circle embedding:** \(\Phi(p)=e^{i\theta(p)}\in S^1\)  
**Wrapped phase:** \(r(p)=\theta(p)\bmod 2\pi\)

Different chapters propose different \(\theta(p)\). The whole game is whether \(r(p)\) behaves like noise, or whether structure survives controls.

---

## 0.5 What We Claim in This Book
**A-claims (definitions we commit to)**  
A1: Every plot corresponds to an explicit \(\theta(p)\) and an explicit prime range.  
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
1) Prime selection: by value range \([p_a,p_b]\) or index range \([n_a,n_b]\)  
2) Transformation: exact formula for \(\theta(p)\)  
3) Wrapping/normalization: exact \(\bmod 2\pi\), scaling, saturation  
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
