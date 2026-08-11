export const Language = {
  French: 'fr'
} as const;

export type LanguageType = typeof Language[keyof typeof Language];