
import React from 'react';
import { Link } from 'react-router-dom';
import { Article } from '../../../types';

interface ArticleCardProps {
  article: Article;
  onClick?: () => void;
}

const ArticleCard: React.FC<ArticleCardProps> = ({ article, onClick }) => {
  const content = (
    <div className="bg-white rounded-lg shadow-lg overflow-hidden transform hover:-translate-y-2 transition-transform duration-300 group cursor-pointer h-full flex flex-col">
      <div className="relative">
        <img src={article.image} alt={article.title} className="w-full h-56 object-cover" />
        <div className="absolute inset-0 bg-black bg-opacity-20 group-hover:bg-opacity-40 transition-opacity duration-300"></div>
        <div className="absolute bottom-0 left-0 bg-blue-600 text-white px-3 py-1 text-sm font-semibold rounded-tr-lg">
          {article.category}
        </div>
      </div>
      <div className="p-6 flex-1 flex flex-col">
        <p className="text-sm text-gray-500 mb-2">{article.publishDate}</p>
        <h3 className="text-xl font-bold text-gray-800 mb-2 group-hover:text-blue-600 transition-colors">{article.title}</h3>
        <p className="text-gray-600 text-sm line-clamp-3 flex-1">{article.excerpt}</p>
        <div className="mt-auto">
          <span className="font-semibold text-blue-600 hover:underline">
            Đọc thêm &rarr;
          </span>
        </div>
      </div>
    </div>
  );

  if (onClick) {
    return (
      <div onClick={onClick} className="cursor-pointer">
        {content}
      </div>
    );
  }

  return (
    <Link to={`/blog/${article.id}`} className="flex flex-col flex-grow">
      {content}
    </Link>
  );
};

export default ArticleCard;
