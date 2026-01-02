#!/usr/bin/env python3
import os, re, argparse
from datetime import date

TODAY = str(date.today())

def slug(s: str) -> str:
    s = s.lower()
    s = s.replace("ψ","psi").replace("π","pi").replace("γ","gamma").replace("ρ","rho")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s or "untitled"

def find_dir_with_prefix(parent: str, prefix: str) -> str:
    if not os.path.isdir(parent): raise FileNotFoundError(parent)
    matches = [d for d in os.listdir(parent) if d.startswith(prefix)]
    if len(matches) != 1:
        raise RuntimeError(f"Expected exactly 1 match for {prefix} in {parent}, got {matches}")
    return os.path.join(parent, matches[0])

def write(path: str, content: str, force: bool):
    if os.path.exists(path) and not force:
        return False
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return True

def chapter_readme(ch_num:int, title:str, overview:str, rel:str) -> str:
    return f"""# Chapter {ch_num} — {title}

## Overview
{overview}

## Operator contract
Every operator in this chapter must be one of:
1) theorem-backed eliminator, 2) coordinate change, or 3) explicitly labeled heuristic probe.

## Where the content lives
- Sections live in `sec_XX-*` folders.
- Each section is decomposed into:
  - `subsec_01-overview/` (primary prose + intuition)
  - `subsec_02-formalism/` (definitions, operators, equations)
  - `subsec_03-tests-ledger/` (falsifiers, drift tests, audit entries)

## Change log
- {TODAY}: populated scaffold ({rel})
"""

def section_readme(sec_title:str, sec_idx:int) -> str:
    return f"""# Section {sec_idx:02d} — {sec_title}

## Purpose
(Define the responsibility of this section inside the operator stack.)

## Content split
- `subsec_01-overview/README.md` — narrative + intent (≥3 sentences for core claims)
- `subsec_02-formalism/README.md` — math objects and operator definitions
- `subsec_03-tests-ledger/README.md` — falsifiers, drift tests, and ledger schema

## Change log
- {TODAY}: populated scaffold
"""

def overview_subsec(sec_title:str, summary:str) -> str:
    return f"""# Overview — {sec_title}

## Summary
{summary}

## Notes
- Keep the claim surface tight: what’s deterministic vs what’s heuristic.
- Keep invariance front-and-center: cross-base, cross-window, cross-compartment.

## Change log
- {TODAY}: inserted summary text
"""

def formalism_subsec(sec_title:str, formalism_bullets:list[str]) -> str:
    bullets = "\n".join([f"- {b}" for b in formalism_bullets]) if formalism_bullets else "- (define operators + notation here)"
    return f"""# Formalism — {sec_title}

## Definitions / Operators
{bullets}

## Open formalization tasks
- (add explicit notation, domains/codomains, and commutation notes)

## Change log
- {TODAY}: created formalism stub
"""

def tests_subsec(sec_title:str, tests:list[str]) -> str:
    bullets = "\n".join([f"- {t}" for t in tests]) if tests else "- (add falsifiers + drift checks here)"
    return f"""# Tests + Ledger — {sec_title}

## Falsifiers (what would disprove this section’s utility)
{bullets}

## Ledger fields
- input window spec (X, r), coordinate gauge (base b, u=ln x)
- operator params (must be state-governed)
- outputs (candidate reduction / residual metrics / diagnostic plots)
- drift flags (scale/base/p-adic/Zeckendorf)

## Change log
- {TODAY}: created tests stub
"""

