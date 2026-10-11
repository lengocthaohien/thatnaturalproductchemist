---
title: Comparing two commercial ampicillin products by 1H NMR
summary: A worked example showing how a single proton spectrum separates a clean ampicillin sodium salt from a less pure product — and why that difference matters when ampicillin is used as a selection marker.
section: example
format: worked-example
audience:
  - junior
  - advanced
author:
  name: Hien Le
  orcid: 0000-0002-8834-593X
publishedAt: 2026-11-10
tags:
  - ampicillin
  - beta-lactam
  - NMR
  - purity
  - selection marker
  - microbiology
references:
  - citation: PubChem Compound Summary for CID 6249, Ampicillin
    url: https://pubchem.ncbi.nlm.nih.gov/compound/6249
  - citation: Cambridge Isotope Laboratories, Inc., NMR Solvent Data Chart (residual DMSO-d₆ at 2.50 ppm)
license: CC BY-NC 4.0
draft: false
---

Ampicillin is a β-lactam antibiotic stocked by almost every molecular-biology laboratory — not to treat infection, but as a **selection marker**: a plasmid-borne *bla* (β-lactamase) gene lets only transformed cells survive on ampicillin medium. That selection quietly assumes the bottle really contains ampicillin, at the labelled potency.

This worked example compares two commercial ampicillin products by ¹H NMR: one quick spectrum separates a clean product from a compromised one, before either is trusted with a cloning experiment.

## The compound and its numbering

Ampicillin is a penam: a thiazolidine ring fused to a β-lactam, with a 2-amino-2-phenylacetamido side chain at C-6. The numbered positions below are used throughout the assignment table further down.

![Skeletal structure of ampicillin with numbered positions. The fused thiazolidine and beta-lactam core carries standard penam numbering: C-2 bears the gem-dimethyl group (methyl singlets at 1.46 and 1.57 ppm), H-3 is the thiazolidine methine (about 3.9 ppm), and H-5/H-6 are the beta-lactam methines (about 5.4 ppm). Primed numbers mark the side chain: C-1' amide carbonyl, H-2' methine (about 4.5 ppm), and phenyl positions 3' to 8' (5-proton multiplet at 7.3-7.4 ppm). Exchangeable NH and NH2 protons resonate weakly above 8.5 ppm.](/media/examples/ampicillin-purity-comparison/ampicillin-structure-numbered.svg)

*Figure 1. Ampicillin (drawn as the free acid; Product B is the sodium salt) with the position numbers used in the assignment table: standard penam numbering for the bicyclic core (2, 3, 5, 6) and primed numbers for the side chain (1′ amide carbonyl, 2′ methine, phenyl 3′–8′). The 6-acylamino side chain is β-oriented (solid wedge).*

## Why purity is not a detail here

Used for selection, ampicillin must kill or arrest every cell lacking the resistance marker; impurity causes two failure modes:

- **Lower effective potency.** Hydrolysed β-lactam and other inactive by-products lower the true active concentration; stringency drops and satellite colonies (cells surviving in the detoxified halo around a resistant colony) become more likely.
- **Misleading troubleshooting.** Satellite-covered plates look like a biology problem; when the real cause is a degraded antibiotic, time is spent chasing the wrong variable.

For a selection marker you therefore want the **purer** product — identity and potency are the whole point.

## The evidence

Both products were dissolved in DMSO-d₆ and their ¹H NMR spectra recorded under comparable conditions on the same day. The traces are stacked below, referenced to residual DMSO-d₆ at 2.50 ppm (Cambridge Isotope Laboratories NMR Solvent Data Chart).

![Stacked 1H NMR spectra of two commercial ampicillin products in DMSO-d6, 0-10 ppm. Lower trace, Product B (ampicillin sodium), is clean: methyl singlets at 1.46/1.57 ppm, methines near 3.9, 4.5 and 5.4 ppm, phenyl multiplet at 7.3-7.4 ppm. Upper trace, Product A, adds extra peaks at 1.0-1.2, 5.0, 5.8 and 8.8-9.2 ppm and aromatic shoulders to 7.6 ppm. The tall 2.50 ppm resonance in both traces is residual DMSO.](/media/examples/ampicillin-purity-comparison/proton-comparison-dmso-d6.svg)

*Figure 2. ¹H NMR spectra (DMSO-d₆) of the two products, 0–10 ppm window, rendered from the source vector data with local paths and acquisition titles removed; the scale was re-referenced to residual DMSO-d₆ at 2.50 ppm (Cambridge Isotope Laboratories NMR Solvent Data Chart). Product B is displayed at a relative scale of 0.1891, so peak heights are **not** comparable between traces — read only the number, position, and cleanliness of the resonances. The tall 2.50 ppm resonance, marked with arrows, is residual DMSO.*

### What each region shows

Positions refer to Figure 1; shifts are those of Product B.

| Assignment (Fig. 1) | Product B (sodium, clean) | Product A (less pure) |
| --- | --- | --- |
| 2-(CH₃)₂, two singlets | 1.46 and 1.57 ppm | Present, plus extra peaks (≈ 1.0, 1.2 ppm) |
| H-3 (singlet) | ≈ 3.9 ppm | Shifted/split (≈ 4.1 ppm) |
| H-2′ (singlet) | ≈ 4.5 ppm | Shifted/split (≈ 4.7 ppm); extra near 5.0 ppm |
| H-5 and H-6 (β-lactam CH) | One clean resonance ≈ 5.4 ppm | Split cluster (≈ 5.4, 5.5 ppm); extra signal ≈ 5.8 ppm |
| H-4′–H-8′ (phenyl, 5H) | Tidy multiplet, 7.3–7.4 ppm | Broader multiplet, shoulders to ≈ 7.6 ppm |
| NH/NH₂ (exchangeable) | One weak signal ≈ 8.7 ppm | Extra weak signals (≈ 8.8, 8.9, 9.2 ppm) |
| Residual DMSO | 2.50 ppm | 2.50 ppm |

Product B gives the spectrum expected of ampicillin: sharp methyl singlets, clean methines, and a tidy phenyl multiplet on a flat baseline. Product A shows the same core pattern — slightly shifted in places, as expected when the salt form or protonation state differs — plus extra upfield resonances, a crowded β-lactam/methine region, further exchangeable signals, and aromatic shoulders: the signature of structurally related impurities or degradation products.

## The decision

**Use Product B (the ampicillin sodium salt).** Its spectrum is the cleaner of the two — fewer, sharper resonances on a flat baseline — so each unit weight carries less inactive material: more reliable stringency and fewer satellite colonies.

Product A is largely ampicillin — the main resonances are present — but the extra resonances mean its active concentration is lower and less certain than labelled: the wrong choice when selection depends on a known, reliable dose.

## Limitations

- This comparison rests on a single ¹H spectrum per product in one solvent: a qualitative purity screen, not an assay.
- The traces were plotted at different display scales (Product B at 0.1891) with no internal integration standard, so **peak heights cannot be compared quantitatively** and no molar purity percentage is reported.
- ¹H NMR detects proton-bearing impurities but is insensitive to inorganic salts and does not prove stereochemical integrity. Exact purity would require a quantitative assay (e.g. qNMR with a certified standard, or HPLC against a reference).
