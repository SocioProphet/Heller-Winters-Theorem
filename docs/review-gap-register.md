# Review Gap Register

Status: live.  
Review date: 2026-05-10.  
Scope: Heller–Winters Programme repository after programme reframing and Candidate C capture.

This register captures the gaps identified in the review pass and records how each gap is being discharged.

## G-01 — Prior ZIP review was preliminary

Risk: an earlier qualitative assessment of the Claude ZIP was stated more strongly than the tool inspection justified.

Disposition: captured as process defect. Future external-agent reviews must be labeled as preliminary unless the uploaded artifact has been inspected.

Status: captured; no code action required.

## G-02 — Repository name still says “Theorem”

Risk: the GitHub path `Heller-Winters-Theorem` leaks theorem-language into clone URLs and agent assumptions.

Disposition: README now states that the repository name is historical and the canonical conceptual object is the Heller–Winters Programme.

Status: mitigated; full discharge requires repository rename or permanent repository-name note.

## G-03 — Programme-map theorem-language drift

Risk: `docs/clay-problem-programme-map.md` contained phrases such as “central theorem” and “Heller–Winters Theorem.”

Disposition: the programme-map has been patched to refer to the Heller–Winters Programme and to future theorem-candidate statements rather than an existing central theorem.

Status: discharged by governance cleanup PR.

## G-04 — Candidate C package missing required files

Risk: the package README named `run-plan.md`, `claim-ledger-entry.md`, and `pfk-receipt-template.json`, but those files were absent.

Disposition: all three are supplied in the Candidate C capture.

Status: discharged by file creation.

## G-05 — Registry was not actually locked

Risk: the registry named phase maps, statistics, windows, and normalizations but did not define them.

Disposition: `registry.md` now defines the exact phase map, frequency set, primary statistic, circular convention, sequence domains, surrogate definitions, seeds, fixture scale, and production scale.

Status: discharged for registry v0.1; mathematical adequacy remains subject to literature review.

## G-06 — Null gates were qualitative

Risk: alternate-substrate gates used phrases like “density-matched” and “wheel-compatible” without operational definitions.

Disposition: `null-gates.md` now defines the all-integers gate, Cramér-Bernoulli gate, wheel-composite count-matched gate, and replay gate with pass/fail outputs.

Status: discharged for executable v0.1.

## G-07 — Fixture had no fixture value

Risk: Wγ was specified but not executed.

Disposition: fixture result for `X_fixture = 1e4`, `B = 16`, and seed `20260510` is included under `results/fixture/`; hosted CI replay passed.

Status: discharged for fixture replay; larger-run replay remains separate work.

## G-08 — PFK was referenced but not integrated

Risk: provenance was aspirational rather than emitted.

Disposition: receipt template and emitted receipts are included. The runner emits deterministic result hashes and receipt files.

Status: partially discharged; full PFK integration awaits native Event-IR / ProofArtifact integration.

## G-09 — Obligations ledger lacked status

Risk: the ledger was a governance note, not a live status register.

Disposition: `04-programme-obligations.md` now includes status, evidence, and next action fields.

Status: discharged structurally; owners can be assigned later.

## G-10 — Candidate C was over-promoted

Risk: the phrase “phase-gate distinguishability theorem” could imply theorem status before literature review and proof.

Disposition: Candidate C is now classified as an empirical artifact candidate and possible finite-window theorem candidate after literature and proof review.

Status: discharged in wording.

## G-11 — Literature check not done

Risk: Candidate C may be known, a restatement, an empirical illustration, or a genuinely new finite-window statement.

Disposition: `claim-ledger-entry.md` records literature status as pending and blocks theorem promotion.

Status: open; tracked by issue #27.

## G-12 — Code layer absent

Risk: no deterministic runner, fixture harness, surrogate generator, statistic implementation, or receipt emitter existed.

Disposition: `scripts/run_phase_gate_candidate_c.py` and `tests/test_phase_gate_candidate_c.py` are supplied.

Status: discharged for v0.1 fixture and preliminary `X = 1e6` execution.

## G-13 — Direct-to-main commits are inconsistent with audit discipline

Risk: prior changes were committed directly to `main`.

Disposition: Candidate C capture and governance cleanup are handled by branch + PR + CI.

Status: mitigated for current work; future work must keep branch/PR discipline.

## G-14 — Candidate C v0.1 does not currently show Cramér-surrogate rejection

Risk: the first executable statistic may not distinguish primes from a density-matched Cramér-Bernoulli surrogate.

Disposition: the artifact reports the negative/ambiguous result rather than inflating claims. This is a successful governance outcome: the apparatus produced a finite-window result without promotion.

Status: captured; tracked by issues #29 and #30.

## G-15 — X1e6 preliminary raw JSON policy

Risk: preliminary `X=1e6` summary and receipt existed without explicit policy for full raw JSON.

Disposition: `results/X1e6-preliminary/README.md` records the decision to treat the full raw JSON as regenerable-only until the stronger B=256 run supersedes it.

Status: discharged by governance cleanup PR.
