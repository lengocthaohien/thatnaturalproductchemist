---
title: A third route for biological selenium — Kayrouz and co-workers' selenoneine pathway
summary: A close reading of Kayrouz and co-workers' 2022 Nature paper, which mined microbial genomes around selD to uncover the widespread three-gene sen cluster and reconstituted selenoneine biosynthesis in vitro, revealing two new carbon–selenium bond-forming enzymes and an unexpected selenosugar intermediate.
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
  - selenium
  - selenoneine
  - ergothioneine
  - genome mining
  - biosynthesis
  - glycosyltransferase
  - natural product discovery
references:
  - citation: Kayrouz C. M., Huang J., Hauser N., Seyedsayamdost M. R. Biosynthesis of selenium-containing small molecules in diverse microorganisms. Nature 2022, 610, 199–204
    url: https://doi.org/10.1038/s41586-022-05174-2
  - citation: Yamashita Y., Yamashita M. Identification of a novel selenium-containing compound, selenoneine, as the predominant chemical form of organic selenium in the blood of bluefin tuna. J. Biol. Chem. 2010, 285, 18134–18138
    url: https://doi.org/10.1074/jbc.C110.106377
  - citation: Achouba A., Dumas P., Ouellet N., et al. Selenoneine is a major selenium species in beluga skin and red blood cells of Inuit from Nunavik. Chemosphere 2019, 229, 549–558
    url: https://doi.org/10.1016/j.chemosphere.2019.04.191
  - citation: Guo H. Selenium-containing small molecules. Commun. Chem. 2022, 5, 138
    url: https://doi.org/10.1038/s42004-022-00756-7
  - citation: Xu S., Zhao J., Liu X., et al. Structures of SenB and SenA enzymes from Variovorax paradoxus provide insights into carbon–selenium bond formation in selenoneine biosynthesis. Heliyon 2024, 10, e32888
    url: https://doi.org/10.1016/j.heliyon.2024.e32888
license: CC BY-NC 4.0
draft: false
---

Selenium sits directly below sulfur in the periodic table, and biology treats it as a prized specialist: until recently, every known route for its use funneled selenide through selenophosphate into exactly two destinations — selenocysteine in proteins and 2-selenouridine in tRNAs. Small molecules were missing from that picture, which was awkward, because analytical chemists had been finding one for over a decade. In 2010, Yamashita and Yamashita identified selenoneine — the selenium analogue of the histidine-derived antioxidant ergothioneine — as the predominant organic selenium species in bluefin tuna blood, and it has since turned up in marine mammals, seabirds, and fish-eating human populations. Nobody knew who made it or how. In this 2022 *Nature* paper, Kayrouz, Huang, Hauser, and Seyedsayamdost answer both questions: diverse microbes make selenoneine, using a dedicated three-gene pathway with two previously unknown carbon–selenium bond-forming enzymes. The paper rewards a close reading because its genome mining started from an *element* rather than a scaffold — and because the pathway it uncovered contains a genuine surprise.

![Chemical structures of hercynine, ergothioneine, and selenoneine drawn side by side. Each is an imidazole ring carrying the same trimethylammonio-alaninate side chain; they differ only at the imidazole 2-position, which bears H in hercynine, a thione C=S in ergothioneine, and a selenone C=Se in selenoneine.](/media/articles/selenoneine-biosynthesis-sen-cluster/structures-hercynine-ergothioneine-selenoneine.svg)

*Figure 1. Structures of hercynine, ergothioneine, and selenoneine, drawn as their predominant tautomers (thione for ergothioneine, selenone for selenoneine). The three betaines share the same side chain and differ only at C2 of the imidazole ring — inspect that position: H, S, or Se.*

## The paper at a glance

