import React, { createContext, useContext, useState, useCallback } from 'react';
import { Language, Translations } from '../types/language';

// Contexto de i18n
interface I18nContextType {
  language: Language;
  setLanguage: (lang: Language) => void;
  t: (key: string) => string;
}

const I18nContext = createContext<I18nContextType | undefined>(undefined);

// Props del provider
interface I18nProviderProps {
  children: React.ReactNode;
  defaultLanguage?: Language;
  translations: Record<Language, Translations>;
}

// Provider de i18n
export const I18nProvider: React.FC<I18nProviderProps> = ({
  children,
  defaultLanguage = 'es',
  translations
}) => {
  const [language, setLanguage] = useState<Language>(defaultLanguage);

  // Función para traducir
  const t = useCallback((key: string): string => {
    const keys = key.split('.');
    let value: any = translations[language];

    for (const k of keys) {
      if (value && typeof value === 'object' && k in value) {
        value = value[k];
      } else {
        console.warn(`Translation key not found: ${key}`);
        return key;
      }
    }

    return typeof value === 'string' ? value : key;
  }, [language, translations]);

  return (
    <I18nContext.Provider value={{ language, setLanguage, t }}>
      {children}
    </I18nContext.Provider>
  );
};

// Hook personalizado para usar las traducciones
export const useI18n = () => {
  const context = useContext(I18nContext);
  if (context === undefined) {
    throw new Error('useI18n debe ser usado dentro de un I18nProvider');
  }
  return context;
}; 