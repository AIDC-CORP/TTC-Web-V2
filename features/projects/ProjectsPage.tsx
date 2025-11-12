
import React, { useState, useMemo } from 'react';
import { motion } from 'framer-motion';
import projectsData from './data/projects.json';
import ProjectCard from './components/ProjectCard';
import ProjectDetailDialog from './components/dialogs/ProjectDetailDialog';
import { Project } from '../../types';

interface ProjectJSON {
  name: string;
  url: string;
  thumbnail_url: string;
  year: string;
  location_specific: string;
  region: string;
  square: string;
  project_manager: string;
  gallery_urls: string[];
}

// Transform JSON data to match Project interface
const transformedProjects: Project[] = projectsData.map((project: ProjectJSON, index: number) => ({
  id: `project-${index}`,
  name: project.name,
  image: project.thumbnail_url || 'https://picsum.photos/seed/project-default/800/600',
  summary: `Dự án tại ${project.location_specific}`,
  description: `Dự án này được thực hiện với quy mô lớn và đúng tiến độ. Chúng tôi tự hào về những kết quả đạt được trong quá trình thi công.`,
  investor: undefined,
  executionTime: project.year,
  gallery: project.gallery_urls.length > 0 ? project.gallery_urls : [],
  category: 'Công trình',
  location_specific: project.location_specific,
  region: project.region,
  square: project.square,
  project_manager: project.project_manager,
  year: project.year
}));

