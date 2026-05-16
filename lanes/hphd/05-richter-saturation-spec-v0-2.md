# Richter Saturation SPEC v0.2 Note

Status: **empirical SPEC refinement / finite-window diagnostic / not RH evidence**.  
Scope: explicit-formula / prime-harness variance-explained diagnostics.  
Source class: Part A Richter saturation measurement handoff.  
Claim discipline: finite-window empirical guidance only.

## 0. Purpose

This note records the Richter saturation measurement as a SPEC v0.2 design input. The result validates the need for the `Delta u / N` correction and shows that interval/box resolution controls whether zero-band expansion improves or over-saturates the model.

This is not evidence for RH, GRH, BSD, or any asymptotic theorem. It is an empirical harness-design result.

## 1. Measurement table

| Interval | n_boxes | Peak R^2 | At T | Interpretation |
|---|---:|---:|---:|---|
| I1 | 4 | 0.949 | 30 | Over-saturation above T=30 |
| I1 | 16 | 0.954 | 1000 | Still climbing |
| I2 | 32 | 0.799 | 300 | Over-saturation above T=300 |
| I3 | 4 | 0.908 | 1000 | Climbing; bandwidth acceptable |
| I3 | 32 | 0.206 | 1000 | Bandwidth-starved |
| I4 | 4 | 0.095 | 1000 | Barely above zero |

## 2. SPEC v0.2 implications

### 2.1 Delta-u correction confirmed

The I1 / 4-box regime peaks at `T = 30` and then over-saturates. This matches the Chebyshev band-edge interpretation: once the zero band exceeds the resolution allowed by the box width, additional zeros self-cancel or add noise.

SPEC v0.2 should therefore keep the primary correction toward smaller `Delta u`, with `Delta u = 0.0025` as the primary target unless a later run falsifies it.

### 2.2 Model-1 floor criterion

`I4` at `T = 1000` has `R^2 = 0.095`. That is structurally underpowered for novelty testing. This is not simply a zero-count problem; it may indicate box-resolution or interval-structure mismatch.

Add the following precondition before any G4 novelty gate:

```text
if VarExpl(Model 1, N*) < 0.30 on an interval:
    flag interval as structurally_underpowered
    exclude interval from G4 novelty gate
```

This prevents Models 2 and 3 from being interpreted as novel when Model 1 cannot establish a minimally explanatory baseline.

### 2.3 Saturation-envelope diagnostic

The `n_boxes` sensitivity is real. For example:

```text
I1, 4 boxes:  peaks at T=30
I1, 16 boxes: still climbing at T=1000
```

These are different resolution regimes, not noise.

SPEC v0.2 should promote the saturation envelope to a first-class M2a output:

```text
Env(N) = max_{N' <= N} VarExpl(Model 1, N')
```

The envelope should be emitted alongside raw variance explained so reviewers can distinguish:

```text
over-saturated regimes
still-climbing regimes
bandwidth-starved regimes
structurally underpowered regimes
```

## 3. Required SPEC changes

### G0 provenance check

Add a Model-1 floor test:

```yaml
model1_floor:
  metric: VarExpl(Model 1, N*)
  threshold: 0.30
  below_threshold_status: structurally_underpowered
  g4_eligible: false
```

### M2a output contract

Add saturation-envelope output:

```yaml
m2a_saturation_envelope:
  metric: Env(N) = max_{N_prime <= N} VarExpl(Model 1, N_prime)
  required: true
  emitted_per_interval: true
  emitted_per_n_boxes: true
```

### G4 novelty gate

Before G4 can score novelty for Models 2 or 3, require:

```text
VarExpl(Model 1, N*) >= 0.30
```

and require that the saturation envelope has been emitted.

## 4. Failure and exclusion semantics

A structurally underpowered interval is not a failed theorem and not a negative result about zeros. It is a harness exclusion flag.

The correct ledger status is:

```text
excluded_from_G4_due_to_model1_floor
```

not:

```text
model failed
zeros irrelevant
claim falsified
```

## 5. Nonclaims

This note does not claim:

- RH or GRH evidence;
- an asymptotic residual theorem;
- that Model 1 captures all explicit-formula structure;
- that I4 is mathematically unimportant;
- that higher models are invalid on I4;
- that the observed finite-window R^2 values generalize without uniformity proof.

It only records SPEC-level consequences of the Richter saturation measurement.

## 6. Follow-on implementation tasks

1. Add `model1_floor` to the provenance schema used by the prime harness.
2. Emit `Env(N)` as a first-class M2a artifact.
3. Update G4 so structurally underpowered intervals are excluded from novelty scoring.
4. Add a replay fixture using the six rows above as expected finite-window behavior.
5. Add the measurement source record to `SocioProphet/systems-learning-loops` under `kb/sources/`.
