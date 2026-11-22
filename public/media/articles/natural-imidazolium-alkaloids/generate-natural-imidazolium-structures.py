#!/usr/bin/env python3
"""Generate the comparison figure for the natural imidazolium article.

Connectivity sources:
- Lepidiline A: Cui et al., J. Nat. Prod. 2003, 66, 1101-1103,
  DOI 10.1021/np030031i; PubChem CID 404702 (cation drawn without chloride).
- Bacillimidazole A: Yan et al., Mar. Drugs 2022, 20, 43,
  DOI 10.3390/md20010043; Piedl et al., Molecules 2026, 31, 159,
  DOI 10.3390/molecules31010159 (C21H25N2+, m/z 305.2017).
Cations are drawn without counterions; no stereochemistry is implied.

Requires Python 3 and RDKit. Run from anywhere:
    python3 generate-natural-imidazolium-structures.py
The self-contained SVG is written next to this script.
"""

import re
from pathlib import Path

from rdkit import Chem
from rdkit.Chem import rdDepictor, rdMolDescriptors
from rdkit.Chem.Draw import rdMolDraw2D

OUT = Path(__file__).resolve().parent / "natural-imidazolium-alkaloids.svg"
BOND = "#3D2036"
HETERO = "#5E3A52"
TINT = (0.96, 0.84, 0.79)

PANELS = [
    (
        "Lepidiline A",
        "CC1=C([N+](=CN1Cc2ccccc2)Cc3ccccc3)C",
        "C19H21N2+",
        277.1699,
    ),
    (
        "Bacillimidazole A",
        "CC1=C([N+](=CN1CCc2ccccc2)CCc3ccccc3)C",
        "C21H25N2+",
        305.2017,
    ),
]

CELL_W, CELL_H = 480, 340


def imidazolium_ring(mol):
    """Return the five-membered ring containing two nitrogens and one N+."""
    matches = [
        ring
        for ring in mol.GetRingInfo().AtomRings()
        if len(ring) == 5
        and sum(mol.GetAtomWithIdx(i).GetAtomicNum() == 7 for i in ring) == 2
        and any(mol.GetAtomWithIdx(i).GetFormalCharge() == 1 for i in ring)
    ]
    assert len(matches) == 1, "Expected exactly one imidazolium ring"
    return set(matches[0])


def restyle_heteroatoms(svg, mol):
    """Recolor heteroatom glyphs and split adjacent bonds at their midpoint."""
    heteroatoms = {
        atom.GetIdx()
        for atom in mol.GetAtoms()
        if atom.GetAtomicNum() in (7, 8, 16)
    }
    for idx in heteroatoms:
        svg = re.sub(
            rf"(<path class='atom-{idx}'[^>]*?fill=')#[0-9A-Fa-f]{{6}}('/>)",
            rf"\g<1>{HETERO}\2",
            svg,
            flags=re.S,
        )

    for bond in mol.GetBonds():
        begin, end = bond.GetBeginAtomIdx(), bond.GetEndAtomIdx()
        if (begin in heteroatoms) == (end in heteroatoms):
            continue
        pattern = re.compile(
            rf"<path class='bond-{bond.GetIdx()} atom-{begin} atom-{end}' "
            rf"d='M (-?[\d.]+),(-?[\d.]+) L (-?[\d.]+),(-?[\d.]+)' "
            rf"style='([^']+)' />"
        )

        def split_bond(match):
            x0, y0, x1, y1 = map(float, match.group(1, 2, 3, 4))
            xm, ym = (x0 + x1) / 2, (y0 + y1) / 2
            style = match.group(5)
            classes = f"bond-{bond.GetIdx()} atom-{begin} atom-{end}"
            first = HETERO if begin in heteroatoms else BOND
            second = HETERO if end in heteroatoms else BOND
            first_style = re.sub(r"stroke:#[0-9A-Fa-f]{6}", f"stroke:{first}", style)
            second_style = re.sub(r"stroke:#[0-9A-Fa-f]{6}", f"stroke:{second}", style)
            return (
                f"<path class='{classes}' d='M {x0:.1f},{y0:.1f} L {xm:.1f},{ym:.1f}' style='{first_style}' />\n"
                f"<path class='{classes}' d='M {xm:.1f},{ym:.1f} L {x1:.1f},{y1:.1f}' style='{second_style}' />"
            )

        svg = pattern.sub(split_bond, svg)
    return svg


