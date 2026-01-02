Chapter 4 — Gauss, Legendre, Density, and the Mean-Field Law

Hebrew (עברית)
לִמְנוֹת יָמֵינוּ כֵּן הוֹדַע
Limnōt yāmēnū kēn hōdaʿ
“Teach us to number our days.” — Psalm 90:12

Greek (Ελληνικά)
Μέτρον ἄριστον.
“Measure is best.” — Cleobulus (attributed)

English
“Mathematics is the queen of the sciences, and arithmetic the queen of mathematics.” — Carl Friedrich Gauss (attributed)

⸻

4.1 The problem changes shape: from where to how often

By the time Euclid has shown primes never end, the natural next question is not “what is the next prime?” but “how do primes behave as the numbers grow?”

If we write

\pi(x)=\#\{p \text{ prime}: p\le x\},

then primes become a counting function, a measurable phenomenon. The jaggedness remains—\pi(x) climbs in steps—but it becomes possible to ask a statistical question with teeth:
    •    What is the average density of primes near x?
    •    How many primes do we expect in a large interval?
    •    What is the typical gap between consecutive primes around size x?

This is the beginning of the “mean-field” mindset: we stop trying to see the exact future and instead learn the law of the weather.

⸻

4.2 Gauss and Legendre: the first density laws

Gauss (as a teenager, by his own later account) and Legendre independently converged on a striking empirical regularity:
    •    Primes thin out.
    •    The thinning looks like a logarithm.

A crude density statement is:

\text{prime density near }x \approx \frac{1}{\ln x}.

If density near x is about 1/\ln x, then the expected number of primes up to x should be approximately the integral of this density:

\operatorname{Li}(x) \;=\; \int_{2}^{x}\frac{dt}{\ln t},

(the logarithmic integral), and one expects

\pi(x)\approx \operatorname{Li}(x).

Legendre also proposed a closely related approximation of the simpler form

\pi(x)\approx \frac{x}{\ln x - B},

for a fitted constant B (an empirical calibration). The philosophical point is not the constant; it’s the shape: logarithm governs thinning.

This is the first moment where primes stop being only a sequence and start behaving like a field: irregular locally, but law-governed in aggregate.

⸻

4.3 The mean-field operator: intensity, expectation, and the “log volume” lens

Once we accept the density heuristic 1/\ln x, we get a clean, portable operator for any window [a,b]:

\mathbb{E}\big[\#\{\text{primes in }[a,b]\}\big]
\;\approx\;
\int_{a}^{b}\frac{dt}{\ln t}.

That integral is the mean-field “coverage” prediction. It is the baseline we must beat or refine.

This also forces a crucial shift in how we measure size.
    •    Linear distance: b-a
    •    Log volume: \ln b-\ln a = \ln(b/a)

Primes live more naturally in multiplicative space than additive space, because \ln x is the coordinate where “relative scale” becomes linear. This is why later chapters treat

u = \ln x

as a primary coordinate. In that coordinate, oscillations (when they appear) become periodic in the right sense.

⸻

4.4 A worked micro-example: a window you can verify by hand

Take the window [100,200].

Actual prime count.
The primes between 100 and 200 are:

101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199

That is 21 primes, so:

\pi(200)-\pi(100)=21.

Mean-field prediction.
The mean-field expectation is:

\int_{100}^{200}\frac{dt}{\ln t}.

We can estimate without machinery using a midpoint approximation. Around t\approx150,

\ln(150)\approx 5.01,
\qquad
\frac{1}{\ln(150)}\approx 0.1996.

So

\int_{100}^{200}\frac{dt}{\ln t}
\approx
\frac{200-100}{\ln(150)}
\approx
\frac{100}{5.01}
\approx
19.96.

Mean-field predicts about 20 primes; reality gives 21. That’s the point: the mean-field model is not magic, but it’s anchoring. It tells us what “normal” looks like before we hunt structure in the residual.

⸻

4.5 Gap scale falls out immediately

If the local density near x is about 1/\ln x, then the typical spacing between primes near x should be about the reciprocal:

\text{typical gap near }x \;\sim\; \ln x.

This is the first appearance of the “gap scale.” It is not a proof of any specific gap bound; it is a baseline. But it is already enough to justify why later “boundedness layers” and “policy layers” work in log-scaled windows: the natural unit of spacing grows like \ln x.

⸻

4.6 What mean-field cannot do (and why we need residuals)

Mean-field explains density, not fine structure.

Even if \pi(x)\approx \operatorname{Li}(x) globally, the deviation

R(x) = \pi(x) - \operatorname{Li}(x)

is where the real fight lives. This residual is not a rounding error; it carries oscillation, correlation, and the fingerprints of deeper mechanisms.

So we treat this chapter as the baseline operator in our stack:
    •    Mean-field gives the expected coverage.
    •    Everything else we build is a policy-enforced refinement that tries to compress the search space beyond what mean-field can justify alone.

We do not pretend mean-field predicts the next prime. We insist it defines what “unstructured randomness” would look like. That matters because it gives us a falsifiable target: any claimed structure must show stable advantage over this baseline across windows, bases, and schedules.

⸻

4.7 Where this lands in our construction

From this chapter forward, we carry four commitments:
    1.    Density lives in \ln-space.
We treat u=\ln x as the honest coordinate for large-scale behavior.
    2.    A window has an expected prime count.
The operator \int_a^b dt/\ln t is our baseline “coverage” predictor.
    3.    Gaps have a natural scale.
The “typical” gap grows like \ln x, so policy layers should be log-aware.
    4.    Residual is the battleground.
If structure exists, it must express itself as stable, cross-validated improvement over mean-field—not as vibes.

This sets the table for the next chapters: Dirichlet’s residue symmetries, Chebyshev’s enclosures, and eventually the analytic machinery that explains why residual oscillation belongs to a spectral story.

⸻

Render Queue — Chapter 4 figures we must generate later (inline PNGs)
    1.    Fig 4.1: Step plot of \pi(x) vs smooth curves x/\ln x and \operatorname{Li}(x) on a moderate range (e.g. x\le 10^5).
    2.    Fig 4.2: Plot of the local intensity 1/\ln x across the same range (to visually show thinning).
    3.    Fig 4.3: A window illustration: [a,b] shaded under the curve 1/\ln t with the integral labeled as expected prime count.
    4.    Fig 4.4: Micro-example panel for [100,200]: “actual count = 21” vs “mean-field ≈ 20,” as a single annotated graphic.

⸻

Self-critique (so we keep tightening)
    •    Strong: This chapter now does what a math book chapter must do: it defines \pi(x), states the density heuristic, makes \operatorname{Li}(x) unavoidable, and gives a checkable micro-example that lands close to reality.
    •    Weak: The micro-example is intentionally small and “by hand.” That’s good for intuition, but we’ll need a later chapter figure that shows the same comparison at larger scales so nobody dismisses it as cherry-picked.
    •    Refinement we will apply when we render figures: Put \pi(x), x/\ln x, and \operatorname{Li}(x) on the same axes and explicitly label the residual R(x). That visually bridges this chapter to the Riemann chapter without hand-waving.
