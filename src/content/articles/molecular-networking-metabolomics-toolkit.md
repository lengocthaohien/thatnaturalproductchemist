---
title: "Molecular networking is a map, not a structure: GNPS, MetGem, and Workflow4Metabolomics in practice"
summary: "A practical assessment of molecular networking and untargeted metabolomics platforms for natural product research: where GNPS, MetGem, and Workflow4Metabolomics excel, where they stop, and how to combine them without turning spectral similarity into structural proof."
section: opinion
format: tool-review
audience:
  - junior
  - advanced
author:
  name: Hien Le
  orcid: 0000-0002-8834-593X
publishedAt: 2026-11-08
updatedAt: 2026-11-08
tags:
  - molecular networking
  - untargeted metabolomics
  - LC-MS/MS
  - GNPS
  - MetGem
  - Workflow4Metabolomics
  - dereplication
  - natural products
references:
  - citation: "Watrous J., Roach P., Alexandrov T., et al. Mass spectral molecular networking of living microbial colonies. Proc. Natl. Acad. Sci. USA 2012, 109, E1743–E1752"
    url: https://doi.org/10.1073/pnas.1203689109
  - citation: "Wang M., Carver J. J., Phelan V. V., et al. Sharing and community curation of mass spectrometry data with Global Natural Products Social Molecular Networking. Nat. Biotechnol. 2016, 34, 828–837"
    url: https://doi.org/10.1038/nbt.3597
  - citation: "Nothias L.-F., Petras D., Schmid R., et al. Feature-based molecular networking in the GNPS analysis environment. Nat. Methods 2020, 17, 905–908"
    url: https://doi.org/10.1038/s41592-020-0933-6
  - citation: "Olivon F., Elie N., Grelier G., Roussi F., Litaudon M., Touboul D. MetGem software for the generation of molecular networks based on the t-SNE algorithm. Anal. Chem. 2018, 90, 13900–13908"
    url: https://doi.org/10.1021/acs.analchem.8b03099
  - citation: "Giacomoni F., Le Corguillé G., Monsoor M., et al. Workflow4Metabolomics: a collaborative research infrastructure for computational metabolomics. Bioinformatics 2015, 31, 1493–1495"
    url: https://doi.org/10.1093/bioinformatics/btu813
  - citation: "Guitton Y., Tremblay-Franco M., Le Corguillé G., et al. Create, run, share, publish, and reference your LC–MS, FIA–MS, GC–MS, and NMR data analysis workflows with the Workflow4Metabolomics 3.0 Galaxy online infrastructure for metabolomics. Int. J. Biochem. Cell Biol. 2017, 93, 89–101"
    url: https://doi.org/10.1016/j.biocel.2017.07.002
  - citation: "Schmid R., Heuckeroth S., Korf A., et al. Integrative analysis of multimodal mass spectrometry data in MZmine 3. Nat. Biotechnol. 2023, 41, 447–449"
    url: https://doi.org/10.1038/s41587-023-01690-2
  - citation: "Tsugawa H., Cajka T., Kind T., et al. MS-DIAL: data-independent MS/MS deconvolution for comprehensive metabolome analysis. Nat. Methods 2015, 12, 523–526"
    url: https://doi.org/10.1038/nmeth.3393
  - citation: "Schymanski E. L., Jeon J., Gulde R., et al. Identifying small molecules via high resolution mass spectrometry: communicating confidence. Environ. Sci. Technol. 2014, 48, 2097–2098"
    url: https://doi.org/10.1021/es5002105
  - citation: "GNPS2 Documentation. Feature-Based Molecular Networking"
    url: https://wang-bioinformatics-lab.github.io/GNPS2_Documentation/fbmn/
license: CC BY-NC 4.0
draft: false
---

Molecular networking changed untargeted natural product research by giving LC–MS/MS data a chemical geography. Instead of inspecting thousands of features one by one, we can ask which compounds fragment alike, which extracts contain related chemistries, and where an uncharacterized metabolite sits relative to a known one. My position is simple: **GNPS is the strongest general environment for networking and shared spectral evidence; MetGem is a useful local exploratory alternative; Workflow4Metabolomics is most valuable upstream, where reproducible processing and statistics decide whether a comparison is trustworthy.** None replaces structure elucidation.

## From spectra to molecular families

A molecular network begins with MS/MS spectra. In classical molecular networking, each node represents a spectrum or consolidated precursor; in feature-based molecular networking (FBMN), nodes represent LC–MS features after detection and alignment. An edge connects two nodes when their fragmentation spectra pass chosen similarity and matched-peak thresholds.

The modified cosine score is the key device. It rewards shared fragment ions and neutral losses, but also allows fragment peaks to shift by the precursor mass difference. Two related molecules can therefore connect when a substitution changes their precursor masses while preserving part of their fragmentation behavior. This is an inference about spectral relatedness, not a structure assignment.

That distinction matters. Related compounds may separate when ionization or collision conditions change their spectra. Unrelated compounds may connect through common fragments, noise, or chimeric spectra. Adducts, isotopes, in-source fragments, and co-isolated precursors further complicate the graph. Cosine thresholds control which relationships become visible; they do not convert those relationships into facts.

## Why this leverages natural product discovery

