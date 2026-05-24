#!/usr/bin/env python3
"""Validate proof-hazard negative-control fixtures.

This checker is intentionally conservative. It does not try to parse arbitrary
mathematical prose. Instead, it enforces that rejected proof-pattern fixtures
carry enough machine-readable structure to be useful as future validator test
cases.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


DEFAULT_FIXTURE_DIR = Path("fixtures/proof_hazards")
REQUIRED_SECTIONS = (
    "# ",
    "Status:",
    "Expected validator disposition:",
    "Hazards:",
    "## Bad proof pattern",
    "## Why this must fail",
    "## Required remediation",
)
REQUIRED_HAZARDS = {
    "dropped-premise",
    "unproved-bridge",
}
PROMOTION_PATTERNS = (
    re.compile(r"X\s+and\s+A\s*->\s*Y"),
    re.compile(r"X\s*∩\s*A"),
    re.compile(r"X\(s\)\s*=\s*0\s+and\s+Aux\(s\)\s*=\s*0\s*->\s*Y\(s\)", re.MULTILINE),
)
DROPPED_CONCLUSION_PATTERNS = (
    re.compile(r"X\s*->\s*Y"),
    re.compile(r"X\(s\)\s*=\s*0\s*->\s*Y\(s\)"),
)
BRIDGE_PATTERNS = (
    re.compile(r"X\s*->\s*A"),
    re.compile(r"X\s*<->\s*A"),
    re.compile(r"X\(s\)\s*=\s*0\s*->\s*Aux\(s\)\s*=\s*0"),
)


@dataclass(frozen=True)
class Finding:
    path: Path
    message: str


def _hazards(text: str) -> set[str]:
    hazards: set[str] = set()
    in_hazards = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped == "Hazards:":
            in_hazards = True
            continue
        if in_hazards and stripped.startswith("## "):
            break
        if in_hazards and stripped.startswith("-"):
            hazards.add(stripped.lstrip("- ").strip())
    return hazards


def _has_any(patterns: tuple[re.Pattern[str], ...], text: str) -> bool:
    return any(pattern.search(text) for pattern in patterns)


def validate_fixture(path: Path) -> list[Finding]:
    text = path.read_text(encoding="utf-8")
    findings: list[Finding] = []

    for required in REQUIRED_SECTIONS:
        if required not in text:
            findings.append(Finding(path, f"missing required marker: {required}"))

    hazards = _hazards(text)
    missing_hazards = REQUIRED_HAZARDS - hazards
    if missing_hazards:
        findings.append(Finding(path, f"missing required hazards: {', '.join(sorted(missing_hazards))}"))

    if "Expected validator disposition: fail" not in text and "Expected validator disposition: reject" not in text:
        findings.append(Finding(path, "expected disposition must be fail or reject"))

    has_auxiliary_promotion = _has_any(PROMOTION_PATTERNS, text)
    has_dropped_conclusion = _has_any(DROPPED_CONCLUSION_PATTERNS, text)
    has_bridge_statement = _has_any(BRIDGE_PATTERNS, text)

    if not has_auxiliary_promotion:
        findings.append(Finding(path, "fixture does not expose an auxiliary-premise proof pattern"))
    if not has_dropped_conclusion:
        findings.append(Finding(path, "fixture does not expose a dropped-premise conclusion pattern"))
    if not has_bridge_statement:
        findings.append(Finding(path, "fixture does not name the missing bridge obligation"))

    if "remove theorem-strength language" not in text:
        findings.append(Finding(path, "remediation must include removing theorem-strength language"))

    return findings


def fixture_paths(root: Path) -> list[Path]:
    if root.is_file():
        return [root]
    if not root.exists():
        return []
    return sorted(root.glob("*.md"))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        default=[DEFAULT_FIXTURE_DIR],
        help="fixture files or directories to validate",
    )
    args = parser.parse_args(argv)

    paths: list[Path] = []
    for supplied in args.paths:
        paths.extend(fixture_paths(supplied))

    if not paths:
        print("no proof-hazard fixtures found", file=sys.stderr)
        return 1

    findings: list[Finding] = []
    for path in paths:
        findings.extend(validate_fixture(path))

    if findings:
        for finding in findings:
            print(f"{finding.path}: {finding.message}", file=sys.stderr)
        return 1

    print(f"validated {len(paths)} proof-hazard fixture(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
