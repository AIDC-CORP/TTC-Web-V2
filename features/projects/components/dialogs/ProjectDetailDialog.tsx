import React from 'react';
import { Link } from 'react-router-dom';

interface ProjectJSON {
  name: string;
  url: string;
  thumbnail_url: string;
  year: string;
  location_specific: string;
  square: string;
  project_manager: string;
  gallery_urls: string[];
}

interface Project {
  id: string;
  name: string;
  image: string;
  summary: string;
  description: string;
  investor: any;
  executionTime: string;
  gallery: string[];
  category: string;
  location_specific: string;
  square: string;
  project_manager: string;
  year: string;
}

interface ProjectDetailDialogProps {
  project: Project | null;
  isOpen: boolean;
  onClose: () => void;
}

const ProjectDetailDialog: React.FC<ProjectDetailDialogProps> = ({ project, isOpen, onClose }) => {
  if (!isOpen || !project) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50">
      <div className="bg-white rounded-lg shadow-xl max-w-6xl w-full mx-4 max-h-[90vh] overflow-y-auto">
        <div className="p-6">
          {/* Header */}
          <div className="flex justify-between items-center mb-6">
            <h2 className="text-2xl md:text-3xl font-bold text-gray-800">{project.name}</h2>
            <button
              onClick={onClose}
              className="text-gray-500 hover:text-gray-700 text-2xl font-bold"
            >
              ×
            </button>
          </div>

          {/* Content */}
          <div className="lg:flex lg:space-x-8">
            {/* Main Content */}
            <div className="lg:w-2/3 mb-6 lg:mb-0">
              <img
                src={project.image}
                alt={project.name}
                className="w-full h-auto object-cover rounded-lg shadow-lg mb-6"
              />
              <div className="prose max-w-none">
                <p className="text-gray-600 leading-relaxed whitespace-pre-line">
                  {project.description}
                </p>
              </div>
            </div>

            {/* Sidebar */}
            <div className="lg:w-1/3">
              <div className="bg-gray-50 p-6 rounded-lg shadow-md">
                <h3 className="text-xl font-bold border-b pb-3 mb-4">Thông tin dự án</h3>
                <div className="space-y-4">
                  {project.project_manager && (
                    <div>
                      <h4 className="font-semibold text-gray-700">Quản lý dự án</h4>
                      <p className="text-gray-600">{project.project_manager}</p>
                    </div>
                  )}
                  {project.year && (
                    <div>
                      <h4 className="font-semibold text-gray-700">Năm thực hiện</h4>
                      <p className="text-gray-600">{project.year}</p>
                    </div>
                  )}
                  {project.location_specific && (
                    <div>
                      <h4 className="font-semibold text-gray-700">Địa điểm</h4>
                      <p className="text-gray-600">{project.location_specific}</p>
                    </div>
                  )}
                  {project.square && (
                    <div>
                      <h4 className="font-semibold text-gray-700">Quy mô</h4>
                      <p className="text-gray-600">{project.square}</p>
                    </div>
                  )}
                </div>
              </div>
            </div>
          </div>

          {/* Gallery */}
          {project.gallery && project.gallery.length > 0 && (
            <div className="mt-8">
              <h3 className="text-xl md:text-2xl font-bold text-center mb-6">Thư viện hình ảnh</h3>
              <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
                {project.gallery.map((image, index) => (
                  <div key={index} className="overflow-hidden rounded-lg shadow-md">
                    <img
                      src={image}
                      alt={`Hình ảnh dự án ${project.name} ${index + 1}`}
                      className="w-full h-full object-cover transform hover:scale-105 transition-transform duration-300"
                    />
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Footer */}
          <div className="mt-8 pt-6 border-t border-gray-200 flex justify-between">
            <Link
              to="/du-an"
              className="text-blue-600 hover:underline"
              onClick={onClose}
            >
              Xem tất cả dự án
            </Link>
            <button
              onClick={onClose}
              className="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition"
            >
              Đóng
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ProjectDetailDialog;