Natural product extracts are mixtures of analogues, and that redundancy becomes useful in a network. A library-anchored node can orient an entire molecular family during dereplication. Neighboring nodes then suggest mass differences and substitution patterns to investigate. Conversely, a family without convincing database matches can become a priority for isolation, even when none of its members is individually identifiable.

Networks also organize comparisons. Node size or color can show abundance across species, tissues, culture conditions, or bioactive fractions. A chemotype enriched in an active fraction is a better isolation target than an anonymous high-intensity peak. The scientific contribution is therefore not simply faster annotation: it is **prioritization with chemical context**.

The limitation is equally important. An unannotated cluster is not evidence of new chemistry, and a new analogue is not established by a mass difference. Isolation, accurate MS, NMR, and appropriate standards remain the evidence chain.

## The research groups behind the platforms

These tools reflect their research communities. GNPS emerged from a UC San Diego–led collaboration involving Pieter Dorrestein, Mingxun Wang, Pavel Pevzner, and many natural product partners; GNPS2 is now built and maintained by Wang’s laboratory at UC Riverside. MetGem was developed at CNRS/ICSN by Florent Olivon, Nicolas Elie, and colleagues working across the natural product and mass spectrometry teams of Marc Litaudon and David Touboul. W4M came from a French infrastructure collaboration across the French Bioinformatics Institute (IFB) and MetaboHUB, with contributions from LABERCA and hosting support from Genotoul. Those origins help explain their different priorities: community spectral knowledge at GNPS, exploratory molecular visualization at MetGem, and shared, reproducible metabolomics workflows at W4M.

## GNPS: the reference ecosystem

GNPS made molecular networking broadly accessible and, more importantly, attached it to spectral libraries, public datasets, and community curation. Its enduring contribution is social as much as computational: results can be revisited, public data reanalyzed, and annotations discussed against inspectable spectra.

Classical networking remains useful for a rapid spectral overview. For comparative LC–MS studies, I prefer FBMN. It retains feature intensity and retention-time information, supports sample-level mappings, and can incorporate adduct relationships through ion-identity approaches. MZmine, MS-DIAL, XCMS, and other processors can supply the feature table and MS/MS summary required by GNPS2.

GNPS still depends on upstream decisions. Poor chromatographic alignment or aggressive blank filtering cannot be repaired by an attractive network. Library coverage is uneven, spectral matches need inspection, and propagated annotations must be labeled as hypotheses. I would report software versions, preprocessing parameters, cosine and matched-peak thresholds, library versions, and annotation confidence alongside every figure.

## MetGem: local exploration with a different view

MetGem offers standalone, open-source visualization of MS/MS data through molecular networks and t-distributed stochastic neighbor embedding (t-SNE). Its interactive views make it attractive for inspecting a project locally, testing spectral-similarity settings, and teaching the difference between individual spectra and molecular families.

The t-SNE projection is both a strength and a trap. It can reveal local spectral neighborhoods without relying only on graph layout, but distances between remote groups and the apparent sizes of clusters are not quantitative measures of structural diversity. Perplexity and other settings affect the display. I use MetGem as a second lens, not as independent confirmation of a GNPS network built from the same spectra.

MetGem also does not remove the need for rigorous feature processing or experimental statistics. Its value lies in exploration and visualization, not in providing a complete metabolomics design.

## Workflow4Metabolomics: reproducibility before networking

Workflow4Metabolomics (W4M) addresses a different bottleneck. Built on Galaxy, it chains steps such as XCMS preprocessing, quality control, statistical analysis, and annotation into reusable workflows. Its support for LC–MS, GC–MS, FIA–MS, and NMR makes it broader than a molecular-networking platform.

This is where I would start a multi-group study with pooled quality controls, blanks, batch correction, and formal comparisons. Histories and workflows make analytical choices easier to share and repeat than a sequence of manual desktop operations. That is a substantial scientific contribution: metabolomics becomes an auditable process rather than a collection of screenshots.

W4M is not an automatic substitute for GNPS or MetGem. Its learning curve includes Galaxy concepts, data formats, and tool-specific parameters. Web execution also depends on available resources and versioned modules. Most importantly, a reproducible workflow can still reproduce a bad design. Replication, randomized acquisition, suitable controls, and biological interpretation remain the chemist’s responsibility.

| Tool | Best contribution | Main strength | Key limitation |
| --- | --- | --- | --- |
| GNPS / GNPS2 | Networking, libraries, public-data reuse | Spectral ecosystem and FBMN integration | Upstream quality and library coverage constrain results |
| MetGem | Local network and t-SNE exploration | Interactive, standalone visualization | Embeddings are exploratory, not structural evidence |
| Workflow4Metabolomics | Preprocessing, statistics, annotation | Shareable Galaxy workflows across several omics | Setup and parameter choices still demand expertise |
| MZmine or MS-DIAL | Feature detection, alignment, deconvolution | Detailed local control before networking | Processing errors propagate into every downstream map |

## My working sequence

For a natural product project, I would acquire LC–MS/MS with pooled controls and blanks, inspect chromatograms before any networking, and process features in MZmine, MS-DIAL, or W4M according to the study design. I would use FBMN on GNPS when abundance and sample comparisons matter, then inspect uncertain families and settings locally in MetGem when another view helps.

The final step is deliberately conservative: separate library matches, propagated family hypotheses, formula predictions, and confirmed structures in the report. Use the network to choose the next experiment, not to avoid it. That is where these tools have their greatest value—and where their authority ends.

