export const Language = {
  {{language_name}}: '{{language_short}}'
} as const;

export type LanguageType = typeof Language[keyof typeof Language];