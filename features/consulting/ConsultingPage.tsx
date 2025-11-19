import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { useTranslation } from 'react-i18next';
import consultingData from './data/consulting.json';
import ConsultingDetailDialog from './components/dialogs/ConsultingDetailDialog';
import ConsultingCards from './components/ConsultingCards';
import { Article } from '../../types';

const ConsultingPage: React.FC = () => {
  const { t, i18n } = useTranslation();
  const [selectedArticle, setSelectedArticle] = useState<Article | null>(null);
  const [isDialogOpen, setIsDialogOpen] = useState(false);

  const currentLang = i18n.language.startsWith('vi') ? 'vi' : 'en';

  // Transform consulting data to match Article interface
  const consultingArticles: Article[] = (consultingData as Article[]).map((item: Article) => {
    const localizedData = item[currentLang] || item.vi; // Fallback to Vietnamese
    const content = localizedData.content || '';
    return {
      ...item,
      title: localizedData.title,
      image: item.thumbnail, // Match the property used in the Card component
      excerpt: content.length > 150 ? content.substring(0, 150) + '...' : content,
      content: content,
      publishDate: item.date || '',
      category: t('blog.category.consulting') as const
    };
  });

  const handleArticleClick = (article: Article) => {
    // Find the original full article from consultingData to pass to the dialog
    const fullArticle = consultingData.find(a => a.id === article.id) as Article | undefined;
    if (fullArticle) {
      setSelectedArticle(fullArticle);
      setIsDialogOpen(true);
    }
  };

  const handleCloseDialog = () => {
    setIsDialogOpen(false);
    setSelectedArticle(null);
  };

  return (
    <div>
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
            {t('consulting.page.title')}
          </motion.h1>
          <motion.p 
            className="mt-4 text-lg text-gray-800 max-w-3xl mx-auto md:text-lg font-medium leading-relaxed"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.4 }}
          >
            {t('consulting.page.subtitle')}
          </motion.p>
        </div>
      </motion.div>

      <motion.div
        initial={{ opacity: 0, y: 50 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8, delay: 0.2 }}
      >
        <ConsultingCards
          articles={consultingArticles}
          onArticleClick={handleArticleClick}
        />
      </motion.div>

      <ConsultingDetailDialog
        article={selectedArticle}
        isOpen={isDialogOpen}
        onClose={handleCloseDialog}
      />
    </div>
  );
};

export default ConsultingPage;