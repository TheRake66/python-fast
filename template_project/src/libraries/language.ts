import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import LanguageDetector from 'i18next-browser-languagedetector';
import Cookies from 'js-cookie';
import configuration from '../configuration.json';
import type { LanguageType } from '../types/language.type';

import fr from '../locales/fr.json';

const defaultLang = configuration.default.language;
const cookieName = configuration.cookies.language;

export function initLanguage(): void {
  const language = getLanguage();
  i18n
    .use(LanguageDetector)
    .use(initReactI18next)
    .init({
      fallbackLng: defaultLang,
      lng: language,
      interpolation: { escapeValue: false },
      resources: {
        fr: { translation: fr }
      },
    });
}

export function setLanguage(language: LanguageType): void {
  i18n.changeLanguage(language);
  Cookies.set(cookieName, language);
}

export function getLanguage(): LanguageType {
  const stored = Cookies.get(cookieName) ?? defaultLang;
  return stored as LanguageType;
}