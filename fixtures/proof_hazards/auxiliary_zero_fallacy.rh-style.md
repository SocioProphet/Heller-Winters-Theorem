# Negative Control: Auxiliary Zero Fallacy

Status: rejected proof pattern  
Expected validator disposition: fail or downgrade  
Hazards:

- auxiliary-intersection-fallacy
- dropped-premise
- unproved-bridge
- zero-set-intersection-promotion

## Bad proof pattern

Let `X(s)` be the classical source condition. Let `A(s)` be an auxiliary condition introduced by a model.

Assume:

```text
X(s) = 0.
```

The model gives an identity of the form:

```text
Aux(s) = K(s) + C(s) X(s).
```

Therefore, at a classical zero,

```text
Aux(s) = K(s).
```

Now set

```text
Aux(s) = 0
```

and solve

```text
K(s) = 0.
```

Suppose this algebra implies

```text
Y(s).
```

The bad proof concludes:

```text
X(s) = 0 -> Y(s).
```

## Why this must fail

From

```text
X(s) = 0
```

we only obtained

```text
Aux(s) = K(s).
```

We did not obtain

```text
Aux(s) = 0
```

or

```text
K(s) = 0.
```

The valid conclusion is only:

```text
X(s) = 0 and Aux(s) = 0 -> Y(s).
```

To promote the result, a separate bridge is required:

```text
X(s) = 0 -> Aux(s) = 0.
```

## Minimal counterexample schema

Let

```text
X = 0
Aux = 3
K = 3
```

Then

```text
Aux = K
```

but neither side is zero. Equality is not vanishing.

## Required remediation

A manuscript passage matching this fixture must do one of the following:

1. retain the auxiliary condition in the conclusion;
2. prove the bridge from the classical source condition to the auxiliary condition;
3. downgrade the claim to heuristic or conditional status;
4. remove theorem-strength language.