import { getCollection } from 'astro:content';
import { entryLabel, entryPath } from '../lib/content';

/* Reduce Markdown to plain text so the client-side search can match against
   the full body without tripping over formatting syntax. */
function toPlainText(markdown: string): string {
  return markdown
    .replace(/```[\s\S]*?```/g, ' ')
    .replace(/!\[[^\]]*\]\([^)]*\)/g, ' ')
    .replace(/\[([^\]]*)\]\([^)]*\)/g, '$1')
    .replace(/<[^>]+>/g, ' ')
    .replace(/^[#>\-\s]+/gm, ' ')
    .replace(/[*_`]/g, '')
    .replace(/\s+/g, ' ')
    .trim();
}

export async function GET() {
  const entries = await getCollection('entries', ({ data }) => !data.draft);
  const index = entries
    .sort((left, right) => right.data.publishedAt.valueOf() - left.data.publishedAt.valueOf())
    .map((entry) => ({
      title: entry.data.title,
      summary: entry.data.summary,
      label: entryLabel(entry),
      path: entryPath(entry),
      tags: entry.data.tags,
      year: String(entry.data.publishedAt.getFullYear()),
      body: toPlainText(entry.body ?? ''),
    }));

  return new Response(JSON.stringify(index), {
    headers: { 'Content-Type': 'application/json; charset=utf-8' },
  });
}
