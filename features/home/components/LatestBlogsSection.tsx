import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import blogData from '../../blog/data/blog.json';
import BlogCards from '../../blog/components/BlogCards';
import ArticleDetailDialog from '../../blog/components/dialogs/ArticleDetailDialog';
import { motion } from 'framer-motion';
import { useTranslation } from 'react-i18next';
import { Article } from '../../../types';

const LatestBlogsSection: React.FC = () => {
  const { t } = useTranslation();
  const [selectedArticle, setSelectedArticle] = useState<Article | null>(null);
  const [isDialogOpen, setIsDialogOpen] = useState(false);

  const latestArticles = blogData
    .filter(article => article.title) // Lọc ra các bài viết không có tiêu đề
    .slice(0, 3)
    .map(article => ({
    id: article.title.toLowerCase().replace(/\s+/g, '-').replace(/[^a-z0-9-]/g, ''),
    title: article.title,
    image: article.thumbnail || 'https://picsum.photos/400/300?random=2',
    excerpt: article.content.length > 150 ? article.content.substring(0, 150) + '...' : article.content,
    content: article.content,
    publishDate: article.date,
    category: article.categories.includes('Tư vấn') ? t('blog.category.consulting') as const : t('blog.category.blog') as const
  }));

  const handleArticleClick = (article: Article) => {
    setSelectedArticle(article);
    setIsDialogOpen(true);
  };

  const handleCloseDialog = () => {
    setIsDialogOpen(false);
    setSelectedArticle(null);
  };

  return (
    <>
      <motion.section
        className="py-16 md:py-24 bg-gray-50"
        initial={{ opacity: 0, y: 50 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8, delay: 0.5 }}
      >
        <div className="container mx-auto px-4">
          <div className="text-center mb-12">
            <h2 className="text-3xl md:text-4xl font-bold text-center mb-4">{t('latestBlogs.title')}</h2>
            <p className="text-center text-gray-600 max-w-2xl mx-auto md:text-lg font-medium leading-relaxed">{t('latestBlogs.subtitle')}</p>
          </div>
          <BlogCards articles={latestArticles} onArticleClick={handleArticleClick} />
          <div className="text-center mt-12">
            <Link to="/blog" className="text-blue-600 font-semibold hover:underline">
              {t('latestBlogs.seeAll')} &rarr;
            </Link>
          </div>
        </div>
      </motion.section>
      <ArticleDetailDialog 
        article={selectedArticle} 
        isOpen={isDialogOpen} 
        onClose={handleCloseDialog} 
      />
    </>
  );
};

export default LatestBlogsSection;
