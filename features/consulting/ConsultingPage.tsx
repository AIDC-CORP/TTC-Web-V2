
import React, { useState } from 'react';
import { motion } from 'framer-motion';
import consultingData from './data/consulting.json';
import ConsultingDetailDialog from './components/dialogs/ConsultingDetailDialog';
import ConsultingCards from './components/ConsultingCards';
import { Article } from '../../types';

const ConsultingPage: React.FC = () => {
  const [selectedArticle, setSelectedArticle] = useState<Article | null>(null);
  const [isDialogOpen, setIsDialogOpen] = useState(false);

  // Transform consulting data to match Article interface
  const consultingArticles: Article[] = consultingData.map((item: any, index: number) => ({
    id: item.url || `consulting-${index}`,
    title: item.title,
    image: item.thumbnail,
    excerpt: item.content.length > 150 ? item.content.substring(0, 150) + '...' : item.content,
    content: item.content,
    publishDate: item.date,
    category: 'Tư vấn' as const
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
            Dịch vụ Tư vấn
          </motion.h1>
          <motion.p 
            className="mt-4 text-lg text-gray-600 max-w-3xl mx-auto"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.4 }}
          >
            Cung cấp giải pháp chuyên môn, đồng hành cùng chủ đầu tư từ ý tưởng đến khi hoàn thiện công trình.
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
