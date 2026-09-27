import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const entries = defineCollection({
  loader: glob({ base: './src/content/articles', pattern: '**/*.{md,mdx}' }),
  schema: z.object({
    section: z.enum(['article', 'opinion', 'exercise', 'example']),
    format: z
      .enum([
        'field-note',
        'paper-perspective',
        'opinion',
        'tool-review',
        'research-journey',
        'method-note',
        'reference',
        'guided-exercise',
        'worked-example',
        'reviewed-solution',
      ]),
    paperType: z
      .enum(['chemical-diversity', 'biosynthesis', 'research-methodology', 'review'])
      .optional(),
    title: z.string(),
    summary: z.string(),
    category: z.enum(['field-note', 'structure-elucidation', 'reference']).optional(),
    audience: z.array(z.enum(['junior', 'advanced'])).min(1),
    author: z.object({
      name: z.string(),
      orcid: z.string().regex(/^\d{4}-\d{4}-\d{4}-\d{3}[\dX]$/),
    }),
    publishedAt: z.coerce.date(),
    updatedAt: z.coerce.date().optional(),
    tags: z.array(z.string()).default([]),
    references: z
      .array(
        z.object({
          citation: z.string(),
          url: z.url().optional(),
        }),
      )
      .default([]),
    license: z.literal('CC BY-NC 4.0').default('CC BY-NC 4.0'),
    correctionNote: z.string().optional(),
    exercise: z
      .object({
        number: z.number().int().positive(),
        solutionStatus: z.enum(['withheld', 'in-review', 'published']),
        learningGoals: z.array(z.string()).min(1),
      })
      .optional(),
    spectrum: z
      .object({
        viewerTitle: z.string(),
        viewerDescription: z.string(),
        compound: z
          .object({
            primaryName: z.string(),
            synonym: z.string().optional(),
            formula: z.string(),
            molecularWeight: z.number().positive(),
            pubchemCid: z.number().int().positive(),
            smiles: z.string(),
            inchiKey: z.string(),
          })
          .optional(),
        experiments: z.array(
          z.object({
            number: z.number().int().positive(),
            label: z.string(),
            nuclei: z.string(),
            frequencyMHz: z.string(),
            solvent: z.string(),
            temperatureK: z.number().positive(),
            pulseProgram: z.string(),
            dimensions: z.enum(['1D', '2D']),
            role: z.enum(['primary', 'comparison']),
          }),
        ),
        archiveUrl: z.union([z.url(), z.string().startsWith('/')]).optional(),
        downloadUrl: z.url().optional(),
      })
      .optional(),
    draft: z.boolean().default(true),
  }).superRefine((entry, context) => {
    if (entry.section === 'article' && entry.format !== 'paper-perspective') {
      context.addIssue({
        code: 'custom',
        path: ['format'],
        message: 'Articles must use the paper-perspective format.',
      });
    }

    if (entry.section === 'article' && !entry.paperType) {
      context.addIssue({
        code: 'custom',
        path: ['paperType'],
        message:
          'Articles must declare a paperType: chemical-diversity, biosynthesis, research-methodology, or review.',
      });
    }

    if (entry.section !== 'article' && entry.paperType) {
      context.addIssue({
        code: 'custom',
        path: ['paperType'],
        message: 'Only articles declare a paperType.',
      });
    }

    if (entry.section === 'opinion' && !['opinion', 'tool-review'].includes(entry.format)) {
      context.addIssue({
        code: 'custom',
        path: ['format'],
        message: 'Opinions must use the opinion or tool-review format.',
      });
    }
  }),
});

export const collections = { entries };