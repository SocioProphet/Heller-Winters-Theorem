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

Figure 2.1 — A 1–120 sieve grid with a 30-wheel overlay (elimination + compression).
We place the integers 1 through 120 in a 10×12 grid. On this single picture we show two mechanisms at once:
    1. Sieve marks (elimination): strike multiples of 2, 3, and 5 (and optionally 7 as a second pass).
    2. Wheel overlay (compression): highlight the residue classes mod 30 that are coprime to 30—these are the only positions that survive divisibility by 2,3,5.

This diagram is not “decoration”; it is the first instrument in the book. It lets the reader see that a prime machine is not prophecy. It is a policy: exclude what cannot be prime, and carry forward what remains with a certificate trail.

Layout specification (for typesetting):
    • Grid: numbers increasing left→right, top→bottom, 1 at top-left, 120 at bottom-right.
    • Strike style: a thin diagonal slash or light gray knockout for eliminated entries.
    • Wheel style: a box or halo around admissible residues mod 30.
    • Legend: “× = eliminated by {2,3,5}” and “□ = wheel-admissible (gcd(n,30)=1)”.

Caption: A sieve eliminates; a wheel eliminates whole congruence classes in advance. Together they form the first deterministic prime engine.

(Sealed Figure 2.1 render + Figure 2.2 gap-cycle are stored in manuscript/_drafts/ch02/FIGURES.md and should be included inline in the final layout.)

⸻

1. Euclid’s permanent strike: infinity by contradiction

The first prime machine is a proof posture. Euclid shows there cannot be a final prime. Given primes p_1,\dots,p_k, form
P=p_1p_2\cdots p_k+1.
No p_i divides P, because division by any p_i leaves remainder 1. Either P is prime, or it has a prime divisor outside the list. In both cases the list was incomplete.

We emphasize what this does and does not do. It does not tell us where the next prime sits. It tells us something stronger: any system that claims closure must fail, and we can force it to fail by a construction whose verification is mechanical. That posture—force the object, check the remainder—is the spine of every later policy operator we use.

⸻

2. Euclid’s algorithm: remainder as state, not debris

Euclid’s second gift is operational: reduction by remainder,
\gcd(a,b)=\gcd\!\bigl(b,\,a\bmod b\bigr),
repeated until the remainder vanishes.

Two properties make this more than a computational trick. First, it terminates: the remainders strictly decrease. Second, it compresses: the remainder is a smaller representative that preserves the invariant we care about (the gcd). This is the ancestor of residue-class reasoning: the remainder is the state variable of arithmetic.

When we later build wheels, CRT compartments, and residue state machines, we are doing Euclid at scale: “the state is the remainder; the policy is what we do with it.”

⸻

3. Eratosthenes: a certified engine, not a predictor

The sieve of Eratosthenes is the first prime engine in the clean sense: it outputs primes up to N together with a proof of why the non-primes were removed.

Start with candidates 2,3,\dots,N. Let p be the smallest surviving candidate. Eliminate all multiples 2p,3p,\dots \le N. Repeat with the next surviving candidate. The sieve stops once p^2>N, because every composite \le N has a prime factor \le\sqrt{N}. That stopping rule is an enclosure: it turns an open-ended question into a finite certified procedure.

This is the first time we see the machine principle that will persist: exclude by rule, stop by boundary, and keep the reasons. The sieve is not a vibe; it is a ledger.

⸻

4. The wheel: residue compression with a concrete micro-example

The sieve can be made more efficient without sacrificing correctness by compressing the candidate space before elimination. The simplest wheel takes the product of small primes as a modulus.

Let
M=2\cdot 3\cdot 5 = 30.
An integer n survives divisibility by 2,3,5 only if gcd(n,30)=1. The reduced residues modulo 30 are:
\mathcal{R}_{30}=\{1,7,11,13,17,19,23,29\}.
Everything outside these residues (mod 30) is eliminated immediately by a hard rule: divisible by 2, 3, or 5 (except the primes 2,3,5 themselves).

The compression is explicit. Since \varphi(30)=8,
\frac{\varphi(30)}{30}=\frac{8}{30}=\frac{4}{15}\approx 0.266\ldots
So before any deeper structure is consulted, about 73\% of integers are deterministically removed—no heuristics, no tuning.

The “wheel” name comes from periodicity. Writing the admissible residues in increasing order, the step pattern repeats every 30:
1\to7(+6)\to11(+4)\to13(+2)\to17(+4)\to19(+2)\to23(+4)\to29(+6)\to31(+2),
so the gap cycle is (6,4,2,4,2,4,6,2), repeating. Candidate generation becomes “walk the cycle” rather than “scan the line.”

This is the exact conceptual bridge to our later wheel-sieve layer: a wheel is a prime machine component that reduces the search domain while preserving correctness.

⸻

5. Why the grid figure matters (and why we insist on it)

This chapter is historical, but the diagram is methodological. A reader can understand the sieve in words; they believe they understand it. The grid forces understanding into the eye:
    • the sieve marks show eliminations as certificates (“killed by 2/3/5”);
    • the wheel boxes show admissibility as periodic structure (“survives 2/3/5 by residue”).

When the same number is both boxed and struck at different stages, the reader sees the difference between “admissible” and “prime.” Admissibility is survival under a policy layer, not a claim of primality. That single visual prevents a thousand category errors later when we introduce more sophisticated operators.

⸻

6. Transition: from elimination to spectrum

Euclid and Eratosthenes give the combinatorial foundation: contradiction, remainder, elimination, enclosure, and periodic compression. The next doorway, opened by Euler, is analytic: primes appear as the skeleton of products and functions, and prime distribution becomes measurable as a residual against mean-field drift. That doorway is where prime machines stop being only eliminators and begin to become instruments.

We move next to Euler’s product.
