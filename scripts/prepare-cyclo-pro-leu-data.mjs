import { createHash } from 'node:crypto';
import { execFile } from 'node:child_process';
import {
  copyFile,
  mkdir,
  readFile,
  readdir,
  rm,
  stat,
  utimes,
  writeFile,
} from 'node:fs/promises';
import { basename, dirname, isAbsolute, join, relative, resolve } from 'node:path';
import { promisify } from 'node:util';

const executeFile = promisify(execFile);

const sourceRoot = process.argv[2] ? resolve(process.argv[2]) : undefined;
const outputRoot = resolve(process.argv[3] ?? 'staging/cyclo-l-pro-l-leu');

if (!sourceRoot) {
  console.error('Usage: npm run prepare:data -- <Bruker source folder> [output folder]');
  process.exit(1);
}

const experiments = [
  {
    number: 30,
    label: '1H 400 MHz comparison',
    nuclei: '1H',
    frequencyMHz: '400.1328',
    temperatureK: 300,
    pulseProgram: 'zg30',
    dimensions: '1D',
    role: 'comparison',
  },
  {
    number: 31,
    label: '1H 600 MHz',
    nuclei: '1H',
    frequencyMHz: '600.4036',
    temperatureK: 298,
    pulseProgram: 'zg30',
    dimensions: '1D',
    role: 'primary',
  },
  {
    number: 32,
    label: 'J-modulated 13C',
    nuclei: '13C',
    frequencyMHz: '150.9858',
    temperatureK: 298,
    pulseProgram: 'jmod',
    dimensions: '1D',
    role: 'primary',
  },
  {
    number: 33,
    label: '1H-1H COSY',
    nuclei: '1H-1H',
    frequencyMHz: '600.4045',
    temperatureK: 298,
    pulseProgram: 'cosygpmfppqf',
    dimensions: '2D',
    role: 'primary',
  },
  {
    number: 34,
    label: 'Edited 1H-13C HSQC',
    nuclei: '1H-13C',
    frequencyMHz: '600.4045 / 150.9843',
    temperatureK: 298,
    pulseProgram: 'hsqcedetgpsp.3',
    dimensions: '2D',
    role: 'primary',
  },
  {
    number: 35,
    label: '1H-13C HMBC',
    nuclei: '1H-13C',
    frequencyMHz: '600.4045 / 150.9888',
    temperatureK: 298,
    pulseProgram: 'hmbcetgpl3nd',
    dimensions: '2D',
    role: 'primary',
  },
];

