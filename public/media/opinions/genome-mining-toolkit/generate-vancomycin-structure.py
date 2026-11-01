#!/usr/bin/env python3
"""Regenerate the numbered vancomycin structure figure (Figure 2).

Linked content: src/content/articles/genome-mining-toolkit.md (Opinions).
Output written next to this script: vancomycin-structure-residues.svg.

Connectivity and stereochemistry are taken from the PubChem record for
vancomycin (CID 14969, free acid/base form, not the hydrochloride salt);
no stereochemical claims beyond that record. The seven residues of the
heptapeptide are located by walking the backbone from the N-terminal
N-methylleucine (residue 1) to the C-terminal carboxylate (residue 7),
and each monomer-derived moiety is highlighted with its own tint from the
site residue-tint palette (one color per residue, numbers as the redundant
second encoding).
The gold residue numbers 1-7 are the labels used in the article's Table 1
(antiSMASH adenylation-domain predictions vs. observed residues); if the
table changes, regenerate this figure. Sugars, chlorines, the N-methyl
group, and the oxidative cross-links are tailoring on top of the predicted
monomers and are not separately numbered.

Requires RDKit (e.g. python3 -m venv .venv-rdkit &&
.venv-rdkit/bin/pip install rdkit). Run with that interpreter from anywhere.
"""

import math
import re
from pathlib import Path

from rdkit import Chem
from rdkit.Chem import rdDepictor
from rdkit.Chem.Draw import rdMolDraw2D

OUT = Path(__file__).resolve().parent / "vancomycin-structure-residues.svg"

SMILES = (
    "C[C@H]1[C@H]([C@@](C[C@@H](O1)O[C@@H]2[C@H]([C@@H]([C@H](O[C@H]2"
    "OC3=C4C=C5C=C3OC6=C(C=C(C=C6)[C@H]([C@H](C(=O)N[C@H](C(=O)N[C@H]5"
    "C(=O)N[C@@H]7C8=CC(=C(C=C8)O)C9=C(C=C(C=C9O)O)[C@H](NC(=O)[C@H]("
    "[C@@H](C1=CC(=C(O4)C=C1)Cl)O)NC7=O)C(=O)O)CC(=O)N)NC(=O)[C@@H]"
    "(CC(C)C)NC)O)Cl)CO)O)O)(C)N)O"
)

BOND = "#3D2036"
HETERO = "#5E3A52"
NUM = "#8C6D1F"

# Residue-tint palette (docs/publication-rules.md section 3): one pastel tint
# per residue, in heptapeptide order 1-7. Residue numbers, not color alone,
# carry the identity of each monomer.
RESIDUE_TINTS = [
    "#F5D6CA",  # 1 light red
    "#EFE0B8",  # 2 pale gold
    "#E7DCEC",  # 3 lavender
    "#DCE6D4",  # 4 pale sage
    "#D2E4E3",  # 5 pale teal
    "#DADFEE",  # 6 pale slate
    "#EBD3DC",  # 7 pale mauve
]


def rgb(hex_color):
    return tuple(int(hex_color[i : i + 2], 16) / 255 for i in (1, 3, 5))

mol = Chem.MolFromSmiles(SMILES)
assert mol is not None
rdMolDraw2D.PrepareMolForDrawing(mol)
rdDepictor.SetPreferCoordGen(True)  # CoordGen lays out macrocycles cleanly
rdDepictor.Compute2DCoords(mol)
if mol.GetNumConformers() == 0:
    rdDepictor.Compute2DCoords(mol)
conf = mol.GetConformer()
coords = {i: conf.GetAtomPosition(i) for i in range(mol.GetNumAtoms())}
atoms = mol.GetAtoms()


def carbonyl_c(a):
    return a.GetAtomicNum() == 6 and any(
        b.GetBondType() == Chem.BondType.DOUBLE
        and b.GetOtherAtom(a).GetAtomicNum() == 8
        for b in a.GetBonds()
    )


def ring6_of(idx):
    for ring in mol.GetRingInfo().AtomRings():
        if idx in ring and len(ring) == 6 and all(
            mol.GetAtomWithIdx(i).GetIsAromatic() for i in ring
        ):
            return list(ring)
    return None


# N-terminal N-methylleucine: the only N bearing a methyl group
n1 = next(
    a for a in atoms
    if a.GetAtomicNum() == 7
    and any(n.GetAtomicNum() == 6 and n.GetDegree() == 1 for n in a.GetNeighbors())
)
a1 = next(
    n for n in n1.GetNeighbors()
    if n.GetAtomicNum() == 6 and n.GetDegree() > 1
)
c1 = next(n for n in a1.GetNeighbors() if carbonyl_c(n))

