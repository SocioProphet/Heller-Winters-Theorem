# CHAPTER 1 — Phase Definitions: From the Log Line to the Circle

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
Plot each prime \(p\) on the unit circle using
\[
\Phi_{\log}(p)=e^{i(\log p \bmod 2\pi)}.
\]
This is the base instrument: the simplest log-phase embedding. Everything else is refinement, control, or alternative phase choice.

*Caption:* The circle is not decoration—it is a phase instrument. The question is whether primes leave a fingerprint after wrapping.

---

## 1.1 The Phase Pipeline (canonical)
1) choose a scalar transform \(x(p)\)  
2) convert to an angle \(\theta(p)\)  
3) wrap to \([0,2\pi)\)  
4) embed on the circle \(e^{i\theta}\)

Formally:
- scalar: \(x:\mathbb{P}\to\mathbb{R}\)
- angle: \(\theta(p)=\alpha x(p)+\beta\)
- wrapped: \(r(p)=\theta(p)\bmod 2\pi\)
- embedding: \(\Phi(p)=e^{ir(p)}\in S^1\)

\(\alpha,\beta\) are explicit constants—not tunable knobs—unless declared as a tested parameter family.

---

## 1.2 Base Phase Families

### 1.2.1 Log phase (baseline)
\(x(p)=\log p\), \(\Phi_{\log}(p)=e^{i(\log p\bmod 2\pi)}\)

### 1.2.2 Double-log phase (slow phase)
\(x(p)=\log\log p\), \(\Phi_{\log\log}(p)=e^{i(\log\log p\bmod 2\pi)}\)

### 1.2.3 Index phase (ordering control)
For \(p_n\) the n-th prime:
\(\Phi_{\mathrm{idx}}(p_n)=e^{i(n\bmod 2\pi)}\)

This is deliberately blunt: if “structure” survives under \(\log p\) but not under \(n\), it is likelier tied to magnitude than enumeration.

---

## 1.3 Hyperbolic Coupling Layer (bridge operator) — **scaled to avoid blowup**
We sometimes pair a bounded phase channel with an unbounded amplitude channel. To keep this numerically meaningful, we **center in a window**.

Let \(u(p)=\log p\). On a window \(W=[n_a,n_b]\), define
\[
\tilde u(p)=u(p)-\mathrm{median}_W(u).
\]
Then:
\[
a(p)=\cosh(\tilde u(p)),\quad b(p)=\sinh(\tilde u(p)),
\quad
u_\circ(p)=\cos(r(p)),\quad v_\circ(p)=\sin(r(p)).
\]
Coupled probes:
\[
I_1(p)=a(p)u_\circ(p),\qquad I_2(p)=b(p)v_\circ(p).
\]
These are **measuring tools**, not proof objects: they test whether the same transform carries coherent signal in bounded and envelope-like channels.

---

## 1.4 The Winters Log-Circle Instrument (credited visualization step) — **non-degenerate form**
The core log-circle instrument is:
\[
r(p)=\log p\bmod 2\pi,\qquad \Phi_{\log}(p)=e^{ir(p)}.
\]
A circle wrap discards scale information, so every serious use is **two-channel**: phase + a second scalar channel \(s(p)\) (window index, density bin, \(\log\log p\), or radial fraction).

Example (phase + radial fraction):
\[
s(p)=\operatorname{frac}\Big(\frac{\log p}{2\pi}\Big),
\]
and we render \(\Phi_{\log}(p)\) with density stratified by \(s(p)\) or by prime-index windows.

This is the point of the instrument: phase is the circle; windowing/density is where signal must survive controls.

---

## 1.5 The Explicit Phase Equation Slot (verbatim insertion point)
Reserved for the explicit phase equation as it appears in the original notes. Insert verbatim, then normalize into unit-clean form (radians, consistent wrapping, defined domain).

---

## 1.6 Validation Checklist (for every phase equation)
Domain validity; unit sanity; growth sanity; small-prime edge cases; wrap applied once; determinism (no hidden knobs); controls (random-phase + odd-integer/wheel baselines).

---

## 1.7 Immediate Experiments
For \(\Phi_{\log},\Phi_{\log\log},\Phi_{\mathrm{idx}}\):
- circle scatter for a fixed window  
- angle histogram on \([0,2\pi)\)  
- window expansion \([n_a,n_b]\to[n_a,10n_b]\)  
- nulls: random phases + odd integers / wheel-filtered integers

Goal: establish what a real signal must survive.

---

## 1.8 Transition
Next chapter: insert the explicit phase equation, normalize it, and run it through the full contract: plots, nulls, stress tests, stability checks.

Now we show the work.
