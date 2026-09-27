---
title: Pairing genomic and spectroscopic signatures to discover piperazic acid-bearing natural products
summary: A close reading of Shin and co-workers' 2023 JACS paper, where PCR amplicons of the N–N bond-forming gene ktzT prioritize producing strains and ¹H–¹⁵N NMR signatures of ¹⁵N-labeled cultures confirm piperazic acid incorporation before any purification begins.
section: article
format: paper-perspective
paperType: research-methodology
audience:
  - junior
  - advanced
author:
  name: Hien Le
  orcid: 0000-0002-8834-593X
publishedAt: 2026-09-25
tags:
  - piperazic acid
  - genome mining
  - 1H-15N HMBC
  - 1H-15N HSQC-TOCSY
  - natural product discovery
  - NMR
references:
  - citation: Shin D., Byun W. S., Kang S., et al. Targeted and Logical Discovery of Piperazic Acid-Bearing Natural Products Based on Genomic and Spectroscopic Signatures. J. Am. Chem. Soc. 2023, 145, 19676–19690
    url: https://doi.org/10.1021/jacs.3c04699
  - citation: Morgan K. D., Andersen R. J., Ryan K. S. Incarnatapeptins A and B, Nonribosomal Peptides Discovered Using Genome Mining and ¹H/¹⁵N HSQC-TOCSY. Org. Lett. 2020, 22, 4202–4206
    url: https://doi.org/10.1021/acs.orglett.0c00818
  - citation: Du Y.-L., He H.-Y., Higgins M. A., Ryan K. S. A heme-dependent enzyme forms the nitrogen–nitrogen bond in piperazate. Nat. Chem. Biol. 2017, 13, 836–838
    url: https://doi.org/10.1038/nchembio.2411
license: CC BY-NC 4.0
draft: false
---

Most natural product discovery still begins with a crude extract and ends, many purification steps later, with a structure. Shin and co-workers invert that order in their 2023 *JACS* paper on piperazic acid (Piz)-bearing metabolites: they decide **which strains are worth culturing** and **which cultures are worth fractionating** before isolating anything, by pairing two independent kinds of evidence — a genomic signature and a spectroscopic signature. It is the pairing itself that makes this paper worth reading closely, and it is why this perspective opens the Articles section.

## The paper at a glance


## The genomic signature: a short amplicon as a structural oracle

The practical problem the paper solves first is screening strains **without whole-genome sequences**. Degenerate PCR primers were designed against conserved regions of *ktzI* and *ktzT* homologues aligned from the biosynthetic gene clusters of 16 known Piz-bearing compound families, targeting ~700 bp and ~370 bp fragments respectively. Notably, the *ktzT* primers had to be engineered to avoid false hits from PaiB-family transcriptional regulators, which share significant amino acid similarity with KtzT but have nothing to do with Piz biosynthesis — a reminder that a "targeted" primer is only as targeted as its design controls.

The deeper move is what the authors do with the amplicons. Rather than treating a PCR band as a binary yes, they sequence the ~370 bp *ktzT* fragments, translate them, and build a phylogeny of 62 hits plus 22 references. Because the reference strains produce known compounds, the tree becomes an **atlas**: clades containing a reference are predicted to produce that structural family, and clades without references are candidates for novelty. Consolidating phylogeny with chemistry, the authors assign clade–structure relationships for 19 of the 23 clades. Group I (69 of 84 strains) maps onto azinothricin-type and related frameworks; the smaller group II carries greater structural diversity — which is exactly where the lenziamides emerged.

Two observations in the paper deserve emphasis because they bound the claim honestly:

- The *ktzT* amplicon phylogeny predicts structure better than the *ktzI* phylogeny; the authors attribute this to KtzI being conditionally dispensable for Piz production. A signature gene is not automatically a good signature — its essentiality matters.

## The spectroscopic signature: extending ¹H–¹⁵N NMR to NH-deficient motifs

A genomic hit says a strain *can* make a Piz-bearing compound, not that it *does* under laboratory conditions. The paper's second signature answers that question directly in culture extracts, before purification.

The prior art here is ¹H–¹⁵N HSQC-TOCSY on ¹⁵N-labeled cultures, used elegantly by Ryan and Andersen to discover the incarnatapeptins: the –N–NH– partial structure of Piz gives a proton-attached nitrogen whose correlations light up the Piz spin system. But Shin and co-workers identify a real blind spot. Piz is frequently modified — roughly twenty derivatives are known — and oxidation by enzymes such as the cytochrome P450 Luz26 converts –N–NH– into the –N=N– of dehydropiperazic acid (Dpz), which has **no NH proton** and is invisible to HSQC-TOCSY.

Their fix is to move from proton-detected NH signatures to nitrogen chemical-shift signatures read by ¹H–¹⁵N HMBC, which only needs a proton within long-range coupling distance. Because ¹⁵N shifts were barely reported for Piz and never for Dpz, they first established the reference data by feeding the lydiamycin A producer *Streptomyces* sp. GG23 with ¹⁵N₂-L-ornithine. The four nitrogens resolved into a diagnostic fingerprint: δN 79.5 (NH) and 140.6 (amide N) for Piz, and δN 173.1 (amide N) and 318.6 (=N–) for Dpz. The imine-like nitrogen near δN 313–318 is the signature that HSQC-TOCSY cannot see — and it is precisely the signature that later flagged depsidomycin D, carrying two Dpz units, in strain BYK1239. Hit strains were screened by culturing with ¹⁵NH₄Cl and acquiring ¹H–¹⁵N HMBC alongside HSQC and HSQC-TOCSY.


