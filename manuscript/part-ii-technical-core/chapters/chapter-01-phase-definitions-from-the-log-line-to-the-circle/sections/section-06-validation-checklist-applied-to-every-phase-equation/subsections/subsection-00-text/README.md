# 1.6 Validation Checklist (applied to every phase equation)

For every \theta(p) we use, we validate:

1) Domain validity: is x(p) defined for all primes in range?  
2) Unit sanity: are we mixing degrees and radians?  
3) Growth sanity: does \theta(p) explode so fast that wrapping becomes effectively uniform?  
4) Edge cases: behavior for small primes p\in\{2,3,5,7,\dots\}  
5) Wrap behavior: confirm \bmod 2\pi is applied once and only once  
6) Determinism: no hidden knobs; if constants exist, they are fixed and declared  
7) Control comparators: run the same transform on (i) random angles and (ii) odd integers / wheel-filtered integers
