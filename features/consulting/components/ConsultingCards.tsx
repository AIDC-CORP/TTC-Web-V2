import React from 'react';
import { motion } from 'framer-motion';
import { useTranslation } from 'react-i18next';
import { Article } from '../../../types';

interface ConsultingCardsProps {
  articles: Article[];
  onArticleClick?: (article: Article) => void;
}

const ConsultingCards: React.FC<ConsultingCardsProps> = ({ articles, onArticleClick }) => {
  const { t } = useTranslation();

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
        {articles.map((article, index) => {
          const cardContent = (
            <motion.div 
              style={{ height: '470px' }}
              className="bg-white rounded-lg shadow-lg overflow-hidden transform hover:-translate-y-2 transition-transform duration-300 group cursor-pointer flex flex-col"
              whileHover={{ 
                y: -8, 
                transition: { duration: 0.3, ease: "easeOut" }
              }}
              whileTap={{ scale: 0.98 }}
            >
              <div className="relative">
                <motion.img 
                  src={article.thumbnail} 
                  alt={article.title} 
                  className="w-full h-56 object-cover" 
                  whileHover={{ scale: 1.05 }}
                  transition={{ duration: 0.3 }}
                />
                <motion.div 
                  className="absolute inset-0 bg-black bg-opacity-20 group-hover:bg-opacity-40 transition-opacity duration-300"
                  whileHover={{ opacity: 0.6 }}
                ></motion.div>
                <motion.div 
                  className="absolute bottom-0 left-0 bg-blue-600 text-white px-3 py-1 text-sm font-semibold rounded-tr-lg"
                  initial={{ x: -100 }}
                  animate={{ x: 0 }}
                  transition={{ duration: 0.5, delay: 0.2 }}
                >
                  {article.categories.includes('Tư vấn') ? t('blog.category.consulting') : t('blog.category.blog')}
                </motion.div>
              </div>
              <motion.div 
                className="p-6 flex-1 flex flex-col"
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5, delay: 0.3 }}
              >
                <motion.p 
                  className="text-sm text-gray-500 mb-2"
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  transition={{ duration: 0.5, delay: 0.4 }}
                >
                  {article.date}
                </motion.p>
                <motion.h3 
                  className="text-xl font-bold text-gray-800 mb-2 group-hover:text-blue-600 transition-colors line-clamp-2"
                  whileHover={{ scale: 1.02 }}
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.5, delay: 0.5 }}
                >
                  {article.title}
                </motion.h3>
                <motion.p 
                  className="text-gray-600 text-sm line-clamp-3"
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  transition={{ duration: 0.5, delay: 0.6 }}
                >
                  {article.excerpt}
                </motion.p>
                <motion.div 
                  className="mt-auto"
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.5, delay: 0.7 }}
                >
                  <motion.span 
                    className="font-semibold text-blue-600 hover:underline"
                    whileHover={{ x: 5 }}
                    transition={{ duration: 0.2 }}
                  >
                    {t('blog.readMore')} &rarr;
                  </motion.span>
                </motion.div>
              </motion.div>
            </motion.div>
          );

          return (
            <motion.div
              key={article.id}
              variants={{
                hidden: { opacity: 0, y: 50 },
                visible: { opacity: 1, y: 0 }
              }}
              transition={{ duration: 0.6 }}
              onClick={() => onArticleClick?.(article)}
              className="cursor-pointer"
            >
              {cardContent}
            </motion.div>
          );
        })}
      </motion.div>
    </div>
  );
};

export default ConsultingCards;