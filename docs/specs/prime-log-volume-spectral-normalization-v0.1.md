# Prime Log-Volume Spectral Normalization v0.1

Status: definitional / empirical-harness normalization. Claim class: definitional.

This specification locks the coordinate, window, mean-field, residual, and claim-boundary conventions for finite-window prime-distribution experiments in the Heller-Winters Programme.

## Coordinate and window

The canonical coordinate is `u = ln(x)`, so `x = exp(u)` and `dx = exp(u) du`. A fixed increment `L` in `u` is a multiplicative window in `x`:

```text
W(u,L) = [exp(u), exp(u+L)]
```

Other bases are display gauges only. If `log_b(x) = ln(x)/ln(b)`, then `gamma_b = gamma ln(b)` preserves `cos(gamma ln x)`.

## Mean field

For prime-count windows, use:

```text
MF_count(u,L) = Li(exp(u+L)) - Li(exp(u))
              = integral_u_to_u+L exp(v)/v dv
```

The leading approximation is `exp(u)/u * (exp(L)-1)`. Finite-window checks must preserve the first deterministic correction:

```text
-exp(u)/u^2 * ((L-1) exp(L) + 1)
```

## Residual channels

Prime-count residual:

```text
R_count(u,L) = pi(exp(u+L)) - pi(exp(u)) - MF_count(u,L)
```

Chebyshev residual:

```text
R_psi(u,L) = psi(exp(u+L)) - psi(exp(u)) - (exp(u+L)-exp(u))
```

The Chebyshev channel is the direct `exp(u/2)` envelope channel. Prime-count residuals require their own declared normalization because the explicit-formula terms pass through `Li(exp(rho u))`.

## Claim boundary

This is not a theorem-promotion artifact. It does not claim RH, GRH, deterministic primality, zero-location results, or asymptotic speedup. It only defines a replayable normalization contract.
