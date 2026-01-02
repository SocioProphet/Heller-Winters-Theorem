CHAPTER 2

The First Experiment: The Log-Phase Circle Instrument and Its Controls

Hebrew (Tanakh / Psalms)
‎לַיהוָה הָאָרֶץ וּמְלוֹאָהּ׃
“The earth is the LORD’s, and all its fullness.”
—Psalm 24:1 (Hebrew; cf. Ps 24:1)

Greek (New Testament)
πάντα δοκιμάζετε· τὸ καλὸν κατέχετε.
“Test all things; hold fast what is good.”
—1 Thessalonians 5:21 (Greek; cf. 1 Thess 5:21)

English (scientific discipline)
“The first principle is that you must not fool yourself—and you are the easiest person to fool.”
—Richard P. Feynman, “Cargo Cult Science” (1974)

⸻

Introductory Visualization for Chapter 2

Log-phase points on the unit circle, with null comparators.
For each prime p in a fixed window we plot
z(p)=e^{i(\log p \bmod 2\pi)}.
On the same axes we plot the identical construction applied to (i) wheel-admissible integers in the same magnitude range and (ii) i.i.d. uniform random angles. The plot is not the argument; the comparison is.

Caption: A circle embedding is an instrument only if it distinguishes primes from controlled non-primes.

⸻

1. What is being tested

A frequent failure mode in exploratory number theory is to mistake a compression artifact for a law. The map \mathbb{R}\to\mathbb{R}/2\pi\mathbb{Z} is a powerful compression, and it can make many monotone sequences appear patterned. For that reason, before we introduce any additional arithmetic coupling, we first test the simplest possible instrument and ask whether it is discriminative.

Let p be prime and let \log denote the natural logarithm. Define
\theta(p)=\log p,\qquad
\phi(p)=\theta(p)\bmod 2\pi\in[0,2\pi),
\qquad
z(p)=e^{i\phi(p)}\in S^1.
This log-phase circle embedding is the baseline object of study. The chapter’s question is precise:

Does the empirical behavior of \phi(p) (equivalently, of z(p)) differ from reasonable null models in a stable way across windows?

If the answer is no, we treat the log-circle plot as a visualization tool but not as evidence of a prime-specific signal.

⸻

2. Windowing is part of the experiment, not an afterthought

Every empirical claim is a finite claim, and every finite claim is vulnerable to selective attention. We therefore fix a windowing protocol in advance.

We use two window types, but standardize to index windows for repeatability:
    •    Index windows: \{p_{n_a},p_{n_a+1},\dots,p_{n_b}\}.
    •    Magnitude windows: \{p\in\mathbb{P}: x\le p\le y\}.

The canonical schedule for index windows is geometric:
[n_a,n_b]\in\{[10^3,2\cdot10^3],\ [10^4,2\cdot10^4],\ [10^5,2\cdot10^5],\dots\}.
The point is to force scale testing: if a deviation is real, it should persist under expansion rather than disappearing when the sample grows.

⸻

3. The controls (null models) are part of the definition

A circle map can generate apparent clustering even when no arithmetic structure is present. For that reason we impose two nulls and refuse to interpret the prime plot without them.

3.1 Random-phase null (geometric baseline)
Let \phi_1,\dots,\phi_N be i.i.d. uniform on [0,2\pi) and define z_j=e^{i\phi_j}. This is the “pure uniform circle cloud.” It calibrates what randomness looks like under our plotting pipeline and sample sizes.

3.2 Arithmetic null (wheel-admissible integers)
To control for the obvious fact that “most integers are composite,” we also use a stronger null than “all odd numbers.”

