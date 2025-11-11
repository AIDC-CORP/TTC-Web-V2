
import React, { useState } from 'react';
import { motion } from 'framer-motion';
import blogData from './data/blog.json';
import BlogCards from './components/BlogCards';
import ArticleDetailDialog from './components/dialogs/ArticleDetailDialog';
import { Article } from '../../types';

const ARTICLES_PER_PAGE = 6;

const BlogPage: React.FC = () => {
  const [currentPage, setCurrentPage] = useState(1);
  const [selectedArticle, setSelectedArticle] = useState<Article | null>(null);
  const [isDialogOpen, setIsDialogOpen] = useState(false);

  // Transform blog data to match Article interface
  const blogArticles: Article[] = (blogData || []).map((item: any, index: number) => ({
    id: item.url || `blog-${index}`,
    title: item.title,
    image: item.thumbnail,
    excerpt: item.content?.length > 150 ? item.content.substring(0, 150) + '...' : item.content || '',
    content: item.content || '',
    publishDate: item.date || '',
    category: 'Blog' as const
  }));

  const totalPages = Math.ceil(blogArticles.length / ARTICLES_PER_PAGE);
  const indexOfLastArticle = currentPage * ARTICLES_PER_PAGE;
  const indexOfFirstArticle = indexOfLastArticle - ARTICLES_PER_PAGE;
  const currentArticles = blogArticles.slice(indexOfFirstArticle, indexOfLastArticle);

  const paginate = (pageNumber: number) => setCurrentPage(pageNumber);

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
            Blog & Tin tức
          </motion.h1>
          <motion.p 
            className="mt-4 text-lg text-gray-600"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.4 }}
          >
            Chia sẻ kiến thức, cập nhật tin tức ngành và hoạt động của công ty
          </motion.p>
        </div>
      </motion.div>

      <motion.div
        initial={{ opacity: 0, y: 50 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true }}
        transition={{ duration: 0.8, delay: 0.2 }}
      >
        <BlogCards
          articles={currentArticles}
          currentPage={currentPage}
          totalPages={totalPages}
          onPageChange={paginate}
          onArticleClick={handleArticleClick}
        />
      </motion.div>

      <ArticleDetailDialog
        article={selectedArticle}
        isOpen={isDialogOpen}
        onClose={handleCloseDialog}
      />
    </div>
  );
};

export default BlogPage;
