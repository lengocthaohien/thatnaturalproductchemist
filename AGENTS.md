# Agent guidelines

Standing rules for this repository. Also read [CONTRIBUTING.md](CONTRIBUTING.md), [ideology.md](ideology.md), [docs/media-authoring.md](docs/media-authoring.md), and [docs/publication-rules.md](docs/publication-rules.md) before editing content or figures.

## General publication rules

- [docs/publication-rules.md](docs/publication-rules.md) is the single ruleset for every new publication in all four sections (articles, opinions, exercises, examples) and must be applied whenever a new publication is planned or added. In short: **declare the target length first** (short ≈ 500, medium ≈ 1000, or long ≈ 1500 words — ask for it if not given); write in the concise voice of an experienced natural product chemist for a quick read; draw all chemical structures through the shared RDKit pipeline and site palette (`#3D2036` bonds, `#5E3A52` heteroatoms, `#8C6D1F` position numbers, light red `(0.96, 0.84, 0.79)` highlight, transparent SVG background) with position numbers synced to the assignment tables; and follow the general and NMR table rules summarized below.

## Articles section

- Every entry in the Articles section declares exactly one `paperType` in its frontmatter: `chemical-diversity`, `biosynthesis`, `research-methodology`, or `review`. This label replaces the old generic "paper perspective" kicker above the article title. Definitions and the build-time validation rule live in [docs/adding-content.md](docs/adding-content.md).

## NMR and data tables

- All tables in every section (articles, opinions, exercises, examples) share one systematic alignment: **headers centred, purely numeric cells centred, text and text+number cells left-aligned**. This is enforced at build time by `src/lib/table-alignment-plugin.mjs` plus the `.cell-number` / `.cell-text` rules in `src/styles/global.css` — write plain Markdown tables without column alignment markers and never add per-table alignment markup or inline styles.

## NMR data and spectra

- **Always calibrate NMR data to the solvent reference values in [`nmrsolventschart_001.pdf`](nmrsolventschart_001.pdf)** (Cambridge Isotope Laboratories, Inc. NMR Solvent Data Chart) — e.g. residual DMSO-d₆ at ¹H 2.50 ppm and ¹³C 39.51 ppm. Never use other conventions such as 2.4 ppm, and state the referencing in captions.
- **Notes and labels on NMR spectra go in the top-left corner** of the plotting area, never in the middle of the spectrum. Provenance footnotes sit below the axis.
- **Annotate the residual solvent peak directly**: place the solvent note on top of or next to the solvent peak and draw an arrow pointing to the peak whenever the format allows.
- **Every NMR figure in every section (articles, opinions, exercises, examples) uses the shared light background** from [`scripts/nmr-figure-style.mjs`](scripts/nmr-figure-style.mjs) (`SPECTRUM_BACKGROUND`, currently `#F4F1EA`). Never hard-code a different background in a figure script or hand-authored spectrum SVG. The only exception is the decorative hero spectrum on the homepage (`src/pages/index.astro`), which is not a data figure.
