import React, { useMemo, useState } from 'react';
import { Link } from 'react-router-dom';
import blogData from '../../blog/data/blog.json';
import BlogCards from '../../blog/components/BlogCards';
import ArticleDetailDialog from '../../blog/components/dialogs/ArticleDetailDialog';
import { motion } from 'framer-motion';
import { useTranslation } from 'react-i18next';
import { Article } from '../../../types';
import { getCurrentLangKey } from '../../../common/utils/i18nUtils';

const LatestBlogsSection: React.FC = () => {
  const { t, i18n } = useTranslation();
  const [selectedArticle, setSelectedArticle] = useState<Article | null>(null);
  const [isDialogOpen, setIsDialogOpen] = useState(false);

  const latestArticles = useMemo<Article[]>(() => {
    const currentLang = getCurrentLangKey(i18n.language);

    const mappedArticles = (blogData as Article[])
      .map<Article | null>((article) => {
        const localized = article[currentLang] || article.vi || article.en;
        const fallback = article.vi || article.en;
        const title = localized?.title?.trim() || fallback?.title?.trim();

        if (!title) {
          return null;
        }

        const content = localized?.content || fallback?.content || '';
        const excerpt = content.length > 150 ? `${content.substring(0, 150)}...` : content;

        return {
          ...article,
          id: article.id || title.toLowerCase().replace(/\s+/g, '-').replace(/[^a-z0-9-]/g, ''),
          title,
          content,
          excerpt,
          publishDate: article.date,
          category: article.categories.includes('Tư vấn')
            ? t('blog.category.consulting')
            : t('blog.category.blog')
        };
      })
      .filter((article): article is Article => Boolean(article));

    return mappedArticles.slice(0, 3);
  }, [i18n.language, t]);

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
