#!/usr/bin/env python3
"""Regenerate the static structure figures for the azodyrecin/azoxy article.

Requires RDKit (pip install rdkit). Run from anywhere; output SVGs are written
next to this script. Structures are drawn from PubChem connectivity records
(no stereochemical claims beyond those records); the azoxy group is
highlighted in red in every panel.
"""

from pathlib import Path

from rdkit import Chem
from rdkit.Chem import rdDepictor
from rdkit.Chem.Draw import rdMolDraw2D

OUT = Path(__file__).resolve().parent
TINT = (0.96, 0.84, 0.79)  # light red tint behind the azoxy group
AZOXY = Chem.MolFromSmarts("[NX2]=[NX3+]-[OX1-]")

FONT = "Georgia, 'Times New Roman', serif"

PANEL = [
    ("elaiomycin", "CCCCCCC=C[N+](=NC(COC)C(C)O)[O-]"),
    ("valanimycin", "CC(C)C[N+](=NC(=C)C(=O)O)[O-]"),
    ("jietacin A", "CC(C)CCCCCC(=O)CCCCCCCN=[N+](C=C)[O-]"),
    ("azoxybacilin", "CN=[N+](CCC(C(=O)O)N)[O-]"),
    ("maniwamycin A", "CCCCC=C[N+](=NC(C)C(=O)C)[O-]"),
    ("azodyrecin A", "CC(C)CCCCCCCCCC=C[N+](=NC(C)C(=O)OC)[O-]"),
    ("azoxymycin A", "C1=CC(=CC=C1C=CC=CC(=O)NC(CCC(=O)N)C(=O)O)N=[N+](C2=CC=C(C=C2)C=CC=CC(=O)NC(CCC(=O)N)C(=O)O)[O-]"),
    ("cycasin", "C[N+](=NCOC1C(C(C(C(O1)CO)O)O)O)[O-]"),
]


def prep(smiles):
    mol = Chem.MolFromSmiles(smiles)
    rdDepictor.Compute2DCoords(mol)
    atoms = sorted({a for match in mol.GetSubstructMatches(AZOXY) for a in match})
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
    cell_w, cell_h, cols = 370, 300, 4
    cells = []
    for name, smiles in PANEL:
        mol, atoms, bonds = prep(smiles)
        assert atoms, f"azoxy group not found in {name}"
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
    (OUT / "natural-azoxy-compounds-structures.svg").write_text("".join(parts))


LADDER = [
    # (smiles, legend, {atomIdx: label}, highlighted atoms, (arrow line 1, line 2))
    ("CCN", "fatty amine", {0: "R"}, (2,), ("AzdH \u00b7 AzdR", "N-hydroxylation")),
    ("CCNO", "hydroxylamine", {0: "R"}, (2, 3), ("AzdA", "Ala transfer")),
    ("CCNNC", "hydrazine", {0: "R", 4: "R'"}, (2, 3), ("unassigned", "dehydrogenation")),
    ("CCN=NC", "azo", {0: "R", 4: "R'"}, (2, 3), ("AzdB", "N-oxidation")),
    ("CCN=[N+](C)[O-]", "azoxy", {0: "R", 4: "R'"}, (2, 3, 5), None),
]

CELL_W, CELL_H, GAP = 240, 200, 116


def mol_inner_svg(smiles, legend, labels, hl_atoms):
    mol = Chem.MolFromSmiles(smiles)
    rdDepictor.Compute2DCoords(mol)
    for idx, text in labels.items():
        mol.GetAtomWithIdx(idx).SetProp("atomLabel", text)
    hl_bonds = []
    for i in hl_atoms:
        for j in hl_atoms:
            if j > i:
                bond = mol.GetBondBetweenAtoms(i, j)
                if bond is not None:
                    hl_bonds.append(bond.GetIdx())
    return inner_svg(mol, legend, list(hl_atoms), hl_bonds, CELL_W, CELL_H, 17)


def figure_ladder():
    width = len(LADDER) * CELL_W + (len(LADDER) - 1) * GAP
    height = CELL_H + 20
    parts = [
        f"<svg xmlns='http://www.w3.org/2000/svg' version='1.1' width='{width}' height='{height}' viewBox='0 0 {width} {height}'>",
        "<defs><marker id='arr' viewBox='0 0 10 10' refX='9' refY='5' markerWidth='7' markerHeight='7' orient='auto-start-reverse'><path d='M0,0 L10,5 L0,10 z' fill='#222'/></marker></defs>",
    ]
    for i, (smiles, legend, labels, hl_atoms, arrow_label) in enumerate(LADDER):
        x = i * (CELL_W + GAP)
        inner = mol_inner_svg(smiles, legend, labels, hl_atoms)
        parts.append(
            f"<svg x='{x}' y='0' width='{CELL_W}' height='{CELL_H}' viewBox='0 0 {CELL_W} {CELL_H}'>{inner}</svg>"
        )
        if arrow_label is not None:
            x0 = x + CELL_W + 10
            x1 = x + CELL_W + GAP - 10
            y = CELL_H // 2 - 28
            parts.append(
                f"<line x1='{x0}' y1='{y}' x2='{x1}' y2='{y}' stroke='#222' stroke-width='1.4' marker-end='url(#arr)'/>"
            )
            cx = (x0 + x1) / 2
            line1, line2 = arrow_label
            parts.append(
                f"<text x='{cx}' y='{y + 22}' font-family=\"{FONT}\" font-size='13' fill='#222' text-anchor='middle'>{line1}</text>"
            )
            parts.append(
                f"<text x='{cx}' y='{y + 38}' font-family=\"{FONT}\" font-size='12' fill='#555' text-anchor='middle'>{line2}</text>"
            )
    parts.append("</svg>")
    (OUT / "azoxy-bond-oxidation-ladder.svg").write_text("".join(parts))


if __name__ == "__main__":
    figure_panel()
    figure_ladder()
    print("wrote:", *(p.name for p in OUT.glob("*.svg")))
