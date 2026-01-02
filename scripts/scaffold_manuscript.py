#!/usr/bin/env python3
import os, re, argparse
from datetime import date

TODAY = str(date.today())

def slug(s: str) -> str:
    s = s.lower()
    s = s.replace("ψ", "psi").replace("π", "pi").replace("γ", "gamma").replace("ρ", "rho")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s or "untitled"

def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

def write_file(path: str, content: str, force: bool):
    if os.path.exists(path) and not force:
        return False
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return True

def mk_readme(kind: str, title: str, rel: str) -> str:
    return f"""# {title}

## Purpose
(Define what this {kind} is responsible for.)

## Scope / Non-scope
- In scope:
- Out of scope:

## Inputs / Dependencies
- Upstream references:
- Required definitions / lemmas:
- Required datasets / plots:

## Outputs / Artifacts
- Expected deliverables (figures, tables, proofs, code, etc.):

## Open Questions / Risks
- 

## Change Log
- {TODAY}: scaffold created ({rel})
"""

def mk_toc(title: str, items: list[str]) -> str:
    lines = [f"# {title}", ""]
    for it in items:
        lines.append(f"- {it}")
    lines.append("")
    return "\n".join(lines)

DEFAULT_SUBSECTIONS = [
    ("01", "Overview"),
    ("02", "Formalism"),
    ("03", "Tests + Ledger"),
]

# ----------------------------
# Book spec (v4 synthesis spine)
# ----------------------------

FRONT_MATTER = [
    "Title Page",
    "Copyright",
    "Author’s Introduction (God-only dedication; canonical)",
    "Preface (canonical prime-history + collaborator credits; canonical)",
    "Acknowledgments",
    "Author Contributions Ledger",
    "Notation, Conventions, and Operator Legend",
    "Reader’s Map",
]

PART_I = [
    (1, "Zero, Representation, and the Birth of Number as Structure"),
    (2, "Euclid and the First Invariants (infinitude; proof posture)"),
    (3, "Eratosthenes and Sieve Thinking (elimination as computation)"),
    (4, "Euler: Products, Series, and the Analytic Doorway"),
    (5, "Gauss, Legendre, and the Mean-Field Law (density as geometry)"),
    (6, "Dirichlet: Progressions and Residue-Class Symmetry"),
    (7, "Chebyshev: Universal Enclosures and First Practical Bounds"),
    (8, "Riemann: Explicit Formula, Zeta Zeros, Log-Scale Oscillation"),
    (9, "Hardy–Littlewood: Constellations, Heuristics, and Correlation"),
    (10, "Modern Sieves and Breakthroughs (tooling limits, what remains hard)"),
]

