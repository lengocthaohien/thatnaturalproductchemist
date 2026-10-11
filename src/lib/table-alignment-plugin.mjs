/**
 * Sätteri hast plugin that enforces the site's systematic table design:
 *
 * - header cells (`th`) are centred;
 * - body cells (`td`) whose entire content is a number are centred;
 * - body cells containing text — including text mixed with numbers — are
 *   left-aligned.
 *
 * Markdown column markers (`---:`, `:--:`) only encode per-column alignment
 * (an inline `text-align` style or an `align` attribute on the rendered
 * cells); the plugin removes them so the class-based rules in
 * `src/styles/global.css` decide the alignment of every table the same way.
 * Classification happens at build time, so authors write plain Markdown
 * tables and the convention applies automatically.
 *
 * Registered in `astro.config.mjs` via
 * `markdown.processor: satteri({ hastPlugins: [tableAlignmentPlugin] })`.
 */

// A "number" cell contains nothing but an optionally signed decimal number.
// Anything else — units, symbols, words, or numbers mixed with text — is
// treated as text and left-aligned.
const NUMBER_PATTERN = /^[+-]?(?:\d+(?:\.\d+)?|\.\d+)$/;

export const tableAlignmentPlugin = {
  name: 'tnpc-table-alignment',
  element: {
    filter: ['th', 'td'],
    visit(node, ctx) {
      const properties = node.properties ?? {};

      if (typeof properties.style === 'string' && properties.style.includes('text-align')) {
        const kept = properties.style
          .split(';')
          .map((declaration) => declaration.trim())
          .filter((declaration) => declaration && !declaration.startsWith('text-align'));
        ctx.setProperty(node, 'style', kept.length > 0 ? kept.join('; ') : null);
      }
      if ('align' in properties) ctx.setProperty(node, 'align', null);

      if (node.tagName === 'td') {
        const existing = properties.className;
        const classes = Array.isArray(existing)
          ? [...existing]
          : typeof existing === 'string'
            ? [existing]
            : [];
        classes.push(NUMBER_PATTERN.test(ctx.textContent(node).trim()) ? 'cell-number' : 'cell-text');
        ctx.setProperty(node, 'className', classes);
      }
    },
  },
};
