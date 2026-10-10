---
title: The azoxy bond is commoner than its compounds — Maleckis and co-workers' azodyrecin pathway
summary: A close reading of Maleckis and co-workers' 2024 ACS Chemical Biology paper, which confirmed the azd gene cluster behind the cytotoxic azodyrecins, captured hydrazine and azo intermediates on the way to the azoxy bond, and found azoxy biosynthetic clusters in roughly a fifth of Streptomyces genomes — evidence that the known family of natural azoxy compounds is a small, visible fraction of a much larger repertoire.
section: article
format: paper-perspective
paperType: biosynthesis
audience:
  - junior
  - advanced
author:
  name: Hien Le
  orcid: 0000-0002-8834-593X
publishedAt: 2026-10-10
tags:
  - azoxy compounds
  - azodyrecin
  - Streptomyces
  - biosynthesis
  - genome mining
  - CRISPR base editing
  - natural product discovery
references:
  - citation: Maleckis M., Wibowo M., Gren T., et al. Biosynthesis of the Azoxy Compound Azodyrecin from Streptomyces mirabilis P8-A2. ACS Chem. Biol. 2024, 19, 641–653
    url: https://doi.org/10.1021/acschembio.3c00632
  - citation: Wibowo M., Ding L. Chemistry and Biology of Natural Azoxy Compounds. J. Nat. Prod. 2020, 83, 3482–3491
    url: https://doi.org/10.1021/acs.jnatprod.0c00725
  - citation: "Wibowo M., Gotfredsen C. H., Sassetti E., Melchiorsen J., Clausen M. H., Gram L., Ding L. Azodyrecins A–C: Azoxides from a Soil-Derived Streptomyces Species. J. Nat. Prod. 2020, 83, 3519–3525"
    url: https://doi.org/10.1021/acs.jnatprod.0c00339
  - citation: Choirunnisa A. R., Arima K., Abe Y., et al. New Azodyrecins Identified by a Genome Mining-Directed Reactivity-Based Screening. Beilstein J. Org. Chem. 2022, 18, 1017–1025
    url: https://doi.org/10.3762/bjoc.18.102
  - citation: Guo Y.-Y., Li Z.-H., Xia T.-Y., Du Y.-L., Mao X.-M., Li Y.-Q. Molecular mechanism of azoxy bond formation for azoxymycins biosynthesis. Nat. Commun. 2019, 10, 4420
    url: https://doi.org/10.1038/s41467-019-12250-1
  - citation: Shi J., Zang X., Zhao Z., et al. Conserved Enzymatic Cascade for Bacterial Azoxy Biosynthesis. J. Am. Chem. Soc. 2023, 145, 27131–27139
    url: https://doi.org/10.1021/jacs.3c12018
  - citation: Yamato M., Iinuma H., Naganawa H., et al. Isolation and properties of valanimycin, a new azoxy antibiotic. J. Antibiot. 1986, 39, 184–191
    url: https://doi.org/10.7164/antibiotics.39.184
  - citation: Stevens C. L., Gillis B. T., French J. C., Haskell T. H. The structure of elaiomycin, a tuberculostatic antibiotic. J. Am. Chem. Soc. 1956, 78, 3229–3230
  - citation: McGahren W. J., Kunstmann M. P. Novel α,β-unsaturated azoxy-containing antibiotic. J. Am. Chem. Soc. 1969, 91, 2808–2810
    url: https://doi.org/10.1021/ja01038a081
  - citation: Otoguro K., Imamura N., Kuga H., et al. Jietacins A and B, new nematocidal antibiotics from a Streptomyces sp. Taxonomy, isolation, and physico-chemical and biological properties. J. Antibiot. 1987, 40, 623–629
    url: https://doi.org/10.7164/antibiotics.40.623
license: CC BY-NC 4.0
draft: true
---

Seventy years separate the first natural azoxy compound from a satisfying account of how such a thing is made. Elaiomycin, a tuberculostatic metabolite reported from a *Streptomyces* in 1954 and assigned its structure by Stevens, Gillis, French, and Haskell two years later, carried a functional group — the azoxy unit, RN=N⁺(O⁻)R — that synthetic chemists knew well from dye chemistry but that biology seemed to use almost nowhere. A slow trickle of isolations in the decades since proved that "almost nowhere" was an artifact of attention rather than of nature: azoxy metabolites kept surfacing in actinomycete extracts, one eccentric structure at a time, while the enzymatic logic behind the N–N bond and its N-oxide remained obscure. In this 2024 *ACS Chemical Biology* paper, Matiss Maleckis, Mario Wibowo, and colleagues in the Ding and Weber groups at the Technical University of Denmark dissect the biosynthesis of the cytotoxic azodyrecins from the soil isolate *Streptomyces mirabilis* P8-A2 and produce the most complete picture yet of one of the two routes by which microbes build the azoxy bond. The paper rewards a close reading twice over: once as pathway enzymology, and once — the emphasis of this perspective — as a census of a structurally diverse and plainly undercounted family of natural products.

