import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import LanguageDetector from 'i18next-browser-languagedetector';

// Import translation files
import viTranslations from './locales/vi.json';
import enTranslations from './locales/en.json';

i18n
  .use(LanguageDetector) // Detects user language
  .use(initReactI18next) // Passes i18n down to react-i18next
  .init({
    resources: {
      vi: {
        translation: viTranslations,
      },
      en: {
        translation: enTranslations,
      },
    },
    fallbackLng: 'vi', // Default language
    supportedLngs: ['vi', 'en'], // Supported languages
    interpolation: {
      escapeValue: false, // React already escapes values
    },
    detection: {
      order: ['localStorage', 'navigator'],
      caches: ['localStorage'],
    },
  });

export default i18n;

