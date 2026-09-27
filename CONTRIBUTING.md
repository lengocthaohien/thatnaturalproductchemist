# Contributing

That Natural Product Chemist accepts topic proposals, scientific corrections, and complete publication contributions through GitHub.

Read [ideology.md](ideology.md) before proposing a contribution. Choose one publication form:

- **Articles** are close readings and perspectives on noteworthy scientific papers. Each article is labeled with one of four article types — chemical diversity, biosynthesis, research methodology, or review — chosen by the contribution the paper makes (see [docs/adding-content.md](docs/adding-content.md)).
- **Opinions** present reasoned positions or practical assessments of tools, with evidence and preference clearly distinguished.
- **Exercises** present evidence progressively and must not reveal the structure in titles, figures, filenames, metadata, downloads, or early text. Solutions require scientific review.
- **Examples** show the structure from the beginning while demonstrating what selected techniques contribute and how the reasoning works.

## Proposals and corrections

Open an issue for a proposed topic or correction. For corrections, identify the article passage, signal, assignment, or correlation precisely and include supporting experimental evidence or a citable source where possible.

## Content contributions

Example proposals may begin with the guided submission window on the Contribute page. An Example submission requires:

- a stable public link to sanitized NMR data;
- the chemical structure as SMILES;
- an elucidation workflow that distinguishes observations, inference, and uncertainty; and
- the submitter's name and affiliation or independent-researcher status.

Submitters who request named inclusion in a resulting publication must provide an ORCID iD. ORCID is optional when a submitter is corresponding only and does not request publication credit. Every proposal remains subject to scientific, rights, and editorial review; submission does not guarantee publication.

The guided window prepares a public GitHub issue. It does not upload or retain files in the website. Deposit NMR data in Zenodo, OSF, an institutional repository, or a GitHub Release and provide the stable URL. Remove private paths, usernames, personal information, credentials, and unrelated sample metadata before sharing it.

1. Fork the repository and create a branch.
2. Add a Markdown file under `src/content/articles/` using the frontmatter schema documented in [docs/adding-content.md](docs/adding-content.md).
3. Set `draft: true` until scientific review is complete.
4. Run `npm run build` locally.
5. Open a pull request describing the scope, evidence, and any unresolved interpretation.

Every contribution must declare:

- the author name and ORCID, when available;
- who created each submitted dataset;
- permission to publish the text, figures, and data under CC BY-NC 4.0;
- the sample identity and acquisition context;
- any sanitization performed on instrument exports; and
- uncertainties, competing interpretations, and known limitations.

Do not commit raw workstation folders, private paths, usernames, audit logs, personal data, credentials, or files whose publication rights are unclear. Large teaching packages belong in a public GitHub Release; citable research deposits may belong in Zenodo. Link the stable record from entry metadata.

Follow [docs/media-authoring.md](docs/media-authoring.md) for figures and PDFs. Every figure needs meaningful alt text and a nearby scientific caption. PDFs must be direct supplementary downloads, not the only place where essential observations or conclusions can be read.

## Style rules

- Main body text is typeset **justified**, as in scientific papers. Write in full paragraphs and never use manual line breaks, trailing spaces, or extra blank lines to control alignment — the stylesheet handles it.
- Headings, captions, metadata, and other small texts stay left-aligned; do not try to center or pad them in Markdown.

## Scientific review

Assignments are evidence claims. Before a draft is published, its author must verify all reported chemical shifts, integrations, multiplicities, correlations, atom labels, experimental metadata, and interpretation paragraphs against the supplied spectra. Reviewers may request processed views, raw data, or revisions to distinguish observation from inference.

Corrections remain visible through the entry update date and optional correction note.
