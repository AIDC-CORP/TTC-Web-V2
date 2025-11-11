import React from 'react';
import { Link } from 'react-router-dom';
import { Article } from '../../../types';

interface ArticleDetailDialogProps {
  article: Article | null;
  isOpen: boolean;
  onClose: () => void;
}

const ArticleDetailDialog: React.FC<ArticleDetailDialogProps> = ({ article, isOpen, onClose }) => {
  if (!isOpen || !article) return null;

  const backLink = article.category === 'Blog' ? '/blog' : '/tu-van';
  const backLinkText = article.category === 'Blog' ? 'Xem tất cả bài viết' : 'Xem tất cả tư vấn';

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50">
      <div className="bg-white rounded-lg shadow-xl max-w-4xl w-full mx-4 max-h-[90vh] overflow-y-auto">
        <div className="p-6">
          {/* Header */}
          <div className="flex justify-between items-center mb-6">
            <div>
              <span className="text-sm text-gray-500">{article.category} | {article.publishDate}</span>
              <h2 className="text-2xl md:text-3xl font-bold text-gray-800 mt-1">{article.title}</h2>
            </div>
            <button
              onClick={onClose}
              className="text-gray-500 hover:text-gray-700 text-2xl font-bold"
            >
              ×
            </button>
          </div>

          {/* Content */}
          <div className="mb-6">
            <img
              src={article.image}
              alt={article.title}
              className="w-full h-auto object-cover rounded-lg shadow-lg mb-6"
            />
            <div className="prose max-w-none">
              <p className="text-gray-600 leading-relaxed whitespace-pre-line">
                {article.content}
              </p>
            </div>
          </div>

          {/* Footer */}
          <div className="mt-8 pt-6 border-t border-gray-200 flex justify-between">
            <Link
              to={backLink}
              className="text-blue-600 hover:underline"
              onClick={onClose}
            >
              {backLinkText}
            </Link>
            <button
              onClick={onClose}
              className="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition"
            >
              Đóng
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ArticleDetailDialog;