# -----------------------
# Source text (Ch 1–6)
# -----------------------
CH = {
  1: {
    "title": "Purpose and Thesis",
    "overview": ("We situate primes as locally discrete but globally lawful, and we frame our contribution as a policy-enforced multiscale program rather than a single trick. "
                 "We separate hard constraints (that remove candidates) from soft analytic layers (that score and diagnose residual structure). "
                 "We define success as producing a disciplined, falsifiable pipeline that outperforms baseline candidate search in inference value, and is auditable in its failure modes. "
                 "We explicitly distinguish constructive localization from proof of RH, treating RH-consistency as an envelope constraint on residuals rather than a generator of primes. "
                 "We commit to rigor: every introduced operator is a theorem-backed eliminator, a coordinate change, or an explicitly labeled heuristic probe."),
    "sections": [
      ("Mean-field vs fluctuation decomposition",
       "We treat π(x) ~ x/ln x as the mean-field baseline and treat deviations as the scientifically informative remainder. This matters because most false “prime laws” confuse mean behavior with residual structure. We define observables that separate these components so we can measure what our construct adds beyond the PNT baseline."),
      ("“Volume not distance” as the central invariant",
       "We work in log-volume u = ln x because multiplicative scaling becomes additive and windowing becomes well-posed. This matters because primes thin out roughly like 1/ln x, so distance in x is the wrong coordinate for stability tests. The volume principle is the backbone that makes ratio schedules (octaves/decades/metallics) comparable."),
      ("Policy-enforced inference vs brute search",
       "We formalize a pipeline where constraints prune candidate space before any expensive tests occur. This matters because primality is easy to check but hard to predict; policy layers target prediction. We treat each sieve/constraint as an auditable operator with a defined failure surface."),
      ("What counts as “signal” vs “artifact”",
       "We define signal as structure stable under base changes, window schedule changes, and identity-channel projections. This matters because digit artifacts can mimic periodicity if we only look in one base or one window family. Residuals that persist across incompatible partitions are candidates for real arithmetic structure."),
      ("Determinism vs fitted parameters",
       "We require tuning parameters be functions of state (wheel residue, sector index, base class, p-adic depth), not post-hoc knobs. This matters because post-hoc tuning makes the model non-predictive by construction. Free parameters are treated as a red flag unless governance rules bind them."),
      ("Falsifiability criteria",
       "We specify failure as false positives, false negatives, instability across scales, and drift under base changes. This matters because beautiful constructions can still be wrong and we need adversarial tests. We define falsifiers at the operator level, not merely at final output."),
      ("Scope limits and non-claims",
       "We separate three claims: candidate reduction, residual diagnosis, and deep conjecture proof. This matters because conflating them is historically the most common failure mode in prime “theories.” We preserve scientific credibility by stating what we do not prove."),
      ("Notation and canonical coordinates",
       "We fix canonical notation: u=ln x, window ratio r, log-length L=ln r, wheel modulus M, and valuations v_p(·). This matters because consistency of notation prevents subtle category errors (index vs value vs state space). The construct is operator-heavy, so notation is part of correctness."),
      ("Relationship to classical prime theorems",
       "We anchor the pipeline in known theorems: Euclid, Dirichlet progressions, Bertrand/Chebyshev bounds, PNT, sieve results, and explicit-formula framing. This matters because our method must be consistent with what is already known and cannot rewrite history. These results provide baselines for evaluation."),
      ("Roadmap of the full stack",
       "We preview operator ordering: bounds → wheel → crystallographic governance → symmetry shells → base/p-adic/Zeckendorf compartments → ratio windows → quotient normalization → identity channels → phase gate → audit tests. This matters because ordering is not cosmetic: non-commuting operators can create artifacts. The roadmap makes later chapters readable as a single machine."),
    ],
  },
  2: {
    "title": "Canonical Coordinate System",
    "overview": ("We formalize coordinate choices that make “volume” measurable and scale comparisons meaningful. "
                 "The log coordinate u=ln x converts multiplicative growth into additive translation and makes window schedules first-class via L=ln r. "
                 "Base changes become frequency rescalings in log-harmonic analysis, making base-e a canonical gauge. "
                 "We distinguish index space, value space, and policy/state space to prevent category errors. "
                 "We also formalize boundary handling so window claims remain reproducible."),
    "sections": [
      ("Log coordinate (u=ln x)",
       "We define u=ln x and treat x=e^u as the primary scale map. This matters because windows [X, rX] become intervals [ln X, ln X+ln r] of fixed log-length. The construction’s harmonic language becomes literal in u."),
      ("Multiplicative windows and log-length (L=ln r)",
       "We define each window family by ratio r with length L=ln r in log space. This matters because it makes octaves, decades, and metallic dilations comparable as operators. It clarifies why volume scales multiplicatively, not additively."),
      ("Change-of-base as frequency rescaling",
       "We show log_b x = (ln x)/(ln b), so base change is linear scaling in u. This matters because features that survive base changes are stronger evidence of intrinsic structure. It prevents mistaking base artifacts for arithmetic phenomena."),
      ("Volume element compatibility",
       "Equal lengths in u represent equal multiplicative factors in x. This matters because prime density uses dt/ln t, aligning naturally with log-volume reasoning. It justifies using window expectations as invariant baselines."),
      ("Octaves/decades as canonical windows",
       "We treat r=2 and r=10 as anchor windows. This matters because they connect to binary/decimal representations and interpretability. They also serve as calibration schedules before irrational probes."),
      ("Metallic/plastic windows as irrational probes",
       "We treat incommensurate ratios as de-aliasing probes. This matters because irrational scalings break resonance with periodic partitions and expose aliasing. We do not claim primes obey these constants; we use them as stress tests."),
      ("Index vs value vs policy space",
       "We define and track transitions between index space, value space, and policy space. This matters because quadratic families are sparse in value space but regular in index space, and confusing them creates false density claims. Policy space behaves like a finite state machine layered on values."),
      ("Window families and nesting",
       "We define nesting rules and multi-resolution schedules. This matters because cross-window consistency is a main defense against artifacts. Nesting reduces boundary cherry-picking."),
      ("Boundary effects and endcaps",
       "We separate interior statistics from boundary corrections. This matters because small-window claims often fail by ignoring end effects. Boundary handling is recorded in the ledger."),
      ("Units, normalization, invariance",
       "We define normalization conventions so comparisons across scales are meaningful. This matters because raw counts grow with volume and cannot diagnose structure. Invariance under coordinate changes is the criterion for reality."),
    ],
  },
  3: {
    "title": "Prime Density Mean-Field Model",
    "overview": ("We restate the classical mean-field picture: prime density ≈ 1/ln x and cumulative count ≈ x/ln x at leading order. "
                 "Any candidate reduction or scoring must preserve this baseline rather than hallucinate structure. "
                 "We define windowed expectations via ∫_X^{rX} dt/ln t and treat deviations as residuals carrying spectral content. "
                 "We distinguish regimes where artifacts dominate versus where asymptotics stabilize. "
                 "This chapter sets the guardrails our operator stack must respect."),
    "sections": [
      ("π(x) ~ x/ln x heuristic",
       "We take x/ln x as the baseline growth law. This matters because it calibrates expected counts and gaps. Deviations must be measured relative to this baseline to avoid false discoveries."),
      ("Local intensity λ(x) ~ 1/ln x",
       "We treat prime occurrence as a thinning process with slowly varying rate 1/ln x. This matters because it motivates window expectation integrals and stabilizes coverage intuition. It clarifies why ln x is the natural local scale."),
      ("Window expectation ∫ dt/ln t",
       "We define expected prime count in a window by ∫_X^{rX} dt/ln t. This matters because it provides a coordinate-invariant baseline for any ratio r. It supplies denominators for quotient observables later."),
      ("Decade vs octave expectations",
       "We compare expectations under r=10 and r=2. This matters because these windows interact differently with digit/bit partitions and can expose aliasing. They anchor the scale ladder before irrational ratios."),
      ("Drift in 1/u in log coordinates",
       "We rewrite intensity as 1/u with u=ln x. This matters because it shows rate varies slowly and window comparisons are stable. It underwrites log-volume as the correct space."),
      ("Coverage interpretations",
       "We interpret coverage as density × volume and gaps as inverse density. This matters because many intuitive arguments assume constant density, which is false. Coverage language forces correct scaling."),
      ("Average gap ~ ln x",
       "We use average gap as the baseline for next-prime proximity. This matters because prediction error should be compared to ln p, not absolute distance. It bounds what is plausible from inference alone."),
      ("Variance intuition",
       "We acknowledge fluctuations and treat variance as something to diagnose, not ignore. This matters because our construction targets residual structure. Later identity channels formalize noise vs structure."),
      ("Scaling regimes",
       "We distinguish small, moderate, and large window behavior. This matters because artifacts are worst in small windows and asymptotics are best in large ones. Ratio scheduling is designed to test stability across regimes."),
      ("Mean-field invariants used by policy",
       "We identify invariants the policy must respect: density scaling, gap scaling, quotient stability. This matters because it prevents the pipeline from cheating by producing numerically pretty results that violate known laws. These invariants are guardrails."),
    ],
  },
  4: {
    "title": "Boundedness Layer",
    "overview": ("We use the Bertrand/Chebyshev theorem as an unconditional enclosure to bound next-prime search. "
                 "This transforms localization from unbounded wandering into a finite policy domain. "
                 "We reinterpret the enclosure as a fixed log-length cell L=ln 2 around u=ln p. "
                 "All subsequent sieves act inside this boundary and are judged by how they shrink candidate mass. "
                 "Boundedness is a scaffold: necessary, never sufficient."),
    "sections": [
      ("Bertrand/Chebyshev bound (n,2n)",
       "We state the theorem guaranteeing a prime between n and 2n for n>1. This matters because it is deterministic, not heuristic. It is the first policy enclosure for localization."),
      ("Specialization to (p,2p)",
       "We apply the bound to primes p. This matters because the next prime lies in a known finite set. Every subsequent operator is evaluated by how it shrinks that set."),
      ("Implications for search complexity",
       "The bound limits worst-case scan length to p−1 candidates before filtering. This matters because it supplies an explicit baseline for reduction. It also shows reductions must be multiplicative to matter asymptotically."),
      ("Interaction with wheel modulus selection",
       "Wheel effectiveness depends on elimination density over the bounded interval. This matters because wheel size has diminishing returns and must be chosen relative to the domain. The bound makes wheel depth an explicit optimization tradeoff."),
      ("Bounds as outer policy boundary",
       "We treat the bound as an irreversible constraint: no candidate outside (p,2p) is considered. This matters because it prevents drifting into untestable generalities. It makes falsification crisp: predicted prime must lie inside the boundary."),
      ("Nested bounds across ratios",
       "Other ratio windows can be nested inside the doubling bound for multi-resolution analysis. This matters because it creates internal checkpoints and prevents cherry-picked windows. Nesting turns ratios into disciplined schedules."),
      ("Bounding in log coordinate (u)",
       "We write the bound as u ∈ [ln p, ln p + ln 2]. This matters because it merges boundedness with log-harmonic analysis. It behaves like a fixed-length cell in log space."),
      ("Practical boundedness metrics",
       "We define candidate count, expected primes per bound, and expected filtered survivors. This matters because it lets us measure whether layers do real work. Metrics replace aesthetic judgments."),
      ("Failure modes (trivial, degenerate)",
       "Boundedness alone does not locate primes; it only encloses them. This matters because it prevents overclaiming and highlights the need for later layers. The bound is scaffolding, not solution."),
      ("Bound-sensitive scoring rules",
       "We score candidates relative to the bounded interval using normalized rank, local intensity, and residue admissibility density. This matters because it aligns scoring with what the bound guarantees. It also enables consistent evaluation across scales."),
    ],
  },
  5: {
    "title": "Wheel Sieve Layer",
    "overview": ("We formalize wheel sieves as modular admissibility filters: candidates must be coprime to a chosen modulus M. "
                 "Wheels eliminate large composite volume cheaply and provide stable periodic structure via residue classes. "
                 "We treat wheel selection as a policy decision balancing pruning power against overhead and resonance hazards. "
                 "Residue classes become state labels in a finite automaton that supports structured scoring and governance. "
                 "The wheel is eliminator first, feature generator second."),
    "sections": [
      ("Modulus definition (M=∏ p_i)",
       "We define M as the product of selected primes. This matters because coprimality to M removes all candidates divisible by those primes. It is the deterministic backbone of sieve pruning."),
      ("Reduced residue classes φ(M)",
       "We define residues modulo M that are coprime to M. This matters because survivors must lie in this reduced set. It gives exact survivor density before higher-order effects."),
      ("Candidate density φ(M)/M",
       "We quantify how much the wheel reduces the space. This matters because wheel depth becomes a measured knob rather than folklore. It predicts expected survivors per bounded window."),
      ("Residue graphs and transitions",
       "We model candidate stepping as transitions between residue classes. This matters because it turns search into a state machine. That representation supports later symmetry governance and scoring."),
      ("Wheel depth vs compute cost",
       "Larger M prunes more but increases residue-handling overhead. This matters because practical effectiveness is total cost, not pruning fraction. The bounded interval makes the tradeoff explicit."),
      ("Interaction with base representations",
       "Wheel periodicity can resonate with base-b digit periodicity. This matters because resonance can create spurious patterns. Cross-base testing becomes mandatory as wheels deepen."),
      ("Compatibility with lattice-safe governance",
       "Periodic compartments must obey lattice-safe sector symmetries to avoid unstable assumptions. This matters because wheels are periodic states and governance prevents importing impossible symmetries. It keeps our periodic backbone disciplined."),
      ("Wheel as deterministic eliminator",
       "Wheels do not predict primes; they exclude impossibilities. This matters because it keeps claims honest. Wheel failures are interpretable: any prime must pass the wheel."),
      ("Wheel as feature generator",
       "Residues are not only filters but features for diagnostics and scoring. This matters because residue structure interacts with higher-order constraints. Features bridge hard pruning to soft inference."),
      ("Wheel invariants across windows",
       "We define wheel invariants expected to persist across window schedules. This matters because invariance is our defense against artifacts. Features that only appear in one schedule are suspicious."),
    ],
  },
  6: {
    "title": "Symmetric Offset Algebra",
    "overview": ("We formalize symmetric-offset identities centered on difference-of-squares that yield composite certificates and connect factor pairs to additive geometry. "
                 "Parity constraints determine when decompositions exist, giving cheap policy filters. "
                 "Shell families can be analyzed statistically in log windows, producing both eliminators and features. "
                 "Hyperbola geometry ab=n in rotated coordinates links to hyperbolic identity-channel reasoning later. "
                 "Shell enforcement is positioned as structural noise reduction."),
    "sections": [
      ("Difference-of-squares identity",
       "We use (n−k)(n+k)=n^2−k^2 as the canonical symmetric divisor-offset mechanism. This matters because it yields an explicit factorization witness whenever representable. It turns multiplicative facts into additive geometry."),
      ("Neighbor shell (k=1)",
       "We isolate (n−1)(n+1)=n^2−1 as a universal composite generator for n>1. This matters because it shows how symmetry immediately implies compositeness near squares. It clarifies why squares attract structured composite mass."),
      ("General offset shells n^2−k^2",
       "Fixed k defines a shell family n^2−k^2. This matters because shell density is predictable and can be analyzed in log windows. Shell families decompose the composite landscape into structured layers."),
      ("Factor-pair ↔ symmetric mapping",
       "Given ab=m, half-sum and half-difference encode a difference-of-squares representation when parity matches. This matters because it converts multiplication into additive geometry. It explains why divisor offsets are genuinely symmetric algebra."),
      ("Parity constraints",
       "Same-parity factor pairs yield integer half-sum/half-diff. This matters because parity becomes a strong, cheap policy filter predicting when symmetric decompositions exist. Parity is easy to enforce and hard to fake."),
      ("Composite certificates from shells",
       "If m=n^2−k^2 with 1≤k<n then m is composite with explicit factors n−k and n+k. This matters because certificates are auditable and falsifiable. Certificates become first-class ledger objects."),
      ("Shell density vs scale",
       "Shell-generated sets up to X have predictable scaling (quadratic anchors often contribute ~√X mass). This matters because it quantifies how much composite structure is captured. Density estimates tell us what is worth enforcing."),
      ("Shell statistics in log windows",
       "We count shell hits in [X,rX] and compare across schedules. This matters because log-window invariance is our diagnostic tool. Shell statistics that drift across bases/windows are suspicious."),
      ("Shell interactions with wheel admissibility",
       "Shells and wheels are complementary: shells capture factor-pair geometry; wheels capture small-prime divisibility. This matters because combining them can be stronger than either alone, but ordering matters. Policy enforces wheel first, then shells on survivors."),
      ("Shells as structural noise reducers",
       "Shells remove deterministic composite structure so residual analysis focuses on what remains unexplained. This matters because apparent noise is often unmodeled composite structure. Removing it converts chaos into analyzable residuals."),
    ],
  },
}

