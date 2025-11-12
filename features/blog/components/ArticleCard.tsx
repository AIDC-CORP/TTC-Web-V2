
import React from 'react';
import { Link } from 'react-router-dom';
import { motion } from 'framer-motion';
import { Article } from '../../../types';

interface ArticleCardProps {
  article: Article;
  onClick?: () => void;
}

const ArticleCard: React.FC<ArticleCardProps> = ({ article, onClick }) => {
  const content = (
    <motion.div 
      style={{ height: '470px' }}
      className="bg-white rounded-lg shadow-lg overflow-hidden transform hover:-translate-y-2 transition-transform duration-300 group cursor-pointer  flex flex-col"
      whileHover={{ 
        y: -8, 
        transition: { duration: 0.3, ease: "easeOut" }
      }}
      whileTap={{ scale: 0.98 }}
    >
      <div className="relative">
        <motion.img 
          src={article.image} 
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
          {article.category}
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
          {article.publishDate}
        </motion.p>
        <motion.h3 
          className="text-xl font-bold text-gray-800 mb-2 group-hover:text-blue-600 transition-colors"
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
            Đọc thêm &rarr;
          </motion.span>
        </motion.div>
      </motion.div>
    </motion.div>
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