# Part II chapters 1–23 with section (subtopic) lists
PART_II = [
    (1, "Purpose and Thesis", [
        "Mean-field vs fluctuation decomposition",
        "Volume-not-distance invariant",
        "Policy inference vs brute search",
        "Signal vs artifact invariance",
        "Determinism vs tuning",
        "Falsifiability criteria",
        "Scope limits and non-claims",
        "Canonical notation",
        "Relation to classical theorems",
        "Full-stack roadmap",
    ]),
    (2, "Canonical Coordinate System", [
        "u = ln x",
        "Multiplicative windows and L = ln r",
        "Base change as frequency rescaling",
        "Volume element and expectation compatibility",
        "Anchor schedules (2, 10)",
        "Irrational probes (metallic/plastic) as de-aliasing",
        "Index/value/policy-space discipline",
        "Nesting and multi-resolution schedules",
        "Boundary effects and endcaps",
        "Normalization and invariance",
    ]),
    (3, "Prime Density Mean-Field Model", [
        "pi(x) ~ x/ln x baseline",
        "Local intensity ~ 1/ln x",
        "Window expectation integral",
        "Decade vs octave calibration",
        "Drift in 1/u",
        "Coverage interpretation",
        "Average gap ~ ln x",
        "Variance posture",
        "Scaling regimes",
        "Mean-field invariants used by policy",
    ]),
    (4, "Boundedness Layer (unconditional enclosure)", [
        "Bertrand/Chebyshev enclosure (n, 2n)",
        "Specialization to (p, 2p)",
        "Complexity baseline",
        "Wheel selection coupling",
        "Nested bounds across ratios",
        "Log-cell representation",
        "Practical metrics",
        "Failure modes",
        "Bound-sensitive scoring",
        "Evaluation harness",
    ]),
    (5, "Wheel Sieve Layer + Periodic-State Governance", [
        "Modulus design",
        "Reduced residues",
        "Survivor density phi(M)/M",
        "Residue-state transitions",
        "Depth vs cost",
        "Resonance hazards with base partitions",
        "Crystallographic/lattice-safe governance for periodic compartments",
        "Wheel as eliminator vs feature generator",
        "Cross-window invariants",
        "Audit checks",
    ]),
    (6, "Symmetric Offset Algebra (shells + certificates)", [
        "Difference-of-squares",
        "Neighbor shell",
        "General shells",
        "Factor-pair mapping",
        "Parity constraints",
        "Composite certificates as ledger objects",
        "Shell density scaling",
        "Log-window shell stats",
        "Wheel+shell ordering",
        "Structural noise reduction",
    ]),
    (7, "Figurate Number Lattices (quadratic scaffolds)", [
        "Triangular/polygonal families",
        "Second differences",
        "sqrt(X) counting",
        "Offset maps",
        "Scaffold exclusions",
        "Residue intersections",
        "Congruence constraints",
        "Density contrasts",
        "Audit summaries",
        "Failure modes",
    ]),
    (8, "Compartmentalization Across Encodings (base-b + Zeckendorf)", [
        "Digit orbits",
        "Carry coupling",
        "Repeating expansions as modular-order features",
        "Resonance management with wheels",
        "Cross-base consensus tests",
        "Zeckendorf compartments (third axis)",
        "Base-agnostic feature definitions",
        "Artifact tests",
        "Boundary interactions",
        "Audit obligations",
    ]),
    (9, "p-adic Structure Layer", [
        "Valuations",
        "p-adic balls",
        "Depth schedules",
        "Filter vs feature",
        "Lifting logic",
        "Wheel/shell interactions",
        "Quotient conditioning",
        "Drift control",
        "Computation patterns",
        "Triangulation with base-b and Zeckendorf",
    ]),
    (10, "Quotient Functions and Normalization", [
        "Windowed quotients",
        "Li/Chebyshev normalizations",
        "Conditioned quotients",
        "Robust denominators",
        "Schedule stability",
        "Boundary correction integration",
        "Aggregation rules",
        "Diagnostics",
        "Invariants",
        "Falsifiers",
    ]),
    (11, "Euler–Mascheroni Calibration (gamma)", [
        "Definition",
        "Harmonic vs log",
        "Calibration role",
        "Error floors",
        "Quotient interactions",
        "Ledger placement",
        "Misuse prevention",
        "Boundary coupling",
        "Stability tests",
        "Audit rules",
    ]),
    (12, "Euler–Maclaurin Bridge (sum ↔ integral)", [
        "Boundary terms",
        "Curvature corrections",
        "Bernoulli structure",
        "Window approximations",
        "Error accounting",
        "Link to gamma",
        "Mean/residual separation",
        "Endcap governance",
        "Diagnostic templates",
        "Falsifiers",
    ]),
    (13, "Ratio Families as Window Schedules", [
        "Anchors 2/10",
        "Irrational probes",
        "De-aliasing",
        "Continued fractions",
        "Nesting",
        "Ratio mixing constraints",
        "Consensus tests",
        "Sensitivity diagnostics",
        "Governance boundaries",
        "Ratio bans",
    ]),
    (14, "Governance of Ratio Application (anti-overfit)", [
        "Tiering",
        "Add/prune rules",
        "Overfit prevention",
        "Conflict resolution",
        "Aggregation",
        "Stability thresholds",
        "Complexity budgeting",
        "Audit templates",
        "Ablation schedules",
        "Drift dashboards",
    ]),
    (15, "Harmonic Signature Formalism (log-harmonics)", [
        "Log-harmonics",
        "Cos/sin decomposition",
        "Coherence",
        "Window fingerprints",
        "Mixers",
        "Base invariance",
        "Ledger mapping",
        "Signal criteria",
        "Aliasing tests",
        "Falsifiers",
    ]),
    (16, "Identity Channels (circular vs hyperbolic)", [
        "Channel definitions",
        "Projections",
        "Off-channel residuals",
        "Mixer constraints",
        "Artifact rejection",
        "Persistence tests",
        "Envelope/phase separation",
        "Ledger spec",
        "Diagnostic thresholds",
        "Failure modes",
    ]),
    (17, "RH-Consistent Envelope Constraint (policy lens, not proof)", [
        "rho = beta + i*gamma",
        "x^rho decomposition",
        "beta=1/2 as envelope constraint",
        "Envelope measurement",
        "Drift tests",
        "Stability regimes",
        "Failure signatures",
        "Scoring guidance",
        "Audit rules",
        "Non-claim boundary",
    ]),
    (18, "Explicit Phase-Selection Operator (Cosine Phase-Gate)", [
        "Canonical transcription",
        "State-governed parameters (no free knobs)",
        "Sector quantization under lattice-safe governance",
        "90/11 normalization component (explicit, testable)",
        "Hit/tolerance definitions",
        "Ablations",
        "Cross-base survival",
        "Cross-window survival",
        "Circular-channel integration",
        "Falsifiers",
    ]),
    (19, "Structural Sieves Beyond the Wheel", [
        "Shell/parity/residue/figurate/digit/p-adic exclusions",
        "Mixed ordering",
        "Depth accounting",
        "Certificates",
        "Benchmarks",
        "Conservatism tradeoffs",
        "Performance metrics",
        "Audit surfaces",
        "Failure modes",
        "Invariance checks",
    ]),
    (20, "Optimization View (policy as constraint system)", [
        "CSP framing",
        "Hard vs soft",
        "Multiobjective",
        "Regularizers (ratio/base/p-adic/Zeckendorf)",
        "Residual-minimization objective",
        "Budgets",
        "Sensitivity analysis",
        "Failure surfaces",
        "Harness design",
        "Audit outputs",
    ]),
    (21, "Classical Theorems as Policy Operators", [
        "Euclid/Dirichlet/Chebyshev baselines",
        "Wilson as certification benchmark",
        "Fermat/Euler tests",
        "CRT combiners",
        "Quadratic residues",
        "Labeled heuristic influences",
        "Misuse warnings",
        "Ledger integration",
        "Invariance constraints",
        "Falsifiers",
    ]),
    (22, "Evidence Ledger and Falsification Protocol", [
        "Prediction events",
        "FP/FN",
        "Drift tests (scale/base/p-adic/Zeckendorf)",
        "Residual thresholds",
        "Ablations",
        "Failure taxonomy",
        "Audit trails",
        "Replication checklist",
        "Novelty criteria",
        "Reporting format",
    ]),
    (23, "Consolidated Spec + Extensions", [
        "One-page spec",
        "Data structures",
        "Governance",
        "Complexity accounting",
        "Claims taxonomy",
        "Constellations",
        "Prime powers",
        "Psi-residuals",
        "Lattice counting/Ehrhart modules",
        "Research map",
    ]),
]

