# General publication rules

These rules apply to **every** publication on That Natural Product Chemist, in all four sections (articles, opinions, exercises, examples). Apply them whenever a new publication is planned or added, alongside [../AGENTS.md](../AGENTS.md), [../CONTRIBUTING.md](../CONTRIBUTING.md), [../ideology.md](../ideology.md), [adding-content.md](adding-content.md), and [media-authoring.md](media-authoring.md).

## 1. Length

Every new publication starts by **declaring its target length**. Ask for it (or state it) before writing begins; it shapes the outline, the number of figures, and the depth of the discussion.

| Tier | Target length | Typical use |
| --- | --- | --- |
| Short | ~500 words | One observation, one method note, one quick comparison. Single figure or table. |
| Medium | ~1000 words | Standard entry: context, evidence, interpretation, limitations. Two to four figures/tables. |
| Long | ~1500 words | Full elucidation walk-through, multi-experiment argument, or broad paper perspective. |

- The word count covers the Markdown body text (excluding frontmatter, figure captions, tables, and reference lists).
- Stay within roughly ±20% of the declared tier. If the draft outgrows it, either cut or split the piece — do not silently drift into a longer tier.
- The declared tier is recorded in the planning notes or pull-request description so reviewers can check the fit.

## 2. Voice and style

Write as an **experienced natural product chemist** talking to a colleague: confident, direct, and economical.

- **Short and concise.** Prefer short sentences and short paragraphs. One idea per paragraph. The whole piece should be readable in a few minutes.
- **Lead with the point.** State the question and why it matters in the opening paragraph; put the answer or decision before the caveats.
- **Separate the three layers** (see [ideology.md](../ideology.md)): observation, inference, opinion. Never let them blur; name uncertainty explicitly.
- **No filler.** No throat-clearing introductions, no restating the abstract of the paper under discussion, no adjectives that carry no information.
- **Quick-read formatting.** Use `##` section headings, short lists where they genuinely help, and tables for parallel data. Body text is justified automatically — never hand-format alignment (see [adding-content.md](adding-content.md) §4).
- **Depth lives in the apparatus, not the prose.** Acquisition details, complete data tables, and downloadable evidence carry the rigor; the running text stays light.


## 3. Chemical structures

All chemical-structure figures follow one visual system, taken from the existing publications (e.g. the ampicillin, azoxy-compound, piperazic-acid, and selenoneine figures). The rules below are mandatory for every new structure figure.

### Generation

- Draw structures with **RDKit** from a SMILES string, via a committed generation script (kept in `scripts/` or next to the figure under `public/media/{section}/{entry-slug}/`, as in `scripts/generate-ampicillin-structure.py`). Figures must be reproducible, never hand-edited exports.
- Source connectivity (and stereochemistry, when claimed) from a citable record — typically the **PubChem CID**, listed in the script header. Make no stereochemical claims beyond that record or the entry's own evidence.
- Output a **self-contained SVG** with a **transparent background** (remove RDKit's white background rectangle) so the site's paper background shows through. Never JPEG; see [media-authoring.md](media-authoring.md).

### Palette and typography

Use the site palette exactly as in the current scripts; do not invent new colors:

| Element | Color | Value |
| --- | --- | --- |
| Carbon skeleton / bonds | dark plum | `#3D2036` |
| Heteroatom glyphs and adjacent bond halves | muted violet | `#5E3A52` |
| Position numbers | gold | `#8C6D1F`, bold DM Mono |
| Structural highlight (reactive group, motif of interest) | light red tint | RGB `(0.96, 0.84, 0.79)` |

- Recolor RDKit's default N/O/S blues and reds to the heteroatom color, and round the bond line caps.
- Highlight the functional group or motif the entry discusses (e.g. the azoxy group, the N–N ring) with the light red tint — consistently across every panel of a multi-structure figure.
- Center the drawing on a wide canvas (≈1000 px viewBox, drawing occupying ~60% of the width) so it renders at a modest size at full column width.

### Numbering and text integration

- If the entry contains an assignment or data table, the structure figure carries **position numbers**, and those numbers are the atom labels used in the table. Keep the two in sync: if the table changes, regenerate the figure (the script documents this dependency in its header).
- Use the compound's standard numbering scheme where one exists (e.g. penam numbering, primed numbers for a side chain) and state the scheme in the caption.
- Every structure figure needs descriptive **alt text** (what is drawn, including numbering and stereochemistry) and a nearby **caption** stating what form is drawn (free acid vs. salt, tautomer), what the numbering is, and what to inspect — per [media-authoring.md](media-authoring.md) §3.
- For **exercises**, structure figures must never leak the answer before the solution stage — no compound names, structures, formulas, or database identifiers in filenames, metadata, or early figures (see [../CONTRIBUTING.md](../CONTRIBUTING.md)).


## 4. Tables, including NMR tables

### General table rules (all sections)

- Write **plain Markdown tables** without column-alignment markers (`---:`, `:--:`); markers are stripped at build time.
- One systematic alignment is enforced by `src/lib/table-alignment-plugin.mjs` and the `.cell-number` / `.cell-text` rules in `src/styles/global.css`: **headers centred, purely numeric cells centred, text and mixed text+number cells left-aligned**. Compose cell content accordingly — a cell is centred only if it contains nothing but a number.
- Keep tables readable on small screens: few columns, short cell text, no merged cells.

### NMR data tables

- **Calibration.** All shifts are referenced to the Cambridge Isotope Laboratories NMR Solvent Data Chart ([`nmrsolventschart_001.pdf`](../nmrsolventschart_001.pdf)) — e.g. residual DMSO-d₆ at δH 2.50 ppm and δC 39.51 ppm, never 2.4 ppm. State the referencing in the caption or the text next to the table.
- **Required information per signal.** An assignment table records, for every retained signal: chemical shift (ppm), multiplicity with coupling constants (J / Hz) where resolved, integral (¹H), and an explicit atom label matching the numbered structure figure (§3). Correlation tables (COSY, HSQC, HMBC) name both partners and the structural use of each correlation.
- **Observation before assignment.** Distinguish candidate values from reviewed ones; overlap, diastereotopic pairs, and ambiguous signals are recorded as such, never compressed into a single unsupported value.
- **Acquisition context.** The table or its caption names the spectrometer frequency, solvent, and temperature (these also live in the `spectrum` frontmatter when the NMRium viewer is used — see [adding-content.md](adding-content.md) §2).
- NMR **figures** accompanying the table follow the shared spectrum conventions in [media-authoring.md](media-authoring.md): light background `#F4F1EA` from `scripts/nmr-figure-style.mjs`, notes in the top-left corner, and the residual solvent peak annotated directly with an arrow.
