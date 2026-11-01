---
title: "Reading genomes like a natural product chemist: antiSMASH, the RiPP miners, and the BGC databases that matter"
summary: "A practical assessment of the bioinformatics toolkit for biosynthetic gene clusters — antiSMASH for detection, specialist miners for RiPPs, and MIBiG and the BGC Atlas for dereplication and context — with the vancomycin cluster as the worked example and a clear line between what these tools predict and what they prove."
section: opinion
format: tool-review
audience:
  - junior
  - advanced
author:
  name: Hien Le
  orcid: 0000-0002-8834-593X
publishedAt: 2026-11-01
tags:
  - biosynthetic gene clusters
  - genome mining
  - antiSMASH
  - RiPP
  - MIBiG
  - BGC Atlas
  - heterologous expression
  - bioinformatics
references:
  - citation: "Medema M. H., Blin K., Cimermancic P., et al. antiSMASH: rapid identification, annotation and analysis of secondary metabolite biosynthesis gene clusters in bacterial and fungal genome sequences. Nucleic Acids Res. 2011, 39, W339–W346"
    url: https://doi.org/10.1093/nar/gkr466
  - citation: "Blin K., Shaw S., Vader L., et al. antiSMASH 8.0: extended gene cluster detection capabilities and analyses of chemistry, enzymology, and regulation. Nucleic Acids Res. 2025, 53, W32–W38"
    url: https://doi.org/10.1093/nar/gkaf334
  - citation: Medema M. H., Kottmann R., Yilmaz P., et al. Minimum information about a biosynthetic gene cluster. Nat. Chem. Biol. 2015, 11, 625–631
    url: https://doi.org/10.1038/nchembio.1890
  - citation: "Zdouc M. M., Blin K., Louwen N. L. L., et al. MIBiG 4.0: advancing biosynthetic gene cluster curation through global collaboration. Nucleic Acids Res. 2025, 53, D678–D690"
    url: https://doi.org/10.1093/nar/gkae1115
  - citation: "Bağcı C., Nuhamunada M., Goyat H., et al. BGC Atlas: a web resource for exploring the global chemical diversity encoded in bacterial genomes. Nucleic Acids Res. 2025, 53, D618–D624"
    url: https://doi.org/10.1093/nar/gkae953
  - citation: Tietz J. I., Schwalen C. J., Patel P. S., et al. A new genome-mining tool redefines the lasso peptide biosynthetic landscape. Nat. Chem. Biol. 2017, 13, 470–478
    url: https://doi.org/10.1038/nchembio.2319
  - citation: Santos-Aberturas J., Chandra G., Frattaruolo L., et al. Uncovering the unexplored diversity of thioamidated ribosomal peptides in Actinobacteria using the RiPPER genome mining tool. Nucleic Acids Res. 2019, 47, 4624–4637
    url: https://doi.org/10.1093/nar/gkz192
  - citation: "van Heel A. J., de Jong A., Song C., Viel J. H., Kok J., Kuipers O. P. BAGEL4: a user-friendly web server to thoroughly mine RiPPs and bacteriocins. Nucleic Acids Res. 2018, 46, W278–W281"
    url: https://doi.org/10.1093/nar/gky383
  - citation: Kloosterman A. M., Cimermancic P., Elsayed S. S., et al. Expansion of RiPP biosynthetic space through integration of pan-genomics and machine learning uncovers a novel class of lanthipeptides. PLoS Biol. 2020, 18, e3001026
    url: https://doi.org/10.1371/journal.pbio.3001026
  - citation: Merwin N. J., Mousa W. K., Dejong C. A., et al. DeepRiPP integrates multiomics data to automate discovery of novel ribosomally synthesized natural products. Proc. Natl. Acad. Sci. USA 2020, 117, 371–380
    url: https://doi.org/10.1073/pnas.1901493116
  - citation: "Kloosterman A. M., Shelton K. E., van Wezel G. P., Medema M. H., Mitchell D. A. RRE-Finder: a genome-mining tool for class-independent RiPP discovery. mSystems 2020, 5, e00267-20"
    url: https://doi.org/10.1128/mSystems.00267-20
  - citation: MIBiG 4.0 entry BGC0000455.6, vancomycin biosynthetic gene cluster from Amycolatopsis orientalis HCCB10007 (underlying GenBank record HQ679900.1)
    url: https://mibig.secondarymetabolites.org/repository/BGC0000455.6/index.html
license: CC BY-NC 4.0
draft: false
---