const acquisitionFiles = ['acqus', 'acqu2s'];
const processingFiles = ['procs', 'proc2s'];
const processedArrays = ['1r', '1i', '2rr', '2ri', '2ir', '2ii'];
const browserArrays = new Set(['1r', '2rr']);
const privateParameterNames = new Set([
  'OWNER',
  'PATH',
  'USER',
  'USERNAME',
  'HOST',
  'HOSTNAME',
  'SREGLST',
  'TI',
]);
const forbiddenText = [
  { label: 'exercise answer', pattern: /Cyclo\s*\(?\s*(?:L-)?Pro\s*[-–]\s*(?:L-)?Leu/i },
  { label: 'exercise answer synonym', pattern: /Gancidin\s+W/i },
  { label: 'exercise answer formula', pattern: /C11H18N2O2/i },
  { label: 'exercise answer InChIKey', pattern: /SZJNCZMRZAUNQT-IUCAKERBSA-N/i },
  { label: 'exercise answer SMILES', pattern: /CC\(C\)C\[C@H\]1C\(=O\)N2CCC\[C@H\]2C\(=O\)N1/i },
  { label: 'stale sample identifier', pattern: /TK203/i },
  { label: 'stale solvent', pattern: /CDCl3/i },
  { label: 'private cloud path', pattern: /OneDrive-Hien/i },
  { label: 'Windows drive path', pattern: /(?:^|[\s<"'])(?:[A-Z]:[\\/])/im },
  { label: 'macOS user path', pattern: /\/Users\//i },
  { label: 'UNC path', pattern: /\\\\[^\\\s]+\\/ },
  { label: 'local username', pattern: /lpiuser/i },
];

assertSeparateTrees(sourceRoot, outputRoot);
await assertDirectory(sourceRoot);

const sourceBinaryHashes = new Map();
for (const experiment of experiments) {
  await assertDirectory(join(sourceRoot, String(experiment.number)));
  for (const sourceFile of await binarySourceFiles(experiment)) {
    sourceBinaryHashes.set(sourceFile, await sha256(sourceFile));
  }
}

await rm(outputRoot, { force: true, recursive: true });

const copiedFiles = [];
for (const experiment of experiments) {
  await prepareExperiment(experiment, 'archive', true);
  await prepareExperiment(experiment, 'browser', false);
}

for (const [sourceFile, hashBefore] of sourceBinaryHashes) {
  const hashAfter = await sha256(sourceFile);
  if (hashBefore !== hashAfter) {
    throw new Error(`Source binary changed during preparation: ${sourceFile}`);
  }
}

const manifest = {
  schemaVersion: 1,
  exercise: {
    number: 1,
    title: 'A cyclic dipeptide from 1D and 2D NMR',
    solutionStatus: 'in-review',
  },
  solvent: 'DMSO-d6',
  experiments,
  packages: {
    archive: 'Sanitized raw and processed Bruker files.',
    browser: 'Sanitized processed Bruker files for interactive viewing.',
  },
  sanitization: {
    copiedByAllowlist: true,
    publicTitlesReplaced: true,
    privateParameterBlocksRemoved: [...privateParameterNames].sort(),
    sourceBinariesVerifiedUnchanged: true,
  },
  files: copiedFiles.sort((left, right) => left.path.localeCompare(right.path)),
};

const manifestPath = join(outputRoot, 'manifest.json');
const releaseNotesPath = join(outputRoot, 'RELEASE-NOTES.md');
await writeFile(manifestPath, `${JSON.stringify(manifest, null, 2)}\n`);
await writeFile(
  releaseNotesPath,
  `# TNPC Exercise 001 analytical data\n\nSanitized Bruker NMR data for the evidence-first exercise “A cyclic dipeptide from 1D and 2D NMR.”\n\n- \`exercise-001-browser.zip\`: processed display arrays and essential parameters for NMRium.\n- \`exercise-001-archive.zip\`: sanitized raw and processed data for reproducibility.\n- \`SHA256SUMS\`: integrity checks for the release assets and package contents.\n\nThe structural answer is intentionally omitted while the reviewed solution is in preparation. Original dataset content is licensed CC BY-NC 4.0 by Hien Le.\n`,
);
await scanPublishedText([manifestPath, releaseNotesPath]);

const releaseArchives = await createReleaseArchives();
const localViewerPath = resolve('public/data/exercise-001-browser.zip');
await mkdir(dirname(localViewerPath), { recursive: true });
await copyFile(releaseArchives[0], localViewerPath);
await writeChecksums(releaseArchives);

const archiveBytes = copiedFiles
  .filter((file) => file.package === 'archive')
  .reduce((total, file) => total + file.bytes, 0);
const browserBytes = copiedFiles
  .filter((file) => file.package === 'browser')
  .reduce((total, file) => total + file.bytes, 0);

console.log(`Prepared ${outputRoot}`);
console.log(`Archive package: ${formatBytes(archiveBytes)}`);
console.log(`Browser package: ${formatBytes(browserBytes)}`);
for (const releaseArchive of releaseArchives) {
  console.log(`${basename(releaseArchive)}: ${formatBytes((await stat(releaseArchive)).size)}`);
}
console.log(`Local viewer package: ${localViewerPath}`);
console.log(`Verified ${sourceBinaryHashes.size} immutable source binaries.`);

async function prepareExperiment(experiment, packageName, includeRaw) {
  const experimentRoot = join(sourceRoot, String(experiment.number));
  const destinationRoot = join(outputRoot, packageName, String(experiment.number));
  const publicTitle = `TNPC Exercise 001 | Experiment ${experiment.number} | ${experiment.label} | DMSO-d6`;

  for (const filename of acquisitionFiles) {
    await copySanitizedTextIfPresent(
      join(experimentRoot, filename),
      join(destinationRoot, filename),
      publicTitle,
      packageName,
    );
  }

  if (includeRaw) {
    for (const filename of ['fid', 'ser']) {
      await copyBinaryIfPresent(
        join(experimentRoot, filename),
        join(destinationRoot, filename),
        packageName,
      );
    }
  }

  const processingRoot = join(experimentRoot, 'pdata', '1');
  const processingDestination = join(destinationRoot, 'pdata', '1');
  for (const filename of processingFiles) {
    await copySanitizedTextIfPresent(
      join(processingRoot, filename),
      join(processingDestination, filename),
      publicTitle,
      packageName,
    );
  }
  for (const filename of processedArrays.filter((filename) => includeRaw || browserArrays.has(filename))) {
    await copyBinaryIfPresent(
      join(processingRoot, filename),
      join(processingDestination, filename),
      packageName,
    );
  }

  const titlePath = join(processingDestination, 'title');
  await mkdir(dirname(titlePath), { recursive: true });
  await writeFile(titlePath, `${publicTitle}\n`);
  await recordFile(titlePath, packageName);
}

async function copySanitizedTextIfPresent(sourceFile, destinationFile, publicTitle, packageName) {
  if (!(await isFile(sourceFile))) return;

  const sourceText = await readFile(sourceFile, 'latin1');
  const sanitized = sanitizeBrukerText(sourceText, publicTitle);
  await mkdir(dirname(destinationFile), { recursive: true });
  await writeFile(destinationFile, sanitized, 'latin1');
  await recordFile(destinationFile, packageName);
}

async function copyBinaryIfPresent(sourceFile, destinationFile, packageName) {
  if (!(await isFile(sourceFile))) return;

  await mkdir(dirname(destinationFile), { recursive: true });
  await copyFile(sourceFile, destinationFile);
  const [sourceHash, destinationHash] = await Promise.all([
    sha256(sourceFile),
    sha256(destinationFile),
  ]);
  if (sourceHash !== destinationHash) {
    throw new Error(`Binary checksum mismatch: ${destinationFile}`);
  }
  await recordFile(destinationFile, packageName);
}

function sanitizeBrukerText(sourceText, publicTitle) {
  const lines = sourceText.split(/\r?\n/);
  const output = [];
  let removeCurrentBlock = false;

  for (const line of lines) {
    if (line.startsWith('##')) {
      const parameterMatch = /^##\$?([^=]+)=/.exec(line);
      const parameterName = parameterMatch?.[1].trim().toUpperCase();
      removeCurrentBlock = parameterName ? privateParameterNames.has(parameterName) : false;

      if (parameterName === 'TITLE') {
        output.push(`##TITLE= ${publicTitle}`);
        removeCurrentBlock = true;
        continue;
      }
    }

    if (!removeCurrentBlock) output.push(line);
  }

  return output.join('\n');
}

async function binarySourceFiles(experiment) {
  const experimentRoot = join(sourceRoot, String(experiment.number));
  const candidates = [
    join(experimentRoot, 'fid'),
    join(experimentRoot, 'ser'),
    ...processedArrays.map((filename) => join(experimentRoot, 'pdata', '1', filename)),
  ];
  const present = [];
  for (const candidate of candidates) {
    if (await isFile(candidate)) present.push(candidate);
  }
  return present;
}

async function scanPublishedText(additionalFiles = []) {
  const textFiles = copiedFiles.filter((file) => !processedArrays.includes(basename(file.path)) && !['fid', 'ser'].includes(basename(file.path)));
  const paths = [...textFiles.map((file) => join(outputRoot, file.path)), ...additionalFiles];
  for (const filePath of paths) {
    const content = await readFile(filePath, 'latin1');
    for (const forbidden of forbiddenText) {
      if (forbidden.pattern.test(content)) {
        throw new Error(`Found ${forbidden.label} in ${relative(outputRoot, filePath)}`);
      }
    }
  }
}

async function createReleaseArchives() {
  const archivePaths = [
    join(outputRoot, 'exercise-001-browser.zip'),
    join(outputRoot, 'exercise-001-archive.zip'),
  ];

  await Promise.all(archivePaths.map((archivePath) => rm(archivePath, { force: true })));
  await setTreeTimestamp(join(outputRoot, 'browser'));
  await setTreeTimestamp(join(outputRoot, 'archive'));
  await executeFile('/usr/bin/zip', ['-X', '-q', '-r', basename(archivePaths[0]), 'browser'], {
    cwd: outputRoot,
  });
  await executeFile('/usr/bin/zip', ['-X', '-q', '-r', basename(archivePaths[1]), 'archive'], {
    cwd: outputRoot,
  });

  return archivePaths;
}

async function setTreeTimestamp(rootPath) {
  const fixedTime = new Date('2000-01-01T00:00:00.000Z');
  const entries = await readdir(rootPath, { withFileTypes: true });
  for (const entry of entries) {
    const entryPath = join(rootPath, entry.name);
    if (entry.isDirectory()) await setTreeTimestamp(entryPath);
    await utimes(entryPath, fixedTime, fixedTime);
  }
  await utimes(rootPath, fixedTime, fixedTime);
}

async function writeChecksums(releaseArchives) {
  const packageLines = copiedFiles
    .filter((file) => file.sha256)
    .sort((left, right) => left.path.localeCompare(right.path))
    .map((file) => `${file.sha256}  ${file.path}`);
  const releaseLines = [];
  for (const archivePath of releaseArchives) {
    releaseLines.push(`${await sha256(archivePath)}  ${basename(archivePath)}`);
  }
  await writeFile(
    join(outputRoot, 'SHA256SUMS'),
    `${[...releaseLines, ...packageLines].join('\n')}\n`,
  );
}

async function recordFile(filePath, packageName) {
  const fileStat = await stat(filePath);
  copiedFiles.push({
    package: packageName,
    path: relative(outputRoot, filePath),
    bytes: fileStat.size,
    sha256: await sha256(filePath),
  });
}

async function sha256(filePath) {
  const content = await readFile(filePath);
  return createHash('sha256').update(content).digest('hex');
}

async function isFile(filePath) {
  try {
    return (await stat(filePath)).isFile();
  } catch (error) {
    if (error.code === 'ENOENT') return false;
    throw error;
  }
}

async function assertDirectory(directoryPath) {
  try {
    if (!(await stat(directoryPath)).isDirectory()) throw new Error();
  } catch {
    throw new Error(`Expected directory: ${directoryPath}`);
  }
}

function assertSeparateTrees(sourcePath, destinationPath) {
  if (containsPath(sourcePath, destinationPath) || containsPath(destinationPath, sourcePath)) {
    throw new Error('Source and output folders must not contain one another.');
  }
}

function containsPath(parent, child) {
  const childRelative = relative(parent, child);
  return childRelative === '' || (!childRelative.startsWith('..') && !isAbsolute(childRelative));
}

function formatBytes(bytes) {
  if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KiB`;
  return `${(bytes / (1024 * 1024)).toFixed(1)} MiB`;
}