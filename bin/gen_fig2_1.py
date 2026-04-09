#!/usr/bin/env python3
"""Generate Figure 2.1 — 1–120 sieve grid with 30-wheel overlay (SVG).

Figure spec (Issue #15, #19):
- 1–120 laid out in a 10×12 grid (left→right, top→bottom)
- Strike entries eliminated by {2, 3, 5}
- Box/halo wheel-admissible residues mod 30 (gcd(n, 30) = 1)
- Legend: elimination vs wheel-admissible; residues {1,7,11,13,17,19,23,29}

Usage:
    python3 bin/gen_fig2_1.py                          # writes to default output
    python3 bin/gen_fig2_1.py --output path/to/fig.svg

Output: manuscript/assets/figures/fig2-1.svg (default)
"""
from __future__ import annotations

import argparse
import math
from pathlib import Path

DEFAULT_OUTPUT = Path("manuscript/assets/figures/fig2-1.svg")

COLS = 10
ROWS = 12  # 10*12 = 120

CELL_W = 48
CELL_H = 40
MARGIN_LEFT = 20
MARGIN_TOP = 20
LEGEND_H = 90

SVG_W = MARGIN_LEFT * 2 + COLS * CELL_W
SVG_H = MARGIN_TOP * 2 + ROWS * CELL_H + LEGEND_H

ELIMINATED_FILL = "#e0e0e0"
ELIMINATED_TEXT = "#aaaaaa"
WHEEL_STROKE = "#1a6faf"
WHEEL_FILL = "#dbeeff"
PRIME_FILL = "#fff8c4"
PRIME_STROKE = "#c8a000"
DEFAULT_FILL = "#ffffff"
DEFAULT_TEXT = "#222222"
STRIKE_COLOR = "#aaaaaa"


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def is_eliminated(n: int) -> bool:
    return n > 1 and (n % 2 == 0 or n % 3 == 0 or n % 5 == 0)


def is_wheel_admissible(n: int) -> bool:
    """gcd(n, 30) == 1."""
    return gcd(n, 30) == 1


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for p in range(2, int(math.isqrt(n)) + 1):
        if n % p == 0:
            return False
    return True


def cell_svg(n: int, col: int, row: int) -> str:
    x = MARGIN_LEFT + col * CELL_W
    y = MARGIN_TOP + row * CELL_H

    eliminated = is_eliminated(n)
    wheel = is_wheel_admissible(n)
    prime = is_prime(n)

    if eliminated:
        fill = ELIMINATED_FILL
        text_color = ELIMINATED_TEXT
    elif prime:
        fill = PRIME_FILL
    elif wheel:
        fill = WHEEL_FILL
    else:
        fill = DEFAULT_FILL

    parts: list[str] = []

    # Cell background
    parts.append(
        f'<rect x="{x}" y="{y}" width="{CELL_W}" height="{CELL_H}" '
        f'fill="{fill}" stroke="#cccccc" stroke-width="0.5"/>'
    )

    # Wheel admissible border
    if wheel and not eliminated:
        stroke = PRIME_STROKE if prime else WHEEL_STROKE
        parts.append(
            f'<rect x="{x+1}" y="{y+1}" width="{CELL_W-2}" height="{CELL_H-2}" '
            f'fill="none" stroke="{stroke}" stroke-width="1.5" rx="3"/>'
        )

    # Number text
    text_color = ELIMINATED_TEXT if eliminated else DEFAULT_TEXT
    cx = x + CELL_W // 2
    cy = y + CELL_H // 2 + 5
    parts.append(
        f'<text x="{cx}" y="{cy}" text-anchor="middle" '
        f'font-size="12" font-family="monospace" fill="{text_color}">{n}</text>'
    )

    # Strike-through for eliminated
    if eliminated:
        sy = y + CELL_H // 2
        parts.append(
            f'<line x1="{x+4}" y1="{sy}" x2="{x+CELL_W-4}" y2="{sy}" '
            f'stroke="{STRIKE_COLOR}" stroke-width="1"/>'
        )

    return "\n".join(parts)


def legend_svg(y_start: int) -> str:
    parts: list[str] = []
    lx = MARGIN_LEFT
    ly = y_start + 10

    # Title
    parts.append(
        f'<text x="{lx}" y="{ly}" font-size="11" font-family="sans-serif" '
        f'font-weight="bold" fill="#333">Legend</text>'
    )
    ly += 16

    items = [
        (ELIMINATED_FILL, STRIKE_COLOR, "× = eliminated by {{2,3,5}} (composite multiple)"),
        (WHEEL_FILL, WHEEL_STROKE, "□ = wheel-admissible: gcd(n,30)=1 — residues {{1,7,11,13,17,19,23,29}}"),
        (PRIME_FILL, PRIME_STROKE, "◇ = prime (wheel-admissible + prime)"),
    ]
    for fill, stroke, label in items:
        parts.append(
            f'<rect x="{lx}" y="{ly-9}" width="14" height="12" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="1" rx="2"/>'
        )
        parts.append(
            f'<text x="{lx+18}" y="{ly}" font-size="10" font-family="sans-serif" '
            f'fill="#333">{label}</text>'
        )
        ly += 16

    # Caption
    parts.append(
        f'<text x="{lx}" y="{ly+4}" font-size="9" font-family="sans-serif" '
        f'fill="#555" font-style="italic">'
        f'Figure 2.1 — A sieve eliminates; a wheel eliminates whole congruence '
        f'classes in advance. Together they form the first deterministic prime engine.'
        f'</text>'
    )
    return "\n".join(parts)


def generate_svg() -> str:
    parts: list[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{SVG_W}" height="{SVG_H}" '
        f'viewBox="0 0 {SVG_W} {SVG_H}">',
        f'<rect width="{SVG_W}" height="{SVG_H}" fill="white"/>',
        f'<text x="{SVG_W//2}" y="14" text-anchor="middle" '
        f'font-size="13" font-family="sans-serif" font-weight="bold" fill="#222">'
        f'Figure 2.1 — Sieve Grid 1–120 with 30-Wheel Overlay</text>',
    ]

    for n in range(1, 121):
        col = (n - 1) % COLS
        row = (n - 1) // COLS
        parts.append(cell_svg(n, col, row))

    legend_y = MARGIN_TOP + ROWS * CELL_H + 4
    parts.append(legend_svg(legend_y))
    parts.append("</svg>")
    return "\n".join(parts)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--output",
        default=str(DEFAULT_OUTPUT),
        help=f"Output SVG path (default: {DEFAULT_OUTPUT})",
    )
    args = parser.parse_args(argv)

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    svg = generate_svg()
    out.write_text(svg, encoding="utf-8")
    print(f"Written: {out} ({len(svg)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
