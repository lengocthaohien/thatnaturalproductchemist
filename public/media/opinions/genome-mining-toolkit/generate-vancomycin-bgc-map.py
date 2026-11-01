#!/usr/bin/env python3
"""Regenerate the vancomycin BGC gene map for the genome-mining-toolkit opinion.

Pure stdlib; run from anywhere, output SVG is written next to this script.

Data source: MIBiG 4.0 entry BGC0000455.6 (vancomycin biosynthetic gene
cluster from Amycolatopsis orientalis HCCB10007), GenBank download at
https://mibig.secondarymetabolites.org/repository/BGC0000455.6/BGC0000455.gbk
(retrieved 2026-11-01); underlying NCBI record HQ679900.1. Gene coordinates,
names, strands, and functional categories below are transcribed from that
record (categories follow the antiSMASH /gene_functions qualifiers:
biosynthetic, biosynthetic-additional, transport, regulatory, resistance,
other). Four coding sequences carry no gene name in the record and are drawn
unlabeled.

Colors stay inside the site palette (see docs/publication-rules.md):
dark plum #3D2036, muted violet #5E3A52, gold #8C6D1F, light red highlight
(0.96, 0.84, 0.79), paper #FDFCF9, paper-deep #F4F1EA. Regulatory and
resistance genes are encoded by outline color instead of fill, so color is
not the only carrier of meaning.
"""

from pathlib import Path

OUT = Path(__file__).resolve().parent / "vancomycin-bgc-gene-map.svg"

# (name, start, end, strand, category); name "" = unnamed in the MIBiG record
GENES = [
    ("vanH", 1, 1032, 1, "tailoring"),
    ("vanA", 1034, 2080, 1, "tailoring"),
    ("vanX", 2070, 2678, 1, "resistance"),
    ("vtrR", 3664, 4638, 1, "regulatory"),
    ("vcm1", 4784, 5635, 1, "other"),
    ("", 5595, 7733, 1, "transport"),
    ("vcm2", 7730, 17188, 1, "core"),
    ("vcm3", 17541, 29693, 1, "core"),
    ("vcm4", 29714, 35290, 1, "core"),
    ("vcm5", 35584, 36759, 1, "tailoring"),
    ("vcm6", 37090, 38313, 1, "tailoring"),
    ("vcm7", 38440, 39660, 1, "tailoring"),
    ("vcm8", 39705, 41180, 1, "tailoring"),
    ("vcm9", 41236, 42462, 1, "tailoring"),
    ("vcm10", 42515, 43741, 1, "tailoring"),
    ("vcm11", 43767, 44993, 1, "other"),
    ("", 44999, 45820, 1, "tailoring"),
    ("vcm12", 45860, 46702, 1, "tailoring"),
    ("vcm13", 46683, 47987, -1, "tailoring"),
    ("vcm14", 48218, 49048, 1, "tailoring"),
    ("vcm15", 49099, 50781, 1, "core"),
    ("vcm16", 50795, 51985, 1, "tailoring"),
    ("vcm17", 52104, 53138, 1, "other"),
    ("vcm18", 53135, 54214, 1, "other"),
    ("", 54431, 55618, 1, "other"),
    ("vcm19", 55798, 57204, 1, "other"),
    ("vcm20", 57205, 58176, 1, "tailoring"),
    ("vcm21", 58173, 59282, 1, "tailoring"),
    ("vcm22", 59306, 59923, 1, "tailoring"),
    ("vcm23", 60011, 61129, 1, "core"),
    ("vcm24", 61156, 61785, 1, "other"),
    ("vcm25", 61782, 63008, 1, "other"),
    ("vcm26", 63005, 63796, 1, "tailoring"),
    ("", 63968, 65044, 1, "other"),
]

MODULES = {"vcm2": "3 modules", "vcm3": "3 modules", "vcm4": "1 module"}

LENGTH = 65044
X0, X1 = 60.0, 960.0
TRACK_Y = 140.0
ARROW_H = 13.0

PLUM = "#3D2036"
VIOLET = "#5E3A52"
GOLD = "#8C6D1F"
PAPER = "#FDFCF9"
PAPER_DEEP = "#F4F1EA"
TINT = "rgba(245, 214, 202, 0.6)"  # (0.96, 0.84, 0.79) highlight

SERIF = "Newsreader, Georgia, serif"
MONO = "'DM Mono', ui-monospace, monospace"

# category -> (fill, stroke, legend label)
CATS = {
    "core": (PLUM, "none", "core biosynthetic"),
    "tailoring": (VIOLET, "none", "tailoring & precursor supply"),
    "transport": (GOLD, "none", "transport"),
    "regulatory": (PAPER, GOLD, "regulatory"),
    "resistance": (PAPER, PLUM, "resistance"),
    "other": (PAPER_DEEP, PLUM, "other / uncharacterized"),
}
LEGEND_ORDER = ["core", "tailoring", "transport", "regulatory", "resistance", "other"]


def x(bp):
    return X0 + (bp - 1) / (LENGTH - 1) * (X1 - X0)


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def arrow(x1, x2, strand, fill, stroke):
    head = min(10.0, max(4.0, 0.3 * (x2 - x1)))
    y, h = TRACK_Y, ARROW_H
    if strand > 0:
        pts = [(x1, y - h), (x2 - head, y - h), (x2, y), (x2 - head, y + h), (x1, y + h)]
    else:
        pts = [(x2, y - h), (x1 + head, y - h), (x1, y), (x1 + head, y + h), (x2, y + h)]
    points = " ".join(f"{px:.1f},{py:.1f}" for px, py in pts)
    sw = ' stroke-width="1.2"' if stroke != "none" else ""
    st = stroke if stroke != "none" else "none"
    return f'<polygon points="{points}" fill="{fill}" stroke="{st}"{sw}/>'


