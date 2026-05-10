# Phase Wγ Fixture Specification

Status: executed for registry v0.1.

## Purpose

The fixture proves deterministic replay at small scale before scaling to `X = 1e6`.

## Fixture scale

```text
X_fixture = 10_000
```

## Replicates

```text
B = 16
```

## Base seed

```text
20260510
```

## Expected deterministic fixture values

The supplied fixture result has:

```text
|P(10_000)| = 1229
T(P(10_000)) = 18.00325097589416
rotation_invariance.max_abs_delta = 4.718447854656915e-16
deterministic_result_sha256 = ab70a276f21fae3e6d3b5e16ba08378c23d0d6a08574784b6e798ae51c3f7c2b
```

The fixture receipt is stored at:

```text
empirical-claims/phase-gate-null-X1e6/results/fixture/pfk_receipt.json
```

## Required outputs

The fixture run must emit:

- locked statistic value,
- normalization constants,
- basis declaration,
- window declaration,
- runtime metadata,
- deterministic result hash,
- provenance receipt.

## Replay requirement

The fixture must replay under:

- identical registry version,
- identical operator definitions,
- identical normalization,
- identical seed policy.

## Promotion rule

Scaling to larger `X` is blocked until fixture replay succeeds independently.