## How the pairing works as a pipeline

Read as a workflow, the paper is a sequence of gates, each removing a different kind of uncertainty:

1. **PCR screen** (2020 → 62 strains): does the strain carry *ktzT*? Cross-validation with *ktzI* primers guards against artifacts.
2. **Amplicon phylogeny** (62 strains → clades): what structural family is likely? Reference-occupied clades flag dereplication risk; empty clades flag novelty.
3. **LC/MS with UV and in-house dereplication** (62 → 12 peptide-producers → 5 prioritized strains): is anything peptide-like actually produced, and is it already known? Seven strains were excluded here on dereplication alone.
4. **¹⁵N labeling + ¹H–¹⁵N 2D NMR**: is the metabolite genuinely Piz- or Dpz-bearing? This gate is what makes downstream isolation "logical" rather than hopeful.
5. **Targeted isolation and structure elucidation** of the surviving cultures, followed by biosynthetic gene cluster analysis (antiSMASH) and, where needed, advanced Marfey's analysis and J-based configuration analysis.

The discoveries track the gates: a new azinothricin congener where group I predicted one; chloptosin, correctly identified as known; depsidomycin D, found **because** the Dpz nitrogen signature said a family thought to contain only Piz actually carried its oxidized derivative; and the lenziamides from an uncharacterized group II clade, exactly where the atlas said novelty was most likely.

## Why the pairing matters more than either half

Neither signature is sufficient alone, and the paper is at its best where the two compensate for each other. The genomic signature is cheap and scales to thousands of strains, but it detects *potential* — silent clusters, primer-mismatched variants, and non-producing cultures all pass through it. The spectroscopic signature detects *production* — the molecule, in the flask, now — but it is expensive per strain (¹⁵N feeding, 2D NMR time on crude extracts) and says nothing about novelty on its own. Run genomics first and spectroscopy second, and each filter removes the other's most expensive failures: NMR time is spent only on strains already predicted to be interesting, and isolation effort only on cultures confirmed to produce the motif. The same logic underpinned this group's earlier macrolactam work, which is what makes the approach a strategy rather than a one-off.

## Limitations and open questions

A close reading should hold onto what the method cannot do:

- **Primer bias.** Degenerate primers amplify conserved homologues; genuinely divergent *ktzT* genes will be missed. The hit set was 98% *Streptomyces*, which may reflect the library, primer bias, or biology — the design cannot fully separate these.
- **The atlas is statistical, not causal.** Nineteen of 23 clades map to structures, but clades 17 and 18 remain unassigned, and within-clade variation (new congeners beside known compounds) means phylogeny prioritizes rather than determines.
- **Labeling cost and sensitivity.** ¹⁵NH₄Cl and ¹⁵N₂-L-ornithine feeding plus HMBC on crude extracts demand both isotope budget and NMR sensitivity; low-titre producers may fall below the HMBC detection gate even when the genomic signature is genuine.
- **Signature scope.** The δN fingerprint is established for Piz and Dpz; other Piz-derived motifs may need their own reference shifts before the same confidence applies.

None of these caveats diminish the central demonstration: that a short, cheap genomic readout and a motif-specific spectroscopic readout, used in sequence, can turn a 2020-strain library into five strains and five structures with a minimum of blind fractionation.

## What to take from it

For a practicing natural product chemist, the transferable lessons are the design principles rather than the specific motifs: choose signature genes whose essentiality you understand and whose primers you have controlled against lookalike families; treat amplicon phylogeny as a prioritization atlas anchored by reference strains; and build spectroscopic signatures from the *chemical shifts of diagnostic nuclei* — not just from the presence of a protonated handle — so that modified forms of the motif remain detectable. And when the biosynthetic machinery installs a motif containing an unusual element or bond, ask what that element's NMR properties uniquely reveal. The N–N bond that makes piperazic acid biosynthetically remarkable is, in this paper, also what makes it spectroscopically findable.

This is the spectroscopic analogue of the genomic move: instead of asking "is there a peak?", ask "what does the chemical shift of this nucleus tell us about the motif?" — and be explicit about which derivatives each experiment can and cannot detect.

- The atlas predicts **structural class**, not structure. Within clade 1, strain GB16 yielded a new azinothricin congener, while GIN13 yielded the known dentigerumycin E. The genomic signature prioritizes; it does not dereplicate.

Piperazic acid is a cyclic hydrazine amino acid found in a small but potent family of bacterial peptides. It is biosynthesized from L-ornithine by two enzymes: the L-ornithine N-hydroxylase KtzI and the heme-dependent N–N bond-forming enzyme KtzT. The authors reasoned that these two genes could serve as a genomic signature of Piz biosynthetic potential, and that the unusual nitrogen atoms of the Piz motif could serve as a spectroscopic signature of actual Piz production. Screening 2020 bacterial strains by PCR against *ktzT* yielded 62 hits (3.1%); phylogenetic analysis of the amplicons sorted them into 23 clades in two monophyletic groups; and ¹⁵N-labeling followed by ¹H–¹⁵N 2D NMR identified which cultures genuinely made Piz-bearing metabolites. The prioritized strains delivered a new azinothricin congener (polyoxyperuin B seco acid), a new depsidomycin with two dehydropiperazic acid units (depsidomycin D), and the lenziamides A and B — structurally novel 31-membered cyclic decapeptides, of which lenziamide A showed STAT3-linked antiproliferative activity and resensitized 5-fluorouracil-resistant colorectal tumors in vitro and in vivo.
