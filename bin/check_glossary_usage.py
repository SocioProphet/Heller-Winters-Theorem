#!/usr/bin/env python3
"""Glossary enforcement tool.

Checks that every term defined in the canonical glossary is used at least
--min-outside N times in the non-glossary manuscript corpus.

Exit codes:
  0 - all terms pass
  1 - one or more terms fail (only when --strict or min_outside > 0)
  2 - configuration error (missing glossary, no terms found)
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

GLOSSARY = Path(
    "manuscript/part-ii-technical-core/chapters/"
    "chapter-00-claims-ledger-notation-and-the-reproducibility-standard/"
    "sections/0.10-glossary-core-terms.md"
)


def normalize_term(raw: str) -> str:
    r"""Strip LaTeX math delimiters and collapse whitespace for comparison.

    Transformations:
      1. Strip \( ... \) delimiters, keep inner content.
      2. Strip $...$ delimiters, keep inner content.
      3. Collapse whitespace.
    """
    text = re.sub(r"\\\((.+?)\\\)", r"\1", raw)
    text = re.sub(r"\$(.+?)\$", r"\1", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def extract_terms(glossary_text: str) -> list[str]:
    """Extract and normalize glossary terms from Markdown patterns.

    Supported:
      - **Term**: ..., **Term** - ..., **Term** -- ...
      - - **Term**: ...   (bullet forms)
      - ## Term / ### Term  (heading forms)
    """
    terms: list[str] = []
    for line in glossary_text.splitlines():
        t = line.strip()
        if not t:
            continue

        m = re.match(r"^(?:[-*+]\s+)?\*\*(.+?)\*\*\s*(?:[.:\-]|$)", t)
        if m:
            raw = m.group(1).strip()
        else:
            m = re.match(r"^#{2,6}\s+(.+?)\s*$", t)
            if not m:
                continue
            raw = m.group(1).strip()

        base = raw.split(" (", 1)[0].strip().rstrip(".").strip()
        normalized = normalize_term(base)
        if normalized and normalized not in terms:
            terms.append(normalized)
    return terms


def md_files(root: Path) -> list[Path]:
    return [p for p in root.rglob("*.md") if p.is_file()]


def count_term(term: str, text: str) -> int:
    """Case-insensitive substring count of normalized term in normalized text."""
    return normalize_term(text).lower().count(normalize_term(term).lower())


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--min-outside",
        type=int,
        default=None,
        metavar="N",
        help=(
            "Minimum outside uses required per term. "
            "Overrides GLOSSARY_MIN_OUTSIDE_USES env var. Default: 0."
        ),
    )
    path_group = parser.add_mutually_exclusive_group()
    path_group.add_argument(
        "--show-path",
        action="store_true",
        help="Print the resolved glossary file path and exit.",
    )
    path_group.add_argument(
        "--print-glossary-path",
        action="store_true",
        help="Alias for --show-path.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help=(
            "Fail (exit 1) if any term has zero outside uses, regardless of "
            "--min-outside. Equivalent to --min-outside 1 when min_outside < 1."
        ),
    )
    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.show_path or args.print_glossary_path:
        print(GLOSSARY.resolve())
        return 0

    if not GLOSSARY.exists():
        print(f"ERROR: glossary not found at {GLOSSARY}")
        return 2

    terms = extract_terms(GLOSSARY.read_text(encoding="utf-8"))
    if not terms:
        print(
            "ERROR: no glossary terms detected "
            "(expected: **Term**: definition, ## Term, etc.)"
        )
        return 2

    if args.min_outside is not None:
        min_outside = args.min_outside
    else:
        min_outside = int(os.environ.get("GLOSSARY_MIN_OUTSIDE_USES", "0"))

    if args.strict and min_outside < 1:
        min_outside = 1

    roots = [Path("manuscript"), Path("toc")]
    files: list[Path] = []
    for r in roots:
        if r.exists():
            files.extend(md_files(r))

    files = [p for p in files if p.resolve() != GLOSSARY.resolve()]

    corpus: dict[Path, str] = {}
    for fp in files:
        try:
            corpus[fp] = fp.read_text(encoding="utf-8")
        except Exception:
            corpus[fp] = ""

    failures: list[tuple[str, int]] = []
    for term in terms:
        outside = sum(count_term(term, txt) for txt in corpus.values())
        if outside < min_outside:
            failures.append((term, outside))

    if failures:
        print("Glossary enforcement failed:")
        print(f"  Required outside uses per term: >= {min_outside}")
        for term, outside in failures:
            print(f"  - {term!r}: outside_uses={outside}")
        print()
        print("Remediation:")
        print(
            "  (a) Use the term in at least one non-glossary chapter/note, or "
            "(b) remove it from the glossary."
        )
        return 1

    print(f"OK: all {len(terms)} glossary terms have outside_uses >= {min_outside}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
