
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

export interface Article {
  id: string;
  url: string;
  date: string;
  thumbnail: string;
  categories: string[];
  vi: {
    title: string;
    content: string;
  };
  en: {
    title: string;
    content: string;
  };
}

export interface Service {
  id: string;
  name: string;
  image: string;
  summary: string;
}