The authors searched microbial genomes for genes co-localized with *selD*, the gene for selenophosphate synthetase — the enzyme at the root of all known selenium trafficking — and uncovered hundreds of candidate three-gene clusters, named *sen*, across diverse bacterial phyla. Selenite-supplemented cultures of cluster-carrying bacteria produced selenoneine, detected by high-resolution mass spectrometry (with selenium's distinctive multi-isotope envelope) and NMR. The three proteins were then expressed recombinantly in *Escherichia coli* and the pathway reconstituted in vitro, which assigned a reaction to each enzyme and revealed the pathway's unexpected intermediate: a selenosugar.

## Genome mining with an elemental beacon

The strategic move worth studying is the query design. Most genome mining asks "where is the machinery for this structural family?" — a scaffold-first question. Kayrouz and co-workers instead asked "where does selenium go?" and anchored the search on the one chemistry checkpoint shared by every known selenium pathway: selenophosphate, made by SelD. Genes found next to *selD* homologues become suspects by guilty association. That is a hypothesis generator, not proof — co-localization says nothing by itself — and the paper is honest about it: the claim is earned downstream, first by detecting the actual metabolite in native producers, then by reconstituting the chemistry enzyme by enzyme. The bioinformatics nominates; only the chemistry confirms.

## Three enzymes, two new carbon–selenium bonds

The reconstituted pathway runs in three steps. SenC, the SelD paralogue, performs the familiar first move: ATP-dependent conversion of selenide into monoselenophosphate. SenB then does something never seen before: it is a selenium glycosyltransferase that transfers Se from selenophosphate onto UDP-glucose, forming a C–Se bond at the anomeric carbon — a selenosugar. Finally SenA, a non-heme iron enzyme homologous to EgtB, the sulfoxide synthase of ergothioneine biosynthesis, uses the selenosugar as its selenium donor and hercynine (N-α-trimethyl-L-histidine) as the acceptor, forming the second C–Se bond at C2 of the imidazole ring and releasing selenoneine. Two of the three enzymes therefore forge carbon–selenium bonds, the first such enzymes known to act on biological small molecules. Note also what the cluster does *not* encode: no histidine methyltransferase, so hercynine supply depends on the host background — a "complete" cluster is only complete for the chemistry that makes it unusual.

![Biosynthetic scheme of the sen pathway. Left to right: selenide (HSe⁻) and ATP are converted by SenC into selenophosphate, releasing AMP and phosphate; SenB then transfers selenium from selenophosphate onto UDP-glucose, releasing UDP and phosphate, to give a selenosugar — glucose bearing an anomeric carbon–selenium bond; finally SenA reacts the selenosugar with hercynine and O₂, releasing the sugar and forming selenoneine.](/media/articles/selenoneine-biosynthesis-sen-cluster/pathway-sen-cluster-selenoneine.svg)

*Figure 2. The selenoneine biosynthetic pathway encoded by the sen cluster, as reconstituted in vitro from purified enzymes by Kayrouz and co-workers. SenC, a SelD paralogue, activates selenide to monoselenophosphate (SeP). SenB, the first known selenium glycosyltransferase, transfers Se from SeP onto the anomeric carbon of UDP-glucose — with inversion of configuration, as later crystal structures confirmed — to give the selenosugar intermediate. SenA, a non-heme iron enzyme homologous to the EgtB sulfoxide synthase, then couples the selenosugar to hercynine at C2 of the imidazole ring and releases selenoneine. Inspect the two C–Se bonds formed in this scheme: one in the selenosugar, one in the product.*

## The ergothioneine mirror

The comparison with ergothioneine is where the biosynthetic logic becomes elegant. In the classical EgtA–E pathway, the sulfur donor is γ-glutamylcysteine, and two further enzymes (EgtC and EgtE) are needed to trim the carrier away and release the free thione. The *sen* pathway reaches the analogous destination with only three enzymes because its carrier is disposable by design: glucose parked on selenium through an anomeric linkage is a good leaving group, so no dedicated trimming machinery is required. This is interpretation rather than something the paper proves, but it is a compelling reading — the selenosugar looks like a safe, soluble storage-and-transfer form for a reactive, toxic chalcogen, with the anomeric C–Se bond pre-activated for delivery. Same destination as sulfur, entirely different logistics. The 2024 crystal structures underlined the divergence: SenB adopts a GT-B glycosyltransferase fold with an inverting mechanism, while SenA closely mirrors the EgtB sulfoxide synthase scaffold.

## Why this matters beyond one molecule

Selenoneine was never an obscure metabolite — it dominates organic selenium in tuna blood and reaches human blood through seafood — but it was an orphan: an analytical observation without a biosynthetic origin. This paper connects that marine and nutritional chemistry to a microbial source, and it does so with a method that generalizes. If a three-gene cluster dedicated to selenium small-molecule chemistry sat undiscovered in hundreds of genomes, the selenometabolome is presumably larger than one compound, and the authors say exactly that. The years since have been kind to the prediction: structural enzymology of SenA and SenB, evidence that SenB accepts multiple UDP-sugar donors, and further selenium antioxidants such as ovoselenol all trace back to this door being opened.

## Limitations and open questions

A close reading should hold onto what the paper does not establish:

- **Function in the producer is unknown.** No knockout fitness, stress-challenge, or ecological phenotype is reported; why a soil β-proteobacterium makes selenoneine — and for whom — remains open.
- **Cluster presence is not production.** Only a handful of the hundreds of candidate clusters were tested for metabolite output; some clusters may encode divergent products rather than selenoneine itself.
- **Mechanism was inferred, not dissected, in 2022.** The selenoxide intermediate was proposed without crystal structures or kinetics; the 2024 structural work filled much of that gap.
- **Detection bias cuts both ways.** Standard metabolomics almost never looks for selenium's multi-isotope envelope, so we are probably undercounting selenium metabolites precisely because our default methods are blind to them.

## What to take from it

For a practicing natural product chemist, three lessons transfer. First, genome mining can be element-first: if an element has a dedicated metabolic checkpoint — selenophosphate for selenium — co-localization around that checkpoint is a discovery engine. Second, expect disposable carriers: cells park reactive chalcogens on transportable handles (γ-glutamylcysteine for sulfur, glucose for selenium), so when a pathway seems to be missing its trimming enzymes, ask whether the carrier is built to leave on its own. Third, unusual elements are analytical allies as much as oddities — a multi-isotope envelope in HRMS or a ⁷⁷Se NMR signal can make a rare metabolite *more* findable, not less, for anyone who includes the element in their search image. The deepest lesson is the one this publication exists to examine: an orphan analytical observation — a selenium peak in tuna blood — was converted into genes, enzymes, and a mechanism. Other orphan peaks are sitting in current metabolomics datasets, waiting for someone to ask the right co-localization question.
