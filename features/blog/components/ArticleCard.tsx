
import React from 'react';
import { Link } from 'react-router-dom';
import { Article } from '../../../types';

interface ArticleCardProps {
  article: Article;
}

const ArticleCard: React.FC<ArticleCardProps> = ({ article }) => {
  return (
    <div className="bg-white rounded-lg shadow-lg overflow-hidden flex flex-col transform hover:-translate-y-2 transition-transform duration-300 group">
      <Link to={`/blog/${article.id}`} className="flex flex-col flex-grow">
        <div className="relative">
            <img src={article.image} alt={article.title} className="w-full h-48 object-cover" />
        </div>
        <div className="p-6 flex flex-col flex-grow">
          <p className="text-sm text-gray-500 mb-2">{article.publishDate}</p>
          <h3 className="text-lg font-bold text-gray-800 mb-2 flex-grow group-hover:text-blue-600 transition-colors">{article.title}</h3>
          <p className="text-gray-600 text-sm line-clamp-3 mb-4">{article.excerpt}</p>
          <div className="mt-auto">
            <span className="font-semibold text-blue-600 hover:underline">
              Đọc thêm &rarr;
            </span>
          </div>
        </div>
      </Link>
    </div>
  );
};

export default ArticleCard;
