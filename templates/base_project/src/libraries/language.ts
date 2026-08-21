import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import LanguageDetector from 'i18next-browser-languagedetector';
import configuration from '../configuration.json';
import type { LanguageType } from '../enums/language.type.ts';

import {{language_short}} from '../locales/{{language_short}}.json';

const defaultLang = configuration.default.language;
const storageKey = configuration.localstorage.language;

export function initLanguage(): void {
  const language = getLanguage();
  i18n
    .use(LanguageDetector)
    .use(initReactI18next)
    .init({
      lng: language,
      fallbackLng: defaultLang,
      interpolation: { escapeValue: false },
      resources: {
        {{language_short}}: { translation: {{language_short}} }
      }});
}

export function setLanguage(language: LanguageType): void {
  i18n.changeLanguage(language);
  localStorage.setItem(storageKey, language);
}

export function getLanguage(): LanguageType {
  const stored = localStorage.getItem(storageKey) ?? defaultLang;
  return stored as LanguageType;
}