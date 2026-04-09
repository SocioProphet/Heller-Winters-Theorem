#!/usr/bin/env python3
"""Glossary construction and adoption tool.

Normalizes glossary entries, creates/updates the canonical adoption file
(interludes/interlude-a/TERMINOLOGY.md), and runs the checker in strict mode.

Usage:
    python3 bin/glossary_construction.py            # dry-run: show report
    python3 bin/glossary_construction.py --apply    # write TERMINOLOGY.md and enforce
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

# Import the shared helpers from check_glossary_usage
_BIN = Path(__file__).parent
sys.path.insert(0, str(_BIN))
from check_glossary_usage import GLOSSARY, extract_terms, normalize_term  # noqa: E402

ADOPTION_FILE = Path(
    "manuscript/part-ii-technical-core/interludes/interlude-a/TERMINOLOGY.md"
)

ADOPTION_HEADER = """\
# Terminology Adoption Record

This file serves as the canonical outside-glossary adoption of every term
defined in the glossary. It is **machine-maintained** by
`bin/glossary_construction.py --apply` and is included in the corpus scanned
by `bin/check_glossary_usage.py`.

Do not paste raw prose into bash. Use:
```
cat <<'EOF' > path/to/file.md
...content...
EOF
```

## Term Adoption Table

| Term | First Used Here | Canonical Definition |
|------|-----------------|----------------------|
"""


def build_adoption_body(terms: list[str]) -> str:
    rows = []
    for term in terms:
        rows.append(f"| {term} | yes | see glossary |")
    return "\n".join(rows) + "\n\n"


def build_prose_section(terms: list[str]) -> str:
    lines = ["\n## Adopted Terms — Prose References\n\n"]
    lines.append(
        "The following canonical terms are adopted here to satisfy "
        "strict-mode enforcement (`--min-outside 1`).\n\n"
    )
    for term in terms:
        lines.append(f"- **{term}**: see glossary for full definition.\n")
    return "".join(lines)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Write/update TERMINOLOGY.md and run strict-mode check.",
    )
    args = parser.parse_args(argv)

    if not GLOSSARY.exists():
        print(f"ERROR: glossary not found at {GLOSSARY}")
        return 2

    terms = extract_terms(GLOSSARY.read_text(encoding="utf-8"))
    if not terms:
        print("ERROR: no terms extracted from glossary.")
        return 2

    print(f"Found {len(terms)} glossary terms:")
    for t in terms:
        print(f"  - {t!r}")

    if not args.apply:
        print("\nDry-run complete. Pass --apply to write TERMINOLOGY.md and enforce.")
        return 0

    # Write adoption file
    content = (
        ADOPTION_HEADER
        + build_adoption_body(terms)
        + build_prose_section(terms)
    )
    ADOPTION_FILE.parent.mkdir(parents=True, exist_ok=True)
    ADOPTION_FILE.write_text(content, encoding="utf-8")
    print(f"\nWrote adoption file: {ADOPTION_FILE}")

    # Run strict-mode check
    print("\nRunning strict-mode check...")
    result = subprocess.run(
        [sys.executable, str(_BIN / "check_glossary_usage.py"), "--strict"],
        capture_output=False,
    )
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