# Walk the backbone N-terminus -> C-terminus; collect residue atom sets
residues = []  # (alpha C, carbonyl C, moiety atom set)
a, c, n_prev = a1, c1, n1
for step in range(7):
    moiety = {a.GetIdx(), c.GetIdx()}
    moiety.update(
        b.GetOtherAtom(c).GetIdx() for b in c.GetBonds()
        if b.GetOtherAtom(c).GetAtomicNum() == 8
    )
    for nb in a.GetNeighbors():
        if nb.GetIdx() in (c.GetIdx(), n_prev.GetIdx()):
            continue
        # aliphatic side-chain segment (may carry OH and an aromatic ring)
        stack = [nb.GetIdx()]
        seen = set()
        while stack:
            idx = stack.pop()
            if idx in seen:
                continue
            seen.add(idx)
            at = mol.GetAtomWithIdx(idx)
            ring = ring6_of(idx)
            if ring:
                moiety.update(ring)
                for r in ring:  # ring substituent heteroatoms (O, Cl) only
                    for rn in mol.GetAtomWithIdx(r).GetNeighbors():
                        if rn.GetAtomicNum() in (8, 17):
                            moiety.add(rn.GetIdx())
                continue
            if at.GetAtomicNum() in (6, 8):
                moiety.add(idx)
                if at.GetAtomicNum() == 8:
                    continue  # do not cross ethers/glycosidic bonds
                for nn in at.GetNeighbors():
                    if nn.GetIdx() in (a.GetIdx(), c.GetIdx(), n_prev.GetIdx()):
                        continue  # never re-enter the backbone
                    if carbonyl_c(nn):
                        # side-chain amide (Asn): include C, =O, NH2, go no further
                        moiety.add(nn.GetIdx())
                        for on in nn.GetNeighbors():
                            if on.GetAtomicNum() in (7, 8):
                                moiety.add(on.GetIdx())
                        continue
                    if nn.GetAtomicNum() == 7:
                        continue  # stay out of backbone amides
                    stack.append(nn.GetIdx())
    residues.append((a.GetIdx(), c.GetIdx(), moiety))
    n_next = [n for n in c.GetNeighbors() if n.GetAtomicNum() == 7]
    if not n_next:
        break  # C-terminal free carboxylate
    n_next = n_next[0]
    a_next = next(
        n for n in n_next.GetNeighbors()
        if n.GetAtomicNum() == 6 and n.GetIdx() != c.GetIdx()
    )
    c_next = next(n for n in a_next.GetNeighbors() if carbonyl_c(n))
    a, c, n_prev = a_next, c_next, n_next

assert len(residues) == 7, f"expected 7 residues, walked {len(residues)}"


def classify(moiety):
    rings = {i for i in moiety if mol.GetAtomWithIdx(i).GetIsAromatic()}
    n_cl = sum(1 for i in moiety if mol.GetAtomWithIdx(i).GetAtomicNum() == 17)
    n_oh = sum(
        1 for i in moiety
        if mol.GetAtomWithIdx(i).GetAtomicNum() == 8
        and mol.GetAtomWithIdx(i).GetDegree() == 1
        and any(j.GetIsAromatic()
                for j in mol.GetAtomWithIdx(i).GetNeighbors())
    )
    if not rings:
        if any(mol.GetAtomWithIdx(i).GetAtomicNum() == 7 for i in moiety):
            return "Asn"
        return "N-Me-Leu"
    if n_cl:
        return "Cl-Bht"
    if n_oh >= 2:
        return "Dpg"
    return "Hpg"


# ---- draw ------------------------------------------------------------------
W, H = 1000, 800
drawer = rdMolDraw2D.MolDraw2DSVG(W, H)
opts = drawer.drawOptions()
opts.padding = 0.06
opts.bondLineWidth = 2.0

# One tint per residue; shared atoms (e.g. cross-link ether oxygens) keep the
# color of the first residue that claims them, and bonds between residues stay
# unhighlighted so cross-links read as connections between monomers.
atom_colors, bond_colors = {}, {}
claimed = set()
for i, (_, _, moiety) in enumerate(residues):
    tint = rgb(RESIDUE_TINTS[i])
    for a in sorted(moiety - claimed):
        atom_colors[a] = tint
    claimed |= moiety
    own = {a for a in moiety if atom_colors.get(a) == tint}
    for b in mol.GetBonds():
        if b.GetBeginAtomIdx() in own and b.GetEndAtomIdx() in own:
            bond_colors[b.GetIdx()] = tint

drawer.DrawMolecule(
    mol,
    highlightAtoms=sorted(atom_colors),
    highlightBonds=sorted(bond_colors),
    highlightAtomColors=atom_colors,
    highlightBondColors=bond_colors,
)
drawer.FinishDrawing()

