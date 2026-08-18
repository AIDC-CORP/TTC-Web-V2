import React from 'react';
import { motion } from 'framer-motion';
import { useTranslation } from 'react-i18next';
import blogData from './data/blog.json';
import BlogCards from './components/BlogCards';
import { Article } from '../../types';
import { getCurrentLangKey } from '../../common/utils/i18nUtils';
import Seo from '../../common/components/Seo';

const BlogPage: React.FC = () => {
  const { t, i18n } = useTranslation();

  const currentLang = getCurrentLangKey(i18n.language);

  // Transform blog data to match Article interface
  const blogArticles: Article[] = (blogData || []).map((item: any) => {
    const localizedData = item[currentLang] || item.vi; // Fallback to Vietnamese
    const content = localizedData.content || '';
    return {
      ...item,
      id: item.id,
      title: localizedData.title,
      image: item.thumbnail,
      excerpt: content.length > 150 ? content.substring(0, 150) + '...' : content,
      content: content,
      publishDate: item.date || '',
      category: t('blog.category.blog') as const
    };
  });

  return (
    <div>
      <Seo
        title="Blog"
        description="Blog Tân Thành Công JSC - Cập nhật tin tức, kiến thức chuyên ngành và xu hướng mới nhất trong lĩnh vực thiết kế và thi công nhà máy công nghiệp."
        canonical="https://tanthanhcongjsc.com/blog"
        image="https://tanthanhcongjsc.com/logo_aidc.png"
        lang="vi"
      />
      <motion.div
        className="bg-white py-20"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 0.8 }}
      >
        <div className="container mx-auto px-4 text-center">
          <motion.h1
            className="text-4xl md:text-5xl font-extrabold text-gray-800"
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.2 }}
          >
            {t('blog.page.title')}
          </motion.h1>
          <motion.p
            className="mt-4 text-lg text-gray-800 max-w-3xl mx-auto md:text-lg font-medium leading-relaxed"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.4 }}
          >
            {t('blog.page.subtitle')}
          </motion.p>
        </div>
      </motion.div>

      <motion.div
        initial={{ opacity: 0, y: 50 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8, delay: 0.2 }}
      >
        <BlogCards
          articles={blogArticles}
        />
      </motion.div>
    </div>
  );
};

export default BlogPage;