KEY_FORMALISM = {
  "mean-field": ["Define mean baseline B(x) ∈ {x/ln x, Li(x)} and residual R(x)=π(x)−B(x).", "Define windowed residual R([X,rX]) and normalize by expectation ∫_X^{rX} dt/ln t."],
  "volume": ["Use u=ln x and L=ln r; represent windows as [u,u+L].", "Record coordinate gauge: base b and log gauge (ln)."],
  "policy": ["Define operator types: eliminator E, coordinate change C, heuristic probe H (must be labeled).", "Define operator ledger entry schema: inputs, params (state-governed), outputs, falsifiers."],
  "wheel": ["Choose modulus M and reduced residues R(M); admissibility is gcd(n,M)=1.", "Survivor density is φ(M)/M; compute expected survivors in (p,2p)."],
  "bound": ["Enclosure: for n>1 exists prime in (n,2n).", "Represent bound as u∈[ln p, ln p+ln 2] for p prime."],
  "shell": ["Difference-of-squares: m=n^2−k^2 ⇒ m=(n−k)(n+k).", "Certificate object: (m,n,k,factors) stored in ledger."],
}

KEY_TESTS = {
  "invariance": ["Cross-base survival: feature must persist for at least b∈{2,10} and one probe base.", "Cross-window survival: feature must persist across r∈{2,10} and one irrational probe.", "Ablation: removing operator should measurably worsen reduction/diagnostics without creating fake stability."],
  "drift": ["Scale drift: compare statistics across nested windows; flag instability beyond tolerance.", "Boundary drift: compare interior-only vs endcap-corrected measurements."],
  "false": ["False-positive control: report composites surviving eliminators.", "False-negative control: confirm that true primes are never eliminated by theorem-backed eliminators (implementation audit)."],
}

