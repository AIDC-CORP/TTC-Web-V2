
import React, { useMemo } from 'react';
import { useSearchParams, Link } from 'react-router-dom';
import { allContent } from '../../data/mockData';
import ProjectCard from '../projects/components/ProjectCard';
import ArticleCard from '../blog/components/ArticleCard';
import { Project, Article } from '../../types';

const SearchResultsPage: React.FC = () => {
  const [searchParams] = useSearchParams();
  const query = searchParams.get('q') || '';

  const results = useMemo(() => {
    if (!query) return [];
    const lowerCaseQuery = query.toLowerCase();
    return allContent.filter(item => 
        ('name' in item && item.name.toLowerCase().includes(lowerCaseQuery)) ||
        ('title' in item && item.title.toLowerCase().includes(lowerCaseQuery)) ||
        ('summary' in item && item.summary.toLowerCase().includes(lowerCaseQuery)) ||
        ('description' in item && item.description.toLowerCase().includes(lowerCaseQuery)) ||
        ('excerpt' in item && item.excerpt.toLowerCase().includes(lowerCaseQuery))
    );
  }, [query]);

  return (
    <div className="container mx-auto px-4 py-16">
      <h1 className="text-3xl md:text-4xl font-bold text-center mb-4">Kết quả tìm kiếm</h1>
      <p className="text-center text-gray-600 mb-12">
        {results.length > 0 
          ? `Tìm thấy ${results.length} kết quả cho từ khóa "${query}"`
          : `Không tìm thấy kết quả phù hợp cho từ khóa "${query}"`
        }
      </p>

      {results.length > 0 && (
         <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {results.map(item => {
                if ('gallery' in item) { // Check if it's a Project
                    return <ProjectCard key={item.id} project={item as Project} />;
                } else { // It's an Article
                    return <ArticleCard key={item.id} article={item as Article} />;
                }
            })}
        </div>
      )}

      {results.length === 0 && (
          <div className="text-center">
            <p>Vui lòng thử với một từ khóa khác hoặc quay lại trang chủ.</p>
            <Link to="/" className="mt-6 inline-block bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition">
              Về trang chủ
            </Link>
          </div>
      )}
    </div>
  );
};

export default SearchResultsPage;