coords = {i: drawer.GetDrawCoords(i) for i in range(mol.GetNumAtoms())}
centroid = (
    sum(p.x for p in coords.values()) / len(coords),
    sum(p.y for p in coords.values()) / len(coords),
)

# Residue numbers sit OUTSIDE the drawing: for each residue, try 16 directions
# from its moiety centroid and keep the closest position that clears every
# atom (no glyph on bonds or inside rings) and every previously placed label.
atom_pts = [(p.x, p.y) for p in coords.values()]
labels, placed = [], []
for i, (ai, ci, moiety) in enumerate(residues, start=1):
    print(f"residue {i}: {classify(moiety)} ({len(moiety)} atoms)")
    ring = [j for j in moiety if mol.GetAtomWithIdx(j).GetIsAromatic()]
    anchor = ring if ring else [j for j in moiety if j not in (ai, ci)]
    px = sum(coords[j].x for j in anchor) / len(anchor)
    py = sum(coords[j].y for j in anchor) / len(anchor)
    outward = math.atan2(py - centroid[1], px - centroid[0])
    best = None
    for k in range(16):
        ang = outward + k * math.pi / 8
        ux, uy = math.cos(ang), math.sin(ang)
        for t in range(28, 300, 4):
            lx, ly = px + ux * t, py + uy * t
            if any(math.hypot(lx - ax, ly - ay) < 30 for ax, ay in atom_pts):
                continue
            if any(math.hypot(lx - qx, ly - qy) < 34 for qx, qy in placed):
                continue
            score = t + (0 if k == 0 else 60)  # prefer outward when similar
            if best is None or score < best[0]:
                best = (score, lx, ly)
            break
    assert best is not None, f"no clear label position for residue {i}"
    _, lx, ly = best
    placed.append((lx, ly))
    labels.append((lx, ly + 6, str(i)))

# ---- restyle the RDKit SVG into the site palette --------------------------
svg = drawer.GetDrawingText()
body = re.search(r"<svg[^>]*>(.*)</svg>", svg, re.S).group(1)
body = re.sub(r"<rect[^>]*fill:#FFFFFF[^>]*>\s*</rect>", "", body)  # drop bg
for col in ("#0000FF", "#FF0000", "#CCCC00", "#00CC00", "#00FF00"):  # N/O/S/Cl
    body = body.replace(f"stroke:{col}", f"stroke:{HETERO}")
    body = body.replace(f"fill:{col}", f"fill:{HETERO}")
    body = body.replace(f"fill='{col}'", f"fill='{HETERO}'")
body = body.replace("stroke:#000000", f"stroke:{BOND}")
body = body.replace("fill:#000000", f"fill:{BOND}")  # wedge bonds
# highlight fills (light red tint) are deliberately left untouched
body = body.replace("stroke-linecap:butt", "stroke-linecap:round")

# ---- compose the outer canvas (labels included in the bounding box) --------
PAD = 30
all_x = [p.x for p in coords.values()] + [lx for lx, _, _ in labels]
all_y = [p.y for p in coords.values()] + [ly for _, ly, _ in labels]
minx, maxx = min(all_x) - PAD, max(all_x) + PAD
miny, maxy = min(all_y) - PAD, max(all_y) + PAD
iw, ih = maxx - minx, maxy - miny

OUT_W = 1000
SCALE = 760 / iw  # drawing occupies ~76% of the width
OUT_H = round(ih * SCALE + 16)
ox = (OUT_W - iw * SCALE) / 2 - minx * SCALE
oy = 8 - miny * SCALE

label_els = "\n".join(
    f'    <text class="num" x="{x:.1f}" y="{y:.1f}" font-size="17">{t}</text>'
    for x, y, t in labels
)

out = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {OUT_W} {OUT_H}" role="img" aria-labelledby="t d">
  <title id="t">Vancomycin structure with the seven heptapeptide residues numbered</title>
  <desc id="d">Skeletal structure of vancomycin (PubChem CID 14969) drawn with stereochemistry from that record. Each of the seven monomer-derived moieties specified by the antiSMASH adenylation-domain predictions carries its own pastel tint and a gold residue number placed outside the drawing: N-methylleucine (1), two chloro-beta-hydroxytyrosines (2 and 6), asparagine (3), two 4-hydroxyphenylglycines (4 and 5), and 3,5-dihydroxyphenylglycine (7). The glucose-vancosamine disaccharide on residue 4, the two chlorines, the N-methyl group, and the three oxidative cross-links are tailoring features outside the monomer predictions.</desc>
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