def bracket(x1, x2, line_y, label, label_y, anchor, lx):
    return (
        f'<text x="{lx:.1f}" y="{label_y}" font-family="{SERIF}" font-size="12" '
        f'font-style="italic" fill="{PLUM}" text-anchor="{anchor}">{esc(label)}</text>'
        f'<line x1="{x1:.1f}" y1="{line_y}" x2="{x2:.1f}" y2="{line_y}" stroke="{PLUM}" stroke-width="1"/>'
        f'<line x1="{x1:.1f}" y1="{line_y}" x2="{x1:.1f}" y2="{line_y + 4}" stroke="{PLUM}" stroke-width="1"/>'
        f'<line x1="{x2:.1f}" y1="{line_y}" x2="{x2:.1f}" y2="{line_y + 4}" stroke="{PLUM}" stroke-width="1"/>'
    )


def main():
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 292">',
        '<title>Gene map of the vancomycin biosynthetic gene cluster (MIBiG BGC0000455.6)</title>',
    ]

    # header
    parts.append(
        f'<text x="{X0}" y="22" font-family="{SERIF}" font-size="13" font-style="italic" '
        f'fill="{PLUM}">Amycolatopsis orientalis HCCB10007 — vancomycin biosynthetic gene cluster</text>'
    )
    parts.append(
        f'<text x="{X1}" y="22" font-family="{MONO}" font-size="9.5" fill="{VIOLET}" '
        f'text-anchor="end">MIBiG BGC0000455.6 · NCBI HQ679900.1 · 65,044 nt</text>'
    )

    # highlight band behind the three NRPS genes (vcm2-vcm4)
    bx1, bx2 = x(7730), x(35290)
    parts.append(
        f'<rect x="{bx1:.1f}" y="104" width="{bx2 - bx1:.1f}" height="72" rx="8" fill="{TINT}"/>'
    )

    # baseline
    parts.append(
        f'<line x1="{X0}" y1="{TRACK_Y}" x2="{X1}" y2="{TRACK_Y}" stroke="{PLUM}" stroke-width="1" opacity="0.3"/>'
    )

    # brackets (two vertical levels to avoid label collisions)
    parts.append(bracket(bx1, bx2, 68, "NRPS assembly line — vcm2, vcm3, vcm4", 60, "middle", (bx1 + bx2) / 2))
    parts.append(bracket(x(52104), x(63796), 68, "precursor supply: Hpg · Dpg · vancosamine", 60, "end", X1))
    parts.append(bracket(x(1), x(2678), 92, "vanHAX resistance", 84, "start", X0))
    parts.append(
        bracket(
            x(35584), x(44993), 92,
            "tailoring: P450s · halogenase · glycosyltransferases",
            84, "middle", (x(35584) + x(44993)) / 2,
        )
    )

    # genes
    named = [g for g in GENES if g[0]]
    for name, start, end, strand, cat in GENES:
        fill, stroke, _ = CATS[cat]
        parts.append(arrow(x(start), x(end), strand, fill, stroke))
        if name in MODULES:
            parts.append(
                f'<text x="{(x(start) + x(end)) / 2:.1f}" y="121" font-family="{MONO}" '
                f'font-size="9.5" fill="{PLUM}" text-anchor="middle">{MODULES[name]}</text>'
            )

    # gene labels in two staggered rows, rotated 70 degrees
    for i, (name, start, end, strand, cat) in enumerate(named):
        xm = (x(start) + x(end)) / 2
        ly = 184 if i % 2 == 0 else 198
        parts.append(
            f'<line x1="{xm:.1f}" y1="{TRACK_Y + ARROW_H + 3}" x2="{xm:.1f}" y2="{ly - 4}" '
            f'stroke="{PLUM}" stroke-width="0.6" opacity="0.35"/>'
            f'<text x="{xm:.1f}" y="{ly}" font-family="{MONO}" font-size="9.5" fill="{PLUM}" '
            f'transform="rotate(70 {xm:.1f} {ly})">{esc(name)}</text>'
        )

    # legend
    lx, ly = X0, 263.5
    for cat in LEGEND_ORDER:
        fill, stroke, label = CATS[cat]
        sw = ' stroke-width="1.2"' if stroke != "none" else ""
        st = stroke if stroke != "none" else "none"
        parts.append(
            f'<rect x="{lx:.1f}" y="{ly}" width="14" height="9" fill="{fill}" stroke="{st}"{sw}/>'
        )
        parts.append(
            f'<text x="{lx + 19:.1f}" y="{ly + 8}" font-family="{SERIF}" font-size="10" fill="{PLUM}">{esc(label)}</text>'
        )
        lx += 19 + len(label) * 5.2 + 16

    # scale bar (10 kb)
    sb_x1 = X1 - 10000 / (LENGTH - 1) * (X1 - X0)
    parts.append(
        f'<line x1="{sb_x1:.1f}" y1="268" x2="{X1}" y2="268" stroke="{PLUM}" stroke-width="1.5"/>'
        f'<line x1="{sb_x1:.1f}" y1="264" x2="{sb_x1:.1f}" y2="272" stroke="{PLUM}" stroke-width="1.5"/>'
        f'<line x1="{X1}" y1="264" x2="{X1}" y2="272" stroke="{PLUM}" stroke-width="1.5"/>'
        f'<text x="{(sb_x1 + X1) / 2:.1f}" y="261" font-family="{MONO}" font-size="9.5" '
        f'fill="{PLUM}" text-anchor="middle">10 kb</text>'
    )

    parts.append("</svg>")
    OUT.write_text("\n".join(parts) + "\n")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()

