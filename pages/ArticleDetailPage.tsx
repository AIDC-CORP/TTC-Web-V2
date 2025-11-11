
import React from 'react';
import { useParams, Link } from 'react-router-dom';
import { articles } from '../data/mockData';

const ArticleDetailPage: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const article = articles.find(a => a.id === id);

  if (!article) {
    return (
      <div className="container mx-auto px-4 py-20 text-center">
        <h1 className="text-3xl font-bold">Không tìm thấy bài viết</h1>
        <p className="mt-4">Bài viết bạn đang tìm kiếm không tồn tại hoặc đã bị xóa.</p>
        <Link to="/blog" className="mt-8 inline-block bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition">
          Quay lại trang Blog
        </Link>
      </div>
    );
  }

  const backLink = article.category === 'Blog' ? '/blog' : '/tu-van';
  const backLinkText = article.category === 'Blog' ? 'Quay lại trang Blog' : 'Quay lại trang Tư vấn';

  return (
    <div className="bg-white py-16">
      <div className="container mx-auto px-4 max-w-4xl">
        <Link to={backLink} className="text-blue-600 hover:underline mb-8 inline-block">
          &larr; {backLinkText}
        </Link>
        <span className="text-sm text-gray-500">{article.category} | {article.publishDate}</span>
        <h1 className="text-3xl md:text-4xl font-extrabold text-gray-800 mt-2 mb-6">{article.title}</h1>
        <img src={article.image} alt={article.title} className="w-full h-auto object-cover rounded-lg shadow-lg mb-8" />
        <div className="prose max-w-none text-gray-700 leading-relaxed">
          <p>{article.content}</p>
        </div>
      </div>
    </div>
  );
};

export default ArticleDetailPage;
