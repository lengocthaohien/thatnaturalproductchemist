/**
 * Shared visual style for published NMR figures.
 *
 * Every script that renders an NMR figure for the site — articles, opinions,
 * exercises, and examples alike — must import these constants instead of
 * hard-coding colors, so all spectra share one background and palette. The
 * only exception is the decorative hero spectrum on the homepage
 * (`src/pages/index.astro`), which is not a data figure.
 */

/**
 * Spectrum figure background. Matches the site's `--paper-deep` token in
 * `src/styles/global.css`. It is deliberately light so that traces and
 * contour signals stay clearly visible.
 */
export const SPECTRUM_BACKGROUND = '#F4F1EA';
