---
title: Elucidating Cyclo(L-Pro-L-Leu) with 1D and 2D NMR
summary: A guided examination of the proton, J-modulated carbon, COSY, edited HSQC, and HMBC evidence for the cyclic dipeptide Gancidin W.
section: exercise
format: reviewed-solution
category: structure-elucidation
audience:
  - junior
  - advanced
author:
  name: Hien Le
  orcid: 0000-0002-8834-593X
publishedAt: 2026-08-02
tags:
  - cyclic dipeptide
  - Gancidin W
  - structure elucidation
  - NMR
references:
  - citation: PubChem Compound Summary for CID 7074739, Gancidin W
    url: https://pubchem.ncbi.nlm.nih.gov/compound/7074739
license: CC BY-NC 4.0
draft: true
spectrum:
  viewerTitle: Reviewed Cyclo(L-Pro-L-Leu) dataset
  viewerDescription: Inspect the complete 1D and 2D NMR evidence used in the reviewed solution.
  compound:
    primaryName: Cyclo(L-Pro-L-Leu)
    synonym: Gancidin W
    formula: C11H18N2O2
    molecularWeight: 210.27
    pubchemCid: 7074739
    smiles: CC(C)C[C@H]1C(=O)N2CCC[C@H]2C(=O)N1
    inchiKey: SZJNCZMRZAUNQT-IUCAKERBSA-N
  experiments:
    - number: 31
      label: Proton NMR
      nuclei: 1H
      frequencyMHz: "600.4036"
      solvent: DMSO-d6
      temperatureK: 298
      pulseProgram: zg30
      dimensions: 1D
      role: primary
    - number: 32
      label: J-modulated carbon NMR
      nuclei: 13C
      frequencyMHz: "150.9858"
      solvent: DMSO-d6
      temperatureK: 298
      pulseProgram: jmod
      dimensions: 1D
      role: primary
    - number: 33
      label: COSY
      nuclei: 1H-1H
      frequencyMHz: "600.4045"
      solvent: DMSO-d6
      temperatureK: 298
      pulseProgram: cosygpmfppqf
      dimensions: 2D
      role: primary
    - number: 34
      label: Edited HSQC
      nuclei: 1H-13C
      frequencyMHz: "600.4045 / 150.9843"
      solvent: DMSO-d6
      temperatureK: 298
      pulseProgram: hsqcedetgpsp.3
      dimensions: 2D
      role: primary
    - number: 35
      label: HMBC
      nuclei: 1H-13C
      frequencyMHz: "600.4045 / 150.9888"
      solvent: DMSO-d6
      temperatureK: 298
      pulseProgram: hmbcetgpl3nd
      dimensions: 2D
      role: primary
    - number: 30
      label: Proton NMR, earlier acquisition
      nuclei: 1H
      frequencyMHz: "400.1328"
      solvent: DMSO-d6
      temperatureK: 300
      pulseProgram: zg30
      dimensions: 1D
      role: comparison
---

> **Scientific review gate:** This working article is intentionally excluded from the public build. Chemical-shift assignments and correlation interpretations below are candidates until Hien Le has reviewed them against the processed spectra.

## Problem and learning goals

This case study asks how a compact set of one- and two-dimensional NMR experiments supports the structure of Cyclo(L-Pro-L-Leu), a cyclic dipeptide also known as Gancidin W. The goal is not merely to reveal an assignment table, but to document how each experiment constrains the interpretation.

By the end of the reviewed article, a reader should be able to:

- distinguish observations from structural interpretation;
- follow proton spin systems through COSY;
- connect proton and carbon signals through edited HSQC;
- evaluate the longer-range HMBC evidence for sequence and ring closure; and
- recognize what changes, and what does not, between the 400 and 600 MHz proton spectra.

## Verified compound metadata

