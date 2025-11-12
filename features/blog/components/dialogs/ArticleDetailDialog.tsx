import React from 'react';
import { Link } from 'react-router-dom';
import { motion, AnimatePresence } from 'framer-motion';
import { Article } from '../../../../types';

interface ArticleDetailDialogProps {
  article: Article | null;
  isOpen: boolean;
  onClose: () => void;
}

// Helper function to parse content with embedded images
const parseContentWithImages = (content: string, articleId: string) => {
  const imageRegex = /\[IMAGE:(.*?)\]/g;
  const parts: Array<{ type: 'text' | 'image'; content: string }> = [];
  let lastIndex = 0;
  let match;

  while ((match = imageRegex.exec(content)) !== null) {
    // Add text before image
    if (match.index > lastIndex) {
      parts.push({
        type: 'text',
        content: content.substring(lastIndex, match.index)
      });
    }
    
    // Add image
    parts.push({
      type: 'image',
      content: match[1] // Image filename
    });
    
    lastIndex = match.index + match[0].length;
  }
  
  // Add remaining text
  if (lastIndex < content.length) {
    parts.push({
      type: 'text',
      content: content.substring(lastIndex)
    });
  }
  
  return parts;
};

const ArticleDetailDialog: React.FC<ArticleDetailDialogProps> = ({ article, isOpen, onClose }) => {
  const backLink = article?.category === 'Blog' ? '/blog' : '/tu-van';
  const backLinkText = article?.category === 'Blog' ? 'Xem tất cả bài viết' : 'Xem tất cả tư vấn';

  return (
    <AnimatePresence>
      {isOpen && article && (
        <motion.div 
          className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          transition={{ duration: 0.3 }}
          onClick={onClose}
        >
          <motion.div 
            className="bg-white rounded-lg shadow-xl max-w-4xl w-full mx-4 max-h-[90vh] overflow-y-auto"
            initial={{ opacity: 0, scale: 0.8, y: 50 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.8, y: 50 }}
            transition={{ duration: 0.4, ease: "easeOut" }}
            onClick={(e) => e.stopPropagation()}
          >
            <div className="p-6">
              {/* Header */}
              <motion.div 
                className="flex justify-between items-center mb-6"
                initial={{ opacity: 0, y: -20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5, delay: 0.2 }}
              >
                <div>
                  <motion.span 
                    className="text-sm text-gray-500"
                    initial={{ opacity: 0, x: -20 }}
                    animate={{ opacity: 1, x: 0 }}
                    transition={{ duration: 0.4, delay: 0.3 }}
                  >
                    {article.category} | {article.publishDate}
                  </motion.span>
                  <motion.h2 
                    className="text-2xl md:text-3xl font-bold text-gray-800 mt-1"
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.5, delay: 0.4 }}
                  >
                    {article.title}
                  </motion.h2>
                </div>
                <motion.button
                  onClick={onClose}
                  className="text-gray-500 hover:text-gray-700 text-2xl font-bold"
                  whileHover={{ scale: 1.1, rotate: 90 }}
                  whileTap={{ scale: 0.9 }}
                  transition={{ duration: 0.2 }}
                >
                  ×
                </motion.button>
              </motion.div>

              {/* Content */}
              <motion.div 
                className="mb-6"
                initial={{ opacity: 0, y: 30 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.6, delay: 0.5 }}
              >
                <motion.img
                  src={article.image}
                  alt={article.title}
                  className="w-full h-auto object-cover rounded-lg shadow-lg mb-6"
                  initial={{ opacity: 0, scale: 0.9 }}
                  animate={{ opacity: 1, scale: 1 }}
                  transition={{ duration: 0.6, delay: 0.6 }}
                />
                <motion.div 
                  className="prose max-w-none"
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.6, delay: 0.7 }}
                >
                  {parseContentWithImages(article.content, article.id).map((part, index) => {
                    if (part.type === 'text') {
                      // Split text by markdown headings
                      const lines = part.content.split('\n');
                      return (
                        <div key={index}>
                          {lines.map((line, lineIndex) => {
                            if (line.startsWith('## ')) {
                              return (
                                <h2 key={lineIndex} className="text-2xl font-bold text-gray-800 mt-6 mb-3">
                                  {line.replace(/^## /, '')}
                                </h2>
                              );
                            } else if (line.startsWith('# ')) {
                              return (
                                <h1 key={lineIndex} className="text-3xl font-bold text-gray-800 mt-6 mb-3">
                                  {line.replace(/^# /, '')}
                                </h1>
                              );
                            } else if (line.startsWith('- ')) {
                              return (
                                <li key={lineIndex} className="text-gray-600 leading-relaxed ml-5 mb-2 list-disc">
                                  {line.replace(/^- /, '')}
                                </li>
                              );
                            } else if (line.trim()) {
                              return (
                                <p key={lineIndex} className="text-gray-600 leading-relaxed mb-4">
                                  {line}
                                </p>
                              );
                            }
                            return null;
                          })}
                        </div>
                      );
                    } else {
                      return (
                        <img
                          key={index}
                          src={`/blog-assets/${part.content}`}
                          alt={`Article image ${index}`}
                          className="w-full h-auto object-cover rounded-lg shadow-lg my-6"
                        />
                      );
                    }
                  })}
                </motion.div>
              </motion.div>

              {/* Footer */}
              <motion.div 
                className="mt-8 pt-6 border-t border-gray-200 flex justify-between"
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5, delay: 0.8 }}
              >
                <Link
                  to={backLink}
                  className="text-blue-600 hover:underline"
                  onClick={onClose}
                >
                  {backLinkText}
                </Link>
                <motion.button
                  onClick={onClose}
                  className="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition"
                  whileHover={{ scale: 1.05 }}
                  whileTap={{ scale: 0.95 }}
                >
                  Đóng
                </motion.button>
              </motion.div>
            </div>
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
};

export default ArticleDetailDialog;