const ProjectsPage: React.FC = () => {
  const [regionFilter, setRegionFilter] = useState('Tất cả');
  const [tempPriceRange, setTempPriceRange] = useState({ min: 0, max: 200000 });
  const [appliedPriceRange, setAppliedPriceRange] = useState({ min: 0, max: 200000 });
  const [selectedProject, setSelectedProject] = useState<Project | null>(null);
  const [isDialogOpen, setIsDialogOpen] = useState(false);
  const [recentlyViewed, setRecentlyViewed] = useState<Project[]>([]);

  const regions = ['Tất cả', 'Miền Bắc', 'Miền Trung', 'Miền Nam'];

  const filteredProjects = useMemo(() => {
    return transformedProjects.filter(project => {
      // Filter by region
      const regionMatch = regionFilter === 'Tất cả' || project.region === regionFilter;
      
      // Filter by square range
      const squareValue = parseInt(project.square) || 0;
      const squareMatch = squareValue >= appliedPriceRange.min && squareValue <= appliedPriceRange.max;
      
      return regionMatch && squareMatch;
    });
  }, [regionFilter, appliedPriceRange]);

  const applyScaleFilter = () => {
    setAppliedPriceRange({ ...tempPriceRange });
  };

  const resetFilters = () => {
    setTempPriceRange({ min: 0, max: 200000 });
    setAppliedPriceRange({ min: 0, max: 200000 });
  };

  const openProjectDialog = (project: Project) => {
    setSelectedProject(project);
    setIsDialogOpen(true);
    
    // Add to recently viewed (keep only last 5)
    setRecentlyViewed(prev => {
      const filtered = prev.filter(p => p.id !== project.id);
      return [project, ...filtered].slice(0, 5);
    });
  };

  const closeProjectDialog = () => {
    setIsDialogOpen(false);
    setSelectedProject(null);
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
            Dự án của chúng tôi
          </motion.h1>
          <motion.p 
            className="mt-4 text-lg text-gray-600"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.4 }}
          >
            Năng lực và kinh nghiệm được chứng thực qua các công trình thực tế
          </motion.p>
        </div>
      </motion.div>

      <div className="container mx-auto px-4 py-16">
        <div className="lg:flex lg:gap-8">
          {/* Filters Sidebar */}
          <motion.div 
            className="lg:w-1/4 mb-8 lg:mb-0"
            initial={{ opacity: 0, x: -50 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6 }}
          >
            {/* Region Filter */}
            <motion.div 
              className="mb-6"
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6, delay: 0.2 }}
            >
              <h3 className="text-lg font-semibold text-gray-800 mb-4">Lọc theo vùng miền</h3>
              <motion.div 
                className="flex flex-wrap gap-2"
                initial="hidden"
                whileInView="visible"
                viewport={{ once: true }}
                transition={{ staggerChildren: 0.1, delayChildren: 0.4 }}
                variants={{
                  hidden: {},
                  visible: {}
                }}
              >
                {regions.map((region, index) => (
                  <motion.button
                    key={region}
                    onClick={() => setRegionFilter(region)}
                    className={`px-4 py-2 rounded-full font-semibold text-sm transition-colors duration-300 ${regionFilter === region ? 'bg-green-600 text-white' : 'bg-gray-200 text-gray-700 hover:bg-green-200'}`}
                    variants={{
                      hidden: { opacity: 0, scale: 0.8 },
                      visible: { opacity: 1, scale: 1 }
                    }}
                    transition={{ duration: 0.4 }}
                    whileHover={{ scale: 1.05 }}
                    whileTap={{ scale: 0.95 }}
                  >
                    {region}
                  </motion.button>
                ))}
              </motion.div>
            </motion.div>

            {/* Scale Filter */}
            <motion.div 
              className="bg-gray-50 p-6 rounded-lg"
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6, delay: 0.6 }}
            >
              <h3 className="text-lg font-semibold text-gray-800 mb-6">Lọc theo quy mô</h3>
              <div className="space-y-6">
                {/* Min Range Slider */}
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-3">
                    Quy mô tối thiểu: <span className="text-green-600 font-semibold">{tempPriceRange.min.toLocaleString()} m²</span>
                  </label>
                  <input
                    type="range"
                    min="0"
                    max="200000"
                    step="5000"
                    value={tempPriceRange.min}
                    onChange={(e) => {
                      const newMin = Number(e.target.value);
                      if (newMin <= tempPriceRange.max) {
                        setTempPriceRange(prev => ({ ...prev, min: newMin }));
                      }
                    }}
                    className="w-full h-2 bg-gray-300 rounded-lg appearance-none cursor-pointer accent-green-600"
                    style={{
                      background: `linear-gradient(to right, #16a34a 0%, #16a34a ${(tempPriceRange.min / 200000) * 100}%, #d1d5db ${(tempPriceRange.min / 200000) * 100}%, #d1d5db 100%)`
                    }}
                  />
                  <div className="flex justify-between text-xs text-gray-500 mt-1">
                    <span>0 m²</span>
                    <span>200,000 m²</span>
                  </div>
                </div>

                {/* Max Range Slider */}
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-3">
                    Quy mô tối đa: <span className="text-green-600 font-semibold">{tempPriceRange.max.toLocaleString()} m²</span>
                  </label>
                  <input
                    type="range"
                    min="0"
                    max="200000"
                    step="5000"
                    value={tempPriceRange.max}
                    onChange={(e) => {
                      const newMax = Number(e.target.value);
                      if (newMax >= tempPriceRange.min) {
                        setTempPriceRange(prev => ({ ...prev, max: newMax }));
                      }
                    }}
                    className="w-full h-2 bg-gray-300 rounded-lg appearance-none cursor-pointer accent-green-600"
                    style={{
                      background: `linear-gradient(to right, #d1d5db 0%, #d1d5db ${(tempPriceRange.max / 200000) * 100}%, #16a34a ${(tempPriceRange.max / 200000) * 100}%, #16a34a 100%)`
                    }}
                  />
                  <div className="flex justify-between text-xs text-gray-500 mt-1">
                    <span>0 m²</span>
                    <span>200,000 m²</span>
                  </div>
                </div>

                {/* Current Range Display */}
                <div className="bg-white p-4 rounded-md border border-gray-200">
                  <div className="text-center">
                    <p className="text-xs text-gray-600 mb-1">Khoảng quy mô đã chọn</p>
                    <p className="text-lg font-bold text-gray-800">
                      {tempPriceRange.min.toLocaleString()} — {tempPriceRange.max.toLocaleString()} m²
                    </p>
                  </div>
                </div>

                {/* Action Buttons */}
                <div className="flex gap-2">
                  <motion.button
                    onClick={applyScaleFilter}
                    className="flex-1 px-4 py-2 bg-green-600 text-white rounded-md hover:bg-green-700 transition-colors font-medium shadow-sm"
                    whileHover={{ scale: 1.02 }}
                    whileTap={{ scale: 0.98 }}
                  >
                    Áp dụng
                  </motion.button>
                  <motion.button
                    onClick={resetFilters}
                    className="flex-1 px-4 py-2 bg-gray-300 text-gray-700 rounded-md hover:bg-gray-400 transition-colors font-medium shadow-sm"
                    whileHover={{ scale: 1.02 }}
                    whileTap={{ scale: 0.98 }}
                  >
                    Đặt lại
                  </motion.button>
                </div>
              </div>
            </motion.div>
          </motion.div>

          {/* Projects Grid */}
          <motion.div 
            className="lg:w-3/4"
            initial={{ opacity: 0, x: 50 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6, delay: 0.2 }}
          >
            {filteredProjects.length === 0 ? (
              <motion.div 
                className="text-center py-16"
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.6 }}
              >
                <div className="text-6xl mb-4">🏗️</div>
                <h3 className="text-2xl font-bold text-gray-800 mb-2">Không tìm thấy dự án</h3>
                <p className="text-gray-600 mb-6">
                  Hiện tại chưa có dự án nào phù hợp với bộ lọc của bạn.
                </p>
                <button
                  onClick={() => {
                    setRegionFilter('Tất cả');
                    resetFilters();
                  }}
                  className="px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
                >
                  Xem tất cả dự án
                </button>
              </motion.div>
            ) : (
              <motion.div 
                key={`projects-${regionFilter}-${appliedPriceRange.min}-${appliedPriceRange.max}`}
                className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-8"
                initial="hidden"
                whileInView="visible"
                viewport={{ once: true }}
                transition={{ staggerChildren: 0.1, delayChildren: 0.4 }}
                variants={{
                  hidden: {},
                  visible: {}
                }}
              >
                {filteredProjects.map((project, index) => (
                  <motion.div
                    key={project.id}
                    variants={{
                      hidden: { opacity: 0, y: 50 },
                      visible: { opacity: 1, y: 0 }
                    }}
                    transition={{ duration: 0.6 }}
                  >
                    <ProjectCard project={project} onClick={openProjectDialog} />
                  </motion.div>
                ))}
              </motion.div>
            )}

            {/* Recently Viewed */}
            {recentlyViewed.length > 0 && (
              <motion.div 
                className="mt-16"
                initial={{ opacity: 0, y: 50 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.6, delay: 0.6 }}
              >
                <motion.h2 
                  className="text-2xl font-bold text-gray-800 mb-8 text-center"
                  initial={{ opacity: 0, scale: 0.9 }}
                  whileInView={{ opacity: 1, scale: 1 }}
                  viewport={{ once: true }}
                  transition={{ duration: 0.6, delay: 0.8 }}
                >
                  Đã xem gần đây
                </motion.h2>
                <motion.div 
                  className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-8"
                  initial="hidden"
                  whileInView="visible"
                  viewport={{ once: true }}
                  transition={{ staggerChildren: 0.1, delayChildren: 1.0 }}
                  variants={{
                    hidden: {},
                    visible: {}
                  }}
                >
                  {recentlyViewed.map((project, index) => (
                    <motion.div
                      key={`recent-${project.id}`}
                      variants={{
                        hidden: { opacity: 0, scale: 0.8 },
                        visible: { opacity: 1, scale: 1 }
                      }}
                      transition={{ duration: 0.5 }}
                    >
                      <ProjectCard project={project} onClick={openProjectDialog} />
                    </motion.div>
                  ))}
                </motion.div>
              </motion.div>
            )}
          </motion.div>
        </div>
      </div>

      <ProjectDetailDialog
        project={selectedProject}
        isOpen={isDialogOpen}
        onClose={closeProjectDialog}
      />
    </div>
  );
};

export default ProjectsPage;
