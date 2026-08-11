import Cookies from 'js-cookie';
import configuration from '../configuration.json';
import type { ThemeType } from '../types/theme.type';

const defaultTheme = configuration.default.theme;
const cookieName = configuration.cookies.theme;

export function initTheme(): void {
  const theme = getTheme();
  document.body.setAttribute('data-theme', theme);
}

export function setTheme(theme: ThemeType): void {
  document.body.setAttribute('data-theme', theme);
  Cookies.set(cookieName, theme);
}

export function getTheme(): ThemeType {
  const stored = Cookies.get(cookieName) ?? defaultTheme;
  return stored as ThemeType;
}