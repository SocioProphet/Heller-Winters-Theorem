from __future__ import annotations
from pathlib import Path
import re
import sys

TARGET = Path("toc/TOC-synthesis-v3.md")
V2_SRC = Path("manuscript/front-matter/INTRO-v2.md")

BEGIN = "<!-- BEGIN INTRO 1.1-1.7 (FROM V2) -->"
END   = "<!-- END INTRO 1.1-1.7 (FROM V2) -->"

def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")

def write(p: Path, s: str) -> None:
    p.write_text(s, encoding="utf-8")

def extract_v2_11_to_17(v2: str) -> str:
    """
    Extract 1.1–1.7 from v2, inclusive. Accepts both Markdown headings and plain '1.1' lines.
    We stop before '2.' (Related Work) if present, otherwise before end of file.
    """
    m11 = re.search(r"(?m)^\s*(#+\s*)?1\.1\b", v2)
    if not m11:
        raise ValueError("V2 source missing a '1.1' heading/marker.")
    start = m11.start()

    # Prefer stopping at "2." section if present.
    m2 = re.search(r"(?m)^\s*(#+\s*)?2\.\b", v2[m11.start():])
    end = (m11.start() + m2.start()) if m2 else len(v2)

    block = v2[start:end].rstrip() + "\n"
    # Sanity: ensure 1.7 exists
    if not re.search(r"(?m)^\s*(#+\s*)?1\.7\b", block):
        raise ValueError("V2 extraction did not include '1.7' (check V2 formatting).")
    return block

def ensure_intro_slot(doc: str) -> str:
    """
    Ensure TARGET has an explicit slot with anchors.
    If anchors already exist, do nothing.
    If not, insert a new '## 1. Introduction (paper-ready)' block near the end.
    """
    if BEGIN in doc and END in doc:
        return doc

    insertion = (
        "\n\n## 1. Introduction (paper-ready)\n\n"
        f"{BEGIN}\n"
        "_(inlined from `manuscript/front-matter/INTRO-v2.md` by script)_\n"
        f"{END}\n"
    )

    # Insert before EOF (append). We keep existing content intact.
    return doc.rstrip() + insertion + "\n"

def replace_between_anchors(doc: str, new_block: str) -> str:
    pattern = re.compile(
        re.escape(BEGIN) + r".*?" + re.escape(END),
        flags=re.S
    )
    if not pattern.search(doc):
        raise ValueError("Anchors not found after ensure_intro_slot().")
    return pattern.sub(lambda _m: f"{BEGIN}\n{new_block.rstrip()}\n{END}", doc, count=1)

def main() -> None:
    if not TARGET.exists():
        print(f"ERROR: missing target file: {TARGET}", file=sys.stderr)
        sys.exit(1)
    if not V2_SRC.exists():
        print(
            f"ERROR: missing v2 source file: {V2_SRC}\n"
            "Create it first (we keep it versioned so merges are mechanical).",
            file=sys.stderr
        )
        sys.exit(2)

    synth = read(TARGET)
    synth = ensure_intro_slot(synth)

    v2 = read(V2_SRC)
    v2_block = extract_v2_11_to_17(v2)

    out = replace_between_anchors(synth, v2_block)
    write(TARGET, out)

    print(f"OK: inlined v2 1.1–1.7 into {TARGET} using anchors.")

if __name__ == "__main__":
    main()
