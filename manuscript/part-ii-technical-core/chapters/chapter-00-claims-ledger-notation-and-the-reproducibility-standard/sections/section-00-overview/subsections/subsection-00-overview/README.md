# CHAPTER 00 — Claims Ledger, Notation, and the Reproducibility Standard

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

**“Prime Ladder on the Log Line”**  
A clean strip-plot of the first N primes on a logarithmic axis, with tick-marks at 10^k. The point is not beauty—it is orientation: primes are sparse, growth is nonlinear, and our “natural” linear intuition is the wrong ruler.

*Caption:* Before we build phase, circle, or spectrum, we set the scale: primes live most naturally on the log line.

---

## 0.1 Why This Chapter Exists
This chapter is the spine that prevents us from lying to ourselves. We separate what we define, what we prove, what we observe, and what we speculate. Nothing in this book is allowed to float between those categories.

---

## 0.2 The Four Bins

**(A) Definitions**  
Objects we define precisely so there is no ambiguity.

**(B) Theorems / Proofs**  
Statements proved deductively from stated assumptions.

**(C) Empirical Regularities**  
Patterns observed in computation or plots. Repeatable experiments. These are not proofs.

**(D) Heuristics / Interpretations**  
Narratives and intuition-guides. Helpful for insight; never used as proof.

Every claim in the manuscript is tagged A/B/C/D at first appearance.

---

## 0.3 Minimal Notation
- \mathbb{P}: the set of primes  
- p_n: the n-th prime  
- \log: natural logarithm  
- S^1 = \{e^{i\theta}:\theta\in\mathbb{R}\}: unit circle  
- \theta \bmod 2\pi: angle wrapped to [0,2\pi)  
- \arg(z): argument of a complex number z  

We will keep notation brutally consistent. If a symbol changes meaning, we rename it.

---

## 0.4 The Prime-to-Geometry Template

**Definition (Angle map).**  
\theta:\mathbb{P}\rightarrow\mathbb{R}

**Definition (Circle embedding).**  
\Phi(p)=e^{i\theta(p)}\in S^1

**Definition (Wrapped phase).**  
r(p)=\theta(p)\ \bmod\ 2\pi

Different chapters propose different \theta(p). The whole game is whether r(p) behaves like noise, or whether structure survives controls.

---

## 0.5 What We Claim in This Book

**A-claims (definitions we commit to)**  
A1: Every plot corresponds to an explicit \theta(p) and an explicit prime range.  
A2: Every figure can be reproduced from text alone.

**C-claims (empirical observations, not yet proofs)**  
C1: Certain log-circle embeddings produce stable geometric structure across large prime windows.  
C2: Certain phase constructions preserve non-random clustering under multiple controls.

**B-claims (what must be proved to earn theorem-status)**  
B1: If a structural claim is asserted as theorem-grade, it must be deduced from stated assumptions and validated against counterexamples.  
B2: Any “regularity” must survive a null model and a stress test (below).

**Not claimed:** We do not claim naïve periodicity of primes. We do not claim a picture is a proof. We do not claim an operator is meaningful unless it survives a control.

---

## 0.6 Reproducibility Contract

Every result in this book must specify:
1. **Prime selection:** by value range [p_a,p_b] or by index range [n_a,n_b]  
2. **Transformation:** the exact formula for \theta(p) (or the intermediate scalar that becomes \theta)  
3. **Wrapping / normalization:** exact rule for \bmod 2\pi, scaling, or saturation  
4. **Rendering:** scatter vs density vs histogram vs cumulative  

If any of the above are missing, the figure is an illustration—not evidence.

---

## 0.7 Controls, Null Models, and Stress Tests

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

---

## 0.8 The Claims Ledger Table
In each chapter, we will maintain a small ledger:
- Definition used (explicit formula)  
- What it predicts (structure type)  
- Which tests it passes (N1/N2/S1/S2/S3)  
- Status (A/B/C/D)

This turns the book into a machine: every chapter either upgrades claims or discards them.

---

## 0.9 Transition
Next we stop framing and start doing:
- We print the exact phase equations.  
- We validate them for unit/scale correctness.  
- We plot.  
- We test controls.  
- Only then do we interpret.

Now we show the work.
