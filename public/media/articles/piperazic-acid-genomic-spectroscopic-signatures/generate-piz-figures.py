#!/usr/bin/env python3
"""Regenerate the static structure figure for the piperazic acid article.

Requires RDKit (pip install rdkit). Run from anywhere; the output SVG is
written next to this script. Structures are drawn from PubChem connectivity
records (no stereochemical claims beyond those records). Every six-membered
ring that contains an N-N bond is highlighted with a light red tint: the
piperazic acid (Piz) residue itself, its oxidized dehydropiperazic acid
(Dpz) form in lydiamycin A, and the hydroxylated or chlorinated Piz
derivatives in piperazimycin A.

PubChem connectivity records used (CID):
  piperazic acid      2762538
  kutzneride 1        11585982
  lydiamycin A        11628907
  piperazimycin A     16103273
  azinothricin        139589018
  depsidomycin        197287
  dentigerumycin E    156581792
  incarnatapeptin A   146684657
"""

from pathlib import Path

from rdkit import Chem
from rdkit.Chem import rdDepictor
from rdkit.Chem.Draw import rdMolDraw2D

OUT = Path(__file__).resolve().parent
TINT = (0.96, 0.84, 0.79)  # light red tint behind each Piz/Dpz ring

# (legend, PubChem CID, connectivity SMILES)
PANEL = [
    ("piperazic acid", 2762538,
     "C1CC(NNC1)C(=O)O"),
    ("kutzneride 1", 11585982,
     "CC1(CC1)C2C(=O)OC(C(=O)N3C(CCCN3)C(=O)NC(C(=O)NC(C(=O)N4C(CC5(C4NC6=C5C=CC(=C6Cl)Cl)O)C(=O)N2)C(CC(=O)O)O)COC)C(C)(C)C"),
    ("lydiamycin A", 11628907,
     "CCCCCC(CC(=O)N1C(CCC=N1)C(=O)NC2COC(=O)C3CCCNN3C(=O)C(NC(=O)C(NC2=O)CC(C)C)C)C(=O)O"),
    ("piperazimycin A", 16103273,
     "CC(C)C=CC=CCC1C(=O)N2C(CC(CN2)Cl)C(=O)N3C(CC(CN3)O)C(=O)NC(C(=O)OCC(=O)N4C(CC(CN4)O)C(=O)N1)(C)CO"),
    ("azinothricin", 139589018,
     "CCC(C=C(C)C1C(CCC(O1)(C(CC)(C(=O)NC2C(OC(=O)C(NC(=O)C3CCCNN3C(=O)C(N(C(=O)C(N(C(=O)C4CCCNN4C2=O)O)COC)C)C)C(C)O)C(C)C)O)O)C)C(=O)C(=CC)C"),
    ("depsidomycin", 197287,
     "CCC(C)C(C(=O)NC1C(OC(=O)C2CCCNN2C(=O)C(NC(=O)C3CCCNN3C(=O)C(NC(=O)C(NC1=O)CC(C)C)C(C)C)CC(C)C)C)NC=O"),
    ("dentigerumycin E", 156581792,
     "CCC1C(CCC(O1)(C(C)(C(=O)NC2C(OC(=O)C(N(C(=O)C3CCCNN3C(=O)C4CCCNN4C(=O)CN(C(=O)C5CCCNN5C2=O)O)O)C(C)O)C(C)C)O)O)CC(=O)O"),
    ("incarnatapeptin A", 146684657,
     "CC1C2CCC(O1)(OC2C)C(C)(C(=O)NC(C(C(C)C)O)C(=O)N3C(CCCN3)C(=O)N(C(C)C(=O)N4C(CCCN4)C(=O)N5C(CCCN5)C(=O)O)O)O"),
]


def piz_rings(mol):
    """Atom-index sets of six-membered rings containing an N-N bond."""
    rings = []
    for ring in mol.GetRingInfo().AtomRings():
        if len(ring) != 6:
            continue
        nitrogens = [i for i in ring if mol.GetAtomWithIdx(i).GetAtomicNum() == 7]
        if len(nitrogens) == 2 and mol.GetBondBetweenAtoms(*nitrogens) is not None:
            rings.append(set(ring))
    return rings


def prep(smiles):
    mol = Chem.MolFromSmiles(smiles)
    rdDepictor.Compute2DCoords(mol)
    atoms = sorted({a for ring in piz_rings(mol) for a in ring})
    aset = set(atoms)
    bonds = [
        b.GetIdx()
        for b in mol.GetBonds()
        if b.GetBeginAtomIdx() in aset and b.GetEndAtomIdx() in aset
    ]
    return mol, atoms, bonds


def inner_svg(mol, legend, hl_atoms, hl_bonds, width, height, font_size):
    drawer = rdMolDraw2D.MolDraw2DSVG(width, height)
    opts = drawer.drawOptions()
    opts.legendFontSize = font_size
    opts.padding = 0.10
    drawer.DrawMolecule(
        mol,
        legend=legend,
        highlightAtoms=list(hl_atoms),
        highlightBonds=list(hl_bonds),
        highlightAtomColors={a: TINT for a in hl_atoms},
        highlightBondColors={b: TINT for b in hl_bonds},
    )
    drawer.FinishDrawing()
    svg = drawer.GetDrawingText()
    start = svg.index("<svg")
    start = svg.index(">", start) + 1
    return svg[start : svg.rindex("</svg>")]


def figure_panel():
    cell_w, cell_h, cols = 420, 340, 4
    cells = []
    for name, cid, smiles in PANEL:
        mol, atoms, bonds = prep(smiles)
        assert atoms, f"Piz/Dpz ring not found in {name} (PubChem CID {cid})"
        print(f"{name}: {len(piz_rings(mol))} N-N ring(s) highlighted (CID {cid})")
        cells.append(inner_svg(mol, name, atoms, bonds, cell_w, cell_h, 20))
    rows = (len(cells) + cols - 1) // cols
    width, height = cols * cell_w, rows * cell_h
    parts = [
        f"<svg xmlns='http://www.w3.org/2000/svg' version='1.1' width='{width}' height='{height}' viewBox='0 0 {width} {height}'>"
    ]
    for i, cell in enumerate(cells):
        x, y = (i % cols) * cell_w, (i // cols) * cell_h
        parts.append(
            f"<svg x='{x}' y='{y}' width='{cell_w}' height='{cell_h}' viewBox='0 0 {cell_w} {cell_h}'>{cell}</svg>"
        )
    parts.append("</svg>")
    (OUT / "piperazic-acid-natural-products-structures.svg").write_text("".join(parts))


if __name__ == "__main__":
    figure_panel()
    print("wrote:", *(p.name for p in OUT.glob("*.svg")))
