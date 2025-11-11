import React from 'react';
import ArticleCard from '../../blog/components/ArticleCard';
import { Article } from '../../../types';

interface ConsultingCardsProps {
  articles: Article[];
  onArticleClick: (article: Article) => void;
}

const ConsultingCards: React.FC<ConsultingCardsProps> = ({ articles, onArticleClick }) => {
  return (
    <div className="container mx-auto px-4 py-16">
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {articles.map(article => (
          <ArticleCard
            key={article.id}
            article={article}
            onClick={() => onArticleClick(article)}
          />
        ))}
      </div>
    </div>
  );
};

export default ConsultingCards;