## The paper at a glance

The authors sequenced the producer's genome (an 11.5 Mb chromosome encoding roughly forty predicted biosynthetic gene clusters), delineated the azodyrecin (*azd*) cluster by comparison with all genetically characterized or proposed azoxy clusters, and confirmed it twice over: CATCH cloning of the cluster followed by heterologous expression in both *S. coelicolor* M1146 and *S. albidoflavus* J1074 reconstituted azodyrecin production. Fourteen genes were then knocked out in the native producer using CRISPR-BEST base editing — a stop-codon introduction method that avoids double-strand breaks — and untargeted LC-MS/MS metabolomics of the mutant panel, organized by feature-based molecular networking, yielded eleven proposed intermediates. Among them were the prizes of the study: hydrazine and azo compounds, the long-postulated precursors of the azoxy group, caught accumulating in specific mutants. Finally, the authors mapped all known azoxy cluster types onto a phylogenomic tree of 1528 *Streptomyces* genomes to ask how common this chemistry actually is. The answer — about one genome in five carries an azoxy cluster — is the finding this perspective wants to put in front of every natural product chemist who screens actinomycetes.

## The chemical diversity behind a single functional group

Natural azoxy compounds are best understood not as a family but as a *bond* that evolution has installed into otherwise unrelated architectures. Arranged by how their two nitrogen substituents are built, the known members fall into a small number of assembly logics, and the spread is striking. Valanimycin (1986) couples two amino acid-derived pieces — an isobutylamine derived from valine and a seryl unit; azoxybacilin, an antifungal from *Bacillus cereus*, shows that the motif is not even restricted to actinomycetes. A larger group couples a fatty amine to an amino acid: elaiomycin and its many congeners, the antifungal KA57A, the maniwamycins, the nematocidal jietacins, and the cytotoxic azodyrecins A–F — the last built from an iso-fatty chain (its starter unit read off the structure as valine or isoleucine, extended by malonate chemistry) and an alanine. A third logic abandons pairing altogether: the azoxymycins and O-alkylazoxymycins arise by dimerization of a phenolic monomer, shown by Guo and co-workers to proceed through enzymatic oxidation of an aniline to a nitroso species followed by spontaneous coupling. And beyond bacteria entirely, cycads accumulate azoxyglycosides such as cycasin — the β-glucoside of methylazoxymethanol — a reminder that this functional group has been invented more than once.

The biological activities are as scattered as the structures: tuberculostatic (elaiomycin), antibacterial (valanimycin, DC-811), antifungal (KA57A, maniwamycins, azoxybacilin), nematocidal (jietacins), and cytotoxic (azodyrecins, geralcin C). A reasonable reading — offered here as interpretation, not as the paper's claim — is that the azoxy group itself is a reactive pharmacophore whose flanking subunits tune delivery, potency, and spectrum; nature's combinatorial experiment has been run on the decorations while the warhead stays constant. There is even chemical diversity *within* single producers, and it is biosynthetically eloquent: the elaiomycin producer also yields alkylhydrazides (elaiomycins B and C), formally reduced relatives of the azoxy products. Hydrazine-level congeners co-isolated with azoxy products are exactly what a hydrazine → azo → azoxy oxidative sequence predicts, and the genetic evidence for that sequence is precisely what this paper supplies.

## Catching the bond being made