Most microbial natural products are made by biosynthetic gene clusters (BGCs): physically contiguous stretches of DNA that gather scaffold-building enzymes, tailoring enzymes, precursor supply, transport, resistance, and regulation into one locus. That organization is a gift twice over. Experimentally, a cluster can be manipulated as a unit — cloned into a heterologous host such as a *Streptomyces albus* or *S. coelicolor* chassis strain, refactored with synthetic promoters, interrogated gene by gene — which has made silent and uncultured pathways accessible to chemistry. Computationally, a cluster is a pattern that software can recognize in a raw genome sequence, and that turned natural product discovery into an exercise in reading genomes. This opinion is a practical assessment of the reading tools: antiSMASH for detection, specialist miners for ribosomal peptides, and two databases — MIBiG and the BGC Atlas — that answer the two questions that matter once a cluster is found. Is it known? And how unusual is it? Evidence and my preferences are kept separate throughout; where I recommend a default, I say so.

## One cluster as a worked example

Figure 1 shows the vancomycin cluster from *Amycolatopsis orientalis* HCCB10007 exactly as a bioinformatician meets it: the MIBiG entry BGC0000455.6, 65 kb and 34 coding sequences. Read it the way the software does. The core is three nonribosomal peptide synthetases — *vcm2*, *vcm3*, and *vcm4*, carrying 3 + 3 + 1 modules — that assemble a heptapeptide mostly from nonproteinogenic monomers: 4-hydroxyphenylglycine (Hpg), 3,5-dihydroxyphenylglycine (Dpg), β-hydroxytyrosine, asparagine, and N-methylleucine. Everything else on the map exists to feed or finish that scaffold: precursor supply for Hpg (*vcm17/18*), Dpg (the type III PKS *vcm23*), and the vancosamine sugar (*vcm19–22*); tailoring by cross-linking P450s (*vcm5–7*), a halogenase (*vcm8*, two chlorines), glycosyltransferases (*vcm9/10*), and methyltransferases; plus a *vanHAX* resistance cassette and a pathway-specific regulator (*vtrR*). Scaffold assembly is the minority of the genes. That is typical, and it is why a genome scan works: the chemistry announces itself through the company the core enzymes keep.

![Gene map of the 65 kb vancomycin biosynthetic gene cluster from Amycolatopsis orientalis HCCB10007 (MIBiG BGC0000455.6). Thirty-four coding sequences are drawn as arrows, colored by function: dark plum core enzymes (NRPS genes vcm2, vcm3, vcm4 and the type III PKS vcm23), violet tailoring enzymes, gold transporter, gold-outlined regulator vtrR, plum-outlined resistance gene vanX, and pale other genes. A light red band highlights the three NRPS genes, annotated 3 modules, 3 modules, and 1 module. Brackets mark the vanHAX resistance cassette, the NRPS assembly line, the tailoring block, and the precursor-supply block.](/media/opinions/genome-mining-toolkit/vancomycin-bgc-gene-map.svg)

*Figure 1. The vancomycin BGC, redrawn from the MIBiG 4.0 entry BGC0000455.6 (GenBank HQ679900.1; 65,044 nt, 34 coding sequences) with the generator script committed next to the figure; functional categories follow the antiSMASH gene-function annotation in the MIBiG record, and gene arrows use the site palette. The light red band marks the three NRPS megaenzymes (vcm2–vcm4, seven modules) that build the heptapeptide; brackets group the resistance cassette, the tailoring enzymes, and the precursor-supply genes for Hpg, Dpg, and vancosamine. Four coding sequences unnamed in the record (including the ABC transporter between vcm1 and vcm2) are drawn without labels. Inspect how little of the locus assembles the scaffold — and how much feeds, decorates, and protects it.*

## From predicted monomers to a structure

The real dividend of an antiSMASH run is not the gene map but the chemical hypothesis it writes down. For this cluster, the adenylation-domain predictions read: leucine, R-β-hydroxytyrosine, and asparagine from Vcm2; 4-hydroxyphenylglycine, 4-hydroxyphenylglycine, and R-β-hydroxytyrosine from Vcm3; and 3,5-dihydroxyphenylglycine from Vcm4. Set those seven calls against the actual molecule and every monomer is right (Figure 2, Table 1). Before a single flask is grown, the researcher holds the heptapeptide's monomer order — and with it a set of concrete spectroscopic expectations: the aromatic spin systems of two Hpg residues and one Dpg, an N-methyl singlet, two chlorinated rings, and an estimated molecular formula to interrogate by LC-HRMS. The standalone Vcm15 protein, whose A-domain prefers tyrosine, sits outside the seven-module line and belongs to β-hydroxytyrosine precursor supply — a useful reminder that not every adenylation domain in a cluster builds the scaffold.

![Skeletal structure of vancomycin with the seven heptapeptide residues numbered 1 to 7: N-methylleucine (1), two chloro-beta-hydroxytyrosines (2 and 6), asparagine (3), two 4-hydroxyphenylglycines (4 and 5), and 3,5-dihydroxyphenylglycine (7). Each residue carries its own pastel tint and a gold number placed outside the drawing. The glucose–vancosamine disaccharide hangs below residue 4; chlorine atoms sit on residues 2 and 6; three oxidative cross-links brace the aglycone.](/media/opinions/genome-mining-toolkit/vancomycin-structure-residues.svg)

