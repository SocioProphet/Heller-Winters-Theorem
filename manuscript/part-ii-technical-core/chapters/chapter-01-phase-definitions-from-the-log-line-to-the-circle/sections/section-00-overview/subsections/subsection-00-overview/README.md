# CHAPTER 01 — Phase Definitions: From the Log Line to the Circle

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

**“The Log-Circle Map of Primes”**  
Plot each prime p as a point on the unit circle using  
\Phi_{\log}(p)=e^{i(\log p \bmod 2\pi)}.  
This is the base instrument: the simplest log-phase embedding. Everything else in the chapter is a refinement, control, or alternative phase choice.

*Caption:* The circle is not decoration—it is a phase instrument. The question is whether primes leave a fingerprint after wrapping.

---

## 1.1 The Phase Pipeline (canonical)

Every phase construction we use in this book follows the same pipeline:
1. Choose a scalar transform x(p)  
2. Convert to an angle \theta(p)  
3. Wrap \theta(p) to [0,2\pi)  
4. Embed on the circle via e^{i\theta(p)}

Formally:
- Scalar transform: x:\mathbb{P}\to\mathbb{R}  
- Angle map: \theta(p)=\alpha\,x(p)+\beta  
- Wrapped phase: r(p)=\theta(p)\bmod 2\pi  
- Circle embedding: \Phi(p)=e^{ir(p)}\in S^1  

Here \alpha,\beta are explicit constants, not tunable knobs, unless a chapter explicitly declares them as part of a tested parameter family.

---

## 1.2 Base Phase Families

### 1.2.1 The Log Phase (baseline)
x(p)=\log p,\qquad \theta_{\log}(p)=\log p  
\Phi_{\log}(p)=e^{i(\log p\bmod 2\pi)}

This baseline is intentionally “dumb.” It exists to define the visual vocabulary and to set the control reference.

### 1.2.2 The Double-Log Phase (slow phase)
x(p)=\log\log p,\qquad \theta_{\log\log}(p)=\log\log p  
\Phi_{\log\log}(p)=e^{i(\log\log p\bmod 2\pi)}

This embedding changes phase far more slowly and often reveals different stability properties across prime windows.

### 1.2.3 Index Phase (ordering control)
Let p_n be the n-th prime. Define:  
x(p_n)=n,\qquad \theta_{\mathrm{idx}}(p_n)=n  
\Phi_{\mathrm{idx}}(p_n)=e^{i(n\bmod 2\pi)}

This is a pure ordering control: if a claimed structure survives under \log p but not under n, the structure is more likely tied to magnitude rather than enumeration.

---

## 1.3 Hyperbolic Coupling Layer (bridge operator)

This layer formalizes the conceptual bridge we use throughout the work: a phase variable (circular, bounded) can be paired with an “amplitude-like” variable (unbounded), producing a controlled way to fuse circular and hyperbolic behavior.

Define a pair:
u(p)=\cos(r(p)),\qquad v(p)=\sin(r(p))
and a hyperbolic amplitude:
a(p)=\cosh(x(p)),\qquad b(p)=\sinh(x(p))

We then build coupled invariants such as:
I_1(p)=a(p)\,u(p)=\cosh(x(p))\cos(r(p))  
I_2(p)=b(p)\,v(p)=\sinh(x(p))\sin(r(p))

These are not “proof objects” by themselves. They are measuring tools: they let us test whether the same prime-derived transform x(p) carries coherent signal in both bounded and unbounded channels.

---

## 1.4 The Winters Log-Circle Instrument (credited visualization step)

We now state the instrument in its most minimal, reproducible form:

Given a prime p, define:
z(p)=\log p + i\,(\log p)
and project to the unit circle by argument:
\Phi_{\arg}(p)=e^{i\arg(z(p))}

Equivalent explicit form:
\arg(\log p + i\log p)=\arg(1+i)=\frac{\pi}{4}
so this particular construction collapses unless we separate the real and imaginary channels.

Therefore the usable log-circle instrument is:

\Phi_{\log}(p)=e^{i(\log p \bmod 2\pi)}
together with a second channel (radial or density) derived from x(p), for example:
- radial scaling: \rho(p)=\operatorname{frac}(\log p / 2\pi)
- density layering by prime index windows

This is the point of the instrument: the circle is the phase; the windowing and density are the signal probes.

---

## 1.5 Explicit Phase Equations (No Placeholders)

We define all phase equations in unit-clean form:

- Angle is always in **radians**.  
- Wrap is always \(\bmod 2\pi\).  
- Embed is always \(\Phi(p)=e^{i(\theta(p)\bmod 2\pi)}\).

Formally, for any phase map \(\theta:\mathbb{P}\to\mathbb{R}\),
\[
r(p)=\theta(p)\bmod 2\pi,\qquad \Phi(p)=e^{i r(p)}\in S^1.
\]

---

### 1.5.1 Baseline Phase Operators (exact)

**(E1) Log-phase (canonical base)**  
\[
\theta_{\log}(p)=\log p,\qquad
r_{\log}(p)=\theta_{\log}(p)\bmod 2\pi,\qquad
\Phi_{\log}(p)=e^{i r_{\log}(p)}.
\]

