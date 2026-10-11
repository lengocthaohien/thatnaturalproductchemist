import { defineConfig } from 'astro/config';
import react from '@astrojs/react';
import { satteri } from '@astrojs/markdown-satteri';
import { tableAlignmentPlugin } from './src/lib/table-alignment-plugin.mjs';

export default defineConfig({
  integrations: [react()],
  markdown: {
    processor: satteri({ hastPlugins: [tableAlignmentPlugin] }),
  },
  output: 'static',
  site: 'https://thatnaturalproductchemist.net',
});