| Property | Value |
| --- | --- |
| Primary name | Cyclo(L-Pro-L-Leu) |
| Synonym | Gancidin W |
| Molecular formula | C11H18N2O2 |
| Molecular weight | 210.27 g mol-1 |
| PubChem CID | [7074739](https://pubchem.ncbi.nlm.nih.gov/compound/7074739) |
| Isomeric SMILES | `CC(C)C[C@H]1C(=O)N2CCC[C@H]2C(=O)N1` |
| InChIKey | `SZJNCZMRZAUNQT-IUCAKERBSA-N` |

The identity record comes from PubChem. Experimental assignments must still be established from the supplied spectra rather than copied from the identity record.

## Sample and acquisition set

Experiments 31–35 form the principal acquisition series on the 600 MHz instrument. Experiment 30 belongs to an earlier 400 MHz session and is treated only as a field-strength comparison.

| Exp. | Experiment | Nuclei | Frequency / MHz | Pulse program | Notes |
| ---: | --- | --- | --- | --- | --- |
| 31 | 1H | 1H | 600.4036 | `zg30` | 16 scans; primary proton spectrum |
| 32 | J-modulated 13C | 13C | 150.9858 | `jmod` | 8192 scans |
| 33 | COSY | 1H-1H | 600.4045 | `cosygpmfppqf` | 256 indirect points |
| 34 | Edited HSQC | 1H-13C | 600.4045 / 150.9843 | `hsqcedetgpsp.3` | 256 indirect points |
| 35 | HMBC | 1H-13C | 600.4045 / 150.9888 | `hmbcetgpl3nd` | 512 indirect points |
| 30 | 1H comparison | 1H | 400.1328 | `zg30` | 64 scans; earlier acquisition |

All six experiments were acquired in DMSO/DMSO-d6 at approximately 298–300 K. Public packages will use sanitized metadata because stale processed title fields incorrectly refer to an unrelated sample and CDCl3.

## 1H observations

The existing peak list provides candidate regions at 7.955, 4.128–4.103, 3.915, 3.432–3.334, 2.354–2.326, 2.151–2.113, 1.852–1.776, 1.018/1.006, and 0.854/0.842 ppm. These values are starting points for visual review, not final assignments.

The reviewed version must record chemical shift, multiplicity, integral, coupling information where resolved, and an explicit atom label for every retained signal.

## J-modulated 13C observations

The saved carbon peak list contains only 170.733, 45.096, 28.317, and 22.545 ppm and is visibly incomplete for an 11-carbon compound. The final carbon list must therefore come from visual inspection of the processed spectrum, including phase classification, rather than automatic reuse of the peak-picking file.

**Referencing review note.** The ¹H spectra are correctly referenced (residual DMSO-d₆ reads 2.500 ppm in experiments 30 and 31), but the processed ¹³C axis of experiment 32 places the residual DMSO-d₆ septet centre at 39.99 ppm instead of the Cambridge Isotope Laboratories NMR Solvent Data Chart value of 39.51 ppm. Before final ¹³C assignments are published, re-reference the ¹³C data (≈ −0.49 ppm) and adjust all candidate ¹³C values accordingly; the ¹³C dimensions of the 2D experiments (33–35) must be checked against the same reference.

## COSY spin systems

Candidate cross-peaks will be used to trace the proline and leucine proton networks. Every claimed link must be entered in the correlation table only after inspection at an appropriate contour level.

| Proton A | Proton B | Observed? | Interpretation | Reviewed |
| --- | --- | --- | --- | --- |
| To review | To review | Pending | Candidate proline spin system | No |
| To review | To review | Pending | Candidate leucine spin system | No |

## Edited HSQC direct attachments

The edited HSQC will establish one-bond proton-carbon attachments and distinguish phase classes supported by the acquisition. Overlap and diastereotopic methylene protons must be recorded rather than compressed into a single unsupported value.

| 1H / ppm | 13C / ppm | Edited phase | Candidate atom | Reviewed |
| ---: | ---: | --- | --- | --- |
| To review | To review | To review | To review | No |

## HMBC sequence and ring-closure evidence

Long-range correlations to both carbonyl regions are expected to carry the strongest sequence and cyclization evidence. The final narrative must identify each displayed correlation and explain which alternative it excludes; absence of a cross-peak will not be treated as proof without considering experiment sensitivity.

| Proton | Carbon | Correlation | Structural use | Reviewed |
| --- | --- | --- | --- | --- |
| To review | To review | Pending | Sequence or ring closure | No |

## 400 versus 600 MHz

Experiment 30 is not part of the same acquisition series as experiments 31–35. Once both spectra are aligned by chemical shift, this section will compare dispersion and apparent second-order behavior without implying that field strength is the only acquisition difference.

## Final assignment table

No final assignments are published yet.

| Atom | 13C / ppm | 1H / ppm | Multiplicity, J / Hz | COSY | Key HMBC | Reviewed |
| --- | ---: | --- | --- | --- | --- | --- |
| Pending | Pending | Pending | Pending | Pending | Pending | No |

## Limitations

The article uses one approved sample and its available experiment set. It does not claim an independent stereochemical determination beyond the stated identity, and it will distinguish spectral evidence from database metadata throughout.

## Data availability

Sanitized browser and archival packages are in preparation. Their raw and processed binary arrays will be checksummed against the immutable source before release. The original workstation folders will not be published directly or modified.
