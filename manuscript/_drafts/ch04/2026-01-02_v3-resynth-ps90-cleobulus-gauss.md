# Chapter 4 — Gauss, Legendre, Density, and the Mean-Field Law (Resynthesized)

## Trifold Epigraph

**Hebrew (עברית)**  
לִמְנוֹת יָמֵינוּ כֵּן הוֹדַע  
Limnōt yāmēnū kēn hōdaʿ  
“Teach us to number our days.” — Psalm 90:12

**Greek (Ελληνικά)**  
Μέτρον ἄριστον.  
“Measure is best.” — Cleobulus (attributed)

**English**  
“Mathematics is the queen of the sciences, and arithmetic the queen of mathematics.” — Carl Friedrich Gauss (attributed)

---

## 4.1 From enumeration to law

Euclid establishes infinity. That settles existence. It does not settle behavior.

The next step is not to stare at the next prime as though it were an oracle, but to ask a higher‑grade question: **how does the set of primes distribute through the integers?** Once we accept that question, we replace the “sequence” viewpoint with a “counting” viewpoint:

\[
\pi(x)=\#\{p\le x : p\ \text{prime}\}.
\]

This function is jagged by nature—stepwise, discrete, locally irregular. Yet the entire modern theory begins with the recognition that jaggedness does not forbid law. It only demands the right scale and the right baseline.

---

## 4.2 Gauss and Legendre: density as a logarithmic thinning

Empirically, primes thin out. Gauss and Legendre’s decisive insight was that this thinning is controlled—very closely—by the logarithm. The guiding heuristic becomes:

\[
\text{density of primes near }x \approx \frac{1}{\ln x}.
\]

Gauss’s entry into this is not folklore; it has a clean epistemic posture: **Gauss later wrote (in an 1849 letter to Encke) that he had already been studying the frequency of primes “as early as 1792 or 1793,”** i.e. mid‑teens, and that this led him toward the logarithmic‑integral approximation.

Once we accept intensity, we inherit a mean‑field prediction for prime counts in any interval \([a,b]\):

\[
\mathbb{E}[\#\text{primes in }[a,b]] \approx \int_{a}^{b}\frac{dt}{\ln t}.
\]

The integral that appears here becomes so central it gets its own name:

\[
\operatorname{Li}(x)=\int_{2}^{x}\frac{dt}{\ln t}.
\]

In the same spirit, Legendre proposed a more elementary closed‑form approximation

\[
\pi(x)\approx \frac{x}{\ln x - B}
\]

with a fitted constant \(B\). The constant is not the point. The point is that both Gauss and Legendre converge on the same governing shape: \(\ln x\) is the right slow variable for prime density.

---

## 4.3 Log‑volume is the honest geometry

The moment \(\ln x\) becomes the thinning law, “distance” in the number line stops being the only meaningful size. In large‑scale prime behavior, what matters is not merely \(b-a\), but the multiplicative span encoded by

\[
\ln b-\ln a = \ln\!\left(\frac{b}{a}\right).
\]

This is the first appearance of what our later construction formalizes: **volume in log‑space**. The coordinate

\[
u=\ln x
\]

is not a stylistic choice; it is the coordinate in which multiplicative scaling becomes linear, and in which later oscillatory phenomena become geometrically readable.

So we mark it plainly: **mean‑field is a law of the log‑coordinate.**

---

## 4.4 The baseline and the object we will study: the residual

A baseline matters only if we commit to measuring departures from it. So we define the residual:

\[
R(x)=\pi(x)-\operatorname{Li}(x).
\]

This residual is not “error” in the casual sense. It is the carrier of structure. If primes have deeper order beyond mean‑field density, it must appear in the behavior of \(R(x)\)—as oscillation, correlation, bias, or spectral signature.

This is the hinge of the chapter:

- \(\operatorname{Li}(x)\) is the mean‑field law (the weather model).
- \(R(x)\) is the signal‑bearing deviation (the storm track).

We do not promise that \(R(x)\) is simple; we promise that it is the right object.

---

## 4.5 Calibration example: small enough to see, not small enough to prove

We include one hand‑checkable calibration window to show what the mean‑field claim means in practice.

In \([100,200]\), the primes are:

101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199.

That is 21 primes, so:

\[
\pi(200)-\pi(100)=21.
\]

A midpoint estimate for the mean‑field expectation gives approximately

\[
\int_{100}^{200}\frac{dt}{\ln t}\approx \frac{100}{\ln(150)}\approx 20.
\]

This example is not evidence of deep structure. It is a sanity check: mean‑field predicts the right scale without tuning, and therefore defines the correct “null” behavior we must beat.

We make the boundary explicit: **calibration is not proof; it is a baseline that prevents self‑deception.**

---

## 4.6 Gap scale drops out: the typical spacing is logarithmic

If the intensity near \(x\) is about \(1/\ln x\), the expected spacing between events is approximately the reciprocal:

\[
g(x)\sim \ln x.
\]

This is not a claim about maximal gaps or extremal behavior. It is the statement of the natural unit: around size \(x\), primes tend to be separated by about \(\ln x\).

That is precisely why, in our later construction, we treat “search,” “boundedness,” and “policy windows” as objects that must be stable under log scaling.

---

## 4.7 Why this chapter must immediately imply the next ones

This chapter is not “history padding.” It installs the first operator in the operator stack:

- **Mean‑field operator:** \(\operatorname{Li}(x)\) and \(\int_a^b dt/\ln t\)

Everything that follows can now be stated as refinement:

- Dirichlet will add residue‑class symmetry (structure inside arithmetic progressions).
- Chebyshev will add enclosure (hard bounding).
- Riemann will reinterpret the residual \(R(x)\) as a spectral phenomenon in log‑space.

So we end where we must end: the mean‑field law gives us the baseline, the log‑coordinate gives us the geometry, and the residual gives us the object that later chapters will “listen to.”

---

## Inline diagram render queue (locked list for later)

To prevent the “toy example” weakness and make the bridge to Riemann visually unavoidable, we commit to these figures:

1. \(\pi(x)\) vs \(\operatorname{Li}(x)\) vs \(x/\ln x\) on a range large enough to see global agreement and local deviation (e.g. \(x\le 10^5\) or \(10^6\)).
2. Residual plot: \(R(x)=\pi(x)-\operatorname{Li}(x)\) on the same range (the bridge figure).
3. Intensity plot: \(1/\ln x\) showing thinning, with marked windows (additive vs multiplicative).
4. Window‑as‑area schematic: a shaded integral under \(1/\ln t\) from \(a\) to \(b\) labeled “expected prime count.”
5. Calibration panel: the \([100,200]\) example as a compact annotated graphic (explicitly labeled “calibration”).

These are not optional decorations. They are the instrument panel for the chapter.

---

## Self‑critique (tight, honest)

**Strong now:** we stopped pretending the hand example is evidence and made it explicitly a calibration; we elevated \(R(x)\) to the central hinge; and we explained why \(u=\ln x\) is geometry, not stylistic flourish.

**Still weak (until figures exist):** without the residual plot, readers can nod and still not feel why Riemann must enter. The figure is the proof‑of‑necessity.

**Refinement that makes the bridge bolt explicit:** we will treat \(R(x)\) as a superposition of log‑scale oscillatory contributions whose frequencies are measurable (and whose stability across windows/bases is testable).
