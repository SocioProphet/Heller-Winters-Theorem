#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import os, re, sys

GLOSSARY = Path("manuscript/part-ii-technical-core/chapters/chapter-00-claims-ledger-notation-and-the-reproducibility-standard/sections/0.10-glossary-core-terms.md")

def extract_terms(glossary_text: str) -> list[str]:
    """Extract glossary terms from common Markdown patterns.

    Supported:
      - **Term** — ..., **Term**: ..., **Term** - ...
      - - **Term**: ...   (bullet forms)
      - ## Term           (heading forms)
    """
    import re

    terms: list[str] = []
    for line in glossary_text.splitlines():
        t = line.strip()
        if not t:
            continue

        # **Term**: ... / **Term** — ... / - **Term**: ...
        m = re.match(r"^(?:[-*+]\s+)?\*\*(.+?)\*\*\s*(?:[\.:\-—]|$)", t)
        if m:
            raw = m.group(1).strip()
        else:
            # ## Term (heading-style)
            m = re.match(r"^#{2,6}\s+(.+?)\s*$", t)
            if not m:
                continue
            raw = m.group(1).strip()

        base = raw.split(" (", 1)[0].strip().rstrip(".").strip()
        if base and base not in terms:
            terms.append(base)
    return terms
def md_files(root: Path) -> list[Path]:
    return [p for p in root.rglob("*.md") if p.is_file()]

def count_term(term: str, text: str) -> int:
    # Case-insensitive literal substring match is intentional: we want practical enforcement, not regex cleverness.
    return text.lower().count(term.lower())

def main() -> int:
    if not GLOSSARY.exists():
        print(f"ERROR: glossary not found at {GLOSSARY}")
        return 2

    terms = extract_terms(GLOSSARY.read_text(encoding="utf-8"))
    if not terms:
        print("ERROR: no glossary terms detected (expected formats like: **Term**: definition, **Term** — definition, bullet **Term**, or ## Term)")
        return 2

    # Default is 1 outside usage. We can raise later by setting env var.
    min_outside = int(os.environ.get("GLOSSARY_MIN_OUTSIDE_USES", "0"))

    roots = [Path("manuscript"), Path("toc")]
    files = []
    for r in roots:
        if r.exists():
            files.extend(md_files(r))

    # Exclude the glossary file itself.
    files = [p for p in files if p.resolve() != GLOSSARY.resolve()]

    corpus = {}
    for p in files:
        try:
            corpus[p] = p.read_text(encoding="utf-8")
        except Exception:
            # Ignore unreadable files (should be rare); we don’t want silent failures, so we count them as empty.
            corpus[p] = ""

    failures = []
    for term in terms:
        outside = sum(count_term(term, txt) for txt in corpus.values())
        if outside < min_outside:
            failures.append((term, outside))

    if failures:
        print("Glossary enforcement failed:")
        print(f"- Required outside uses per term: >= {min_outside}")
        for term, outside in failures:
            print(f"  - {term!r}: outside_uses={outside}")
        print("\nRemediation rule:")
        print("- Either (a) use the term in at least one non-glossary chapter/note, or (b) remove it from the glossary.")
        return 1

    print(f"OK: glossary terms all have outside_uses >= {min_outside}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
