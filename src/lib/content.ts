import type { CollectionEntry } from 'astro:content';

export const sectionPaths = {
  article: 'articles',
  opinion: 'opinions',
  exercise: 'exercises',
  example: 'examples',
} as const;

export function entryPath(entry: CollectionEntry<'entries'>) {
  return `/${sectionPaths[entry.data.section]}/${entry.id}/`;
}

export function entryLabel(entry: CollectionEntry<'entries'>) {
  const label =
    entry.data.section === 'article' && entry.data.paperType
      ? entry.data.paperType
      : entry.data.format;
  return label.replaceAll('-', ' ');
}