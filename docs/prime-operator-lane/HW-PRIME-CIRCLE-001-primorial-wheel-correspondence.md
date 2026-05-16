# HW-PRIME-CIRCLE-001 — Prime-Circle / Primorial-Wheel Correspondence

Identifier: `HW-PRIME-CIRCLE-001`  
Status: active  
Lane: prime/operator lane  
Claim class: C0 definitions + C1 bounded finite verification + C3 imported background where standard references are cited  
Companion-reserved: `HW-PRIME-CIRCLE-002`, `HW-PRIME-CIRCLE-INV-001`  
Anti-seed: `A-HW-PRIME-001`, `A-HW-PRIME-002`  
Source provenance: `primes2_circle2.xlsx` (Drive artifact, 2018-03-17, “Prime Number Evaluator”), reconciled against direct computation.

## Summary

The prime-circle construction places an integer `P` at angular position `P` degrees on a circle. The construction observes recurring prime/composite structure on that circle.

This note identifies the underlying arithmetic object: the construction is the primorial wheel, with the initial `360`-degree display exposing the reduced residue structure of `2`, `3`, and `5`.

Three objects are recorded:

1. residue counts of primorial wheels — exactly Euler totients of primorials;
2. maximal cyclic wave-front gap — exactly the Jacobsthal function evaluated at primorials;
3. distinct wave-front gap count — computed and characterized as open for exact growth.

No physical-constant claim is made. The anti-seed `A-HW-PRIME-001` permanently separates this number-theoretic correspondence from fine-structure-constant or other physical-coupling claims.

## 1. The construction

For an integer `P`, define the circle position:

```text
theta(P) = P mod 360
```

The number `360 = 2^3 * 3^2 * 5` is highly composite. A prime `p > 5` is coprime to `2`, `3`, and `5`, so its residue modulo `30` lies in one of the eight reduced residue classes:

```text
1, 7, 11, 13, 17, 19, 23, 29 mod 30
```

Thus primes appear to fall into a recurring pattern because all primes greater than `5` lie inside the reduced residue system of the wheel modulus. The visible prime-circle structure is the mod-30 wheel, and the natural generalization is the primorial wheel.

For the kth primorial:

```text
P_k = p_1 p_2 ... p_k = 2 * 3 * 5 * ... * p_k
```

let:

```text
R_k = {a mod P_k : gcd(a, P_k) = 1}
```

ordered cyclically.

The wave-front gaps are the cyclic consecutive differences of `R_k`.

## 2. Object I — residue counts

The number of residues coprime to the kth primorial is:

```text
phi(P_k) = product_{i=1}^k (p_i - 1)
```

For `k = 1..9`, the values are:

```text
1, 2, 8, 48, 480, 5760, 92160, 1658880, 36495360
```

This is the standard totient-of-primorial sequence, commonly indexed as OEIS A005867.

This identification is exact and follows from multiplicativity of Euler's totient for squarefree primorials.

Claim class: C3 background when cited to standard number theory; C0 as local definition of the residue-count object.

## 3. Object II — maximal wave-front gap is the Jacobsthal function

Let `g_max(P_k)` denote the maximal cyclic gap between consecutive elements of `R_k`.

Then:

```text
g_max(P_k) = j(P_k)
```

where `j(n)` is the Jacobsthal function: the least `m` such that every interval of `m` consecutive integers contains at least one integer coprime to `n`.

For primorials, the first values recorded in this note are:

```text
2, 4, 6, 10, 14, 22, 26, 34, 40
```

This is the Jacobsthal-at-primorials sequence, commonly indexed as OEIS A048670.

### Proof sketch

The complement of `R_k` modulo `P_k` is the set of residues sharing a factor with `P_k`. A run of consecutive non-coprime integers of maximal length `L` corresponds to a cyclic gap of length `L + 1` between two consecutive coprime residues. The Jacobsthal function `j(P_k)` is exactly the smallest interval length forcing at least one coprime residue, hence exactly the maximal cyclic gap between coprime residues.

Thus the prime-circle construction's maximal wave-front gap is not an ad hoc feature; it is the Jacobsthal function at primorials.

Claim class: C0/C3 background for the definition-level identification, with C1 bounded finite verification in this PR.

## 4. Object III — distinct wave-front gap count

Let:

```text
dgc(k) = |{cyclic gap values in R_k}|
```

For `k = 1..9`, direct computation / recurrence gives:

```text
1, 2, 3, 5, 7, 10, 13, 16, 20
```

The first differences are:

```text
1, 1, 2, 2, 3, 3, 3, 4
```

The exact growth law is not asserted in this note. The working conjectural frontier is reserved as `HW-PRIME-CIRCLE-INV-001`:

```text
dgc(k) = k^2/4 + O(k)
```

The closed form `floor(k^2/4) + 1` matches early terms but fails at later checked terms, so it is not recorded as a theorem.

Claim class: C1 finite computed observation plus reserved conjectural frontier.

## 5. Reconciliation of the seed-work observation

The source artifact `primes2_circle2.xlsx` records a hand-read prime pattern as a sequence of singles and pairs.

Direct computation identifies the intended object as the twin-prime adjacency sequence: label a consecutive-prime relation `pair` when the prime gap is `2`, otherwise `single`.

The first eleven computed labels are:

```text
single, pair, pair, single, pair, single, pair, single, single, pair, single
```

or:

```text
1, 2, 2, 1, 2, 1, 2, 1, 1, 2, 1
```

The seed-work observation agrees in ten of eleven positions under this interpretation; the mismatch is treated as a manual-transcription artifact, not a mathematical object.

The exact object underneath the circle observation is therefore the primorial wheel gap cycle, not the hand-read adjacency string.

## 6. Research positioning

The Jacobsthal function at primorials has a nontrivial growth frontier. The Maier-Pomerance context concerns unusually large prime gaps and Jacobsthal-type growth. This note records only the object identification and finite verification.

This note does **not** prove a growth law for `j(P_k)`. `HW-PRIME-CIRCLE-002` is reserved for any future Jacobsthal-growth-frontier work.

This note also does **not** prove a closed form for `dgc(k)`. `HW-PRIME-CIRCLE-INV-001` is reserved for the distinct-gap-count growth law.

## 7. Verification appendix

The verification script added in this PR is:

```text
tests/prime_operator_lane/test_hw_prime_circle_001.py
```

It validates:

- the totient formula for the first nine primorials;
- direct residue/gap enumeration through `k = 7`, where naive enumeration is appropriate for CI;
- the recorded nine-term Jacobsthal and distinct-gap-count values as explicit document data;
- the mod-30 reduced residue classes;
- the lane-local anti-overclaim boundary `A-HW-PRIME-001`.

The script is deliberately stdlib-only. It intentionally does not brute-force the ninth primorial, whose totient is `36,495,360`.

## What this note does not do

This note does not:

- derive the fine-structure constant or any other physical constant;
- claim a physical interpretation for the prime-circle construction;
- prove a growth law for the Jacobsthal function;
- prove a closed form for the distinct-gap-count sequence;
- prove or imply the Riemann hypothesis;
- connect the construction to zeta zeros except as background prime/operator-lane context;
- transfer methodology to constitute a Clay-program claim.

## Citation form

```text
[HW-PRIME-CIRCLE-001 @ <merge-sha>]
[A-HW-PRIME-001 @ <merge-sha>]
```

## Versioning

This is `HW-PRIME-CIRCLE-001 v1.0`. Future revisions may add references, broaden verification range, or attach replay receipts. Any Jacobsthal-growth or distinct-gap-growth result requires a separate identifier.
