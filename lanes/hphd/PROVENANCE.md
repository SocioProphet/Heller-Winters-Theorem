# Lane Provenance: hphd

## Origin

This lane was absorbed from the standalone repository `SocioProphet/hphd-zeta-mirror-lattice`.

The originating repo had evolved beyond the earlier 7-commit / three-document summary. At absorption time, current `main` was:

```text
b995d34f664b7dde3e1311294934db0ad27a94a6
```

and included five current documents under `docs/`.

## What was absorbed

Current source documents from `hphd-zeta-mirror-lattice/docs/`:

- `01-negative-mirror-lattice.md`
- `02-formal-claims.md`
- `03-research-roadmap.md`
- `04-explicit-formula-typing-gate.md`
- `05-richter-saturation-spec-v0-2.md`

The originating `README.md` was adapted into lane-internal framing at `lanes/hphd/README.md`.

## What was not absorbed

- `pyproject.toml` — superseded by Heller-Winters project metadata.
- `LICENSE` — superseded by the Heller-Winters license.
- `experiments/`, `tests/`, and generated `receipts/` — not copied in this Stage A absorption. They remain in the source repo as forensic provenance and may be imported later as runnable HW lane apparatus in a separate PR.

## Citation rewrite

After this PR merges, references to:

```text
SocioProphet/hphd-zeta-mirror-lattice
```

should be rewritten to:

```text
SocioProphet/Heller-Winters-Theorem/lanes/hphd
```

at the merge commit of this PR or a successor.

## Dependency consolidation

Under Heller-Winters, this lane inherits the repository-level dependency declaration:

```text
SocioProphet/Heller-Godel @ 988307215ad38ccb16514311222184a1b757752b
```

No additional dependency is introduced by this absorption.

## Claim boundary

This lane is RH-method material. It is not a proof of RH, GRH, an envelope theorem, a critical-line theorem, BSD, or any asymptotic theorem. The Richter saturation note remains finite-window empirical SPEC guidance only.
