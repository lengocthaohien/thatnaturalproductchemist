#!/usr/bin/env python3
"""Generate the numbered ampicillin structure figure (Figure 1).

Linked content:
  - Article:  src/content/articles/ampicillin-purity-comparison.md
              (Examples section, "Comparing two commercial ampicillin
              products by 1H NMR")
  - Output:   public/media/examples/ampicillin-purity-comparison/
              ampicillin-structure-numbered.svg
  - The gold position numbers (penam numbering 2, 3, 5, 6 for the bicyclic
    core; primed 1'-8' for the side chain) are the ones referenced by the
    article's NMR assignment table. If the table changes, regenerate this
    figure so the two stay in sync.

RDKit draws the molecule (clean 2D layout, stereochemistry from the
isomeric SMILES); this script then rebuilds the SVG in the site palette,
removes the background rectangle so the site's paper background shows
through, crops the canvas to the drawing, and adds the position numbers.

Requires: Python 3 + RDKit (e.g. `python3 -m venv .venv-rdkit &&
.venv-rdkit/bin/pip install rdkit`). Run from the repository root:

    .venv-rdkit/bin/python scripts/generate-ampicillin-structure.py

Label placement uses outward-from-centroid defaults plus the manual nudges
in OFFSETS; adjust those if you change the SMILES or the drawing size.
"""
import math
import re
from pathlib import Path

from rdkit import Chem
from rdkit.Chem.Draw import rdMolDraw2D

REPO_ROOT = Path(__file__).resolve().parent.parent
SMILES = "CC1(C)S[C@@H]2[C@H](NC(=O)[C@H](N)C3=CC=CC=C3)C(=O)N2[C@H]1C(=O)O"
OUT = REPO_ROOT / "public/media/examples/ampicillin-purity-comparison" \
    / "ampicillin-structure-numbered.svg"

# Site palette (see src/styles/global.css and scripts/nmr-figure-style.mjs)
BOND = "#3D2036"      # carbon skeleton
HETERO = "#5E3A52"    # heteroatom glyphs and adjacent bond halves
NUM = "#8C6D1F"       # position numbers

mol = Chem.MolFromSmiles(SMILES)
assert mol is not None
rdMolDraw2D.PrepareMolForDrawing(mol)

def neighbors(i):
    return [b.GetOtherAtomIdx(i) for b in mol.GetAtomWithIdx(i).GetBonds()]

def atomic_num(i):
    return mol.GetAtomWithIdx(i).GetAtomicNum()

def is_methyl(i):
    return atomic_num(i) == 6 and mol.GetAtomWithIdx(i).GetDegree() == 1

# Atoms are identified from the molecular graph, not hard-coded indices.
# C-2: quaternary carbon bonded to S and two methyls
c2 = next(i for i in range(mol.GetNumAtoms())
          if atomic_num(i) == 6
          and sum(1 for n in neighbors(i) if atomic_num(n) == 16) == 1
          and sum(1 for n in neighbors(i) if is_methyl(n)) == 2)

# C-3: carbon neighbour of C-2 that is also bonded to N
c3 = next(n for n in neighbors(c2)
          if atomic_num(n) == 6 and not is_methyl(n)
          and any(atomic_num(m) == 7 for m in neighbors(n)))

# N-4: nitrogen neighbour of C-3 (ring junction N)
n4 = next(n for n in neighbors(c3) if atomic_num(n) == 7)

# C-5: carbon bonded to S and N-4
c5 = next(i for i in range(mol.GetNumAtoms())
          if atomic_num(i) == 6
          and n4 in neighbors(i)
          and any(atomic_num(n) == 16 for n in neighbors(i)))

# C-6: carbon neighbour of C-5 that carries the side-chain NH
c6 = next(n for n in neighbors(c5)
          if atomic_num(n) == 6 and n != n4
          and any(atomic_num(m) == 7 and m != n4 for m in neighbors(n)))

# C-1': amide carbonyl carbon of the side chain
n_side = next(n for n in neighbors(c6) if atomic_num(n) == 7 and n != n4)
c1p = next(n for n in neighbors(n_side)
           if atomic_num(n) == 6
           and any(atomic_num(m) == 8 and
                   mol.GetBondBetweenAtoms(n, m).GetBondType() == Chem.BondType.DOUBLE
                   for m in neighbors(n)))

# C-2': alpha carbon (bonded to C-1', NH2 and phenyl ipso)
c2p = next(n for n in neighbors(c1p) if atomic_num(n) == 6 and n != n_side)

# Phenyl ring atoms ordered from ipso (3') around the ring
ipso = next(n for n in neighbors(c2p)
            if atomic_num(n) == 6 and mol.GetAtomWithIdx(n).GetIsAromatic())
ri = mol.GetRingInfo()
phenyl = next(r for r in ri.AtomRings() if ipso in r)
order = [ipso]
prev, cur = None, ipso
while True:
    nxt = [n for n in neighbors(cur) if n in phenyl and n != prev][0]
    if nxt == ipso:
        break
    order.append(nxt)
    prev, cur = cur, nxt
assert len(order) == 6
ring_labels = {order[0]: "3\u2032", order[1]: "4\u2032", order[2]: "5\u2032",
               order[3]: "6\u2032", order[4]: "7\u2032", order[5]: "8\u2032"}

