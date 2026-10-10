#!/usr/bin/env node
/*
 * Creates one GitHub Release per published entry so that repository watchers
 * (Watch → Custom → Releases) receive an email notification for each new
 * post. Idempotent: an entry is announced only once, keyed by the release tag
 * `post-<entry-id>`. Runs in the post-releases workflow; requires the `gh`
 * CLI with GH_TOKEN set (preinstalled on GitHub-hosted runners).
 *
 * First run creates releases for all currently published entries; delete any
 * unwanted ones once (or pre-create their tags) to avoid backfill noise.
 */
import { execFileSync } from 'node:child_process';
import { readdirSync, readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { join } from 'node:path';

const site = 'https://thatnaturalproductchemist.net';
const contentDir = fileURLToPath(new URL('../src/content/articles/', import.meta.url));
const sectionPaths = {
  article: 'articles',
  opinion: 'opinions',
  exercise: 'exercises',
  example: 'examples',
};

function parseFrontmatter(source) {
  const match = source.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!match) return null;
  const field = (name) => {
    const line = match[1].match(new RegExp(`^${name}:\\s*(.+)$`, 'm'));
    return line ? line[1].trim().replace(/^["']|["']$/g, '') : null;
  };
  return {
    title: field('title'),
    summary: field('summary'),
    section: field('section'),
    draft: field('draft'),
  };
}

const entries = readdirSync(contentDir)
  .filter((file) => file.endsWith('.md'))
  .map((file) => ({
    id: file.replace(/\.md$/, ''),
    ...parseFrontmatter(readFileSync(join(contentDir, file), 'utf8')),
  }))
  // The content schema defaults draft to true, so only an explicit
  // `draft: false` marks an entry as published and announceable.
  .filter((entry) => entry.title && entry.draft === 'false' && sectionPaths[entry.section]);

const dryRun = process.argv.includes('--dry-run');

const existingTags = JSON.parse(
  execFileSync('gh', ['release', 'list', '--limit', '1000', '--json', 'tagName'], {
    encoding: 'utf8',
  }),
).map((release) => release.tagName);

let created = 0;
for (const entry of entries) {
  const tag = `post-${entry.id}`;
  if (existingTags.includes(tag)) continue;

  const url = `${site}/${sectionPaths[entry.section]}/${entry.id}/`;
  const notes = [
    `**New publication:** [${entry.title}](${url})`,
    '',
    entry.summary ?? '',
    '',
    '---',
    'You received this email because you watch releases for this repository. To unsubscribe, choose **Unwatch** on the repository page.',
  ].join('\n');

  if (dryRun) {
    console.log(`[dry-run] Would announce ${tag} -> ${url}`);
  } else {
    execFileSync(
      'gh',
      ['release', 'create', tag, '--title', entry.title, '--notes', notes, '--latest=false'],
      { stdio: 'inherit' },
    );
    console.log(`Announced ${tag} -> ${url}`);
  }
  created += 1;
}

const verb = dryRun ? 'Would announce' : 'Announced';
console.log(created === 0 ? 'No new publications to announce.' : `${verb} ${created} publication(s).`);
