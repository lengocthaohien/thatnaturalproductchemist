---
title: "Feature extraction decides what metabolomics can find: MZmine and MS-DIAL in practice"
summary: "A practical assessment of feature extraction for natural product metabolomics: what MZmine and MS-DIAL contribute, where their current versions differ, and why a feature table is an analytical model rather than a list of compounds."
section: opinion
format: tool-review
audience:
  - junior
  - advanced
author:
  name: Hien Le
  orcid: 0000-0002-8834-593X
publishedAt: 2026-11-15
tags:
  - feature extraction
  - untargeted metabolomics
  - LC-MS/MS
  - MZmine
  - MS-DIAL
  - dereplication
  - molecular networking
  - data processing
references:
  - citation: "Pluskal T., Castillo S., Villar-Briones A., Orešič M. MZmine 2: modular framework for processing, visualizing, and analyzing mass spectrometry-based molecular profile data. BMC Bioinformatics 2010, 11, 395"
    url: https://doi.org/10.1186/1471-2105-11-395
  - citation: "Schmid R., Heuckeroth S., Korf A., et al. Integrative analysis of multimodal mass spectrometry data in MZmine 3. Nat. Biotechnol. 2023, 41, 447–449"
    url: https://doi.org/10.1038/s41587-023-01690-2
  - citation: "Heuckeroth S., Damiani T., Smirnov A., et al. Reproducible mass spectrometry data processing and compound annotation in MZmine 3. Nat. Protoc. 2024, 19, 2597–2641"
    url: https://doi.org/10.1038/s41596-024-00996-y
  - citation: "Tsugawa H., Cajka T., Kind T., et al. MS-DIAL: data-independent MS/MS deconvolution for comprehensive metabolome analysis. Nat. Methods 2015, 12, 523–526"
    url: https://doi.org/10.1038/nmeth.3393
  - citation: "Takeda H., Matsuzawa Y., Takeuchi M., et al. MS-DIAL 5 multimodal mass spectrometry data mining unveils lipidome complexities. Nat. Commun. 2024, 15, 9903"
    url: https://doi.org/10.1038/s41467-024-54137-w
  - citation: "Nothias L.-F., Petras D., Schmid R., et al. Feature-based molecular networking in the GNPS analysis environment. Nat. Methods 2020, 17, 905–908"
    url: https://doi.org/10.1038/s41592-020-0933-6
  - citation: "MZmine 4.11.0 release notes, released 30 October 2026"
    url: https://github.com/mzmine/mzmine/releases/tag/v4.11
  - citation: "MS-DIAL 5.5.261105 release notes, released 5 November 2026"
    url: https://github.com/systemsomicslab/MsdialWorkbench/releases/tag/MSDIAL-v5.5.261105
  - citation: "MZmine documentation. Untargeted LC–MS workflow"
    url: https://mzmine.github.io/mzmine_documentation/latest/workflows/lcmsworkflow/lcms-workflow.html
  - citation: "MS-DIAL 5 tutorial. General introduction and data-processing workflow"
    url: https://systemsomicslab.github.io/msdial5tutorial/
license: CC BY-NC 4.0
draft: false
---

Untargeted metabolomics does not begin with statistics or molecular networking. It begins when software decides which signals deserve a row in a table. That decision controls what can be compared, annotated, or isolated. My position is simple: **MZmine is my default for modular natural product LC–MS/MS processing, while MS-DIAL is the stronger integrated choice for DIA-heavy and lipidomics work.** Neither produces a list of metabolites. Both produce a model of the data that must be inspected.

## A feature is not a compound

Feature extraction converts mass scans into chromatographic peaks, resolves overlapping peaks, groups isotopes and sometimes adducts, aligns corresponding signals across samples, and estimates their abundances. The resulting feature usually carries an *m/z*, retention time, intensity, and links to MS/MS spectra. A sample-by-feature table then supports statistics, dereplication, and feature-based molecular networking (FBMN).

This chain contains consequential choices. A noise threshold can erase a minor analogue. A chromatographic resolver can split one tailing peak or merge two coeluting compounds. Alignment tolerances can connect different isomers. Gap filling can recover a missed peak, but it cannot establish biological absence. One metabolite may generate several adducts, isotopologues, and in-source fragments; one feature may contain contributions from several metabolites.

![Schematic LC–MS feature-extraction workflow. Raw scans pass through mass detection, chromatogram building, peak resolving, and alignment to produce a sample-by-feature table. Each stage has a decision to inspect: noise thresholds, peak shape, coelution, and retention-time or mass matching. The table branches to statistics, molecular networking, and isolation rather than directly to compound identities.](/media/opinions/feature-extraction-metabolomics-tools/feature-extraction-workflow.svg)

