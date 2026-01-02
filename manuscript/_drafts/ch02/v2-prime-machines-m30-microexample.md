CHAPTER 2

Euclid, Eratosthenes, and the First Prime Machines

Hebrew (Tanakh)
וּבִקַּשְׁתֶּם אֹתִי וּמְצָאתֶם׃
“You will seek Me and find Me.”
—Jeremiah 29:13 (Hebrew; Jer. 29:13)

Greek (New Testament)
ζητεῖτε καὶ εὑρήσετε.
“Seek, and you shall find.”
—Matthew 7:7 (Greek; Matt. 7:7)

English (method and unity)
“Mathematics is the art of giving the same name to different things.”
—Henri Poincaré, Science and Method (1908)

⸻

Introductory Visualization for Chapter 2

The Sieve Table and the Wheel: elimination and compression on the same page.
We imagine the integers 1 through N laid out in a grid. The sieve marks composites by rule: strike multiples of 2, then 3, then 5, and so on. The wheel compresses before we strike: it removes whole congruence classes in advance, so the sieve touches fewer candidates while preserving correctness.

Caption: A sieve is elimination; a wheel is elimination made periodic.

⸻

1. Euclid’s permanent strike: infinity by contradiction

The first “prime machine” is not an algorithm but a proof posture. Euclid shows that primes cannot be exhausted by any finite list. Given primes p_1,\dots,p_k, form
P=p_1p_2\cdots p_k+1.
No p_i divides P, since division leaves remainder 1. Therefore either P is prime, or it has a prime divisor not among the list. In both cases the list was incomplete.

This matters because it fixes the problem’s geometry: we are not hunting a final prime; we are designing procedures whose correctness survives arbitrary extension.

⸻

2. Euclid’s algorithm: reduction is the first state machine

Euclid’s algorithm converts divisibility into an iterative remainder state:
\gcd(a,b)=\gcd\!\bigl(b,\,a\bmod b\bigr),
repeated until the remainder is 0. Two properties make it a prototype for later policy operators:
    • Termination: the remainder strictly decreases, so the process cannot run forever.
    • State compression: the residue a\bmod b is a smaller representative that preserves the gcd.

The remainder is not computational debris. It is the primitive “state variable” that later reappears as residue classes, reduced systems, and CRT compartments.

⸻

3. Eratosthenes: the sieve as the first deterministic prime engine

The sieve of Eratosthenes is the earliest reliable prime engine because it does not attempt prophecy. It certifies by exclusion.

Given N, begin with candidates 2,3,\dots,N. Let p be the smallest remaining candidate. Eliminate all multiples 2p,3p,\dots\le N. Then advance to the next remaining candidate and repeat.

The decisive boundary is p^2\le N. Once we have sieved by every prime p\le \sqrt{N}, every composite \le N must already have been eliminated, because every composite has a prime factor at most its square root. This boundary is one of the earliest examples of a universal enclosure: an infinite-looking task collapses to a finite certified stopping rule.

⸻

4. From sieve to wheel: residue compression with a concrete micro-example

A raw sieve wastes effort touching numbers that are visibly composite—evens, multiples of 3, multiples of 5. The first refinement is to compress the number line by congruence classes so that we only generate candidates that could survive small-prime divisibility.

Fix the modulus
M=2\cdot 3\cdot 5=30.
An integer n can only avoid divisibility by 2, 3, and 5 if \gcd(n,30)=1. The admissible residue classes mod 30 are:
\mathcal{R}_{30}=\{1,7,11,13,17,19,23,29\}.
That list is not decoration. It is a mechanical compressor.

How it acts as a “machine.”
Every integer n\ge 2 lies in exactly one residue class modulo 30. If n\bmod 30\notin\mathcal{R}_{30}, then n is divisible by 2 or 3 or 5, hence composite (unless n\in\{2,3,5\}). If n\bmod 30\in\mathcal{R}_{30}, then n is merely admissible: it survives the first policy layer and is passed to deeper tests.

The density drop is explicit.
There are \varphi(30)=8 admissible residues out of 30, so the survivor density is
\frac{\varphi(30)}{30}=\frac{8}{30}=\frac{4}{15}\approx 0.266\ldots
So before we do any further work, we have eliminated about 73\% of integers deterministically, with a certificate (“divisible by 2, 3, or 5”).

The periodic pattern is the wheel.
If we write the admissible residues in increasing order, the gaps between them repeat with period 30:
1\to7(+6),\ 7\to11(+4),\ 11\to13(+2),\ 13\to17(+4),\ 17\to19(+2),\ 19\to23(+4),\ 23\to29(+6),\ 29\to31(+2),
so the gap cycle is
(6,4,2,4,2,4,6,2)
and then it repeats. This is why it is called a wheel: candidate generation becomes walking a repeating step pattern rather than scanning every integer.

The philosophical point is sharp: this is not a heuristic; it is a correctness-preserving compression. It does not claim primes live only here; it claims composites live almost everywhere else.

⸻

5. Why these “old tools” are operator ancestry, not museum pieces

Euclid gives necessity (primes do not end) and a construction posture (force contradiction). Euclid’s algorithm gives reduction-by-state (remainders as invariants). Eratosthenes gives certified elimination with a finite stopping boundary. The wheel gives periodic compression, turning elimination into a repeating state machine.

This is the inheritance that later becomes explicit in Part II:
    • enclosures become boundedness layers,
    • residues become wheel and CRT compartments,
    • elimination becomes policy operators with ledgers,
    • stopping rules become complexity budgets and audit boundaries.

⸻

6. Transition: the analytic doorway that turns lists into spectra

The sieve and wheel live entirely in divisibility. The next doorway, opened by Euler, is that primes can be encoded into analytic objects—products and functions—so that prime distribution becomes visible as a kind of spectrum. That is the bridge from “prime machines as eliminators” to “prime machines as instruments,” and it is where mean-field and residual begin to separate cleanly.

We move next to Euler’s product.

⸻

Self-critique and refinements

Strong: We plugged the major weakness: the wheel is now demonstrated concretely with M=30, the reduced residue set, the survivor density \varphi(M)/M, and the repeating gap cycle. The continuity from Eratosthenes to later wheel-sieve layers is no longer asserted—it’s shown.

Weak: We still haven’t drawn the actual grid figure in the manuscript. The text is now sufficient, but the final book should include a single small diagram: a 1–120 sieve grid with the 30-wheel overlay. That’s layout work, not theory, and it will make the “instrument” theme land immediately.