INTERLUDES = [
    ("A", "Worked Example (Enclosure → Wheel → Shells)", [
        "Candidate counts after each eliminator",
        "Ledger entry schema",
        "Failure classification example",
    ]),
    ("B", "Worked Example (Phase-Gate Ablation + Ledger)", [
        "On/off comparisons + tolerance sweeps",
        "Drift classification",
        "Failure narrative templates",
    ]),
]

APPENDICES = [
    ("A", "Prime Milestones Timeline"),
    ("B", "Operator Genealogy"),
    ("C", "Ledger Templates"),
    ("D", "Data Structures & Schemas"),
    ("E", "Reproducibility Checklist"),
    ("F", "Glossary"),
    ("G", "Index"),
]

def scaffold(args):
    root = args.root
    force = args.force

    ensure_dir(root)

    # Root README/TOC
    write_file(os.path.join(root, "README.md"),
               mk_readme("root", "Manuscript Workspace", "manuscript/README.md"),
               force=False)
    write_file(os.path.join(root, "TOC.md"),
               mk_toc("Manuscript TOC", [
                   "front_matter/",
                   "part_i/",
                   "part_ii/",
                   "appendices/",
               ]),
               force=False)

    # Front matter
    fm_dir = os.path.join(root, "front_matter")
    ensure_dir(fm_dir)
    fm_items = []
    for i, title in enumerate(FRONT_MATTER, start=1):
        d = os.path.join(fm_dir, f"{i:02d}-{slug(title)}")
        ensure_dir(d)
        fm_items.append(os.path.basename(d) + "/")
        write_file(os.path.join(d, "README.md"),
                   mk_readme("front-matter item", title, os.path.relpath(d, root)),
                   force)
        write_file(os.path.join(d, "TOC.md"),
                   mk_toc(title + " — TOC", []),
                   force)

    write_file(os.path.join(fm_dir, "README.md"),
               mk_readme("folder", "Front Matter", os.path.relpath(fm_dir, root)),
               force=False)
    write_file(os.path.join(fm_dir, "TOC.md"),
               mk_toc("Front Matter — TOC", fm_items),
               force=False)

    # Part I
    p1 = os.path.join(root, "part_i")
    ensure_dir(p1)
    p1_items = []
    for n, title in PART_I:
        ch = os.path.join(p1, f"ch_{n:02d}-{slug(title)}")
        ensure_dir(ch)
        p1_items.append(os.path.basename(ch) + "/")

        # We don’t have subtopics enumerated here; create three canonical sections.
        sections = [("01", "Overview"), ("02", "Operator genealogy"), ("03", "Notes + sources")]
        sec_dirs = []
        for sn, st in sections:
            sd = os.path.join(ch, f"sec_{sn}-{slug(st)}")
            ensure_dir(sd)
            sec_dirs.append(os.path.basename(sd) + "/")
            write_file(os.path.join(sd, "README.md"),
                       mk_readme("section", f"{st}", os.path.relpath(sd, root)),
                       force)
            # Default subsections
            sub_items = []
            for subn, subt in DEFAULT_SUBSECTIONS:
                subd = os.path.join(sd, f"subsec_{subn}-{slug(subt)}")
                ensure_dir(subd)
                sub_items.append(os.path.basename(subd) + "/")
                write_file(os.path.join(subd, "README.md"),
                           mk_readme("subsection", subt, os.path.relpath(subd, root)),
                           force)
                write_file(os.path.join(subd, "TOC.md"),
                           mk_toc(subt + " — TOC", []),
                           force)
            write_file(os.path.join(sd, "TOC.md"),
                       mk_toc(st + " — TOC", sub_items),
                       force)

        write_file(os.path.join(ch, "README.md"),
                   mk_readme("chapter", f"Part I — Chapter {n}: {title}", os.path.relpath(ch, root)),
                   force=False)
        write_file(os.path.join(ch, "TOC.md"),
                   mk_toc(f"Chapter {n} — TOC", sec_dirs),
                   force)

    write_file(os.path.join(p1, "README.md"),
               mk_readme("part", "Part I — Ancestry of Constraints", os.path.relpath(p1, root)),
               force=False)
    write_file(os.path.join(p1, "TOC.md"),
               mk_toc("Part I — TOC", p1_items),
               force=False)

    # Part II
    p2 = os.path.join(root, "part_ii")
    ensure_dir(p2)
    p2_items = []

    # Interludes folder
    inter_dir = os.path.join(p2, "interludes")
    ensure_dir(inter_dir)

    for n, title, sections in PART_II:
        ch = os.path.join(p2, f"ch_{n:02d}-{slug(title)}")
        ensure_dir(ch)
        p2_items.append(os.path.basename(ch) + "/")

        sec_dirs = []
        for idx, sec_title in enumerate(sections, start=1):
            sd = os.path.join(ch, f"sec_{idx:02d}-{slug(sec_title)}")
            ensure_dir(sd)
            sec_dirs.append(os.path.basename(sd) + "/")

            write_file(os.path.join(sd, "README.md"),
                       mk_readme("section", sec_title, os.path.relpath(sd, root)),
                       force)

            # Subsections under each section
            sub_items = []
            for subn, subt in DEFAULT_SUBSECTIONS:
                subd = os.path.join(sd, f"subsec_{subn}-{slug(subt)}")
                ensure_dir(subd)
                sub_items.append(os.path.basename(subd) + "/")
                write_file(os.path.join(subd, "README.md"),
                           mk_readme("subsection", subt, os.path.relpath(subd, root)),
                           force)
                write_file(os.path.join(subd, "TOC.md"),
                           mk_toc(subt + " — TOC", []),
                           force)

            write_file(os.path.join(sd, "TOC.md"),
                       mk_toc(sec_title + " — TOC", sub_items),
                       force)

        write_file(os.path.join(ch, "README.md"),
                   mk_readme("chapter", f"Part II — Chapter {n}: {title}", os.path.relpath(ch, root)),
                   force=False)
        write_file(os.path.join(ch, "TOC.md"),
                   mk_toc(f"Chapter {n} — TOC", sec_dirs),
                   force)

    # Interludes
    inter_items = []
    for tag, title, bullets in INTERLUDES:
        d = os.path.join(inter_dir, f"interlude_{tag.lower()}-{slug(title)}")
        ensure_dir(d)
        inter_items.append(os.path.basename(d) + "/")
        write_file(os.path.join(d, "README.md"),
                   mk_readme("interlude", f"Interlude {tag} — {title}", os.path.relpath(d, root)),
                   force=False)
        write_file(os.path.join(d, "TOC.md"),
                   mk_toc(f"Interlude {tag} — TOC", [f"- {b}" for b in bullets]),
                   force)

    write_file(os.path.join(inter_dir, "README.md"),
               mk_readme("folder", "Interludes", os.path.relpath(inter_dir, root)),
               force=False)
    write_file(os.path.join(inter_dir, "TOC.md"),
               mk_toc("Interludes — TOC", inter_items),
               force=False)

    write_file(os.path.join(p2, "README.md"),
               mk_readme("part", "Part II — The Heller–Winters Construction", os.path.relpath(p2, root)),
               force=False)
    write_file(os.path.join(p2, "TOC.md"),
               mk_toc("Part II — TOC", p2_items + ["interludes/"]),
               force=False)

    # Appendices
    app = os.path.join(root, "appendices")
    ensure_dir(app)
    app_items = []
    for tag, title in APPENDICES:
        d = os.path.join(app, f"app_{tag.lower()}-{slug(title)}")
        ensure_dir(d)
        app_items.append(os.path.basename(d) + "/")
        write_file(os.path.join(d, "README.md"),
                   mk_readme("appendix", f"Appendix {tag} — {title}", os.path.relpath(d, root)),
                   force=False)
        write_file(os.path.join(d, "TOC.md"),
                   mk_toc(f"Appendix {tag} — TOC", []),
                   force)

    write_file(os.path.join(app, "README.md"),
               mk_readme("folder", "Appendices", os.path.relpath(app, root)),
               force=False)
    write_file(os.path.join(app, "TOC.md"),
               mk_toc("Appendices — TOC", app_items),
               force=False)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="manuscript", help="root folder for manuscript scaffold")
    ap.add_argument("--force", action="store_true", help="overwrite existing README.md/TOC.md skeletons")
    args = ap.parse_args()
    scaffold(args)

if __name__ == "__main__":
    main()
