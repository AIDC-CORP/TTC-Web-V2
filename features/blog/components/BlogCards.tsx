import React from 'react';
import { motion } from 'framer-motion';
import ArticleCard from './ArticleCard';
import { Article } from '../../../types';

interface BlogCardsProps {
  articles: Article[];
  currentPage?: number;
  totalPages?: number;
  onPageChange?: (pageNumber: number) => void;
  onArticleClick?: (article: Article) => void;
}

const BlogCards: React.FC<BlogCardsProps> = ({
  articles,
  currentPage = 1,
  totalPages = 1,
  onPageChange,
  onArticleClick
}) => {
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
              onClick={onArticleClick ? () => onArticleClick(article) : undefined}
            />
          </motion.div>
        ))}
      </motion.div>

      {totalPages > 1 && onPageChange && (
        <motion.div 
          className="flex justify-center mt-12 space-x-2"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6, delay: 0.4 }}
        >
          {Array.from({ length: totalPages }, (_, i) => i + 1).map(number => (
            <motion.button
              key={number}
              onClick={() => onPageChange(number)}
              className={`px-4 py-2 rounded-md font-semibold ${currentPage === number ? 'bg-blue-600 text-white' : 'bg-gray-200 text-gray-700 hover:bg-blue-200'}`}
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              transition={{ duration: 0.2 }}
            >
              {number}
            </motion.button>
          ))}
        </motion.div>
      )}
    </div>
  );
};

export default BlogCards;