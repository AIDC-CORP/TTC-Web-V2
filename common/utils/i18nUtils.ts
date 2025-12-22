/**
 * Get the current language key for data localization
 * Falls back to Vietnamese if language is not supported
 */
export const getCurrentLangKey = (i18nLanguage: string): 'vi' | 'en' | 'ko' | 'zh' => {
    if (i18nLanguage.startsWith('ko')) return 'ko';
    if (i18nLanguage.startsWith('en')) return 'en';
    if (i18nLanguage.startsWith('zh')) return 'zh';
    return 'vi'; // Default fallback
};

/**
 * Get localized data with fallback chain: requested lang -> vi -> first available
 */
export const getLocalizedData = <T extends Record<string, any>>(
    data: T,
    langKey: 'vi' | 'en' | 'ko' | 'zh'
): any => {
    // Try requested language
    if (data[langKey]) return data[langKey];

    // Fallback to Vietnamese
    if (data.vi) return data.vi;

    // Fallback to English
    if (data.en) return data.en;

    // Fallback to Korean
    if (data.ko) return data.ko;

    // Last resort: return first available value
    const firstKey = Object.keys(data)[0];
    return data[firstKey];
};
