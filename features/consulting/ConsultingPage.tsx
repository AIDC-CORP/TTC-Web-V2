
import React, { useState } from 'react';
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
      <div className="bg-white py-20">
        <div className="container mx-auto px-4 text-center">
          <h1 className="text-4xl md:text-5xl font-extrabold text-gray-800">Dịch vụ Tư vấn</h1>
          <p className="mt-4 text-lg text-gray-600 max-w-3xl mx-auto">Cung cấp giải pháp chuyên môn, đồng hành cùng chủ đầu tư từ ý tưởng đến khi hoàn thiện công trình.</p>
        </div>
      </div>

      <ConsultingCards
        articles={consultingArticles}
        onArticleClick={handleArticleClick}
      />

      <ConsultingDetailDialog
        article={selectedArticle}
        isOpen={isDialogOpen}
        onClose={handleCloseDialog}
      />
    </div>
  );
};

export default ConsultingPage;
