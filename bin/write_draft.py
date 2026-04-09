#!/usr/bin/env python3
"""Safe file writer — writes content to a target file without heredoc foot-guns.

Usage:
    echo "content" | python3 bin/write_draft.py path/to/file.md
    python3 bin/write_draft.py path/to/file.md < content.txt
    python3 bin/write_draft.py path/to/file.md --stdin   # read from stdin explicitly

This avoids the common failure of pasting prose directly into bash, where the
shell interprets words as commands. Always write content via this script or a
heredoc in a single compound statement.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("path", help="Target file path to write.")
    parser.add_argument(
        "--append",
        action="store_true",
        help="Append to file instead of overwriting.",
    )
    parser.add_argument(
        "--encoding",
        default="utf-8",
        help="File encoding (default: utf-8).",
    )
    args = parser.parse_args(argv)

    target = Path(args.path)
    target.parent.mkdir(parents=True, exist_ok=True)

    content = sys.stdin.read()
    mode = "a" if args.append else "w"
    target.open(mode, encoding=args.encoding).write(content)

    action = "Appended to" if args.append else "Wrote"
    print(f"{action} {target} ({len(content)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
