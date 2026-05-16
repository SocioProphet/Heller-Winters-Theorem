# HW-THM-001 — RH-Equivalent Prime-Residual Envelope (Theorem Target)

Identifier: `HW-THM-001`  
Status: theorem-target — NOT PROVED  
Claim grade: target-grade / no theorem claim  
Repo: `SocioProphet/Heller-Winters-Theorem`  
Anti-seed: `A-HW-THM-001`

## 0. Status declaration

This document **commits a theorem target**. It does not prove it, does not claim partial progress toward it, and does not assert that any existing Heller-Winters apparatus constitutes evidence for it.

- Status: theorem-target, not proved.
- Claim grade: target-grade / no theorem claim.
- Boundary: no RH proof is claimed, and none is implied, until a complete proof artifact discharges this target.

Until then, `HW-THM-001` names a goal, not a result.

## 1. Primary theorem target — the psi(x) envelope

Let:

```text
psi(x) = sum_{p^k <= x} log p
```

be the second Chebyshev function.

**Target (HW-THM-001).** There exist constants `C > 0` and `x_0` such that for all `x >= x_0`:

```text
|psi(x) - x| <= C x^{1/2} (log x)^2
```

Equivalently:

```text
psi(x) = x + O(x^{1/2} (log x)^2)
```

This is the working target of the Heller-Winters program. It is stated on the **prime side** of the explicit formula, in the language in which the repository's existing apparatus operates.

## 2. Equivalent formulation — the critical line

The envelope target of Section 1 is equivalent to the Riemann Hypothesis:

**RH.** Every nontrivial zero `rho` of the Riemann zeta function `zeta(s)` satisfies:

```text
Re(rho) = 1/2
```

The equivalence is classical and is **not a Heller-Winters contribution**. The prime-residual envelope `psi(x) = x + O(x^{1/2}(log x)^2)` is equivalent to RH by classical work of von Koch (1901), in the standard refined form.

This document commits to the **envelope as the working target**. It does not claim the equivalence, and it does not re-prove the equivalence.

The critical-line statement is recorded here as the terminal / Clay-facing form of the same target. The Heller-Winters machinery is currently organized around the prime side of the explicit formula; the envelope statement is therefore the first working form, and the critical-line proof-form successor is reserved as `HW-THM-003`.

## 3. Explicit-formula bridge

The two formulations are linked by the explicit formula. Schematically:

```text
psi(x) = x - sum_rho x^rho/rho - log(2 pi) - (1/2) log(1 - x^{-2})
```

with the sum over nontrivial zeros `rho` of `zeta(s)`.

The location of the zeros controls the size of `psi(x) - x`: a zero with real part `sigma` contributes a term of size `x^sigma`. RH, which puts every nontrivial zero on `Re(s)=1/2`, yields the `x^{1/2}` envelope up to logarithmic factors. Conversely, the envelope forces all zeros into `Re(s) <= 1/2`, and the functional equation gives the critical line.

This bridge is the reason the program may work on the prime side: the zeros are not manipulated directly in the target statement; their aggregate effect on `psi(x)-x` is the object of study.

## 4. Current apparatus mapping

The following Heller-Winters components are mapped to their role relative to `HW-THM-001`. Mapping a component here does **not** make it evidence for the target.

| Component | Role relative to HW-THM-001 |
|---|---|
| Prime-operator lane | Working environment for the `psi(x)-x` residual; the lane in which the target is stated |
| Candidate C | Operator-side candidate object; relation to the target is structural, not evidential, until a proof artifact says otherwise |
| hphd lane | Points toward later Dirichlet / L-function generalization (`HW-THM-002`); not load-bearing for `HW-THM-001` |
| PFK receipts | Evidence-ledger infrastructure; records computational checks, does not constitute proof |
| `HW-PRIME-CIRCLE-001` | Seed arithmetic only. NOT load-bearing for this target. NOT partial progress toward RH. See Section 6. |

## 5. Non-claims

This document does not:

- claim a proof of the Riemann Hypothesis;
- claim any partial result toward RH;
- claim GRH or any statement about Dirichlet L-functions;
- claim Dirichlet-family uniformity, conductor uniformity, or uniformity in `q`;
- claim any physical-constant result;
- promote any empirical or computational diagnostic to theorem status;
- claim the classical envelope-RH equivalence as a Heller-Winters result.

## 6. Anti-seed: A-HW-THM-001

Two failure modes are registered against this target.

### A-HW-THM-001(a) — equivalence is not ours

The envelope-RH equivalence in Section 2 is von Koch's classical result, in standard refined form. Any citation of `HW-THM-001` that attributes the equivalence to the Heller-Winters program is incorrect.

Correct statement: `HW-THM-001` commits a target. It does not contribute the equivalence.

### A-HW-THM-001(b) — the prime-circle work is not progress toward RH

`HW-PRIME-CIRCLE-001` establishes the primorial-wheel correspondence and the Jacobsthal identification. These are sieve-structure and reduced-residue-system facts.

They are **not** a step toward the `psi(x)` envelope. The envelope is a statement about the analytic distribution of `zeta` zeros, and there is no current path from the wheel arithmetic to it.

Correct statement: `HW-PRIME-CIRCLE-001` must not be cited as partial progress toward, or evidence for, `HW-THM-001`. It is seed arithmetic of the program, in the same repository, and nothing more relative to this target.

Closure condition: none. Both disciplines apply permanently to `HW-THM-001` and successors.

## 7. Reserved successors

| Identifier | Role | Status |
|---|---|---|
| `HW-THM-002` | GRH-compatible extension: envelope targets for Dirichlet `L(s, chi)`, with conductor / uniformity dependency surface | reserved |
| `HW-THM-003` | Critical-line proof form: direct statement that all nontrivial `zeta` zeros satisfy `Re(s)=1/2` | reserved |
| `HW-THM-004` | Explicit-formula operator closure: the operator-side route connecting Candidate C to the envelope | reserved |

`HW-THM-002` is deliberately not the first target. GRH introduces Dirichlet characters, conductor dependence, uniformity in `q`, and zero-free regions in families. The first load-bearing object is `zeta(s)` alone.

## 8. Discharge conditions

`HW-THM-001` moves from theorem-target to theorem only when a complete proof artifact establishes the Section 1 envelope. Such an artifact must:

- prove `|psi(x)-x| <= C x^{1/2}(log x)^2` for explicit `C, x_0`, or prove the `O`-form with complete constant analysis;
- not rely on RH, GRH, numerical zero verification, or any unproved substitute;
- discharge or explicitly isolate every lemma it depends on;
- identify every imported theorem used in the proof;
- pass the repository's claim-boundary review before any theorem-grade promotion.

Until such an artifact exists and is verified, `HW-THM-001` is a goal. This file is a commitment to that goal, not its achievement.

## Citation form

```text
[HW-THM-001 @ <merge-sha>]       # theorem target, not proof
[A-HW-THM-001 @ <merge-sha>]     # anti-seed
```

Bibliographic:

```text
von Koch, H. (1901). Sur la distribution des nombres premiers.
Riemann-von Mangoldt explicit formula.
```

## Versioning

This is `HW-THM-001 v1.0`. Successor theorem-target or theorem-proof forms must use separate identifiers.
