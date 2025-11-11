
import React from 'react';
import { articles } from '../data/mockData';
import ArticleCard from '../features/blog/components/ArticleCard';

const ConsultingPage: React.FC = () => {
  const consultingArticles = articles.filter(article => article.category === 'Tư vấn');

  return (
    <div>
      <div className="bg-white py-20">
        <div className="container mx-auto px-4 text-center">
          <h1 className="text-4xl md:text-5xl font-extrabold text-gray-800">Dịch vụ Tư vấn</h1>
          <p className="mt-4 text-lg text-gray-600 max-w-3xl mx-auto">Cung cấp giải pháp chuyên môn, đồng hành cùng chủ đầu tư từ ý tưởng đến khi hoàn thiện công trình.</p>
        </div>
      </div>

      <div className="container mx-auto px-4 py-16">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {consultingArticles.map(article => (
            <ArticleCard key={article.id} article={article} />
          ))}
        </div>
      </div>
    </div>
  );
};

export default ConsultingPage;
