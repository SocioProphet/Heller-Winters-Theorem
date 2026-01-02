Preface
A historical restatement of the study of primes (as the backbone of our paper)

Prime numbers enter mathematics first as irreducible multiplicative atoms: integers (>1) that admit no nontrivial factorization. The earliest “theory of primes” is therefore inseparable from the earliest theory of proof about divisibility, because primes are not an empirical category (like “large numbers”) but a logical category (defined by universal negation over divisors). From the beginning, the subject has been a tension between local discreteness (each prime is a stubborn individual) and global law (their distribution exhibits stable large-scale structure).

1) Antiquity: existence, infinitude, and the first algorithmic lens
The classical starting point is Euclid’s proof that there are infinitely many primes, which is the first decisive statement that primes are not a finite “resource” but an inexhaustible phenomenon of the integers. The proof is constructive in spirit: from any finite list of primes, we build a number that forces a new prime divisor, guaranteeing perpetual novelty. This is not only a theorem about primes; it is a theorem about the structure of arithmetic itself—an early instance of “no finite policy can close the world of integers.”

In the same era of thought, the sieve of Eratosthenes provides the first systematic computational view: rather than seeking primes directly, we iteratively eliminate composites. This “negative definition” viewpoint—prime as “not killed by any small divisor”—will eventually mature into modern sieve theory. The key historical motif already appears here: primes are understood by constraining the composite phase space.

2) Early modern arithmetic: congruence, identities, and tests
As number theory expands, primes become the organizing units of congruences and modular arithmetic. Fermat’s and Euler’s work (and the later refinement into group-theoretic language) treats primes as the moduli where multiplicative structure becomes clean. Along this line, Wilson’s theorem crystallizes a sharp equivalence:
p prime iff (p-1)! ≡ -1 (mod p),
a kind of “perfect but expensive” primality witness. Wilson’s theorem’s significance is conceptual: it sets a gold standard for what it means to characterize primes exactly, while simultaneously exposing the practical barrier (factorial growth) that forces other approaches.

This era also teaches a structural lesson we reuse in our work: identities can be logically complete but computationally intractable; the enduring strategy is therefore to develop policy layers (constraints) that eliminate impossibilities cheaply before any expensive certification.

3) The empirical-to-asymptotic transition: Gauss and Legendre’s prime-density conjectures
By the late 18th century, attention shifts from “what primes are” to “how many primes lie below x.” Gauss (as a teenager, by his later recollection) and Legendre converge on the idea that prime density is controlled by logarithms—an astonishing step because it replaces exact arithmetic with smooth approximation. The logarithmic integral Li(x) becomes a natural candidate for π(x), the prime-counting function, marking the birth of the modern “mean-field + fluctuation” mindset.

This phase matters for our paper because it introduces the essential coordinate change: primes are sparse in x-space but become more regular in logarithmic coordinates. That coordinate change is exactly the philosophical ancestor of our “log-harmonic signature” language: multiplicative phenomena often linearize in log x.

4) Analytic number theory begins: Dirichlet, Chebyshev, and the first distribution laws beyond “all primes”
Dirichlet’s theorem on primes in arithmetic progressions establishes that primes are not merely infinite as a set, but equidistributed across congruence classes that are not obstructed by a common factor. This is the first decisive theorem that primes obey a deep fairness principle modulo m, proven via what are now called Dirichlet L-functions—opening the analytic portal.

Chebyshev then builds strong partial progress toward the prime number theorem by proving that if π(x) behaves like x/log x, then the limiting constant must be 1, and by obtaining robust upper/lower bounds that establish the correct order of growth even without a full limit proof. This is a foundational precursor because it shows how far one can go using relatively elementary inequalities and careful bounding, a template that later reappears in sieve and elementary-proof traditions.

5) Riemann’s revolution: primes as a spectral phenomenon of zeros
Riemann links prime distribution to the complex-analytic behavior of ζ(s). Two ingredients dominate the modern worldview: (i) the Euler product (primes encoded multiplicatively), and (ii) the zeros of ζ(s) (fluctuations encoded spectrally). Riemann sketches an explicit-formula relationship between prime counting (in a smoothed sense) and sums over zeros, thereby turning “prime irregularity” into “spectral interference.”

This is where our paper’s architecture naturally lives: once primes are understood as “mean field + oscillatory residual,” it becomes mathematically meaningful to talk about channels: a logarithmic base coordinate for the mean field, and harmonic components in log x for fluctuations. The Riemann Hypothesis then reads as an envelope constraint on those oscillations (real part 1/2 for nontrivial zeros), rather than as a mystical statement about primes themselves.

6) 1896: the Prime Number Theorem is proved
The Prime Number Theorem formalizes Gauss/Legendre’s asymptotic insight: π(x) ~ x/log x. Hadamard and de la Vallée Poussin prove it using complex analysis and, critically, the non-vanishing of ζ(s) on the line Re(s)=1. For our purposes, PNT is the baseline: any refined prime-localization method is judged against the fact that density is 1/log x at leading order, and any proposed “policy enforcement layer” must respect that asymptotic geometry.

7) Early 20th century: sieve theory, conjectural constellations, and probabilistic structure
Hardy and Littlewood propose conjectures on prime constellations (including twin primes and general k-tuples), giving a quantitative heuristic superstructure for patterns beyond single primes.

Brun’s theorem—showing the sum of reciprocals of twin primes converges—introduces sieve methods as a mature technique with genuinely nontrivial outcomes. Even without proving twin primes are infinite, sieve methods can rigorously bound densities of structured prime subsets, and therefore act as “policy eliminators” of impossibility and overcounting.

Erdős helps open probabilistic number theory, reframing certain multiplicative statistics of integers as obeying universal distributions. That shift matters because it legitimizes the use of distributional diagnostics—exactly the kind of lens we invoke when we talk about compartmentalizing statistics by base, residue, or window schedule.

8) Mid-century structural expansion: zeta functions beyond ζ(s)
Zeta functions generalize to count solutions over finite fields. Weil’s conjectures (now theorems) show that zeta-like objects for varieties have rationality, functional equations, and RH-type zero constraints in that setting. The bridge “counting ↔ zeta ↔ zeros ↔ error terms” is not an accident of primes, but a recurring organizing principle across arithmetic geometry.

9) Late 20th to 21st century: computation, combinatorics, and major modern breakthroughs
Selberg (and Erdős) produce elementary proofs of PNT, demonstrating that deep asymptotics can emerge without complex analysis, provided one has sufficiently sharp combinatorial identities and inequalities. This strengthens the legitimacy of a heavily “policy + sieve + bounding” architecture.

Green and Tao prove that primes contain arbitrarily long arithmetic progressions, and modern bounded-gap work (Zhang; Maynard) refines sieve-weight technology into an optimized constraint engine.

On the algorithmic side, AKS shows primality can be decided deterministically in polynomial time—clarifying the goal boundary: faster-than-baseline search is meaningful, but must be judged against a moving benchmark landscape.