**(E2) Double-log phase (slow phase)**  
\[
\theta_{\log\log}(p)=\log\log p,\qquad
r_{\log\log}(p)=\theta_{\log\log}(p)\bmod 2\pi,\qquad
\Phi_{\log\log}(p)=e^{i r_{\log\log}(p)}.
\]

**(E3) Index-phase control (ordering-only)**  
Let \(p_n\) be the \(n\)-th prime.
\[
\theta_{\mathrm{idx}}(p_n)=n,\qquad
r_{\mathrm{idx}}(p_n)=n\bmod 2\pi,\qquad
\Phi_{\mathrm{idx}}(p_n)=e^{i r_{\mathrm{idx}}(p_n)}.
\]

These three operators are our **non-negotiable baselines**: every later “structure” claim must be compared against them and against the null/stress tests in Chapter 0.

---

### 1.5.2 Degree-constants normalization (exact, non-guessing)

If your handwritten equation contains degree measures (e.g. \(90^\circ\), \(60^\circ\)), we normalize them **exactly**:

\[
90^\circ = \frac{\pi}{2},\qquad
60^\circ = \frac{\pi}{3},\qquad
1^\circ=\frac{\pi}{180}.
\]

So any term intended as “\(\pi\) plus one degree” must be written unambiguously as:
\[
\pi + 1^\circ \;=\; \pi + \frac{\pi}{180} \;=\; \pi\left(1+\frac{1}{180}\right).
\]

Any term intended as “\(\pi\) plus one arcminute” is:
\[
\pi + 1' \;=\; \pi + \frac{\pi}{10800}.
\]

We do **not** infer intent from ambiguous forms like \(\pi + \tfrac{1}{60}\). The text you paste decides whether \(\tfrac{1}{60}\) means degrees, arcminutes, radians, or an ad hoc constant.

---

### 1.5.3 The explicit equation insertion protocol (one-line, verbatim)

We reserve **exactly one line** for your handwritten equation, inserted **verbatim** as text. The manuscript uses anchors so the slot is mechanically findable and scriptable.

**Raw equation slot (verbatim, one line):**

<!-- BEGIN THETA_STAR_RAW (verbatim one-line equation; no edits) -->

<!-- END THETA_STAR_RAW -->

Rules:

1. The line between anchors must be **one line** containing your exact \(\theta_\star(p)=\cdots\) as you wrote it (including any \(^\circ\), primes \( '\), constants, indices, etc.).  
2. We do not “clean it up” first. We preserve the raw artifact, then normalize it deterministically.  
3. After insertion, we immediately derive the unit-clean operator:

\[
r_{\star}(p)=\theta_{\star}(p)\bmod 2\pi,\qquad
\Phi_{\star}(p)=e^{i r_{\star}(p)}.
\]

This guarantees the object becomes **testable** the moment the line exists: it can be plotted, null-tested, stress-tested, and compared against baselines.

---

### 1.5.4 Canonical publication form (what we report after normalization)

Every explicit phase gate we publish is reported in this canonical form:

\[
\theta_{\star}(p)=A\cdot f(p)+B,
\qquad
r_{\star}(p)=\theta_{\star}(p)\bmod 2\pi,
\qquad
\Phi_{\star}(p)=e^{i r_{\star}(p)}.
\]

Where:

- \(f(p)\) is the prime-derived scalar (commonly \(\log p\), \(\log\log p\), the index \(n\), or a deterministic traversal index defined elsewhere).  
- \(A,B\) are **fixed constants** (declared; not tuned post hoc).  
- If your pasted \(\theta_\star\) is not affine in a single scalar \(f(p)\), we report the exact functional form as-is and then explicitly state which parts are constants, which are indices, and which are transforms—no compression that hides degrees/radians, and no “it’s basically…” handwaving.

This is the reproducibility boundary: once we can’t express the operator clearly and deterministically, we stop pretending it’s an instrument.


## 1.6 Validation Checklist (applied to every phase equation)

For every \theta(p) we use, we validate:
1. Domain validity: is x(p) defined for all primes in range?
2. Unit sanity: are we mixing degrees and radians?
3. Growth sanity: does \theta(p) explode so fast that wrapping becomes effectively uniform?
4. Edge cases: behavior for small primes p\in\{2,3,5,7,\dots\}
5. Wrap behavior: confirm \bmod 2\pi is applied once and only once
6. Determinism: no hidden knobs; if constants exist, they are fixed and declared
7. Control comparators: run the same transform on (i) random angles and (ii) odd integers / wheel-filtered integers

---

## 1.7 Immediate Experiments (what we run first)

Using the three baseline embeddings \Phi_{\log},\Phi_{\log\log},\Phi_{\mathrm{idx}}, we produce:
1. Circle scatter of \Phi(p) for a fixed prime window
2. Angle histogram of r(p) on [0,2\pi)
3. Window comparison: same plots over increasing ranges [n_a,n_b]\to[n_a,10n_b]
4. Nulls: repeat with random odd integers and random phases

The goal is not to “win” in Chapter 1. The goal is to establish what a real signal must survive.

---

## 1.8 Transition
Next chapter we stop being generic. We insert the exact explicit phase equation, normalize it, and run it through the full reproducibility contract: plots, nulls, stress tests, and stability checks.

Now we show the work.