def infer_formalism(sec_title:str):
    t = sec_title.lower()
    out = []
    if "mean-field" in t or "residual" in t: out += KEY_FORMALISM["mean-field"]
    if "volume" in t or "log" in t or "window" in t or "base" in t: out += KEY_FORMALISM["volume"]
    if "policy" in t or "falsifi" in t or "scope" in t or "roadmap" in t or "notation" in t: out += KEY_FORMALISM["policy"]
    if "bound" in t or "(p,2p)" in t or "bertrand" in t or "chebyshev" in t: out += KEY_FORMALISM["bound"]
    if "wheel" in t or "residue" in t or "modulus" in t or "phi(" in t: out += KEY_FORMALISM["wheel"]
    if "shell" in t or "difference" in t or "offset" in t or "parity" in t or "certificate" in t: out += KEY_FORMALISM["shell"]
    return list(dict.fromkeys(out))[:6]  # dedupe, cap

def infer_tests(sec_title:str):
    t = sec_title.lower()
    out = []
    if any(k in t for k in ["signal", "artifact", "base", "window", "invariant", "schedule"]): out += KEY_TESTS["invariance"]
    if any(k in t for k in ["boundary", "endcap", "nest", "scale", "drift"]): out += KEY_TESTS["drift"]
    if any(k in t for k in ["falsifi", "policy", "eliminator", "wheel", "bound", "shell"]): out += KEY_TESTS["false"]
    # always at least one invariance item
    if not out: out = KEY_TESTS["invariance"][:2]
    return list(dict.fromkeys(out))[:6]

