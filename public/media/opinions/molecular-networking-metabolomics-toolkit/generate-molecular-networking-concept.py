#!/usr/bin/env python3
"""Generate the conceptual molecular-networking figure for the Opinions article.

Pure Python standard library; run from anywhere. The SVG is written next to
this script. All spectra and networks are schematic, not experimental data.
"""
from html import escape
from pathlib import Path

OUT = Path(__file__).resolve().parent / "molecular-networking-concept.svg"
PLUM, VIOLET, GOLD = "#3D2036", "#5E3A52", "#8C6D1F"
PAPER, DEEP, RED = "#FDFCF9", "#F4F1EA", "#F5D6CA"
SERIF = "Newsreader, Georgia, serif"
MONO = "'DM Mono', ui-monospace, monospace"
p = []


def text(x, y, value, size=16, fill=PLUM, family=SERIF, anchor="start", weight="400"):
    p.append(f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}">{escape(value)}</text>')


def line(x1, y1, x2, y2, color=PLUM, width=2, extra=""):
    p.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}" {extra}/>')


def arrow(x1, y1, x2, y2):
    line(x1, y1, x2, y2, VIOLET, 2, 'marker-end="url(#arrow)"')


def spectrum(x, y, precursor, shifted=False):
    line(x, y + 90, x + 130, y + 90, PLUM, 1)
    heights = [34, 68, 46, 80, 28, 58]
    for i, height in enumerate(heights):
        xx = x + 12 + i * 20 + (7 if shifted and i in (2, 5) else 0)
        color = GOLD if shifted and i in (2, 5) else VIOLET
        line(xx, y + 90, xx, y + 90 - height, color, 4)
    text(x + 65, y + 112, precursor, 12, PLUM, MONO, "middle")


def node(x, y, top, bottom="", feature=False):
    if feature:
        p.append(f'<rect x="{x-42}" y="{y-30}" width="84" height="60" rx="12" fill="{PAPER}" stroke="{VIOLET}" stroke-width="2"/>')
        text(x, y - 4, top, 12, PLUM, MONO, "middle")
        text(x, y + 16, bottom, 11, VIOLET, MONO, "middle")
        for i, height in enumerate((9, 18, 13)):
            p.append(f'<rect x="{x-28+i*20}" y="{y+42-height}" width="12" height="{height}" fill="{RED if i == 1 else DEEP}" stroke="{VIOLET}" stroke-width="0.7"/>')
        text(x, y + 60, "S1  S2  S3", 9, VIOLET, MONO, "middle")
    else:
        p.append(f'<circle cx="{x}" cy="{y}" r="30" fill="{PAPER}" stroke="{VIOLET}" stroke-width="2"/>')
        text(x, y + 4, top, 11, PLUM, MONO, "middle")


p.append(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 790" role="img" aria-labelledby="title desc">
<title id="title">Concept of classical and feature-based molecular networking</title>
<desc id="desc">Schematic fragmentation spectra are compared by modified cosine similarity to form nodes, edges, and candidate molecular families. Classical networking consolidates spectra by precursor. Feature-based networking links spectra to LC-MS features with retention time and sample abundances, and is identified as the current mainstream approach for comparative LC-MS/MS studies.</desc>
<defs><marker id="arrow" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 Z" fill="{VIOLET}"/></marker></defs>''')
text(40, 40, "Molecular networking: spectral relationships become a searchable map", 25, weight="600")
p.append(f'<rect x="35" y="62" width="1130" height="300" rx="16" fill="{DEEP}"/>')
text(58, 92, "A  Shared and shifted fragment ions", 17, weight="600")
spectrum(70, 130, "precursor 300.1")
spectrum(225, 130, "precursor 314.1", True)
arrow(370, 190, 430, 190)
text(400, 169, "modified cosine", 12, VIOLET, MONO, "middle")
for a, b in [((505, 155), (590, 120)), ((505, 155), (575, 235)), ((590, 120), (665, 175)), ((575, 235), (665, 175))]:
    line(*a, *b, GOLD, 2)
for x, y, label in [(505, 155, "300.1"), (590, 120, "314.1"), (575, 235, "328.1"), (665, 175, "342.1")]:
    node(x, y, label)
text(585, 290, "candidate molecular family", 14, VIOLET, SERIF, "middle")
line(760, 92, 760, 330, VIOLET, 1, 'opacity="0.3"')
text(795, 112, "NODE", 13, GOLD, MONO, weight="700")
text(795, 137, "MS/MS spectrum or LC–MS feature", 16)
text(795, 181, "EDGE", 13, GOLD, MONO, weight="700")
text(795, 206, "Spectral similarity above set thresholds", 16)
text(795, 250, "CLUSTER", 13, GOLD, MONO, weight="700")
text(795, 275, "Candidate molecular family", 16)
text(795, 315, "An edge is not structural proof.", 16, VIOLET, weight="600")

p.append(f'<rect x="35" y="385" width="550" height="365" rx="16" fill="{PAPER}" stroke="{VIOLET}" stroke-width="1"/>')
p.append(f'<rect x="615" y="385" width="550" height="365" rx="16" fill="{PAPER}" stroke="{GOLD}" stroke-width="2"/>')
text(60, 420, "B  Classical molecular networking", 19, weight="600")
text(640, 420, "C  Feature-based molecular networking", 19, weight="600")
p.append(f'<rect x="640" y="439" width="500" height="30" rx="8" fill="{RED}"/>')
text(890, 459, "CURRENT MAINSTREAM FOR COMPARATIVE LC–MS/MS", 12, PLUM, MONO, "middle", "700")
text(60, 457, "Consolidate MS/MS spectra by precursor", 15, VIOLET)
for a, b in [((155, 565), (285, 520)), ((285, 520), (420, 565)), ((155, 565), (285, 640)), ((285, 640), (420, 565))]:
    line(*a, *b, GOLD, 2)
for x, y, label in [(155, 565, "300.1"), (285, 520, "314.1"), (285, 640, "328.1"), (420, 565, "342.1")]:
    node(x, y, label)
text(60, 704, "Node = consensus MS/MS spectrum", 15)
text(60, 729, "Rapid survey; chromatographic context is not retained", 14, VIOLET)
text(640, 497, "Link MS/MS to detected, aligned LC–MS features", 15, VIOLET)
for a, b in [((735, 565), (865, 535)), ((865, 535), (1000, 565)), ((735, 565), (865, 640)), ((865, 640), (1000, 565))]:
    line(*a, *b, GOLD, 2)
for x, y, label, rt in [(735, 565, "300.1", "6.2 min"), (865, 535, "314.1", "7.0 min"), (865, 640, "328.1", "7.8 min"), (1000, 565, "342.1", "8.1 min")]:
    node(x, y, label, rt, True)
text(640, 720, "Node = precursor m/z + RT + sample abundances", 15)
text(40, 778, "Conceptual schematic · S1–S3 denote three samples · No experimental intensity or similarity values are implied", 12, VIOLET, MONO)
p.append("</svg>")
OUT.write_text("\n".join(p) + "\n")
print(f"wrote {OUT}")
