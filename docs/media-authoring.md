# Adding scientific figures and PDFs

Interactive viewers are valuable for inspection, but they are not the publication record by themselves. Every analytical entry should remain understandable through HTML text, static figures, captions, tables, and direct file links.

## 1. Prepare the figure

Export from trusted analytical software at a size that remains legible without enlargement.

- Prefer SVG for line spectra, schemes, and plots when the export is self-contained and safe.
- Prefer PNG or WebP for raster images such as TLC plates, chromatograms, gels, microscopy, or instrument screenshots.
- Do not use JPEG for spectra, structures, or text-heavy plots because compression artifacts obscure fine lines.
- Remove workstation paths, usernames, sample identifiers, audit trails, unrelated compounds, and credentials.
- For Exercises, also remove the compound name, structure, formula, database identifiers, and any file title that reveals the answer.

Use a descriptive filename rather than `figure1-final.png`. For example:

```text
public/media/exercises/exercise-001-cyclic-dipeptide/proton-600-mhz.svg
public/media/examples/example-slug/uhplc-uv-254nm.webp
```

## 2. Place the asset

Store public media under:

```text
public/media/{section}/{entry-slug}/
```

Use `articles`, `exercises`, or `examples` as the section. Keep source project files from proprietary instrument software outside `public/`; publish only the intentional export.

## 3. Embed an image in Markdown

Use Markdown image syntax with alt text that communicates the scientific content rather than saying only “spectrum” or “figure.” Files under `public/` use root-relative URLs:

```md
![UHPLC chromatogram with the principal peak at 8.4 minutes and two minor earlier peaks.](/media/examples/example-slug/uhplc-uv-254nm.webp)

*Figure 2. UHPLC-UV chromatogram at 254 nm. The 8.4 minute fraction was selected for MS and NMR analysis.*
```

The nearby caption should state:

1. the analytical technique;
2. the sample or fraction context that may be disclosed;
3. essential acquisition or display conditions;
4. what the reader should inspect; and
5. whether intensity, contour levels, or axes were normalized or cropped.

Do not put the only interpretation in alt text or in the image. Explain the conclusion in normal HTML prose as well.

## 4. Add a PDF

Use PDF for a supplementary report, complete spectrum set, protocol, or printable worksheet, not as the only readable version of an article.

1. Sanitize the PDF metadata and every displayed page.
2. Give it a descriptive filename and place it in the same media directory.
3. Record the file size after export.
4. Link directly with the document type and size:

```md
[Download the complete annotated spectrum set (PDF, 2.8 MB)](/media/examples/example-slug/annotated-spectrum-set.pdf)
```

5. Repeat essential observations, conclusions, and accessibility information in the page HTML.

Avoid embedded PDF viewers. Direct links work better across mobile browsers, assistive technologies, downloads, and archival copies.

## 5. Review before publication

- Open every asset at desktop and mobile widths.
- Confirm labels, axes, legends, and longest words fit without overlap.
- Check that color is not the only way phases, series, or categories are distinguished.
- Confirm the caption agrees with the displayed processing and acquisition metadata.
- Search the exported files for private metadata and, for Exercises, structural spoilers.
- Confirm that you created the asset or have permission to publish it under the stated content license.
- Run `npm run build` and inspect the generated page.

## Reproducing Exercise 001 previews

After preparing the sanitized browser ZIP, regenerate the committed static figures with:

```sh
npm run prepare:figures
```

The script parses the same Bruker package used by NMRium and writes a calibrated proton trace and edited-HSQC contour preview. It does not modify the original NMR folders.