The mechanistic heart of the paper is the fate of four conserved genes, *azdA*, *azdB*, *azdH*, and *azdO*, whose homologues recur across the azodyrecin, KA57A, maniwamycin, valanimycin, and elaiomycin cluster types. Knockout metabolomics assigns them a working division of labor. AzdH, with its partner AzdR, resembles the two-component VlmH/VlmR system from valanimycin biosynthesis and is proposed to N-hydroxylate the fatty amine — when *azdH* is inactivated, the pathway stalls and the fatty amine is instead captured as an amide shunt product. AzdA belongs to the aminoacyl-tRNA-dependent transferase family (its characterized relatives remodel membrane lipids with lysine in pathogens) and is proposed to deliver alanine from tRNA-Ala onto the hydroxylated amine, setting up the N–N connectivity through a hydrazine intermediate. The decisive observation concerns AzdB: its knockout accumulates hydrazine compounds (proposed structures 13–15) and azo compounds (10–12) but produces no azoxy products, identifying AzdB as the enzyme that oxidizes the azo stage to the azoxy group. The overall sequence — amine, N-hydroxylation, aminoacyl transfer, hydrazine, azo, azoxy — turns a seventy-year-old structural mystery into an ordered oxidation ladder, and it dovetails with the in vitro reconstitution of the homologous valanimycin cascade reported by Shi, Du, and co-workers in 2023. Tailoring is equally legible: AzdM is the SAM-dependent methyltransferase that esterifies the carboxylate (shown in vitro by Choirunnisa and co-workers), and AzdT is a fatty acid desaturase that installs the double bond last, converting azodyrecins D–F into A–C.

## A genus-wide census

The paper's most quotable numbers come last. Across 1528 medium- and high-quality *Streptomyces* genomes, 351 — about 22% — carry a recognizable azoxy biosynthetic cluster. Sorted by assembly logic, azodyrecin-like clusters appear in 191 genomes (12%) and KA57A-like clusters in 136 (9%), while valanimycin-like and azoxymycin-like clusters are scarce (14 and 12 genomes, respectively). Only 16 genomes carry more than one azoxy cluster. Two details deserve emphasis. First, even *S. coelicolor* A3(2) — the most studied streptomycete in existence — harbors an azodyrecin-like cluster, yet no azoxy compound has ever been reported from it: the known chemical record and the genomic record are badly out of register. Second, the authors converted their cluster definitions into antiSMASH detection rules, so the census is now repeatable by anyone with a genome. For a field that has described perhaps a dozen natural azoxy families in seventy years, a one-in-five carriage rate is not a footnote; it is a discovery forecast.

## Limitations and open questions

A close reading should hold onto what the paper does not establish:

- **The intermediates are proposals, not isolates.** Compounds 7–17 are annotated from exact mass and MS/MS fragmentation in mutant extracts, not from purified material with NMR support. The hydrazine and azo assignments are chemically plausible and internally consistent with the genetic logic, but they remain one layer below structural proof.
- **The N–N bond-forming step itself is still unassigned.** AzdO, a small transmembrane protein with no characterized homologues, is the leading candidate for organizing the hydrazine-forming rearrangement, but its knockout gave no detectable intermediates, and which steps between aminoacyl transfer and the hydrazine are enzymatic versus spontaneous is unresolved.
- **No in vitro chemistry here.** Excepting the previously published AzdM methylation, every activity is inferred from knockout phenotypes in the native producer. The complementary valanimycin study shows what reconstitution can add; AzdB's own cofactor requirements and mechanism remain to be demonstrated.
- **Precursors are read from structures, not labels.** The valine/isoleucine starter units and the reductase-then-aminotransferase route to the fatty amine are inferred from the products and gene annotations; isotope feeding would firm this up.
- **Cluster presence is not production.** The genomic census cannot say which of the 351 clusters are expressed, and the azodyrecin-like tally carries a sampling bias toward closely related strains. Silent clusters may encode azodyrecin — or something azoxy but new.

## What to take from it

For a practicing natural product chemist, three lessons transfer. First, put the azoxy group in your search image: a functional group encoded in a fifth of *Streptomyces* genomes but isolated perhaps a dozen times is exactly the kind of blind spot that reactivity-based screening — as Choirunnisa and co-workers demonstrated for azodyrecins — and targeted MS/MS features can exploit. Second, read reduced congeners as pathway echoes: when hydrazides or hydrazines co-occur with oxidized N–N products in an extract, they are not noise but breadcrumbs marking the oxidative ladder, and their presence can flag azoxy chemistry before any azoxy compound is isolated. Third, the study is a model of how to dissect a bond-forming pathway without in vitro biochemistry: base-editing knockouts in the native producer plus network-organized metabolomics caught even transient, shunt-prone intermediates, precisely because the analysis compared mutant *and* wild-type extracts feature by feature rather than peak-list by peak-list. The deepest lesson is the one this publication exists to examine: a functional group can be genetically common and chemically invisible at the same time. Somewhere in the extracts already sitting in freezers, the other three hundred clusters are waiting to be noticed.

