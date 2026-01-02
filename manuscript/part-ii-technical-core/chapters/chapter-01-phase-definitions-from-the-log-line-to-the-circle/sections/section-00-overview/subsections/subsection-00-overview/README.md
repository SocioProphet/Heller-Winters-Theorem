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

## 1.5 The Explicit Phase Equation Slot (verbatim insertion point)

This section is reserved for the explicit phase equation as it appears in the original notes. In this manuscript it will be inserted verbatim, then immediately normalized into a unit-clean form (radians, consistent wrapping, defined domain).

**Equation 1.5.A (verbatim form).**  
\theta_{\star}(p)=\;\;\text{[INSERT EQUATION EXACTLY AS WRITTEN IN NOTES]}

**Normalization rule (applied once, immediately).**
- All angles expressed in degrees are converted to radians via \theta^\circ \mapsto \theta\cdot\pi/180.
- Any constant like 90^\circ is rewritten as \pi/2.
- Any wrapping is stated as \bmod 2\pi.
- Any indexing variable k is defined explicitly: whether it refers to prime index n, residue class index, or another deterministic traversal.

This guarantees the equation becomes a reproducible operator rather than a handwritten artifact.

---

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
