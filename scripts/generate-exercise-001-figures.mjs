import { readFile, mkdir, writeFile } from 'node:fs/promises';
import { resolve, join } from 'node:path';
import { contours } from 'd3-contour';
import { FileCollection } from 'file-collection';
import initializeNMRiumCore from '@zakodium/nmrium-core-plugins';

const archivePath = resolve(
  process.argv[2] ?? 'staging/exercise-001/exercise-001-browser.zip',
);
const outputRoot = resolve(
  process.argv[3] ?? 'public/media/exercises/exercise-001-cyclic-dipeptide',
);

const core = initializeNMRiumCore();
const archiveBytes = await readFile(archivePath);
const files = await FileCollection.fromZip(archiveBytes);
const { state } = await core.read(files);
const spectra = state.data?.spectra ?? [];

const proton = spectra.find((spectrum) => spectrum.info?.name === 'browser/31');
const hsqc = spectra.find((spectrum) => spectrum.info?.name === 'browser/34');

if (!proton?.data?.x || !proton.data.re) {
  throw new Error('Exercise 001 experiment 31 did not parse as a 1D spectrum.');
}
if (!hsqc?.data?.rr?.z) {
  throw new Error('Exercise 001 experiment 34 did not parse as a 2D spectrum.');
}

await mkdir(outputRoot, { recursive: true });
await writeFile(join(outputRoot, 'proton-600-mhz.svg'), renderProton(proton));
await writeFile(join(outputRoot, 'edited-hsqc.svg'), renderHsqc(hsqc));

console.log(`Created ${join(outputRoot, 'proton-600-mhz.svg')}`);
console.log(`Created ${join(outputRoot, 'edited-hsqc.svg')}`);

function renderProton(spectrum) {
  const width = 1400;
  const height = 620;
  const plot = { left: 90, right: 1350, top: 95, bottom: 505 };
  const minPpm = 0;
  const maxPpm = 10;
  const bins = plot.right - plot.left;
  const points = [];

  for (let bin = 0; bin <= bins; bin++) {
    const highPpm = maxPpm - (bin / bins) * (maxPpm - minPpm);
    const lowPpm = maxPpm - ((bin + 1) / bins) * (maxPpm - minPpm);
    let maximum = Number.NEGATIVE_INFINITY;

    for (let index = 0; index < spectrum.data.x.length; index++) {
      const ppm = spectrum.data.x[index];
      if (ppm <= highPpm && ppm >= lowPpm) {
        maximum = Math.max(maximum, spectrum.data.re[index]);
      }
    }
    if (Number.isFinite(maximum)) points.push(maximum);
  }

  const sorted = [...points].sort((left, right) => left - right);
  const baseline = quantile(sorted, 0.5);
  const ceiling = quantile(sorted, 0.995);
  const scale = Math.max(1, ceiling - baseline);
  const path = points
    .map((value, index) => {
      const x = plot.left + (index / (points.length - 1)) * (plot.right - plot.left);
      const normalized = clamp((value - baseline) / scale, -0.04, 1.05);
      const y = plot.bottom - normalized * (plot.bottom - plot.top);
      return `${index === 0 ? 'M' : 'L'}${x.toFixed(2)},${y.toFixed(2)}`;
    })
    .join(' ');
  const ticks = [10, 8, 6, 4, 2, 0]
    .map((ppm) => {
      const x = plot.left + ((maxPpm - ppm) / (maxPpm - minPpm)) * (plot.right - plot.left);
      return `<line x1="${x}" y1="${plot.bottom}" x2="${x}" y2="${plot.bottom + 10}"/><text x="${x}" y="${plot.bottom + 36}" text-anchor="middle">${ppm}</text>`;
    })
    .join('');

  // Residual solvent annotation: DMSO-d₆ at 2.50 ppm, the calibration reference
  // from the Cambridge Isotope Laboratories NMR Solvent Data Chart
  // (nmrsolventschart_001.pdf). The note sits next to the solvent peak with an
  // arrow pointing at it.
  const solventPpm = 2.5;
  const solventBin = Math.round(((maxPpm - solventPpm) / (maxPpm - minPpm)) * bins);
  const solventX = plot.left + (solventBin / (points.length - 1)) * (plot.right - plot.left);
  const solventNormalized = clamp((points[solventBin] - baseline) / scale, -0.04, 1.05);
  const solventY = plot.bottom - solventNormalized * (plot.bottom - plot.top);
  const solventNoteY = Math.max(30, solventY - 44);

  return svgDocument(
    width,
    height,
    `<text class="label" x="${plot.left}" y="42">TNPC EXERCISE 001 · EXPERIMENT 31</text>
     <text class="title" x="${plot.left}" y="76">¹H NMR · 600 MHz · DMSO-d₆</text>
     <line class="axis" x1="${plot.left}" y1="${plot.bottom}" x2="${plot.right}" y2="${plot.bottom}"/>
     <g class="ticks">${ticks}<text x="${plot.right}" y="${plot.bottom + 70}" text-anchor="end">δ / ppm</text></g>
     <path class="trace" d="${path}"/>
     <text class="note" x="${solventX}" y="${solventNoteY}" text-anchor="end">2.50 ppm = residual DMSO-d₆</text>
     <line class="arrow" x1="${solventX}" y1="${solventNoteY + 7}" x2="${solventX}" y2="${solventY - 7}" marker-end="url(#arrowhead)"/>
     <text class="note" x="${plot.left}" y="590">Display trace generated from the sanitized processed real array; intensity is normalized for overview.</text>`,
  );
}

