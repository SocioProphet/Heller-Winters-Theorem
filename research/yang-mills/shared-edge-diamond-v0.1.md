# Shared-Edge Diamond v0.1 — exact SU(2) Wilson contraction and finite gap proxy

## Result

The first non-product Wilson object is the two-plaquette shared-edge diamond:

```text
P1 = a u b
P2 = c u^(-1) d
K_diamond(a,b,c,d) = int_SU2 W_beta(a u b) W_beta(c u^(-1) d) du
```

With `W_beta(g)=exp(beta cos(theta))` and `chi_j(theta)=sin((2j+1)theta)/sin(theta)`, the character coefficient convention is:

```text
c_j(beta) = int_SU2 W_beta(g) chi_j(g) dg
          = I_(2j)(beta) - I_(2j+2)(beta)
          = 2(2j+1) I_(2j+1)(beta) / beta
```

The shared-link contraction gives:

```text
int du W_beta(a u b) W_beta(c u^(-1) d)
= sum_j c_j(beta)^2/(2j+1) chi_j(d c b a)
```

up to cyclic orientation convention for the boundary loop.

## beta = 1 coefficients

| j | d_j | c_j(1) | kappa_j=c_j^2/d_j | mu_j=kappa_j/kappa_0 | mass proxy |
|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 1.130318207984970 | 1.277619251302354 | 1.000000000000000 |  |
| 0.5 | 2 | 0.542990679068153 | 0.147419438777447 | 0.115386049973162 | 2.159471816329927 |
| 1 | 3 | 0.133010549545991 | 0.005897268763509 | 0.004615826473730 | 5.378264342829072 |

The Jmax=1/2 normalized diamond gap proxy is:

```text
mu_(1/2)^diamond = 0.115386049973162
m_diamond = -log(mu) = 2.159471816329927
```

## Direct Haar validation

| boundary angle phi | direct Haar quadrature | character sum | absolute error |
|---:|---:|---:|---:|
| 0.0 | 1.590636854637357 | 1.590636854637329 | 2.842e-14 |
| 0.7 | 1.511087927924335 | 1.511087927924308 | 2.642e-14 |
| 1.4 | 1.322440571320893 | 1.322440571320874 | 1.910e-14 |
| 2.4 | 1.067104104744874 | 1.067104104744858 | 1.621e-14 |

## Non-product witness

At Jmax=1 the shared-edge coefficient matrix across matched channels is diagonal with entries:

```text
1.277619251302354, 0.147419438777447, 0.005897268763509
```

Its rank across the face partition is 3. A product kernel over the same retained channels has rank 1. The connected defect for channels 0 and 1/2 is:

```text
Delta_(0,1/2) = 0.188345912998255
```

This is the first finite Wilson shared-link object that cannot be reduced to the closed S3 product-kernel branch.

## Non-claims

- No continuum Yang-Mills theorem.
- No infinite-volume mass gap theorem.
- No weak-coupling uniformity theorem.
- No cutoff-removal theorem.

## Next gate

Build the strip by composing diamond kernels and test fixed-cutoff N-uniformity.
