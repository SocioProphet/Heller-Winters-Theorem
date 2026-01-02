Chapter 5

Dirichlet and the Symmetry of Residue Classes

Epigraph Triad

Hebrew (עברית)
לְךָ מִשְׁפָּט
“Judgment is Yours.” — (Psalm-language; we keep the full citation line for the final pass when we finalize the exact verse selection.)

Greek (Ελληνικά)
ἀριθμὸς ἄρχει
“Number rules.” — (Pythagorean/ancient attribution tradition; final citation locked in editing pass.)

English
“The law of small numbers.” — Richard K. Guy (attributed phrase; final edition will cite the exact source placement)

(Editorial note: we’ll tighten citations for epigraphs in the final proof stage; we are keeping forward momentum here.)

Introductory visualization (to render later)

Fig 5.A: A wheel diagram for modulus M=30: mark reduced residues {1,7,11,13,17,19,23,29}, show composites eliminated.
Fig 5.B: A “prime rays” plot: primes colored by residue mod 4 and mod 6 (showing primes live in 1 or 5 mod 6 beyond 3).

⸻

5.1 Why Dirichlet belongs in the operator stack

Once Gauss and Legendre teach us that primes have a mean-field climate, the next question is not “what is the next prime?” but “what symmetries constrain where primes are even allowed to appear?”

This is the start of policy enforcement in arithmetic form.

The integers are not a blank line. They are partitioned by congruence classes. And primes are not free to roam them arbitrarily.

Dirichlet is the first to prove, with full force, that residue-class structure is not an accident—it is a governing symmetry.

⸻

5.2 Residues: the simplest structural lens

Fix a modulus q≥2. Every integer n has a residue class

n ≡ a (mod q),    a∈{0,1,…,q−1}.

But primes (beyond the small exceptions that divide q) cannot lie in residue classes that share a nontrivial gcd with q. Formally, if p∤q and p is prime, then:

gcd(p,q)=1  ⇒  p ∈ (ℤ/qℤ)×.

So the “allowed” locations for primes mod q are the reduced residue classes a with gcd(a,q)=1. Their count is

φ(q),

Euler’s totient.

This is already our first structural sieve: if we know a number lies in a forbidden class, it is composite (or one of the primes dividing q). That’s policy enforcement as arithmetic necessity.

⸻

5.3 The theorem that turns symmetry into inevitability

Dirichlet’s theorem on arithmetic progressions says:

If gcd(a,q)=1, then there are infinitely many primes p such that
    p ≡ a (mod q).

This is not merely existence. It is symmetry-as-law:
    • primes do not just avoid forbidden classes;
    • they actively populate every admissible class without dying out.

This has two consequences we carry forward:
    1. Residues are not just filters; they are balanced channels.
    2. Any method for prime localization that contradicts this symmetry is automatically wrong.

So in our construction language: Dirichlet gives us a “policy operator” that must be respected by any downstream heuristic or scoring function.

⸻

5.4 Uniformity as a mean-field inside each class

If primes are infinite in every admissible class, we can ask whether they appear “equally often.” The precise asymptotic statement is:

π(x;q,a) ~ (1/φ(q))·(x/ln x),

where

π(x;q,a)=#{p≤x : p≡a (mod q)}.

This is the Gauss mean-field law, now refined: not only do primes thin like 1/ln x, they thin evenly across admissible residue channels, up to the symmetry factor 1/φ(q).

So Dirichlet installs “channel fairness” into the prime climate model.

⸻

5.5 The wheel as an instrument, not a trick

A “wheel sieve” is just the practical expression of reduced residues. Take q as a product of small primes:

M = ∏_{p≤P} p.

Then numbers coprime to M are the only survivors after sieving out multiples of primes ≤P. The survivor proportion is:

φ(M)/M = ∏_{p≤P}(1−1/p).

This is a compression instrument:
    • it does not prove primality;
    • it reduces the candidate space aggressively;
    • and it does so in a way that is transparent, deterministic, and audit-friendly.

In our stack, that means the wheel is not “heuristic spice.” It is a policy layer derived from residue symmetry.

⸻

5.6 The bridge to analytic structure: characters are the hidden basis

Dirichlet’s proof does something deeper than “primes in progressions.” It introduces the idea that congruence classes can be analyzed using harmonic-like basis functions over (ℤ/qℤ)×: Dirichlet characters.

A character χ is a multiplicative function mod q that behaves like a basis vector for residue structure. The distribution of primes in progressions can be studied through the associated Dirichlet L-functions:

L(s,χ)=∑_{n=1}^{∞} χ(n)/n^s
      = ∏_{p}(1−χ(p)/p^s)^{−1}.

We do not need the full proof here; what we need is the conceptual inheritance:
    • residues → characters (a basis)
    • characters → analytic functions (spectral objects)
    • spectral objects → oscillation control in log-scale

That line is exactly what later makes our “log-harmonic signature” language legitimate. The ancestry is real.

⸻

5.7 Core teaching points (what this chapter must drill into the reader)

    1. Residues are structure, not decoration.
    2. Forbidden classes are hard eliminations.
    3. Admissible classes must be populated infinitely often (Dirichlet).
    4. Mean-field splits across residue channels by 1/φ(q).
    5. The wheel is a deterministic compression layer derived from symmetry.
    6. Characters foreshadow spectral decomposition—the analytic doorway to oscillations.

This is the “symmetry chapter.” Without it, later claims about policy-enforced pruning have no classical spine.

⸻

Running list: figures to render later (updated)

Chapter 5 renders:
    1. Fig 5.A — Wheel M=30: reduced residues and eliminated spokes.
    2. Fig 5.B — Prime rays mod 6 / mod 30: primes marked by residue channel.
    3. Fig 5.C — Survivor density curve: plot φ(M)/M as P grows (visual compression).
    4. Fig 5.D — Character “basis” schematic: characters as orthogonal channels over residues (conceptual diagram).

⸻
