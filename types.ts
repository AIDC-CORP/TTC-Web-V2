
export interface Project {
  id: string;
  name: string;
  image: string;
  summary: string;
  description: string;
  investor?: string;
  executionTime?: string;
  gallery: string[];
  category: string;
  location_specific: string;
  region: string;
  regionKey?: string;
  square: string;
  project_manager: string;
  year: string;
}

export type LangKey = 'vi' | 'en' | 'ko' | 'zh';

export interface LocalizedContent {
  title: string;
  content: string;
}

export interface GalleryImage {
  src: string;
  caption?: Partial<Record<LangKey, string>>;
}

export interface Article {
  id: string;
  url: string;
  date: string;
  thumbnail: string;
  categories: string[];
  vi: LocalizedContent;
  en: LocalizedContent;
  ko?: LocalizedContent;
  zh?: LocalizedContent;
  leadImage?: GalleryImage;
  gallery?: GalleryImage[];
  title?: string;
  content?: string;
  excerpt?: string;
  publishDate?: string;
  category?: string;
}

export interface Service {
  id: string;
  name: string;
  image: string;
  summary: string;
}
