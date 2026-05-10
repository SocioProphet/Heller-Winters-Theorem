# Phase Wγ Fixture Specification

Status: scaffold.

## Purpose

The fixture exists to prove deterministic replay at small scale before scaling to `X = 1e6`.

## Fixture scale

Initial fixture:

```text
X_fixture = 1e4.
```

## Required outputs

The fixture run must emit:

- the locked statistic value,
- normalization constants,
- basis declaration,
- window declaration,
- runtime metadata,
- provenance receipt.

## Replay requirement

The fixture must replay exactly under:

- identical registry version,
- identical operator definitions,
- identical normalization.

## Promotion rule

Scaling to larger `X` is blocked until fixture replay succeeds.
