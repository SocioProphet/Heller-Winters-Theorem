from __future__ import annotations
from pathlib import Path
import re

ROOT = Path("manuscript")

def slug(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^\w\s\-\.]+", "", s)
    s = re.sub(r"[\s\.]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s or "untitled"

def write(path: Path, content: str, overwrite: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not overwrite:
        return
    path.write_text(content, encoding="utf-8")

def toc_md(title: str, items: list[tuple[str, str]]) -> str:
    lines = [f"# {title}", ""]
    for name, rel in items:
        lines.append(f"- [{name}]({rel})")
    lines.append("")
    return "\n".join(lines)

def mk_level(dirpath: Path, title: str, toc_items: list[tuple[str, str]]) -> None:
    write(dirpath / "README.md", f"# {title}\n\n_Status: scaffold_\n", overwrite=False)
    write(dirpath / "toc" / "TOC.md", toc_md(f"TOC — {title}", toc_items), overwrite=True)

def mk_chapter(base: Path, ch_num: str, ch_title: str, sections: list[str]) -> None:
    ch_dir = base / f"chapter-{ch_num}-{slug(ch_title)}"
    sec_items: list[tuple[str, str]] = []
    for sec_title in sections:
        sec_id = sec_title.split(" ", 1)[0]  # expects "11.1 ..." etc, but works even if not
        sec_dirname = f"sec-{slug(sec_id)}-{slug(sec_title)}"
        sec_dir = ch_dir / "sections" / sec_dirname

        # one stub subsection per section (3-level invariant)
        sub_dir = sec_dir / "subsections" / f"sub-{slug(sec_id)}-1-notes"
        mk_level(sub_dir, f"{sec_title} — Notes", [])
        mk_level(sec_dir, sec_title, [(f"{sec_title} — Notes", f"subsections/{sub_dir.name}/README.md")])

        sec_items.append((sec_title, f"sections/{sec_dirname}/README.md"))

    mk_level(ch_dir, f"Chapter {ch_num} — {ch_title}", sec_items)

def main() -> None:
    # Top-level structure
    write(ROOT / "README.md",
          "# Manuscript\n\nCanonical writing tree. Draft TOCs live in /toc; canonical text lives here.\n",
          overwrite=False)

    for part in ["front-matter", "preface", "references", "part-i-history", "part-ii-technical-core"]:
        write(ROOT / part / "README.md", f"# {part}\n\n_Status: scaffold_\n", overwrite=False)

    # Part II (technical core) — we scaffold Chapter 0, 1, and 11–33
    part2 = ROOT / "part-ii-technical-core"

    ch00_sections = [
        "0.1 Why This Chapter Exists",
        "0.2 The Four Bins",
        "0.3 Minimal Notation",
        "0.4 The Prime-to-Geometry Template",
        "0.5 What We Claim in This Book",
        "0.6 Reproducibility Contract",
        "0.7 Controls, Null Models, and Stress Tests",
        "0.8 The Claims Ledger Table",
        "0.9 Transition",
    ]
    mk_chapter(part2, "00", "Claims Ledger, Notation, and the Reproducibility Standard", ch00_sections)

    ch01_sections = [
        "1.1 The Phase Pipeline (canonical)",
        "1.2 Base Phase Families",
        "1.3 Hyperbolic Coupling Layer (bridge operator)",
        "1.4 The Winters Log-Circle Instrument (credited visualization step)",
        "1.5 The Explicit Phase Equation Slot (verbatim insertion point)",
        "1.6 Validation Checklist (applied to every phase equation)",
        "1.7 Immediate Experiments (what we run first)",
        "1.8 Transition",
    ]
    mk_chapter(part2, "01", "Phase Definitions: From the Log Line to the Circle", ch01_sections)

    chapters_11_33 = {
        "11": ("Purpose and Thesis", [
            "11.1 Mean-field vs fluctuation decomposition",
            "11.2 Volume not distance (log-volume invariance)",
            "11.3 Policy-enforced inference vs brute search",
            "11.4 Signal vs artifact (cross-base/cross-schedule invariance)",
            "11.5 Determinism vs fitted parameters (state-governed only)",
            "11.6 Falsifiability criteria (operator-level)",
            "11.7 Scope limits and non-claims",
            "11.8 Canonical notation + coordinate commitments",
            "11.9 Relationship to classical theorems (baselines + guardrails)",
        ]),
        "12": ("Canonical Coordinate System", [
            "12.1 u = ln x; x = e^u",
            "12.2 Multiplicative windows; L = ln r",
            "12.3 Change-of-base as frequency rescaling",
            "12.4 Volume element compatibility (dt/ln t)",
            "12.5 Anchors (r=2, r=10) + interpretability",
            "12.6 Irrational probes as de-aliasing stress tests",
            "12.7 Index vs value vs policy state discipline",
            "12.8 Nesting/multiresolution schedules",
            "12.9 Boundary effects and endcaps",
            "12.10 Units/normalization/invariance",
        ]),
        "13": ("Prime Density Mean-Field Model", [
            "13.1 π(x) ~ x/ln x baseline",
            "13.2 Local intensity ~ 1/ln x",
            "13.3 Window expectation ∫ dt/ln t",
            "13.4 Gap scale ~ ln x",
            "13.5 Regimes + drift + variance posture",
            "13.6 Residual definition and guardrails",
            "13.7 Mean-field invariants used by policy",
        ]),
        "14": ("Boundedness Layer", [
            "14.1 Bertrand/Chebyshev enclosure (n,2n)",
            "14.2 Next-prime enclosure (p,2p)",
            "14.3 Complexity baseline + bound-sensitive scoring",
            "14.4 Interaction with wheel selection",
            "14.5 Nested bounds across ratios",
            "14.6 Log-cell representation",
            "14.7 Failure modes + evaluation harness",
        ]),
        "15": ("Wheel Sieve Layer", [
            "15.1 Modulus design; reduced residues; φ(M)/M density",
            "15.2 Residue state machines and features",
            "15.3 Depth vs cost tradeoff",
            "15.4 Resonance hazards with base partitions",
            "15.5 Lattice-safe governance for periodic compartments",
            "15.6 Cross-window invariants",
        ]),
        "16": ("Symmetric Offset Algebra", [
            "16.1 Difference-of-squares families; shells; parity constraints",
            "16.2 Composite certificates as ledger objects",
            "16.3 Shell statistics in log windows",
            "16.4 Wheel + shell interaction; structural noise reduction",
        ]),
        "17": ("Figurate Number Lattices", [
            "17.1 Triangular/polygonal scaffolds",
            "17.2 Second differences and curvature cues",
            "17.3 Index/value discipline",
            "17.4 sqrt(X) laws and scaling posture",
            "17.5 Offset maps and residue intersections",
            "17.6 Congruence constraints",
            "17.7 Density contrasts + audit summaries",
        ]),
        "18": ("Base-(b) Compartmentalization", [
            "18.1 Digit orbits",
            "18.2 Carry coupling",
            "18.3 Base invariance",
            "18.4 Repeating expansions",
            "18.5 Resonance management",
            "18.6 Cross-base consensus",
            "18.7 Artifact tests",
            "18.8 Base-agnostic representations",
            "18.9 Zeckendorf compartment as third triangulation axis",
        ]),
        "19": ("(p)-Adic Structure Layer", [
            "19.1 Valuations",
            "19.2 (p)-adic balls",
            "19.3 Depth schedules",
            "19.4 Filter vs feature",
            "19.5 Lifting logic",
            "19.6 Wheel/shell interaction",
            "19.7 Quotient conditioning",
            "19.8 Drift control",
            "19.9 Computation patterns",
            "19.10 Triangulation with base-(b) and Zeckendorf",
        ]),
        "20": ("Quotient Functions and Normalization", [
            "20.1 Windowed quotients",
            "20.2 Li/Chebyshev normalizations",
            "20.3 Conditioned quotients",
            "20.4 Robust denominators",
            "20.5 Schedule stability",
            "20.6 Boundary correction integration",
            "20.7 Aggregation rules",
            "20.8 Diagnostics",
        ]),
        "21": ("Euler–Mascheroni Calibration (γ)", [
            "21.1 γ definition",
            "21.2 Harmonic vs log",
            "21.3 Calibration role",
            "21.4 Error floors",
            "21.5 Quotient interaction",
            "21.6 Ledger placement",
            "21.7 Misuse prevention",
        ]),
        "22": ("Euler–Maclaurin Bridge", [
            "22.1 Sum↔integral map",
            "22.2 Boundary terms",
            "22.3 Curvature corrections",
            "22.4 Bernoulli structure",
            "22.5 Window approximations",
            "22.6 Error accounting",
            "22.7 Link to γ",
            "22.8 Mean/residual separation",
        ]),
        "23": ("Ratio Families as Window Schedules", [
            "23.1 Anchors 2/10",
            "23.2 Irrational probes",
            "23.3 De-aliasing",
            "23.4 Continued fractions",
            "23.5 Nesting",
            "23.6 Ratio mixing constraints",
            "23.7 Consensus tests",
            "23.8 Sensitivity diagnostics",
            "23.9 Governance boundaries",
            "23.10 Ratio bans",
        ]),
        "24": ("Ordering and Governance of Ratio Application", [
            "24.1 Tiering",
            "24.2 Add/prune rules",
            "24.3 Overfit prevention",
            "24.4 Conflict resolution",
            "24.5 Aggregation",
            "24.6 Stability thresholds",
            "24.7 Complexity budgeting",
            "24.8 Audit templates",
        ]),
        "25": ("Harmonic Signature Formalism", [
            "25.1 Log-harmonics",
            "25.2 cos/sin basis",
            "25.3 Coherence metrics",
            "25.4 Window fingerprints",
            "25.5 Mixers",
            "25.6 Base invariance",
            "25.7 Ledger mapping",
            "25.8 Signal criteria",
        ]),
        "26": ("Identity Channels (circular vs hyperbolic)", [
            "26.1 Circular vs hyperbolic channels",
            "26.2 Projections",
            "26.3 Off-channel residuals",
            "26.4 Mixer constraints",
            "26.5 Artifact rejection",
            "26.6 Persistence tests",
            "26.7 Ledger spec",
        ]),
        "27": ("RH-Consistent Envelope Constraint (policy lens; not proof)", [
            "27.1 ρ=β+iγ notation",
            "27.2 x^ρ decomposition",
            "27.3 Envelope meaning of β=1/2",
            "27.4 Envelope measurement",
            "27.5 Drift tests",
            "27.6 Stability checks",
            "27.7 Failure signatures",
            "27.8 Policy use (not proof)",
        ]),
        "28": ("Explicit Phase-Selection Operator (Cosine Phase-Gate)", [
            "28.1 Canonical transcription",
            "28.2 State-governed parameters (no free knobs)",
            "28.3 Sector quantization under lattice-safe governance",
            "28.4 The (90/11) normalization component (documented, testable)",
            "28.5 Hit conditions and tolerances",
            "28.6 Ablations: on/off and tolerance sweeps",
            "28.7 Cross-base survival requirement",
            "28.8 Cross-window survival requirement",
            "28.9 Circular-channel integration",
            "28.10 Falsifiers and failure taxonomy",
        ]),
        "29": ("Structural Sieves Beyond the Wheel", [
            "29.1 shell/parity/residue/figurate/digit/p-adic exclusions",
            "29.2 mixed ordering",
            "29.3 depth accounting",
            "29.4 certificates",
            "29.5 benchmarks",
        ]),
        "30": ("Optimization View", [
            "30.1 CSP framing",
            "30.2 multiobjective structure",
            "30.3 regularizers",
            "30.4 residual minimization objective",
            "30.5 budgets",
            "30.6 sensitivity analysis",
            "30.7 failure surfaces",
            "30.8 harness",
        ]),
        "31": ("Classical Theorems as Policy Operators", [
            "31.1 Euclid/Dirichlet/Chebyshev baselines",
            "31.2 Wilson",
            "31.3 Fermat/Euler tests",
            "31.4 CRT",
            "31.5 quadratic residues",
            "31.6 labeled heuristic influences",
            "31.7 misuse warnings",
            "31.8 ledger integration",
        ]),
        "32": ("Evidence Ledger and Falsification Protocol", [
            "32.1 prediction events",
            "32.2 FP/FN",
            "32.3 drift tests (scale/base/p-adic)",
            "32.4 residual thresholds",
            "32.5 ablations",
            "32.6 failure taxonomy",
            "32.7 audit trails",
        ]),
        "33": ("Consolidated Spec and Extensions", [
            "33.1 one-page executable spec",
            "33.2 data structures",
            "33.3 governance",
            "33.4 complexity accounting",
            "33.5 claims taxonomy",
            "33.6 constellations",
            "33.7 prime powers",
            "33.8 psi-residuals",
            "33.9 lattice counting/Ehrhart modules",
            "33.10 research map",
        ]),
    }

    for num, (title, sections) in chapters_11_33.items():
        mk_chapter(part2, num, title, sections)

if __name__ == "__main__":
    main()
