
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
  const [priceRange, setPriceRange] = useState({ min: 0, max: 200000 });
  const [selectedProject, setSelectedProject] = useState<Project | null>(null);
  const [isDialogOpen, setIsDialogOpen] = useState(false);
  const [recentlyViewed, setRecentlyViewed] = useState<Project[]>([]);

  const regions = ['Tất cả', 'Miền Bắc', 'Miền Trung', 'Miền Nam'];

  const filteredProjects = useMemo(() => {
    let filtered = transformedProjects;

    // Filter by region
    if (regionFilter !== 'Tất cả') {
      filtered = filtered.filter(project => project.region === regionFilter);
    }

    // Filter by price range (using square footage as proxy for size)
    // Convert all measurements to m² for comparison
    filtered = filtered.filter(project => {
      let squareValue = 0;
      const squareText = project.square.toLowerCase();
      
      // Extract numeric value (including decimal point)
      const numericMatch = squareText.match(/[\d.]+/);
      const numericValue = numericMatch ? parseFloat(numericMatch[0]) : 0;
      
      if (squareText.includes('ha')) {
        // Convert hectares to m² (1 ha = 10,000 m²)
        squareValue = numericValue * 10000;
      } else {
        // Assume m²
        squareValue = numericValue || 0;
      }
      
      return squareValue >= priceRange.min && squareValue <= priceRange.max;
    });

    return filtered;
  }, [regionFilter, priceRange]);

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

            {/* Price Filter */}
            <motion.div 
              className="bg-gray-50 p-4 rounded-lg"
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6, delay: 0.6 }}
            >
              <h3 className="text-lg font-semibold text-gray-800 mb-4">Lọc theo quy mô</h3>
              <div className="space-y-4">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">Quy mô tối thiểu (m²):</label>
                  <input
                    type="number"
                    value={priceRange.min}
                    onChange={(e) => setPriceRange(prev => ({ ...prev, min: Number(e.target.value) }))}
                    className="w-full px-3 py-2 border border-gray-300 rounded-md text-center"
                    min="0"
                    step="1000"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">Quy mô tối đa (m²):</label>
                  <input
                    type="number"
                    value={priceRange.max}
                    onChange={(e) => setPriceRange(prev => ({ ...prev, max: Number(e.target.value) }))}
                    className="w-full px-3 py-2 border border-gray-300 rounded-md text-center"
                    min="0"
                    step="1000"
                  />
                </div>
                <button
                  onClick={() => setPriceRange({ min: 0, max: 200000 })}
                  className="w-full px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition-colors"
                >
                  Đặt lại
                </button>
                <div className="text-center text-sm text-gray-600">
                  Quy mô: {priceRange.min.toLocaleString()}m² — {priceRange.max.toLocaleString()}m²
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
                    setPriceRange({ min: 0, max: 200000 });
                  }}
                  className="px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
                >
                  Xem tất cả dự án
                </button>
              </motion.div>
            ) : (
              <motion.div 
                key={`projects-${regionFilter}`}
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
