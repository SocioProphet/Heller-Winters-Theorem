#!/usr/bin/env python3
"""Patch residual theorem-language drift in docs/clay-problem-programme-map.md.

This is intentionally narrow: it preserves the document while correcting
programme-level phrasing after the decision to treat Heller-Winters as a
programme in search of theorem-worthy results.
"""
from pathlib import Path

PATH = Path("docs/clay-problem-programme-map.md")

REPLACEMENTS = {
    "neutral with respect to the eventual statement of the Heller–Winters Theorem":
        "neutral with respect to future Heller–Winters theorem-candidate statements",
    "the Heller–Winters Theorem itself, until and unless it is proved":
        "any Heller–Winters theorem candidate, until and unless it is proved",
    "The central theorem the construction is being assembled to state and prove is the Heller–Winters Theorem of Chapter 1; its precise formulation is the subject of ongoing research and is not committed at this stage of the draft.":
        "The programme is being assembled to discover, state, and test theorem-worthy results; no central Heller–Winters theorem is committed at this stage of the draft.",
    "What we can say now is that the theorem is expected to:":
        "What we can say now is that a future theorem-candidate track may take the following form:",
    "These describe the intended theorem form, not the theorem itself.":
        "These describe a possible theorem-candidate shape, not an existing theorem.",
    "Whether the final result reaches RH, GRH, a partial L-function result, or a non-RH envelope theorem is to be determined by what the operator stack can actually prove.":
        "Whether any future result reaches RH, GRH, a partial L-function result, or a non-RH envelope theorem is to be determined by what the operator stack can actually prove.",
    "When the central theorem is stated, it will appear at the end of Chapter 1":
        "When a theorem-candidate statement is ready, it should appear at the end of Chapter 1",
    "The eventual theorem statement should appear at the end of Chapter 1":
        "Any future theorem-candidate statement should appear at the end of Chapter 1",
    "where the work imports, what it adds, and what it does not yet claim":
        "where the programme imports, what it adds, and what it does not yet claim",
    "not as a proof of RH or GRH":
        "not as a proof of RH or GRH, and not as evidence that a Heller–Winters theorem already exists",
}

def main() -> None:
    if not PATH.exists():
        raise SystemExit(f"missing {PATH}")
    text = PATH.read_text(encoding="utf-8")
    original = text
    for src, dst in REPLACEMENTS.items():
        text = text.replace(src, dst)
    if text == original:
        print("No replacements applied; file may already be patched.")
    else:
        PATH.write_text(text, encoding="utf-8")
        print(f"Patched {PATH}")

if __name__ == "__main__":
    main()