*Figure 2. Vancomycin (PubChem CID 14969), drawn with RDKit/CoordGen from the isomeric SMILES of that record (free acid/base form, not the hydrochloride salt); the generator script is committed next to the figure. Residues are numbered 1–7 from the N-terminus of the heptapeptide, matching Table 1, and each monomer-derived moiety carries its own tint from the site's residue-tint palette (numbers placed outside the drawing); the tints mark the residues specified by the antiSMASH adenylation-domain predictions. The disaccharide, the two chlorines, the N-methyl group, and the three oxidative cross-links are tailoring beyond those calls and stay untinted. Inspect residues 2, 4, and 6: their cross-linked aryl rings are where the genome prediction ends and structural chemistry begins.*

Table 1. The seven antiSMASH adenylation-domain calls for the vancomycin assembly line (MIBiG BGC0000455.6) against the residues they specify. Module numbering follows the heptapeptide from the N-terminus; evidence tiers are quoted as reported in the MIBiG record.

| Residue | NRPS module | antiSMASH A-domain call (evidence) | What the actual structure adds |
| --- | --- | --- | --- |
| 1 | M1 (vcm2) | Leucine (structure-based inference; ATP-PPi exchange assay) | N-Methylation (Vcm12) |
| 2 | M2 (vcm2) | R-β-Hydroxytyrosine (structure-based inference) | Chlorination (Vcm8); aryl ether to residue 4 |
| 3 | M3 (vcm2) | Asparagine (structure-based inference) | None — incorporated as predicted |
| 4 | M4 (vcm3) | 4-Hydroxyphenylglycine (structure-based inference) | Glucose + vancosamine (Vcm9/10); two aryl ethers |
| 5 | M5 (vcm3) | 4-Hydroxyphenylglycine (structure-based inference) | C–C biaryl link to residue 7 |
| 6 | M6 (vcm3) | R-β-Hydroxytyrosine (structure-based inference) | Chlorination (Vcm8); aryl ether to residue 4 |
| 7 | M7 (vcm4) | 3,5-Dihydroxyphenylglycine (structure-based inference) | C–C biaryl link to residue 5 |

Just as instructive is what the prediction leaves blank. The two chlorines, the glucose–vancosamine disaccharide, the N-methyl group, and the three oxidative cross-links that lock the aglycone into its antibiotic-active cup all arrive as tailoring, invisible to an adenylation-domain code. Prediction hands you the skeleton and the search image; the decorations — and the stereochemistry — are still earned with spectra.

## The groups behind the toolkit

The field runs on a small, identifiable community, and knowing who maintains what helps when a tool misbehaves. antiSMASH has been co-developed since 2011 by Marnix Medema's group at Wageningen and Tilmann Weber's group at the DTU Novo Nordisk Foundation Center for Biosustainability, with Kai Blin as long-time lead developer; the same Wageningen orbit, including Justin van der Hooft, maintains the cluster-similarity stack (BiG-SCAPE, BiG-SLiCE, BiG-FAM) and steers MIBiG. Nadine Ziemert's group in Tübingen contributes to antiSMASH and built the BGC Atlas. RiPP mining draws on Douglas Mitchell's group at Illinois (RODEO, RRE-Finder), Andy Truman's group at the John Innes Centre (RiPPER), and Nathan Magarvey's group at McMaster (DeepRiPP). None of this is a faceless pipeline: MIBiG 4.0 was curated by 267 named contributors in a community annotathon, and the databases accept corrections.

## antiSMASH: the default first pass

Run antiSMASH first, on every genome, before anything cleverer. Version 8 detects 101 cluster types — up from 81 in the previous release — and for each candidate region it annotates gene functions against curated profile databases, parses NRPS and PKS domains down to predicted monomers, and compares the region against other clusters with ClusterBlast and against experimentally characterized ones with KnownClusterBlast. The output is a clickable gene map exactly of the kind shown in Figure 1, plus predicted core structures for many NRPS and PKS products. Two properties make it the right default: it is conservative about chemistry (substrate calls are labeled with their evidence tier, not asserted), and it is reproducible (a downloadable stand-alone version; everything scriptable). Its blind spots are equally well defined. Boundary calls are heuristic, so flanking tailoring genes are sometimes cut off. Monomer predictions for adenylation domains are statistical priors — treat "4-hydroxyphenylglycine (structure-based inference)" as a hypothesis to test, not a result; Figure 2 and Table 1 show that loop closed for one molecule. And antiSMASH finds clusters, not compounds: it says nothing about whether the pathway is switched on.