# ---- draw -----------------------------------------------------------------
W, H = 560, 380
drawer = rdMolDraw2D.MolDraw2DSVG(W, H)
opts = drawer.drawOptions()
opts.padding = 0.08
opts.bondLineWidth = 2.4
drawer.DrawMolecule(mol)
drawer.FinishDrawing()

coords = {i: drawer.GetDrawCoords(i) for i in range(mol.GetNumAtoms())}
centroid = (sum(p.x for p in coords.values()) / len(coords),
            sum(p.y for p in coords.values()) / len(coords))
ring_cx = sum(coords[i].x for i in phenyl) / 6
ring_cy = sum(coords[i].y for i in phenyl) / 6

# Labels sit outward from the molecular centroid; ring labels outward from
# the phenyl centre. OFFSETS are manual nudges from visual inspection.
core_labels = {c2: "2", c3: "3", c5: "5", c6: "6", c1p: "1\u2032", c2p: "2\u2032"}
OFFSETS = {"2": (-17, 7), "3": (-12, 10), "5": (-11, 11), "6": (7, -9),
           "1\u2032": (0, 0), "2\u2032": (7, -3),
           "3\u2032": (3, -15), "4\u2032": (0, 0), "5\u2032": (0, 0),
           "6\u2032": (0, 0), "7\u2032": (0, 0), "8\u2032": (0, 0)}
labels = []
for idx, text in core_labels.items():
    p = coords[idx]
    dx, dy = p.x - centroid[0], p.y - centroid[1]
    d = math.hypot(dx, dy) or 1.0
    off = OFFSETS[text]
    labels.append((p.x + dx / d * 24 + off[0],
                   p.y + dy / d * 24 + 5 + off[1], text, 15))
for idx, text in ring_labels.items():
    p = coords[idx]
    dx, dy = p.x - ring_cx, p.y - ring_cy
    d = math.hypot(dx, dy) or 1.0
    off = OFFSETS[text]
    labels.append((p.x + dx / d * 20 + off[0],
                   p.y + dy / d * 20 + 4 + off[1], text, 12.5))


# ---- restyle the RDKit SVG ------------------------------------------------
svg = drawer.GetDrawingText()
body = re.search(r"<svg[^>]*>(.*)</svg>", svg, re.S).group(1)
body = re.sub(r"<rect[^>]*fill:#FFFFFF[^>]*>\s*</rect>", "", body)  # drop bg
for c in ("#0000FF", "#FF0000", "#CCCC00"):      # default N / O / S colours
    body = body.replace(f"stroke:{c}", f"stroke:{HETERO}")
body = body.replace("stroke:#000000", f"stroke:{BOND}")
body = re.sub(r"fill:#([0-9A-Fa-f]{6})", f"fill:{HETERO}", body)   # glyphs
body = re.sub(r"fill='#[0-9A-Fa-f]{6}'", f"fill='{HETERO}'", body)
body = body.replace("stroke-linecap:butt", "stroke-linecap:round")

# ---- compose the outer canvas ----------------------------------------------
# The site stylesheet renders article images at full column width, so the
# drawing is centred on a wide canvas to keep its apparent size modest.
PAD = 30
minx = min(p.x for p in coords.values()) - PAD
maxx = max(p.x for p in coords.values()) + PAD
miny = min(p.y for p in coords.values()) - PAD
maxy = max(p.y for p in coords.values()) + PAD
iw, ih = maxx - minx, maxy - miny

OUT_W = 1000
SCALE = 620 / iw                     # drawing occupies ~62% of the width
OUT_H = round(ih * SCALE + 16)
ox = (OUT_W - iw * SCALE) / 2 - minx * SCALE
oy = 8 - miny * SCALE

label_els = "\n".join(
    f'    <text class="num" x="{x:.1f}" y="{y:.1f}" font-size="{s}">{t}</text>'
    for x, y, t, s in labels)

out = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {OUT_W} {OUT_H}" role="img" aria-labelledby="t d">
  <title id="t">Ampicillin structure with numbered positions for NMR assignment</title>
  <desc id="d">Skeletal structure of ampicillin drawn as the free acid. The fused thiazolidine and beta-lactam rings carry standard penam position numbers: C-2 bears the gem-dimethyl group (methyl singlets near 1.5 ppm), H-3 is the thiazolidine methine near 3.9 ppm, and H-5 and H-6 are the beta-lactam methines near 5.4 ppm. The side chain at C-6 carries primed numbers: C-1' is the amide carbonyl, H-2' the side-chain methine near 4.5 ppm, and the phenyl ring positions 3' to 8' give the 5-proton aromatic multiplet at 7.3 to 7.4 ppm. Exchangeable NH and NH2 protons appear weakly above 8.5 ppm.</desc>
  <style>
    .num {{ font-family:'DM Mono',ui-monospace,SFMono-Regular,Menlo,monospace;
           font-weight:700; fill:{NUM}; text-anchor:middle }}
  </style>
  <g transform="translate({ox:.1f} {oy:.1f}) scale({SCALE:.4f})">
{body}
{label_els}
  </g>
</svg>
'''
OUT.write_text(out)
print("wrote", OUT)
print("labelled atoms:",
      {t: i for i, t in list(core_labels.items()) + list(ring_labels.items())})
