# HW-PRIME-WEIL-014 — Non-Cancelling Fraction Theorem

Status: finite arithmetic theorem surface.  
Claim class: theorem-grade finite character-count identity; diagnostic implications only.  
Lane: prime/operator lane, orbit-class / primorial packet surface.  
Depends on: `HW-PRIME-WEIL-007`, `HW-PRIME-WEIL-012`, `HW-PRIME-WEIL-013`.

## Purpose

This document records the exact finite theorem controlling how many local characters fail to cancel on the base-10 digit orbit, and how those local non-cancelling characters accumulate in the primorial tower.

It has two forms:

1. a local prime-modulus theorem;
2. a cumulative primorial tower theorem.

Both are unconditional finite character-count identities. Neither proves RH, GRH, Artin's conjecture, or any variance bound.

## Local theorem

Let `p` be a prime with `gcd(p,10)=1`. Let:

```text
G_p = (Z/pZ)^x,
H_p = <10> subset G_p,
d_p = ord_p(10).
```

Then:

```text
|G_p| = p-1,
|H_p| = d_p,
[G_p : H_p] = (p-1) / d_p.
```

A character `chi in hat(G_p)` cancels over the base-10 orbit iff its restriction to `H_p` is nontrivial:

```text
sum_{h in H_p} chi(h) = 0 iff chi|_{H_p} is nontrivial.
```

A character is non-cancelling iff it is trivial on `H_p`.

Therefore the number of nontrivial local non-cancelling characters is:

```text
n_nc(p) = (p-1) / ord_p(10) - 1.
```

## Proof

Characters of `G_p` that are trivial on `H_p` are exactly characters of the quotient group:

```text
G_p / H_p.
```

The quotient has size:

```text
|G_p/H_p| = (p-1) / ord_p(10).
```

The trivial character is one of these quotient characters. Removing it gives:

```text
n_nc(p) = |G_p/H_p| - 1 = (p-1)/ord_p(10) - 1.
```

This is finite character orthogonality.

## Artin-prime corollary

If `10` is a primitive root modulo `p`, then:

```text
ord_p(10) = p-1.
```

Therefore:

```text
n_nc(p) = (p-1)/(p-1) - 1 = 0.
```

Thus base-10 Artin primes have no local nontrivial non-cancelling characters.

This is an exact finite corollary. It does not prove Artin's conjecture or assert infinitely many such primes.

## Local table through p=37

| p | `ord_p(10)` | `n_nc(p)` | Orbit type |
|---:|---:|---:|---|
| 2 | — | 0 | terminating |
| 3 | 1 | 1 | degenerate |
| 5 | — | 0 | terminating |
| 7 | 6 | 0 | full orbit / Artin |
| 11 | 2 | 4 | partial |
| 13 | 6 | 1 | partial |
| 17 | 16 | 0 | full orbit / Artin |
| 19 | 18 | 0 | full orbit / Artin |
| 23 | 22 | 0 | full orbit / Artin |
| 29 | 28 | 0 | full orbit / Artin |
| 31 | 15 | 1 | partial |
| 37 | 3 | 11 | partial |

## Cumulative primorial tower theorem

Let:

```text
P_k = product_{j=1}^k p_j,
P_0 = 1.
```

When a new prime `p_j` is appended to the primorial tower, its local non-cancelling characters lift across all characters of the previous tower. The new contribution is:

```text
phi(P_{j-1}) * n_nc(p_j).
```

Therefore the cumulative number of locally non-cancelling tower characters through `P_k` is:

```text
N_nc(P_k) = sum_{j=1}^k phi(P_{j-1}) * n_nc(p_j).
```

This is the tower accumulation formula used in the packet diagnostics.

This is not the same as the diagonal inert count:

```text
phi(P_k) / lcm_j ord_{p_j}(10) - 1.
```

The diagonal/lcm expression counts characters trivial on the simultaneous diagonal orbit. That is a different finite object and must not be conflated with the cumulative local non-cancelling tower count.

## Cumulative table through p=37

| Through prime p | Local contribution | Cumulative `N_nc` |
|---:|---:|---:|
| 2 | 0 | 0 |
| 3 | 1 | 1 |
| 5 | 0 | 1 |
| 7 | 0 | 1 |
| 11 | 192 | 193 |
| 13 | 480 | 673 |
| 17 | 0 | 673 |
| 19 | 0 | 673 |
| 23 | 0 | 673 |
| 29 | 0 | 673 |
| 31 | 1021870080 | 1021870753 |
| 37 | 337217126400 | 338238997153 |

The value `673` is correct for the cumulative tower through `p=29`.

It is not correct through `p=37`. Adding `p=31` raises the cumulative count above one billion, and adding `p=37` raises it above three hundred billion.

## Interpretation

The local theorem says that orbit quality is exactly measured by the quotient size:

```text
|G_p/H_p| = (p-1)/ord_p(10).
```

Full-orbit primes have quotient size `1`, hence no local non-cancelling characters.

Partial-orbit primes have quotient size greater than `1`, hence some local non-cancelling characters.

The cumulative theorem says that a local non-cancelling contribution is amplified by the size of the preceding primorial character group.

## Boundary

This theorem counts characters. It does not bound their prime-window character sums.

A count of non-cancelling characters is not a variance estimate unless paired with analytic control of the corresponding `psi_{W_K}(chi)` values.

## Non-claims

This document does not prove RH.

This document does not prove GRH.

This document does not prove Artin's conjecture.

This document does not prove an unconditional variance bound.

This document does not prove the non-cancelling variance is small.

This document does not prove the non-cancelling fraction tends to zero in any tower unless the tower and limiting regime are separately specified.

This document does not close the square-root barrier.