*Figure 1. Feature extraction as a sequence of analytical decisions, not a single preprocessing step. A feature combines *m/z*, retention time (RT), abundance, and optionally MS/MS evidence; it is not synonymous with a metabolite. Blank subtraction, isotope and adduct handling, filtering, and export settings add further choices. The schematic does not prescribe universal thresholds or imply experimental intensities.*

## MZmine: control the chain

MZmine’s strength is modularity. For LC–MS, a typical chain runs from mass detection through chromatogram building and peak resolving to isotope grouping, alignment, gap filling, filtering, and export. Each step can be inspected, replaced, and saved in a batch workflow. The same platform extends to GC–MS, ion mobility, imaging, and several annotation and networking methods.

That transparency is valuable in complex extracts. I can inspect extracted-ion chromatograms, change the resolver when shoulders disappear, and export a feature table with MS/MS spectra for GNPS FBMN. Command-line batch execution makes the chosen chain easier to reproduce than a sequence of undocumented clicks.

The cost is parameter responsibility. Default settings are starting points, not validation. Optimizing only for the largest feature count rewards noise and split peaks. I would tune on representative samples and pooled quality controls, then inspect low-intensity, saturated, coeluting, and blank-associated signals before freezing the workflow.

## MS-DIAL: an integrated interpretation pipeline

MS-DIAL combines peak detection, deconvolution, alignment, normalization, and library-based annotation in a project-oriented environment. It supports vendor formats directly and spans LC–MS, GC–MS, ion mobility, imaging, DDA, DIA, and all-ion fragmentation workflows. Its handling of data-independent MS/MS and its extensive lipidomics resources are particular strengths.

This integration reduces handoffs. A user can move from aligned peaks to spectral libraries, candidate annotations, PCA, and exports without assembling every module separately. For lipidomics or SWATH/DIA data, that is often the more direct route. Console workflows support repeatable processing.

Integration does not make annotation independent evidence. An accurate-mass or library match remains subject to spectral quality, adduct assignment, chromatographic behavior, and library coverage. Predicted MS/MS libraries widen the search space but do not raise a match to structural confirmation. I would keep annotation levels explicit and inspect the spectra behind every feature that drives a conclusion.

| Decision | MZmine | MS-DIAL |
| --- | --- | --- |
| Strongest fit | Modular LC–MS/MS, FBMN, multimodal processing | Integrated DIA, lipidomics, and annotation |
| Working style | Configurable modules and batch files | Project-oriented pipeline and console |
| Main advantage | Fine control and chromatographic inspection | Fewer handoffs from peaks to candidates |
| Main caution | Parameter complexity | Treating integrated annotation as confirmation |

## What is current in November 2026

Release details below were checked on **15 November 2026**. They describe the latest stable releases, not a recommendation to update a validated study midway.

| Tool | Latest stable release | Relevant changes |
| --- | --- | --- |
| MZmine | 4.11.0; 30 October 2026 | Wizard parameter estimation and optimization; improved isotope finder; QC RSD columns and normalization options |
| MS-DIAL | 5.5.261105; 5 November 2026 | In-silico MSP library support; compound preview; lipidomics and annotation fixes |

MZmine 4.11.0 also introduces a new login and license system, so deployment requirements should be checked rather than inferred from an older installation. MS-DIAL 5.6.260323 remains labeled beta. The stable MS-DIAL release notes warn that representative-peak selection and annotator priority can change results even with unchanged settings. That is exactly why a publication should archive the full version, method or batch file, libraries, sample metadata, and exports—not merely write “processed with default parameters.”

## Where feature extraction earns its place

In natural product work, I use the aligned table for four tasks: comparing strains, treatments, or fractions; removing blank-associated signals; prioritizing features for dereplication and FBMN; and selecting peaks for isolation. The gain is chemical triage. A minor ion restricted to one active fraction can become worth pursuing even when it is invisible in a total-ion chromatogram.

The same workflow supports broader metabolomics: QC assessment, group comparisons, temporal changes, and hypothesis generation. It does not replace experimental design. Randomized acquisition, extraction and solvent blanks, pooled QCs, internal standards, and drift assessment belong upstream. Nor does feature abundance automatically provide absolute quantification; ionization response and matrix effects remain compound-dependent.

## My working rule

Choose the tool after the acquisition and the question, then validate the feature table before interpreting it. I would start MZmine for modular LC–MS/MS and FBMN, and MS-DIAL for integrated DIA or lipidomics. XCMS remains attractive for R-based, script-first studies, while OpenMS suits programmable pipelines and workflow engines; neither removes the inspection burden.

Most importantly, do not use agreement between two programs as automatic validation. Shared library hits or similar PCA plots may reflect shared assumptions. Inspect the raw chromatograms and spectra, retain uncertainty in annotation labels, and confirm decisive structures independently. Feature extraction is successful when it preserves the signals worth questioning—not when it produces the longest table.