Fix a wheel modulus
M=\prod_{q\le Q} q
for some small Q (e.g. Q=5 gives M=30, Q=7 gives M=210, etc.). In the same magnitude range [x,y] as the prime window, define the wheel-admissible integers
\mathcal{A}_{[x,y]}=\{m\in[x,y]\cap\mathbb{Z}:\gcd(m,M)=1\}.
For each m\in\mathcal{A}_{[x,y]}, compute
\phi(m)=\log m \bmod 2\pi,\qquad z(m)=e^{i\phi(m)}.
This null answers the only question that matters here: if we remove the easiest compositeness structure (divisibility by small primes), does the “prime signal” remain, or does it dissolve into the same behavior as general admissible integers?

⸻

4. What we measure (statistics that match the claim)

A scatter plot is not a theorem. If we claim a deviation, we must quantify it. We therefore attach to each window a small set of circular measurements that (i) detect concentration, (ii) detect distributional shape differences, and (iii) allow stability checking across windows.

4.1 Mean resultant length (first-order concentration)
Given angles \phi_1,\dots,\phi_N, define
R=\left|\frac{1}{N}\sum_{j=1}^N e^{i\phi_j}\right|.
If angles are uniform, R is small on average and decreases with sample size. If the points concentrate around a direction, R increases. This statistic is blunt but honest: it directly measures whether the cloud has a preferred direction.

4.2 Distributional comparison on [0,2\pi)
Define the empirical distribution function
F(\theta)=\frac{1}{N}\#\{\phi_j\le\theta\},\qquad \theta\in[0,2\pi).
We compare F for primes to F for each null. This catches deviations that are not well summarized by a single mean direction (for example, multimodal structure).

4.3 Stability across windows
For each window in the fixed schedule, we compute the same statistics. A deviation that appears only in a single window is not evidence; it is a finite-range accident. The stability plot is therefore part of the experiment’s definition.

⸻

5. The experiment protocol (what is actually done)

For each index window [n_a,n_b] in the schedule:
    1.    Compute primes p_{n_a},\dots,p_{n_b}.
    2.    Compute \phi(p)=\log p\bmod 2\pi and z(p)=e^{i\phi(p)}.
    3.    Generate a random-phase sample of size N=n_b-n_a+1.
    4.    Choose a magnitude range [x,y] matching the primes’ range in that window and compute wheel-admissible integers \mathcal{A}_{[x,y]}. If |\mathcal{A}_{[x,y]}|\neq N, subsample to size N without replacement to keep sample sizes comparable.
    5.    Produce three figures for primes and each null:
    •    the circle scatter z(\cdot),
    •    a histogram of \phi(\cdot) on [0,2\pi),
    •    an empirical CDF overlay F(\cdot).
    6.    Record R for each sequence and plot R across windows.

No constants are tuned during this process. No windows are added after the fact to “make it look good.” The protocol is fixed once and then repeated mechanically.

⸻

6. Interpretation rules (what we allow ourselves to claim)

We adopt rules that keep us honest:
    •    If primes and wheel-admissible integers are statistically indistinguishable under these measurements across windows, then the log-phase circle embedding is a baseline visualization, not a prime discriminator.
    •    If primes differ from both nulls in a way that persists across expanding windows, we treat that as evidence that a prime-linked residue survives the log-wrap.
    •    If the deviation collapses under scale, subsampling, or mild perturbations, we treat it as an artifact.

This chapter therefore does not promise a “prime predictor.” It establishes whether the simplest instrument has any discriminative content worth building on.

⸻

7. Why we move next to arithmetic coupling

If the baseline fails, the correct response is not to defend it but to refine the instrument. The refinement must not be cosmetic. It must inject additional arithmetic information that primes carry and non-primes do not carry in the same way.

Two classical, deterministic sources are available immediately:
    1.    residue-class structure modulo a fixed wheel base;
    2.    multiplicative order \operatorname{ord}_p(b), i.e., the base-b repetend period of 1/p.

The next chapter introduces such a coupling by modifying the phase map using one of these arithmetic invariants, while keeping the same window schedule, the same nulls, and the same stability tests. Only then can any observed sharpening be attributed to arithmetic structure rather than to presentation.