function renderHsqc(spectrum) {
  const width = 1400;
  const height = 900;
  const plot = { left: 110, right: 1330, top: 110, bottom: 800 };
  const gridWidth = 480;
  const gridHeight = 480;
  const xRange = [10, 0];
  const yRange = [180, 0];
  const rr = spectrum.data.rr;
  const grid = downsampleMatrix(rr, gridWidth, gridHeight, xRange, yRange);
  const positive = grid.map((value) => Math.max(0, value));
  const negative = grid.map((value) => Math.max(0, -value));
  const absolute = grid.map(Math.abs).sort((left, right) => left - right);
  const baseThreshold = quantile(absolute, 0.995);
  const levels = [1, 1.8, 3.2, 5.8].map((factor) => baseThreshold * factor);
  const contourGenerator = contours().size([gridWidth, gridHeight]).thresholds(levels);
  const positivePaths = contourGenerator(positive)
    .map((contour) => geometryPath(contour.coordinates, plot, gridWidth, gridHeight))
    .join('');
  const negativePaths = contourGenerator(negative)
    .map((contour) => geometryPath(contour.coordinates, plot, gridWidth, gridHeight))
    .join('');
  const xTicks = [10, 8, 6, 4, 2, 0]
    .map((ppm) => {
      const x = plot.left + ((10 - ppm) / 10) * (plot.right - plot.left);
      return `<line x1="${x}" y1="${plot.bottom}" x2="${x}" y2="${plot.bottom + 10}"/><text x="${x}" y="${plot.bottom + 34}" text-anchor="middle">${ppm}</text>`;
    })
    .join('');
  const yTicks = [180, 150, 120, 90, 60, 30, 0]
    .map((ppm) => {
      const y = plot.top + ((180 - ppm) / 180) * (plot.bottom - plot.top);
      return `<line x1="${plot.left - 10}" y1="${y}" x2="${plot.left}" y2="${y}"/><text x="${plot.left - 18}" y="${y + 5}" text-anchor="end">${ppm}</text>`;
    })
    .join('');

  return svgDocument(
    width,
    height,
    `<text class="label" x="${plot.left}" y="42">TNPC EXERCISE 001 · EXPERIMENT 34</text>
     <text class="title" x="${plot.left}" y="76">Edited ¹H–¹³C HSQC · DMSO-d₆</text>
     <rect class="plot" x="${plot.left}" y="${plot.top}" width="${plot.right - plot.left}" height="${plot.bottom - plot.top}"/>
     <g class="contours positive">${positivePaths}</g>
     <g class="contours negative">${negativePaths}</g>
     <g class="ticks">${xTicks}${yTicks}<text x="${plot.right}" y="${plot.bottom + 66}" text-anchor="end">δ ¹H / ppm</text><text transform="translate(26 ${plot.top}) rotate(-90)" text-anchor="end">δ ¹³C / ppm</text></g>
    <g class="legend"><line x1="110" y1="96" x2="145" y2="96" class="positive-key"/><text x="155" y="101">positive phase</text><line x1="270" y1="96" x2="305" y2="96" class="negative-key"/><text x="315" y="101">negative phase</text></g>
     <text class="note" x="${plot.left}" y="880">Contours generated from the sanitized processed real matrix; levels are normalized for overview.</text>`,
  );
}

