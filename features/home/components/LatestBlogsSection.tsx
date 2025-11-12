import React from 'react';
import { Link } from 'react-router-dom';
import blogData from '../../blog/data/blog.json';
import ArticleCard from '../../blog/components/ArticleCard';
import { motion } from 'framer-motion';

const LatestBlogsSection: React.FC = () => {
  const latestArticles = blogData.slice(0, 3).map(article => ({
    id: article.title.toLowerCase().replace(/\s+/g, '-').replace(/[^a-z0-9-]/g, ''),
    title: article.title,
    image: article.thumbnail || 'https://picsum.photos/400/300?random=2',
    excerpt: article.content.length > 150 ? article.content.substring(0, 150) + '...' : article.content,
    content: article.content,
    publishDate: article.date,
    category: article.categories.includes('Tư vấn') ? 'Tư vấn' as const : 'Blog' as const
  }));

  return (
    <motion.section
      className="py-16 md:py-24 bg-gray-50"
      initial={{ opacity: 0, y: 50 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.8, delay: 0.5 }}
    >
      <div className="container mx-auto px-4">
        <div className="text-center mb-12">
          <h2 className="text-3xl md:text-4xl font-bold text-center mb-4">Bài viết mới nhất</h2>
          <p className="text-center text-gray-600 max-w-2xl mx-auto">Cập nhật những tin tức, tư vấn và kiến thức mới nhất về xây dựng và thiết kế công nghiệp.</p>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {latestArticles.map(article => (
            <ArticleCard key={article.id} article={article} />
          ))}
        </div>
        <div className="text-center mt-12">
          <Link to="/blog" className="text-blue-600 font-semibold hover:underline">
            Xem tất cả bài viết &rarr;
          </Link>
        </div>
      </div>
    </motion.section>
  );
};

export default LatestBlogsSection;
