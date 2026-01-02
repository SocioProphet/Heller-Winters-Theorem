#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import re

ROOT = Path("manuscript/part-ii-technical-core")
CHAPTERS_DIR = ROOT / "chapters"
INTERLUDES_DIR = ROOT / "interludes"

DEFAULT_SECTION = ("section-00-overview", "Overview")
DEFAULT_SUBSECTION = ("subsection-00-overview", "Overview")

def ensure_file(path: Path, content: str) -> None:
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)

def slugify(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s

def parse_chapters_from_toc() -> list[tuple[str,str,str]]:
    """
    Returns list of (chapter_num, slug, path_hint).
    We parse toc/TOC-synthesis-v3.md for lines like:
      - Chapter 00: `manuscript/.../chapter-00-.../`
    """
    toc = Path("toc/TOC-synthesis-v3.md")
    if not toc.exists():
        return []
    text = toc.read_text(encoding="utf-8")
    out = []
    for m in re.finditer(r"-\s*Chapter\s+(\d+)\s*:\s*`([^`]+)`", text):
        num = m.group(1).zfill(2)
        path_hint = m.group(2).strip().rstrip("/")
        slug = Path(path_hint).name  # expects chapter-XX-...
        out.append((num, slug, path_hint))
    return out

def scaffold_chapter(ch_dir: Path, chapter_num: str, chapter_slug: str) -> None:
    ensure_dir(ch_dir)
    ensure_file(ch_dir / "README.md",
f"""# Chapter {chapter_num}

Status: DRAFT

## Purpose
- What this chapter is for.
- What it is *not* claiming.

## Claims ledger (A/B/C/D)
- A:
- B:
- C:
- D:

## Reproducibility
- Inputs:
- Transform(s):
- Controls (N1/N2/S1/S2/S3):
- Output artifacts:

## Local navigation
See `toc/TOC.md`.
""")
    ensure_file(ch_dir / "toc/TOC.md",
f"""# Chapter {chapter_num} — TOC

## Sections
- {DEFAULT_SECTION[1]} (`sections/{DEFAULT_SECTION[0]}/`)
""")
    sec_dir = ch_dir / "sections" / DEFAULT_SECTION[0]
    ensure_dir(sec_dir / "subsections" / DEFAULT_SUBSECTION[0])
    ensure_file(sec_dir / "README.md",
f"""# {DEFAULT_SECTION[1]}

Status: DRAFT

## What this section does
- ...

## Claims touched (A/B/C/D)
- ...
""")
    ensure_file(sec_dir / "toc/TOC.md",
f"""# {DEFAULT_SECTION[1]} — TOC

## Subsections
- {DEFAULT_SUBSECTION[1]} (`subsections/{DEFAULT_SUBSECTION[0]}/`)
""")
    sub_dir = sec_dir / "subsections" / DEFAULT_SUBSECTION[0]
    ensure_file(sub_dir / "README.md",
f"""# {DEFAULT_SUBSECTION[1]}

Status: DRAFT

## Content
- ...
""")
    ensure_file(sub_dir / "toc/TOC.md",
f"""# {DEFAULT_SUBSECTION[1]} — TOC

- Placeholder. Populate from the technical-core outline.
""")

def scaffold_interludes() -> None:
    for key, title in [("interlude-a", "Interlude A"), ("interlude-b", "Interlude B")]:
        base = INTERLUDES_DIR / key
        ensure_dir(base)
        ensure_file(base / "README.md",
f"""# {title}

Status: STRUCTURE-ONLY

Purpose: worked examples / diagnostics that we want to edit independently from chapter skeletons.
""")
        ensure_file(base / "toc/TOC.md",
f"""# {title} — TOC

- Placeholder. Link from chapter TOCs when we pin where each interlude belongs.
""")

def main() -> int:
    ensure_dir(CHAPTERS_DIR)
    chapters = parse_chapters_from_toc()

    # Fallback: if TOC isn’t listing chapters yet, we at least scaffold 00 and 01.
    if not chapters:
        chapters = [
            ("00", "chapter-00-claims-ledger-notation-and-the-reproducibility-standard", ""),
            ("01", "chapter-01-phase-definitions-from-the-log-line-to-the-circle", ""),
        ]

    for num, slug, _hint in chapters:
        # If the TOC hint already names the full slug folder, use it.
        folder = CHAPTERS_DIR / slug
        scaffold_chapter(folder, num, slug)

    scaffold_interludes()
    print(f"OK: scaffolded {len(chapters)} chapter skeleton(s) + interludes.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
