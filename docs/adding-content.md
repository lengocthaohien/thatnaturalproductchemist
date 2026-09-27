# Adding new content

That Natural Product Chemist stores every publication as a Markdown file in a single Astro **content collection** called `entries`. This page explains how to add a new one. It complements [../CONTRIBUTING.md](../CONTRIBUTING.md) (scope and review) and [media-authoring.md](media-authoring.md) (figures and PDFs).

## 1. Where content lives

```text
src/content/articles/<your-slug>.md
```

All sections share this one folder; the `section` frontmatter field (not the path) decides where an entry is published. The file name becomes the URL slug:

```text
src/content/articles/ampicillin-purity-comparison.md
  section: example   ->   https://thatnaturalproductchemist.net/examples/ampicillin-purity-comparison/
```

Section-to-URL mapping (defined in `src/lib/content.ts`):

| `section` | URL prefix |
| --- | --- |
| `article` | `/articles/` |
| `opinion` | `/opinions/` |
| `exercise` | `/exercises/` |
| `example` | `/examples/` |

## 2. Frontmatter schema

Frontmatter is validated at build time by `src/content.config.ts`. Required fields are marked below.

| Field | Type | Notes |
| --- | --- | --- |
| `section` * | `article \| opinion \| exercise \| example` | Chooses the section and URL. |
| `format` * | see list below | Must be compatible with `section` (see validation rules). |
| `paperType` | `chemical-diversity \| biosynthesis \| research-methodology \| review` | **Required for articles**, forbidden for other sections. Shown as the kicker above the title and in listings; see "Article types" below. |
| `title` * | string | |
| `summary` * | string | One or two sentences; used for listings and `<meta name="description">`. |
| `category` | `field-note \| structure-elucidation \| reference` | Optional. |
| `audience` * | array of `junior` / `advanced` | At least one. |
| `author` * | `{ name, orcid }` | `orcid` must match `0000-0000-0000-000X` format. |
| `publishedAt` * | date | e.g. `2026-08-30`. |
| `updatedAt` | date | Set when a published entry is revised. |
| `tags` | array of strings | Defaults to `[]`. |
| `references` | array of `{ citation, url? }` | Rendered as a numbered reference list. |
| `license` | `CC BY-NC 4.0` | Fixed; defaults to this. |
| `correctionNote` | string | Shown in a highlighted box when present. |
| `exercise` | object | Only for exercises; see below. |
| `spectrum` | object | Optional NMRium viewer config; see below. |
| `draft` | boolean | **Defaults to `true`.** Drafts build but get no route. |

Allowed `format` values: `field-note`, `paper-perspective`, `opinion`, `tool-review`, `research-journey`, `method-note`, `reference`, `guided-exercise`, `worked-example`, `reviewed-solution`.

### Article types (`paperType`)

Every article declares exactly one `paperType`, chosen by the contribution the paper under discussion makes. It replaces the old generic "paper perspective" kicker above the article title and appears in section listings:

- `chemical-diversity` — the paper's core contribution is new chemistry: novel skeletons, new structural classes, isolation and structure elucidation.
- `biosynthesis` — the paper is about how organisms build natural products: gene clusters, enzymology, precursor feeding, pathway engineering.
- `research-methodology` — the paper's core contribution is a way of working: discovery workflows, analytical or computational methods, dereplication and prioritization strategies.
- `review` — the paper synthesizes a field (review, census, or meta-analysis) rather than reporting a single study.

### Section/format validation rules

The schema enforces these pairings and fails the build if violated:

- `section: article` → `format` **must** be `paper-perspective`, and `paperType` **must** be set to one of the four article types. `paperType` must not be set for other sections.
- `section: opinion` → `format` must be `opinion` or `tool-review`.
- `section: exercise` / `example` → use `guided-exercise` / `reviewed-solution` / `worked-example` as appropriate.

### Exercise-only block

```yaml
exercise:
  number: 1                      # positive integer
  solutionStatus: withheld       # withheld | in-review | published
  learningGoals:
    - At least one learning goal.
```

### Optional interactive spectrum (NMRium)

```yaml
spectrum:
  viewerTitle: Short viewer title
  viewerDescription: What the reader can inspect.
  archiveUrl: /data/<package>.zip        # same-origin NMRium package
  downloadUrl: https://.../archive.zip   # optional full download
  experiments:
    - number: 31
      label: Proton NMR
      nuclei: 1H
      frequencyMHz: "600.4036"
      solvent: DMSO-d6
      temperatureK: 298
      pulseProgram: zg30
      dimensions: 1D                     # 1D | 2D
      role: primary                      # primary | comparison
```

## 3. Minimal template

```md
---
title: Descriptive title
summary: One- or two-sentence summary used in listings and metadata.
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
  - NMR
license: CC BY-NC 4.0
draft: true
---

Opening paragraph that states the question and why it matters.

## A section

Body text. Keep observations separate from interpretation, and name uncertainties.
```

## 4. Text style rules

- Main body text is rendered **justified** (like scientific papers) with automatic hyphenation. Write normal flowing paragraphs; never insert manual line breaks, double spaces, or blank lines to influence alignment.
- Headings, figure captions, and metadata (kicker, author line, footer notes) are intentionally left-aligned — leave them as plain Markdown.
- Use `##` for sections and `*emphasis*` on the line directly after a figure for its caption.

## 5. The draft / review gate

`draft` **defaults to `true`**. A draft entry is validated during `npm run build` but is **not** assigned a route, so it never reaches the public site. Publish by setting `draft: false` only after scientific review: verify every chemical shift, integral, multiplicity, correlation, atom label, and acquisition metadata against the spectra. Keep `solutionStatus: withheld` on exercises until the solution has passed review, and never reveal a structure in an exercise's title, figures, filenames, or metadata.

## 6. Adding figures and data

Follow [media-authoring.md](media-authoring.md). In short:

- Put public assets under `public/media/{section}/{entry-slug}/` and reference them with root-relative URLs.
- Prefer SVG for spectra/schemes, PNG or WebP for raster images; never JPEG for line art.
- Every image needs descriptive alt text and a nearby scientific caption (technique, sample context, conditions, what to inspect, any normalization).
- **Sanitize before publishing**: remove local file paths, usernames, sample identifiers, audit trails, and credentials from every exported figure, PDF, and data package. Instrument-software exports frequently embed workstation paths — check them.

## 7. Local checks

```sh
npm install
npm run dev     # live preview at http://localhost:4321/
npm run build   # astro check + production build; must pass with 0 errors
```

Open the built page on desktop and mobile widths, confirm every figure loads and its caption matches the data, and confirm no draft-only content is reachable.