## RiPPs need specialist miners

Ribosomally synthesized and post-translationally modified peptides break the assumptions antiSMASH is built on. The precursor peptide is a short ORF — often 20 to 110 codons — that standard gene callers routinely miss, and there is no universal scaffold enzyme to anchor detection. The class-independent handle that most modern miners exploit is the RiPP recognition element (RRE), a small protein domain that binds the leader peptide; RRE-Finder, now integrated into antiSMASH, searches for RREs directly. Around that handle the specialist tools differ in strategy. BAGEL4 is the friendly web server, strongest on bacteriocins. RODEO reannotates short ORFs around a query enzyme and scores candidate precursors with a support vector machine; its 2017 lasso peptide survey showed how much diversity a focused search can surface. RiPPER combines RRE hunting with reannotation of short ORFs and scoring of co-localized tailoring enzymes, and was built with actinomycetes in mind. decRiPPter goes class-independent at scale, filtering pan-genomic data with machine learning, and found a previously unknown lanthipeptide class. DeepRiPP adds metabolomics: a neural-network precursor detector coupled to genomic and mass-spectrometric matching, so the output prioritizes RiPPs that are actually being produced. My preference, stated as such: for an actinomycete genome I run antiSMASH and RiPPER; I reach for RODEO when I am mining a specific enzyme family across hundreds of genomes; decRiPPter and DeepRiPP are worth the setup cost only when novelty at scale is the explicit goal.

## Databases: MIBiG for dereplication, the BGC Atlas for context

MIBiG is the ground-truth layer: 3,059 curated clusters in version 4.0, each experimentally tied to a characterized compound, each versioned with a visible changelog. The vancomycin entry of Figure 1 shows the anatomy — gene table, NRPS domain predictions with evidence tiers, compound records, literature, and similar known clusters. Use it for dereplication: a close KnownClusterBlast match to a MIBiG entry is a strong prior that you have rediscovered a known chemotype, and it tells you which structures to expect in the mass spectrum. Read the metadata, though. Entries carry quality flags — this vancomycin record is currently flagged "questionable" — and curation status is information, not decoration. The BGC Atlas answers the complementary question. Built from more than 35,000 MGnify metagenomic datasets, it maps nearly 1.8 million predicted BGCs clustered into gene cluster families with habitat metadata; its headline findings — RiPPs are the most abundant class, and most families are strongly environment-specific — are exactly the context an isolate genome lacks. Where MIBiG says "someone has characterized this," the Atlas says "this family occurs in these biomes, in these taxa, this often." Worth knowing in the same space: the antiSMASH-DB for pre-computed clusters from complete isolate genomes, BiG-FAM for cross-genome family memberships, and the legacy ClusterMine360.

| Tool | What it contributes | What it will not tell you |
| --- | --- | --- |
| antiSMASH | Detection, domain parsing, dereplication hints | Whether the cluster is expressed |
| RiPP miners (RODEO, RiPPER, BAGEL4, decRiPPter, DeepRiPP) | Precursor peptides invisible to standard annotation | The final post-translational structure |
| MIBiG | Experimentally characterized ground truth | Coverage of uncharacterized chemistry |
| BGC Atlas | Family-level distribution and ecology | The product a family makes |

## What the predictions cannot do

Four cautions, stated plainly:

- **Detection is not production.** Regulators such as *vtrR* gate expression; silent clusters pass every bioinformatic filter. Heterologous expression — moving the cluster into a chassis host, refactoring promoters — is the experimental answer, not an optional extra.
- **Predictions are priors.** Substrate codes and boundary calls are statistical. The MIBiG habit of labeling evidence tiers ("structure-based inference" versus experimentally validated) is the honesty standard to demand from every tool.
- **Database identity is not experimental support.** A KnownClusterBlast hit or an Atlas family membership prioritizes; it never confirms. The compound in the flask is decided by LC-MS and NMR, on this site as elsewhere.
- **Inherited uncertainty propagates.** The Atlas inherits antiSMASH boundary choices and metagenome assembly gaps; MIBiG inherits the variable rigor of the primary literature. Cite versions.

## A working order of operations

The sequence I teach, as opinion: (1) annotate the genome with antiSMASH and read the gene maps before any table of scores — count modules, look for resistance and regulatory genes, ask what the precursors are; (2) dereplicate against MIBiG through KnownClusterBlast; (3) check family distribution and habitat in the BGC Atlas before claiming novelty; (4) if RiPPs are in play, add RiPPER or RODEO; (5) move promising silent clusters into a heterologous host early, while the chemistry is cheap; (6) confirm with spectra, not sequence. The genomic tools have quietly inverted discovery: sequence now generates the hypotheses, and the spectrometer — as always on this site — disposes of them.
