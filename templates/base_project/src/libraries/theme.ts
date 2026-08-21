import configuration from '../configuration.json';
import type { ThemeType } from '../enums/theme.type.ts';

const defaultTheme = configuration.default.theme;
const storageKey = configuration.localstorage.theme;

export function initTheme(): void {
  const theme = getTheme();
  document.body.setAttribute('data-theme', theme);
}

export function setTheme(theme: ThemeType): void {
  document.body.setAttribute('data-theme', theme);
  localStorage.setItem(storageKey, theme);
}

export function getTheme(): ThemeType {
  const stored = localStorage.getItem(storageKey) ?? defaultTheme;
  return stored as ThemeType;
}