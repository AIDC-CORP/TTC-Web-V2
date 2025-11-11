import React from 'react';
import ArticleCard from './ArticleCard';
import { Article } from '../../../types';

interface BlogCardsProps {
  articles: Article[];
  currentPage: number;
  totalPages: number;
  onPageChange: (pageNumber: number) => void;
  onArticleClick?: (article: Article) => void;
}

const BlogCards: React.FC<BlogCardsProps> = ({
  articles,
  currentPage,
  totalPages,
  onPageChange,
  onArticleClick
}) => {
  return (
    <div className="container mx-auto px-4 py-16">
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {articles.map(article => (
          <ArticleCard
            key={article.id}
            article={article}
            onClick={onArticleClick ? () => onArticleClick(article) : undefined}
          />
        ))}
      </div>

      {totalPages > 1 && (
        <div className="flex justify-center mt-12 space-x-2">
          {Array.from({ length: totalPages }, (_, i) => i + 1).map(number => (
            <button
              key={number}
              onClick={() => onPageChange(number)}
              className={`px-4 py-2 rounded-md font-semibold ${currentPage === number ? 'bg-blue-600 text-white' : 'bg-gray-200 text-gray-700 hover:bg-blue-200'}`}
            >
              {number}
            </button>
          ))}
        </div>
      )}
    </div>
  );
};

export default BlogCards;