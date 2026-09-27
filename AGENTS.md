# Agent guidelines

Standing rules for this repository. Also read [CONTRIBUTING.md](CONTRIBUTING.md), [ideology.md](ideology.md), and [docs/media-authoring.md](docs/media-authoring.md) before editing content or figures.

## Articles section

- Every entry in the Articles section declares exactly one `paperType` in its frontmatter: `chemical-diversity`, `biosynthesis`, `research-methodology`, or `review`. This label replaces the old generic "paper perspective" kicker above the article title. Definitions and the build-time validation rule live in [docs/adding-content.md](docs/adding-content.md).

## NMR data and spectra

- **Always calibrate NMR data to the solvent reference values in [`nmrsolventschart_001.pdf`](nmrsolventschart_001.pdf)** (Cambridge Isotope Laboratories, Inc. NMR Solvent Data Chart) — e.g. residual DMSO-d₆ at ¹H 2.50 ppm and ¹³C 39.51 ppm. Never use other conventions such as 2.4 ppm, and state the referencing in captions.
- **Notes and labels on NMR spectra go in the top-left corner** of the plotting area, never in the middle of the spectrum. Provenance footnotes sit below the axis.
- **Annotate the residual solvent peak directly**: place the solvent note on top of or next to the solvent peak and draw an arrow pointing to the peak whenever the format allows.