def inner_svg(name, smiles):
    mol = Chem.MolFromSmiles(smiles)
    assert mol is not None, name
    rdDepictor.Compute2DCoords(mol)
    atoms = imidazolium_ring(mol)
    bonds = [
        bond.GetIdx()
        for bond in mol.GetBonds()
        if bond.GetBeginAtomIdx() in atoms and bond.GetEndAtomIdx() in atoms
    ]

    drawer = rdMolDraw2D.MolDraw2DSVG(CELL_W, CELL_H)
    options = drawer.drawOptions()
    options.legendFontSize = 23
    options.padding = 0.12
    options.bondLineWidth = 2.0
    options.singleColourBonds = False
    palette = options.getAtomPalette()
    plum = (61 / 255, 32 / 255, 54 / 255, 1.0)
    violet = (94 / 255, 58 / 255, 82 / 255, 1.0)
    palette[6] = plum
    palette[7] = violet
    palette[8] = violet
    options.setAtomPalette(palette)
    options.setLegendColour(plum)
    options.setSymbolColour(violet)
    drawer.DrawMolecule(
        mol,
        legend=name,
        highlightAtoms=sorted(atoms),
        highlightBonds=bonds,
        highlightAtomColors={atom: TINT for atom in atoms},
        highlightBondColors={bond: TINT for bond in bonds},
    )
    drawer.FinishDrawing()
    svg = drawer.GetDrawingText()

    # Remove RDKit's white background so the site's paper colour shows through.
    svg = re.sub(r"<rect[^>]*fill(?:=|:)['\"]?#FFFFFF[^>]*>\s*</rect>", "", svg)
    svg = re.sub(r"<rect[^>]*fill=['\"]white['\"][^>]*>\s*</rect>", "", svg)

    # Apply the shared palette to bonds, carbon labels, and heteroatoms.
    svg = svg.replace("stroke:#000000", f"stroke:{BOND}")
    svg = svg.replace("stroke:rgb(0,0,0)", f"stroke:{BOND}")
    svg = svg.replace("fill:#000000", f"fill:{BOND}")
    svg = svg.replace("fill:rgb(0,0,0)", f"fill:{BOND}")
    for colour in ("#0000FF", "rgb(12,12,255)", "#FF0000", "rgb(255,12,12)"):
        svg = svg.replace(f"stroke:{colour}", f"stroke:{HETERO}")
        svg = svg.replace(f"fill:{colour}", f"fill:{HETERO}")
    svg = svg.replace("stroke-linecap:butt", "stroke-linecap:round")
    svg = restyle_heteroatoms(svg, mol)

    start = svg.index("<svg")
    start = svg.index(">", start) + 1
    return svg[start : svg.rindex("</svg>")]


def main():
    panels = []
    for index, (name, smiles, expected_formula, reported_mz) in enumerate(PANELS):
        mol = Chem.MolFromSmiles(smiles)
        assert mol is not None
        formula = rdMolDescriptors.CalcMolFormula(mol)
        assert formula == expected_formula, (name, formula, expected_formula)
        exact_mass = rdMolDescriptors.CalcExactMolWt(mol)
        # The paper reports monoisotopic m/z rounded to four decimal places;
        # RDKit's atomic masses can differ slightly at the final decimal.
        assert abs(exact_mass - reported_mz) < 0.0006, (name, exact_mass)
        body = inner_svg(name, smiles)
        panels.append(
            f"<svg x='{index * CELL_W}' y='0' width='{CELL_W}' height='{CELL_H}' "
            f"viewBox='0 0 {CELL_W} {CELL_H}'>{body}</svg>"
        )

    width = CELL_W * len(PANELS)
    out = f"""<svg xmlns='http://www.w3.org/2000/svg' width='{width}' height='{CELL_H}' viewBox='0 0 {width} {CELL_H}' role='img' aria-labelledby='title desc'>
<title id='title'>Lepidiline A and bacillimidazole A</title>
<desc id='desc'>Two natural products with a permanently cationic imidazolium ring highlighted in light red. Lepidiline A from maca has two N-benzyl substituents. Bacillimidazole A from a marine Bacillus has two N-phenethyl substituents. Both have methyl groups at C4 and C5 and hydrogen at C2. Cations are drawn without counterions.</desc>
{''.join(panels)}
</svg>
"""
    OUT.write_text(out)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