function downsampleMatrix(rr, width, height, xRange, yRange) {
  const sourceHeight = rr.z.length;
  const sourceWidth = rr.z[0].length;
  const output = new Array(width * height);

  for (let row = 0; row < height; row++) {
    const yHigh = interpolate(yRange[0], yRange[1], row / height);
    const yLow = interpolate(yRange[0], yRange[1], (row + 1) / height);
    const sourceYStart = axisIndex(yHigh, rr.minY, rr.maxY, sourceHeight);
    const sourceYEnd = axisIndex(yLow, rr.minY, rr.maxY, sourceHeight);

    for (let column = 0; column < width; column++) {
      const xHigh = interpolate(xRange[0], xRange[1], column / width);
      const xLow = interpolate(xRange[0], xRange[1], (column + 1) / width);
      const sourceXStart = axisIndex(xHigh, rr.minX, rr.maxX, sourceWidth);
      const sourceXEnd = axisIndex(xLow, rr.minX, rr.maxX, sourceWidth);
      let strongest = 0;

      for (let sourceY = Math.min(sourceYStart, sourceYEnd); sourceY <= Math.max(sourceYStart, sourceYEnd); sourceY++) {
        for (let sourceX = Math.min(sourceXStart, sourceXEnd); sourceX <= Math.max(sourceXStart, sourceXEnd); sourceX++) {
          const value = rr.z[sourceY][sourceX];
          if (Math.abs(value) > Math.abs(strongest)) strongest = value;
        }
      }
      output[row * width + column] = strongest;
    }
  }
  return output;
}

function geometryPath(multiPolygon, plot, gridWidth, gridHeight) {
  const scaleX = (plot.right - plot.left) / gridWidth;
  const scaleY = (plot.bottom - plot.top) / gridHeight;
  const path = multiPolygon
    .flatMap((polygon) => polygon)
    .map((ring) => ring.map(([x, y], index) => `${index === 0 ? 'M' : 'L'}${(plot.left + x * scaleX).toFixed(1)},${(plot.top + y * scaleY).toFixed(1)}`).join(' ') + ' Z')
    .join(' ');
  return `<path d="${path}"/>`;
}

function svgDocument(width, height, contents) {
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${width} ${height}" role="img">
  <style>
    .label,.ticks,.legend,.note{font-family:ui-monospace,SFMono-Regular,Menlo,monospace}.label{font-size:17px;fill:#5E3A52}.title{font-family:Georgia,serif;font-size:27px;fill:#3D2036}.axis,.ticks line,.plot{stroke:#3D2036;stroke-width:1;fill:none}.ticks,.legend{font-size:15px;fill:#3D2036}.trace{stroke:#C9A227;stroke-width:1.5;fill:none}.contours path{fill:none;stroke-width:1}.positive path,.positive-key{stroke:#5E3A52}.negative path,.negative-key{stroke:#C9A227}.note{font-size:13px;fill:#7A6A5F}.arrow{stroke:#7A6A5F;stroke-width:1.2;fill:none}
  </style>
  <defs>
    <marker id="arrowhead" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0 0L10 5L0 10z" fill="#7A6A5F"/>
    </marker>
  </defs>
  <rect width="100%" height="100%" fill="#E7DCC0"/>
  ${contents}
</svg>\n`;
}

function axisIndex(value, minimum, maximum, length) {
  return Math.round(clamp((value - minimum) / (maximum - minimum), 0, 1) * (length - 1));
}

function quantile(sorted, probability) {
  return sorted[Math.floor((sorted.length - 1) * probability)];
}

function interpolate(start, end, ratio) {
  return start + (end - start) * ratio;
}

function clamp(value, minimum, maximum) {
  return Math.min(maximum, Math.max(minimum, value));
}