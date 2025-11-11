
import React from 'react';
import { useParams, Link } from 'react-router-dom';
import { projects } from '../../data/mockData';

const ProjectDetailPage: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const project = projects.find(p => p.id === id);

  if (!project) {
    return (
      <div className="container mx-auto px-4 py-20 text-center">
        <h1 className="text-3xl font-bold">Không tìm thấy dự án</h1>
        <p className="mt-4">Dự án bạn đang tìm kiếm không tồn tại hoặc đã bị xóa.</p>
        <Link to="/du-an" className="mt-8 inline-block bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition">
          Quay lại danh sách dự án
        </Link>
      </div>
    );
  }

  return (
    <div className="bg-white">
      <div className="container mx-auto px-4 py-12 md:py-20">
        <Link to="/du-an" className="text-blue-600 hover:underline mb-8 inline-block">
          &larr; Quay lại danh sách dự án
        </Link>
        <div className="lg:flex lg:space-x-12">
            <div className="lg:w-2/3">
                <img src={project.image} alt={project.name} className="w-full h-auto object-cover rounded-lg shadow-lg mb-8"/>
                <h1 className="text-3xl md:text-4xl font-bold text-gray-800 mb-4">{project.name}</h1>
                <p className="text-gray-600 leading-relaxed">{project.description}</p>
            </div>
            <div className="lg:w-1/3 mt-8 lg:mt-0">
                <div className="bg-gray-50 p-6 rounded-lg shadow-md sticky top-28">
                    <h3 className="text-xl font-bold border-b pb-3 mb-4">Thông tin dự án</h3>
                    <div className="space-y-4">
                        {project.investor && (
                            <div>
                                <h4 className="font-semibold text-gray-700">Chủ đầu tư</h4>
                                <p className="text-gray-600">{project.investor}</p>
                            </div>
                        )}
                        {project.executionTime && (
                             <div>
                                <h4 className="font-semibold text-gray-700">Thời gian thực hiện</h4>
                                <p className="text-gray-600">{project.executionTime}</p>
                            </div>
                        )}
                        <div>
                            <h4 className="font-semibold text-gray-700">Lĩnh vực</h4>
                            <p className="text-gray-600">{project.category}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        {project.gallery && project.gallery.length > 0 && (
          <div className="mt-16">
            <h2 className="text-2xl md:text-3xl font-bold text-center mb-8">Thư viện hình ảnh</h2>
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
              {project.gallery.map((image, index) => (
                <div key={index} className="overflow-hidden rounded-lg shadow-md">
                  <img src={image} alt={`Hình ảnh dự án ${project.name} ${index + 1}`} className="w-full h-full object-cover transform hover:scale-105 transition-transform duration-300" />
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default ProjectDetailPage;
