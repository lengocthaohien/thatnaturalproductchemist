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
publishedAt: 2026-08-30
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
license: CC BY-NC 4.0
draft: false
---

Ampicillin is a β-lactam antibiotic that almost every molecular-biology laboratory keeps in stock, not to treat infection but as a **selection marker**. A plasmid carrying a *bla* (β-lactamase) gene lets only transformed cells survive on ampicillin-containing medium. That selection step depends on a quiet assumption: the ampicillin in the bottle is actually ampicillin, at the potency the label claims.

This worked example compares two commercial ampicillin products by ¹H NMR and shows how a single, quick spectrum distinguishes a clean product from a compromised one — before either is trusted with a cloning experiment.

## Why purity is not a detail here

When ampicillin is used for selection, its job is to kill or arrest every cell that does not carry the resistance marker. Two failure modes follow directly from impurity:

- **Lower effective potency.** If a fraction of the material is hydrolysed β-lactam or other inactive by-products, the true concentration of active ampicillin is below the nominal value. The selection stringency drops, and slow-growing or satellite colonies (cells surviving in the detoxified halo around a resistant colony) become far more likely.
- **Misleading troubleshooting.** A plate overgrown with satellites looks like a biology problem. When the real cause is a degraded antibiotic, time is spent chasing the wrong variable.

For a selection marker you therefore want the **purer** product. Identity and potency are the whole point; there is no "close enough."

## The evidence

Both products were dissolved in DMSO-d₆ and their ¹H NMR spectra recorded under comparable conditions on the same day. The two traces are stacked below, on a shared chemical-shift scale.

![Stacked 1H NMR spectra of two commercial ampicillin products in DMSO-d6. The lower trace, Product B (ampicillin sodium), is clean: an aromatic multiplet around 7.3 ppm, a two-proton signal near 3.25 ppm, and a methyl singlet near 1.48 ppm. The upper trace, Product A, shows additional split resonances between 6.9 and 7.2 ppm and several extra small peaks, indicating lower purity.](/media/examples/ampicillin-purity-comparison/proton-comparison-dmso-d6.svg)

*Figure 1. ¹H NMR spectra (DMSO-d₆) of two commercial ampicillin products on a shared chemical-shift axis (displayed window ≈ 0.8–7.9 ppm). Traces were recovered from the source vector data and rendered with local file paths and acquisition titles removed. Product B was plotted at a relative display scale of 0.1891, so absolute peak heights are **not** comparable between the two traces — only the number, position, and cleanliness of the resonances should be read.*

### What each region shows

| Region / ppm | Product B (sodium, clean) | Product A (less pure) |
| --- | --- | --- |
| 7.2–7.5 aromatic | One tidy phenyl multiplet centred near 7.3 ppm | Extra split resonances and shoulders across 6.9–7.2 ppm |
| 3.2–3.4 | A single dominant signal near 3.25 ppm | Several additional peaks (≈ 3.11, 3.19, 3.20, 3.35 ppm) |
| 1.9–2.4 | Quiet baseline | Extra small peaks (≈ 1.94, 2.03, 2.39 ppm) |
| 1.4–1.5 methyl | A single sharp singlet near 1.48 ppm | Broader, less defined upfield region |

Product B gives the spectrum expected of ampicillin: a clean aromatic phenyl group, well-resolved aliphatic signals, and sharp methyls, with a flat baseline in between. Product A shows the same core resonances but adds a cluster of split signals in the aromatic region and a scattering of extra peaks elsewhere — the signature of a sample carrying structurally related impurities or degradation products.

## The decision

**Use Product B (the ampicillin sodium salt).** Its spectrum is the cleaner of the two: fewer, sharper resonances and a flat baseline, meaning less inactive or interfering material per unit weight. For a selection marker, that translates directly into more reliable stringency and fewer satellite colonies.

Product A is not necessarily useless — the main resonances are present, so it is largely ampicillin — but its extra resonances mean the active concentration is lower and less certain than the label implies. It is the wrong choice when selection depends on a known, reliable dose.

## Limitations

- This comparison rests on a single ¹H spectrum per product in one solvent; it is a qualitative purity screen, not an assay.
- The two traces were plotted at different display scales (Product B at 0.1891), so **peak heights cannot be compared quantitatively**. No internal integration standard was used, so no molar purity percentage is reported.
- ¹H NMR detects proton-bearing impurities but is insensitive to inorganic salts and does not by itself prove stereochemical integrity. A quantitative assay (e.g. qNMR with a certified standard, or HPLC against a reference) would be needed to assign an exact purity value.
