import React from 'react';
import { motion } from 'framer-motion';
import ArticleCard from '../../blog/components/ArticleCard';
import { Article } from '../../../types';

interface ConsultingCardsProps {
  articles: Article[];
  onArticleClick: (article: Article) => void;
}

const ConsultingCards: React.FC<ConsultingCardsProps> = ({ articles, onArticleClick }) => {
  return (
    <div className="container mx-auto px-4 py-16">
      <motion.div 
        className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8"
        initial="hidden"
        animate="visible"
        transition={{ staggerChildren: 0.1, delayChildren: 0.2 }}
        variants={{
          hidden: {},
          visible: {}
        }}
      >
        {articles.map((article, index) => (
          <motion.div
            key={article.id}
            variants={{
              hidden: { opacity: 0, y: 50 },
              visible: { opacity: 1, y: 0 }
            }}
            transition={{ duration: 0.6 }}
          >
            <ArticleCard
              article={article}
              onClick={() => onArticleClick(article)}
            />
          </motion.div>
        ))}
      </motion.div>
    </div>
  );
};

export default ConsultingCards;
