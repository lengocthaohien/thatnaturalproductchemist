#!/usr/bin/env python3
"""Generate the schematic feature-extraction figure; standard library only."""
from html import escape
from pathlib import Path

OUT = Path(__file__).resolve().parent / "feature-extraction-workflow.svg"
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


def box(x, title, subtitle):
    p.append(f'<rect x="{x}" y="105" width="196" height="210" rx="14" fill="{PAPER}" stroke="{VIOLET}" stroke-width="1.5"/>')
    text(x + 98, 137, title, 18, weight="600", anchor="middle")
    text(x + 98, 160, subtitle, 12, fill=VIOLET, family=MONO, anchor="middle")


p.append(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 620" role="img" aria-labelledby="title desc">
<title id="title">Feature extraction turns raw mass spectrometry scans into an aligned feature table</title>
<desc id="desc">Five schematic stages show raw scans, mass detection, chromatogram building, peak resolving, and alignment. Decisions at each stage affect the resulting sample-by-feature table, which can support statistics, molecular networking, and isolation but is not a list of confirmed compounds.</desc>
<defs><marker id="arrow" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 Z" fill="{VIOLET}"/></marker></defs>''')
text(35, 43, "Feature extraction: the table is built by analytical decisions", 26, weight="600")
text(35, 72, "RAW DATA → FEATURES → HYPOTHESES; NOT RAW DATA → CONFIRMED COMPOUNDS", 13, GOLD, MONO, weight="700")

xs = [28, 266, 504, 742, 980]
for x, title, subtitle in zip(xs, ["1  Raw scans", "2  Mass detection", "3  Chromatograms", "4  Resolve peaks", "5  Align features"], ["m/z × RT × intensity", "signal versus noise", "one trace per m/z", "separate coelution", "match across samples"]):
    box(x, title, subtitle)
for x in [224, 462, 700, 938]:
    arrow(x + 4, 210, x + 34, 210)

for j in range(4):
    x = 48 + j * 40
    line(x, 267, x + 27, 267, VIOLET, 1)
    for k, height in enumerate(([30, 57, 22], [22, 66, 37], [35, 48, 63], [18, 40, 29])[j]):
        xx = x + 5 + k * 8
        line(xx, 267, xx, 267 - height, VIOLET, 2)
text(126, 293, "successive scans", 12, VIOLET, MONO, "middle")

line(286, 267, 442, 267, PLUM, 1)
line(286, 242, 442, 242, GOLD, 1, 'stroke-dasharray="5 4"')
for xx, height in [(300, 20), (321, 67), (343, 15), (363, 49), (389, 76), (422, 29)]:
    line(xx, 267, xx, 267 - height, VIOLET, 3)
text(364, 293, "noise threshold", 12, VIOLET, MONO, "middle")

line(524, 267, 680, 267, PLUM, 1)
p.append(f'<path d="M526 266 C550 265 552 252 565 250 C578 247 578 195 594 191 C610 187 614 254 632 257 C650 259 658 264 678 265" fill="none" stroke="{VIOLET}" stroke-width="3" stroke-linecap="round"/>')
text(602, 293, "EIC: intensity vs RT", 12, VIOLET, MONO, "middle")

line(762, 267, 918, 267, PLUM, 1)
p.append(f'<path d="M764 265 C790 264 792 190 817 188 C839 186 845 264 866 265" fill="none" stroke="{VIOLET}" stroke-width="3"/>')
p.append(f'<path d="M792 265 C815 264 827 210 850 207 C875 204 882 263 916 265" fill="none" stroke="{GOLD}" stroke-width="3"/>')
line(840, 179, 840, 274, VIOLET, 1, 'stroke-dasharray="4 4" opacity="0.45"')
text(840, 293, "retain or split?", 12, VIOLET, MONO, "middle")

for i, label in enumerate(["feature", "S1", "S2", "S3"]):
    text(997 + i * 39, 192, label, 11, GOLD if i == 0 else VIOLET, MONO, "middle")
for r in range(4):
    y = 207 + r * 20
    line(990, y + 7, 1150, y + 7, VIOLET, 0.7, 'opacity="0.3"')
    text(997, y, f"F{r + 1}", 11, PLUM, MONO, "middle")
    for c, width in enumerate([22, 13, 28]):
        p.append(f'<rect x="{1024 + c * 39}" y="{y - 10}" width="{width - (r * 3 + c * 2) % 11}" height="8" rx="2" fill="{RED if (r + c) % 3 == 0 else DEEP}" stroke="{VIOLET}" stroke-width="0.5"/>')
text(1078, 293, "m/z + RT + abundance", 12, VIOLET, MONO, "middle")

prompts = [(28, "Which ions are noise?"), (266, "What is lost at baseline?"), (504, "Is the peak shape credible?"), (742, "Are two compounds merged?"), (980, "Are rows truly equivalent?")]
for x, label in prompts:
    p.append(f'<rect x="{x}" y="335" width="196" height="43" rx="9" fill="{RED}"/>')
    text(x + 98, 362, label, 13, PLUM, SERIF, "middle", "600")
text(35, 417, "AN ALIGNED FEATURE TABLE CAN PRIORITIZE THREE DIFFERENT TASKS", 13, GOLD, MONO, weight="700")
for x, title, subtitle in [(95, "Statistics", "group and QC comparisons"), (465, "Molecular networking", "feature-linked MS/MS families"), (835, "Isolation", "targets for chemical follow-up")]:
    p.append(f'<rect x="{x}" y="443" width="270" height="88" rx="13" fill="{DEEP}" stroke="{VIOLET}" stroke-width="1"/>')
    text(x + 135, 478, title, 19, weight="600", anchor="middle")
    text(x + 135, 506, subtitle, 13, VIOLET, MONO, "middle")
text(600, 575, "Every downstream result inherits the feature-detection and alignment choices.", 17, VIOLET, SERIF, "middle", "600")
text(35, 606, "Conceptual schematic · EIC = extracted-ion chromatogram · S1–S3 = samples · No experimental values are implied", 12, VIOLET, MONO)
p.append("</svg>")
OUT.write_text("\n".join(p) + "\n")
print(f"wrote {OUT}")
