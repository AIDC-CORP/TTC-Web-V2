import React from 'react';
import { useParams, Link } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import articlesData from './data/blog.json';
import { Article } from '../../types';
import { getCurrentLangKey } from '../../common/utils/i18nUtils';

// Cast the imported JSON to the correct type
const articles = articlesData as Article[];

// Helper function to parse content with embedded images and markdown
const parseContent = (content: string) => {
  if (!content) return [];
  const imageRegex = /\[IMAGE:(.*?)\]/g;
  const parts: Array<{ type: 'text' | 'image'; content: string }> = [];
  let lastIndex = 0;
  let match;

  while ((match = imageRegex.exec(content)) !== null) {
    if (match.index > lastIndex) {
      parts.push({ type: 'text', content: content.substring(lastIndex, match.index) });
    }
    parts.push({ type: 'image', content: match[1] });
    lastIndex = match.index + match[0].length;
  }

  if (lastIndex < content.length) {
    parts.push({ type: 'text', content: content.substring(lastIndex) });
  }

  const getImageClassName = (layout: string) => {
    switch (layout) {
      case 'left':
        return 'w-full md:w-1/2 md:float-left md:mr-6 my-4 h-auto object-cover rounded-lg shadow-lg';
      case 'right':
        return 'w-full md:w-1/2 md:float-right md:ml-6 my-4 h-auto object-cover rounded-lg shadow-lg';
      case 'center':
        return 'w-full md:max-w-2xl mx-auto my-6 block h-auto object-cover rounded-lg shadow-lg';
      case 'full':
      default:
        return 'w-full h-auto object-cover rounded-lg shadow-lg my-6';
    }
  };

  return parts.map((part, index) => {
    if (part.type === 'text') {
      return (
        <div key={index}>
          {part.content.split('\n').map((line, lineIndex) => {
            if (line.startsWith('## ')) {
              return <h2 key={lineIndex} className="text-2xl font-bold text-gray-800 mt-6 mb-3 clear-both">{line.replace(/^## /, '')}</h2>;
            } else if (line.trim()) {
              return <p key={lineIndex} className="text-gray-600 leading-relaxed mb-4">{line}</p>;
            }
            return null;
          })}
        </div>
      );
    } else {
      const [filename, layout = 'full'] = part.content.split(':');
      return <img key={index} src={`/blog-assets/${filename}`} alt={`Article content image ${index}`} className={getImageClassName(layout)} />;
    }
  });
};

const ArticleDetailPage: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const { t, i18n } = useTranslation();
  const article = articles.find(a => a.id === id);

  const currentLang = getCurrentLangKey(i18n.language);

  if (!article) {
    return (
      <div className="container mx-auto px-4 py-20 text-center">
        <h1 className="text-3xl font-bold">{t('article.notFound')}</h1>
        <p className="mt-4">{t('article.notFoundText')}</p>
        <Link to="/blog" className="mt-8 inline-block bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition">
          {t('article.backToBlog')}
        </Link>
      </div>
    );
  }

  const localizedContent = article[currentLang] || article.vi;

  return (
    <div className="bg-white py-16">
      <div className="container mx-auto px-4 max-w-4xl">
        <Link to="/blog" className="text-blue-600 hover:underline mb-8 inline-block">
          &larr; {t('article.backToBlog')}
        </Link>
        <span className="text-sm text-gray-500">{article.categories.join(' | ')} | {article.date}</span>
        <h1 className="text-3xl md:text-4xl font-extrabold text-gray-800 mt-2 mb-6">{localizedContent.title}</h1>
        <img src={article.thumbnail} alt={localizedContent.title} className="w-full h-auto object-cover rounded-lg shadow-lg mb-8" />
        <div className="prose max-w-none text-gray-700 leading-relaxed">
          {parseContent(localizedContent.content)}
        </div>
      </div>
    </div>
  );
};

export default ArticleDetailPage;