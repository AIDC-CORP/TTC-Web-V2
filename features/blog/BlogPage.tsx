
import React, { useState } from 'react';
import { articles } from '../../data/mockData';
import BlogCards from './components/BlogCards';
import ArticleDetailDialog from './components/dialogs/ArticleDetailDialog';
import { Article } from '../../types';

const ARTICLES_PER_PAGE = 6;

const BlogPage: React.FC = () => {
  const [currentPage, setCurrentPage] = useState(1);
  const [selectedArticle, setSelectedArticle] = useState<Article | null>(null);
  const [isDialogOpen, setIsDialogOpen] = useState(false);
  const blogArticles = articles.filter(article => article.category === 'Blog');

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
      <div className="bg-white py-20">
        <div className="container mx-auto px-4 text-center">
          <h1 className="text-4xl md:text-5xl font-extrabold text-gray-800">Blog & Tin tức</h1>
          <p className="mt-4 text-lg text-gray-600">Chia sẻ kiến thức, cập nhật tin tức ngành và hoạt động của công ty</p>
        </div>
      </div>

      <BlogCards
        articles={currentArticles}
        currentPage={currentPage}
        totalPages={totalPages}
        onPageChange={paginate}
        onArticleClick={handleArticleClick}
      />

      <ArticleDetailDialog
        article={selectedArticle}
        isOpen={isDialogOpen}
        onClose={handleCloseDialog}
      />
    </div>
  );
};

export default BlogPage;
