
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
}

export interface Article {
  id: string;
  title: string;
  image: string;
  excerpt: string;
  content: string;
  publishDate: string;
  category: 'Blog' | 'Tư vấn';
}

export interface Service {
  id: string;
  name: string;
  image: string;
  summary: string;
}
