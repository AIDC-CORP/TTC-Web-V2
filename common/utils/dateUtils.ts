const VI_MONTHS: Record<string, string> = {
  'tháng 1': '01', 'tháng 2': '02', 'tháng 3': '03', 'tháng 4': '04',
  'tháng 5': '05', 'tháng 6': '06', 'tháng 7': '07', 'tháng 8': '08',
  'tháng 9': '09', 'tháng 10': '10', 'tháng 11': '11', 'tháng 12': '12',
};

/**
 * Convert a Vietnamese display date ("5 Tháng 6, 2026") to ISO "2026-06-05"
 * for use in <time datetime> and JSON-LD. Returns undefined if unparseable.
 */
export const viDateToISO = (display: string): string | undefined => {
  if (!display) return undefined;
  const normalized = display.toLowerCase().trim();
  const match = normalized.match(/^(\d{1,2})\s+(tháng\s+\d{1,2})\s*,\s*(\d{4})$/);
  if (!match) return undefined;
  const [, day, monthLabel, year] = match;
  const month = VI_MONTHS[monthLabel.replace(/\s+/g, ' ')];
  if (!month) return undefined;
  return `${year}-${month}-${day.padStart(2, '0')}`;
};
