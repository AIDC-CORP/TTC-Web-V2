import React from 'react';
import { Link } from 'react-router-dom';
import { motion, AnimatePresence } from 'framer-motion';

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
  return (
    <AnimatePresence>
      {isOpen && project && (
        <motion.div 
          className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          transition={{ duration: 0.3 }}
          onClick={onClose}
        >
          <motion.div 
            className="bg-white rounded-lg shadow-xl max-w-6xl w-full mx-4 max-h-[90vh] overflow-y-auto"
            initial={{ opacity: 0, scale: 0.8, y: 50 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.8, y: 50 }}
            transition={{ duration: 0.4, ease: "easeOut" }}
            onClick={(e) => e.stopPropagation()}
          >
            <div className="p-6">
              {/* Header */}
              <motion.div 
                className="flex justify-between items-center mb-6"
                initial={{ opacity: 0, y: -20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5, delay: 0.2 }}
              >
                <h2 className="text-2xl md:text-3xl font-bold text-gray-800">{project.name}</h2>
                <motion.button
                  onClick={onClose}
                  className="text-gray-500 hover:text-gray-700 text-2xl font-bold"
                  whileHover={{ scale: 1.1, rotate: 90 }}
                  whileTap={{ scale: 0.9 }}
                  transition={{ duration: 0.2 }}
                >
                  ×
                </motion.button>
              </motion.div>

              {/* Content */}
              <motion.div 
                className="lg:flex lg:space-x-8"
                initial={{ opacity: 0, y: 30 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.6, delay: 0.3 }}
              >
                {/* Main Content */}
                <motion.div 
                  className="lg:w-2/3 mb-6 lg:mb-0"
                  initial={{ opacity: 0, x: -30 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ duration: 0.6, delay: 0.4 }}
                >
                  <motion.img
                    src={project.image}
                    alt={project.name}
                    className="w-full h-auto object-cover rounded-lg shadow-lg mb-6"
                    initial={{ opacity: 0, scale: 0.9 }}
                    animate={{ opacity: 1, scale: 1 }}
                    transition={{ duration: 0.6, delay: 0.5 }}
                  />
                  <motion.div 
                    className="prose max-w-none"
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.6, delay: 0.6 }}
                  >
                    <p className="text-gray-600 leading-relaxed whitespace-pre-line">
                      {project.description}
                    </p>
                  </motion.div>
                </motion.div>

                {/* Sidebar */}
                <motion.div 
                  className="lg:w-1/3"
                  initial={{ opacity: 0, x: 30 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ duration: 0.6, delay: 0.5 }}
                >
                  <motion.div 
                    className="bg-gray-50 p-6 rounded-lg shadow-md"
                    initial={{ opacity: 0, scale: 0.95 }}
                    animate={{ opacity: 1, scale: 1 }}
                    transition={{ duration: 0.5, delay: 0.6 }}
                  >
                    <motion.h3 
                      className="text-xl font-bold border-b pb-3 mb-4"
                      initial={{ opacity: 0, x: -20 }}
                      animate={{ opacity: 1, x: 0 }}
                      transition={{ duration: 0.5, delay: 0.7 }}
                    >
                      Thông tin dự án
                    </motion.h3>
                    <motion.div 
                      className="space-y-4"
                      initial="hidden"
                      animate="visible"
                      transition={{ staggerChildren: 0.1, delayChildren: 0.8 }}
                      variants={{
                        hidden: {},
                        visible: {}
                      }}
                    >
                      {project.project_manager && (
                        <motion.div
                          variants={{
                            hidden: { opacity: 0, x: -20 },
                            visible: { opacity: 1, x: 0 }
                          }}
                          transition={{ duration: 0.4 }}
                        >
                          <h4 className="font-semibold text-gray-700">Quản lý dự án</h4>
                          <p className="text-gray-600">{project.project_manager}</p>
                        </motion.div>
                      )}
                      {project.year && (
                        <motion.div
                          variants={{
                            hidden: { opacity: 0, x: -20 },
                            visible: { opacity: 1, x: 0 }
                          }}
                          transition={{ duration: 0.4 }}
                        >
                          <h4 className="font-semibold text-gray-700">Năm thực hiện</h4>
                          <p className="text-gray-600">{project.year}</p>
                        </motion.div>
                      )}
                      {project.location_specific && (
                        <motion.div
                          variants={{
                            hidden: { opacity: 0, x: -20 },
                            visible: { opacity: 1, x: 0 }
                          }}
                          transition={{ duration: 0.4 }}
                        >
                          <h4 className="font-semibold text-gray-700">Địa điểm</h4>
                          <p className="text-gray-600">{project.location_specific}</p>
                        </motion.div>
                      )}
                      {project.square && (
                        <motion.div
                          variants={{
                            hidden: { opacity: 0, x: -20 },
                            visible: { opacity: 1, x: 0 }
                          }}
                          transition={{ duration: 0.4 }}
                        >
                          <h4 className="font-semibold text-gray-700">Quy mô</h4>
                          <p className="text-gray-600">{project.square}</p>
                        </motion.div>
                      )}
                    </motion.div>
                  </motion.div>
                </motion.div>
              </motion.div>

              {/* Gallery */}
              {project.gallery && project.gallery.length > 0 && (
                <motion.div 
                  className="mt-8"
                  initial={{ opacity: 0, y: 50 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.6, delay: 0.9 }}
                >
                  <motion.h3 
                    className="text-xl md:text-2xl font-bold text-center mb-6"
                    initial={{ opacity: 0, scale: 0.9 }}
                    animate={{ opacity: 1, scale: 1 }}
                    transition={{ duration: 0.5, delay: 1.0 }}
                  >
                    Thư viện hình ảnh
                  </motion.h3>
                  <motion.div 
                    className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4"
                    initial="hidden"
                    animate="visible"
                    transition={{ staggerChildren: 0.1, delayChildren: 1.1 }}
                    variants={{
                      hidden: {},
                      visible: {}
                    }}
                  >
                    {project.gallery.map((image, index) => (
                      <motion.div 
                        key={index} 
                        className="overflow-hidden rounded-lg shadow-md"
                        variants={{
                          hidden: { opacity: 0, scale: 0.8 },
                          visible: { opacity: 1, scale: 1 }
                        }}
                        transition={{ duration: 0.5 }}
                        whileHover={{ scale: 1.05 }}
                      >
                        <motion.img
                          src={image}
                          alt={`Hình ảnh dự án ${project.name} ${index + 1}`}
                          className="w-full h-full object-cover transform hover:scale-105 transition-transform duration-300"
                          whileHover={{ scale: 1.1 }}
                          transition={{ duration: 0.3 }}
                        />
                      </motion.div>
                    ))}
                  </motion.div>
                </motion.div>
              )}

              {/* Footer */}
              <motion.div 
                className="mt-8 pt-6 border-t border-gray-200 flex justify-between"
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5, delay: 1.2 }}
              >
                <Link
                  to="/du-an"
                  className="text-blue-600 hover:underline"
                  onClick={onClose}
                >
                  Xem tất cả dự án
                </Link>
                <motion.button
                  onClick={onClose}
                  className="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition"
                  whileHover={{ scale: 1.05 }}
                  whileTap={{ scale: 0.95 }}
                >
                  Đóng
                </motion.button>
              </motion.div>
            </div>
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
};

export default ProjectDetailDialog;
