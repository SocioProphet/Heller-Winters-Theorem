# Theorem Statement Identifier Reservations

Status: theorem-statement registry for Heller-Winters theorem targets and theorem-target anti-seed.

## HW-THM-* — Theorem targets

| Identifier | Role | Status |
|---|---|---|
| `HW-THM-001` | RH-equivalent prime-residual envelope for `psi(x)` | active target; not proved |
| `HW-THM-002` | GRH-compatible extension for Dirichlet L-functions | reserved |
| `HW-THM-003` | Critical-line proof form for zeta zeros | reserved |
| `HW-THM-004` | Explicit-formula operator closure connecting Candidate C to the envelope | reserved |

## A-HW-THM-* — Theorem-target anti-seed

| Identifier | Failure mode | Status |
|---|---|---|
| `A-HW-THM-001` | (a) classical envelope-RH equivalence is not a Heller-Winters contribution; (b) `HW-PRIME-CIRCLE-001` is not progress toward RH | active |

## Citation rule

Use merged commit pins:

```text
[HW-THM-001 @ <merge-sha>]       # target-grade only
[A-HW-THM-001 @ <merge-sha>]     # anti-seed
```

Reserved identifiers may be cited only as pending/open successors, not as active theorem statements.
