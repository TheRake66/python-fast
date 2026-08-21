import configuration from '../configuration.json';

const defaultLang = configuration.default.language;

export function formatNumber(amount: number, lang: string | null = null): string {
  return new Intl.NumberFormat(lang ?? defaultLang).format(amount);
}