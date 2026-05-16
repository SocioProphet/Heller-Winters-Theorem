# Research Roadmap and Reproducibility Backlog

Status: Draft v0.1  
Lane: HPHD / zeta mirror-lattice / reproducible analytic-number-theory experiments  
Purpose: Convert the current HPHD zeta mirror-lattice section into a research program with staged claims, experiments, and BSD-adjacent extensions.

## 1. Operating principle

This repository should advance in three layers:

1. **Manuscript layer** — precise definitions, claim boundaries, and explanatory prose.
2. **Formal layer** — lemmas, conjectures, admissible transformations, and typed symbolic objects.
3. **Experimental layer** — reproducible numerical experiments, explicit-formula decompositions, plots, fixtures, and receipts.

The current work lives mostly in layers 1 and 2. The next stage is to build layer 3 without overstating what the experiments prove.

## 2. Immediate backlog

### R1: Define admissible embeddings

Problem: The trivial-zero lattice and non-trivial-zero spectrum have different raw counting densities.

Goal: Define admissible maps:

```math
\Phi:\mathcal M^-_{\zeta}\to Z_{\mathrm{nt}}
```

or admissible measure transports:

```math
\Phi_*\mu_{\mathrm{triv}}\sim\mu_{\mathrm{nt}}.
```

Acceptance criteria:

- At least three candidate embedding classes are defined.
- Each candidate states its domain, codomain, measure, and comparison invariant.
- Each candidate explicitly avoids claiming raw density equality.

Candidate families:

- logarithmic coordinate transforms;
- zero-counting quantile maps;
- spectral-index maps;
- explicit-formula contribution maps;
- operator-theoretic comparison maps.

### R2: Explicit-formula decomposition experiment

Problem: The manuscript claims that prime counting decomposes into main growth, non-trivial-zero fluctuation, and completion/trivial-zero correction terms.

Goal: Build a reproducible notebook or script that demonstrates a truncated explicit-formula decomposition.

Acceptance criteria:

- Compute a prime-counting or Chebyshev-function target on a bounded range.
- Compare a smooth main term against a zero-corrected approximation.
- Track the contribution class of each term.
- Record numerical error and limitations.

Deliverables:

```text
experiments/explicit_formula_decomposition.py
notebooks/explicit_formula_decomposition.ipynb
receipts/explicit_formula_decomposition_v0.json
```

### R3: Regularized density examples

Problem: Divergent-series regularization must remain typed as regularization, not ordinary equality.

Goal: Provide minimal reproducible examples for:

```math
1+1+1+\cdots\overset{\zeta\text{-reg}}{=}-\frac12
```

and:

```math
1+2+3+4+\cdots\overset{\zeta\text{-reg}}{=}-\frac1{12}.
```

Acceptance criteria:

- Ordinary divergence is shown separately.
- Analytic-continuation value is shown separately.
- Output labels use `zeta-reg`, not ordinary equality.

### R4: Dirichlet L-function extension

Problem: The zeta mirror lattice is only the base case. HPHD needs character-dependent mirror lattices.

Goal: Extend the framework from `zeta(s)` to `L(s, chi)`.

Acceptance criteria:

- Define primitive Dirichlet characters used in examples.
- Identify how parity changes completion data and trivial-zero structure.
- Define `M^-_chi` as a character-dependent mirror lattice.
- Add at least one worked example for even and odd characters.

Deliverables:

```text
docs/04-dirichlet-l-mirror-lattices.md
experiments/dirichlet_l_mirror_lattice.py
```

### R5: BSD-adjacent bridge map

Problem: The repository is BSD-adjacent but must not pretend to prove BSD.

Goal: Map the analytic pattern from zeta/Dirichlet L-functions toward elliptic-curve L-functions.

Acceptance criteria:

- Explain the shared template:

```text
arithmetic object -> L-function -> analytic continuation / functional equation -> zeros / special values / arithmetic invariant
```

- Separate zeta-level facts from elliptic-curve-level facts.
- Define what would be required before a BSD-lane claim is admissible.

Deliverables:

```text
docs/05-bsd-adjacent-bridge.md
```

## 3. Suggested repository structure

```text
.
├── README.md
├── LICENSE
├── docs/
│   ├── 01-negative-mirror-lattice.md
│   ├── 02-formal-claims.md
│   ├── 03-research-roadmap.md
│   ├── 04-dirichlet-l-mirror-lattices.md
│   └── 05-bsd-adjacent-bridge.md
├── experiments/
│   ├── explicit_formula_decomposition.py
│   ├── regularized_density_examples.py
│   └── dirichlet_l_mirror_lattice.py
├── notebooks/
│   └── explicit_formula_decomposition.ipynb
├── receipts/
│   └── explicit_formula_decomposition_v0.json
└── tests/
    └── test_claim_boundaries.py
```

## 4. Claim taxonomy for future commits

Every new document should label claims as:

- `Definition`
- `Lemma`
- `Conjecture`
- `Analogy`
- `External theorem`
- `Computational experiment`
- `HPHD interpretation`
- `Open problem`

This prevents interpretive language from silently hardening into theorem language.

## 5. First experimental design: explicit formula v0

### Objective

Show that a prime-counting target can be approximated by a smooth term plus zero-derived corrections, while preserving the distinction among:

- pole/main-term contribution;
- non-trivial-zero oscillatory contribution;
- trivial-zero/completion contribution;
- truncation error.

### Minimal implementation

Use `mpmath`, `sympy`, or Sage/PARI bindings if available. Prefer open-source and reproducible dependencies.

Initial Python direction:

```text
Python 3.11+
mpmath
sympy
pytest
ruff
```

### Receipt schema sketch

```json
{
  "experiment": "explicit_formula_decomposition_v0",
  "status": "draft",
  "target_function": "psi(x) or pi(x)",
  "x_range": [10, 100000],
  "zero_count": 0,
  "terms": {
    "main": "recorded",
    "non_trivial_zero_correction": "recorded",
    "trivial_completion_correction": "recorded",
    "truncation_error": "recorded"
  },
  "claim_boundary": "numerical illustration, not proof"
}
```

## 6. Quality gates

Before promoting any result:

1. Ordinary equality and regularized equality must be visually distinct.
2. All density comparisons must name the measure.
3. Any use of RH must be labeled conditional.
4. Any BSD mention must be labeled adjacent unless elliptic-curve L-function machinery is actually present.
5. Every experiment must emit a receipt.
6. Every plot must state whether it is illustrative, heuristic, or validated.

## 7. Next two implementation steps

1. Add `experiments/regularized_density_examples.py` with explicit divergence-vs-regularization labels.
2. Add `experiments/explicit_formula_decomposition.py` as a bounded numerical demonstration, initially without claiming theorem-level significance.

## 8. Current completion estimate

- Manuscript capture: 70%
- Formal claim boundary: 55%
- Experimental scaffolding: 0%
- Dirichlet L-function extension: 0%
- BSD-adjacent bridge: 0%
- Overall repo lane readiness: 25%

This is enough to preserve the work and prevent loss. It is not yet enough to claim a functioning research harness.
