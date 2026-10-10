import { getCollection } from 'astro:content';
import { entryLabel, entryPath } from '../lib/content';

const site = 'https://thatnaturalproductchemist.net';

function escapeXml(value: string) {
  return value
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&apos;');
}

export async function GET() {
  const entries = (await getCollection('entries', ({ data }) => !data.draft)).sort(
    (a, b) => b.data.publishedAt.getTime() - a.data.publishedAt.getTime(),
  );

  const items = entries
    .map((entry) => {
      const url = `${site}${entryPath(entry)}`;
      return `  <item>
    <title>${escapeXml(entry.data.title)}</title>
    <link>${url}</link>
    <guid isPermaLink="true">${url}</guid>
    <pubDate>${entry.data.publishedAt.toUTCString()}</pubDate>
    <category>${escapeXml(entryLabel(entry))}</category>
    <description>${escapeXml(entry.data.summary)}</description>
  </item>`;
    })
    .join('\n');

  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
  <title>That Natural Product Chemist</title>
  <link>${site}/</link>
  <description>Evidence, reasoning, and perspective across natural product chemistry.</description>
  <language>en</language>
${items}
</channel>
</rss>
`;

  return new Response(xml, {
    headers: { 'Content-Type': 'application/xml; charset=utf-8' },
  });
}