def populate(root: str, force: bool):
    part2 = os.path.join(root, "part_ii")
    for ch_num in range(1, 7):
        ch = CH[ch_num]
        ch_dir = find_dir_with_prefix(part2, f"ch_{ch_num:02d}-")
        write(os.path.join(ch_dir, "README.md"), chapter_readme(ch_num, ch["title"], ch["overview"], os.path.relpath(ch_dir, root)), force)

        # sections are ordered sec_01..sec_10
        for i, (sec_title, sec_summary) in enumerate(ch["sections"], start=1):
            sec_dir = find_dir_with_prefix(ch_dir, f"sec_{i:02d}-")
            write(os.path.join(sec_dir, "README.md"), section_readme(sec_title, i), force)

            # sub-subsections
            ov_dir = find_dir_with_prefix(sec_dir, "subsec_01-")
            fo_dir = find_dir_with_prefix(sec_dir, "subsec_02-")
            te_dir = find_dir_with_prefix(sec_dir, "subsec_03-")

            write(os.path.join(ov_dir, "README.md"), overview_subsec(sec_title, sec_summary), force)
            write(os.path.join(fo_dir, "README.md"), formalism_subsec(sec_title, infer_formalism(sec_title)), force)
            write(os.path.join(te_dir, "README.md"), tests_subsec(sec_title, infer_tests(sec_title)), force)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root", nargs="?", default="manuscript")
    ap.add_argument("--force", action="store_true", help="overwrite existing populated READMEs")
    args = ap.parse_args()
    populate(args.root, args.force)

if __name__ == "__main__":
    main()
