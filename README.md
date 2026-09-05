# That Natural Product Chemist

A static scientific publication about the practice, evidence, tools, and ideas of natural product chemistry. It supports literature-focused Articles, reasoned Opinions, evidence-first Exercises, and structure-forward Examples.

The educational and communicative principles are recorded in [ideology.md](ideology.md).

## Local development

Requirements: Node.js 22 or newer and npm.

```sh
npm install
npm run dev
```

Run the complete content, type, and production check with:

```sh
npm run build
```

If a local npm cache contains files owned by another user, use a disposable cache without changing system permissions:

```sh
npm_config_cache="$TMPDIR/tnpc-npm-cache" npm install
```

## NMR data preparation

The source Bruker folders are external to this repository and must be treated as immutable. Create sanitized publication copies by passing the source and output folders explicitly:

```sh
npm run prepare:data -- /path/to/A_UBL staging/cyclo-l-pro-l-leu
```

The script:

- accepts experiments `30` through `35` only;
- creates separate archival and browser trees;
- copies an explicit allowlist of acquisition, processing, and binary spectral files;
- removes private path/identity blocks and stale processed sample metadata;
- replaces public titles;
- verifies copied and source spectral binaries with SHA-256; and
- emits `manifest.json` and `SHA256SUMS`.

Generated packages are ignored by Git. The current complete archive is approximately 73 MiB compressed and the display-only browser ZIP approximately 25 MiB, so neither is committed to repository history. Exercise 001 uses public GitHub Release assets; future citable research deposits may use Zenodo when a DOI is appropriate.

For Exercise 001, the script also creates neutral, reproducible GitHub Release assets:

- `exercise-001-browser.zip` for NMRium;
- `exercise-001-archive.zip` for complete sanitized data;
- `SHA256SUMS`; and
- neutral `RELEASE-NOTES.md`.

The exercise packages deliberately omit the structural answer from titles, manifests, and metadata. The current public assets are attached to [`exercise-001-data-v1`](https://github.com/lengocthaohien/thatnaturalproductchemist/releases/tag/exercise-001-data-v1). Direct Release downloads do not permit browser cross-origin requests, so the Pages workflow mirrors the browser ZIP into `dist/data/` and NMRium loads it from the same site origin. The complete archive remains a direct Release download.

Generate the static no-JavaScript figures after preparing the browser package:

```sh
npm run prepare:figures
```

See [docs/media-authoring.md](docs/media-authoring.md) for the stepwise figure and PDF workflow, and [docs/adding-content.md](docs/adding-content.md) for how to add a new entry.

## Scientific release gate

The public Exercise 001 prompt contains no structural reveal. The Cyclo(L-Pro-L-Leu) solution remains `draft: true`; draft entries validate during the build but do not receive routes. Hien Le must review every chemical shift, integral, multiplicity, COSY correlation, HSQC attachment, HMBC correlation, atom label, and interpretation before publication.

## Deployment

Pushes to `main` are checked and deployed to GitHub Pages by `.github/workflows/deploy.yml`. Pull requests run the build without deploying. The canonical host and `CNAME` are `thatnaturalproductchemist.net`.

### Deployment test

A deployment test serves the production build (`dist/`) locally, exactly as GitHub Pages will serve it:

```sh
npm run build      # astro check + build into dist/
npm run preview    # serve dist/ locally
```

Then open [http://localhost:4321/](http://localhost:4321/). The preview server binds to `localhost` (which may resolve to the IPv6 loopback `::1`), so use the `localhost` URL — `http://127.0.0.1:4321/` (IPv4) may not connect. Stop the server with `Ctrl+C`.

To check the build without starting a server, run only `npm run build` and confirm it reports `0 errors`.

The live site deploys automatically on every push to `main`; a merged pull request is itself the pre-deployment check, since the workflow builds every PR without publishing it.

## Licensing

Code is licensed under the MIT License in `LICENSE`. Original articles and published datasets are licensed under CC BY-NC 4.0 as described in `LICENSE-CONTENT.md`. Third-party packages and referenced sources retain their own licenses.
