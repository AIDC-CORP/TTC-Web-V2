
import React, { useState, useMemo } from 'react';
import { motion } from 'framer-motion';
import projectsData from './data/projects.json';
import ProjectCard from './components/ProjectCard';
import ProjectDetailDialog from './components/dialogs/ProjectDetailDialog';

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
}

// Transform JSON data to match Project interface
const transformedProjects = projectsData.map((project: ProjectJSON, index: number) => ({
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
  square: project.square,
  project_manager: project.project_manager,
  year: project.year
}));

const ProjectsPage: React.FC = () => {
  const [filter, setFilter] = useState('Tất cả');
  const [regionFilter, setRegionFilter] = useState('Tất cả');
  const [priceRange, setPriceRange] = useState({ min: 0, max: 30000 });
  const [selectedProject, setSelectedProject] = useState<Project | null>(null);
  const [isDialogOpen, setIsDialogOpen] = useState(false);
  const [recentlyViewed, setRecentlyViewed] = useState<Project[]>([]);
  
  const categories = useMemo(() => ['Tất cả', ...Array.from(new Set(transformedProjects.map(p => p.category)))], []);

  // Function to determine region based on location
  const getRegion = (location: string): string => {
    // Northern provinces
    if (location.includes('Bắc Giang') || location.includes('Hưng Yên') || location.includes('Hà Nam') || 
        location.includes('Thái Nguyên') || location.includes('Bắc Ninh') || location.includes('Vĩnh Phúc') ||
        location.includes('Hải Dương') || location.includes('Hải Phòng') || location.includes('Quảng Ninh') ||
        location.includes('Nam Định') || location.includes('Ninh Bình') || location.includes('Thanh Hóa') ||
        location.includes('Hà Nội') || location.includes('Hà Tây')) {
      return 'Miền Bắc';
    }
    
    // Southern provinces
    if (location.includes('TP. Hồ Chí Minh') || location.includes('Đồng Nai') || location.includes('Bình Dương') ||
        location.includes('Long An') || location.includes('Tiền Giang') || location.includes('Bến Tre') ||
        location.includes('Vĩnh Long') || location.includes('Trà Vinh') || location.includes('Hậu Giang') ||
        location.includes('Kiên Giang') || location.includes('An Giang') || location.includes('Đồng Tháp') ||
        location.includes('Tây Ninh') || location.includes('Bình Phước') || location.includes('Bà Rịa') ||
        location.includes('Cần Thơ') || location.includes('Sóc Trăng')) {
      return 'Miền Nam';
    }
    
    // Central provinces (default for any other location)
    return 'Miền Trung';
  };

  const regions = ['Tất cả', 'Miền Bắc', 'Miền Trung', 'Miền Nam'];

  const filteredProjects = useMemo(() => {
    let filtered = transformedProjects;

    // Filter by category
    if (filter !== 'Tất cả') {
      filtered = filtered.filter(project => project.category === filter);
    }

    // Filter by region
    if (regionFilter !== 'Tất cả') {
      filtered = filtered.filter(project => getRegion(project.location_specific) === regionFilter);
    }

    // Filter by price range (using square footage as proxy for size)
    // Convert all measurements to m² for comparison
    filtered = filtered.filter(project => {
      let squareValue = 0;
      const squareText = project.square.toLowerCase();
      
      if (squareText.includes('ha')) {
        // Convert hectares to m² (1 ha = 10,000 m²)
        squareValue = parseFloat(squareText.replace(/[^\d.]/g, '')) * 10000;
      } else {
        // Assume m²
        squareValue = parseFloat(squareText.replace(/[^\d.]/g, '')) || 0;
      }
      
      return squareValue >= priceRange.min && squareValue <= priceRange.max;
    });

    return filtered;
  }, [filter, regionFilter, priceRange]);

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
            {/* Category Filter */}
            <motion.div 
              className="mb-6"
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6, delay: 0.2 }}
            >
              <h3 className="text-lg font-semibold text-gray-800 mb-4">Lọc theo danh mục</h3>
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
                {categories.map((category, index) => (
                  <motion.button 
                    key={category} 
                    onClick={() => setFilter(category)}
                    className={`px-4 py-2 rounded-full font-semibold text-sm transition-colors duration-300 ${filter === category ? 'bg-blue-600 text-white' : 'bg-gray-200 text-gray-700 hover:bg-blue-200'}`}
                    variants={{
                      hidden: { opacity: 0, scale: 0.8 },
                      visible: { opacity: 1, scale: 1 }
                    }}
                    transition={{ duration: 0.4 }}
                    whileHover={{ scale: 1.05 }}
                    whileTap={{ scale: 0.95 }}
                  >
                    {category}
                  </motion.button>
                ))}
              </motion.div>
            </motion.div>

            {/* Region Filter */}
            <motion.div 
              className="mb-6"
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6, delay: 0.4 }}
            >
              <h3 className="text-lg font-semibold text-gray-800 mb-4">Lọc theo vùng miền</h3>
              <motion.div 
                className="flex flex-wrap gap-2"
                initial="hidden"
                whileInView="visible"
                viewport={{ once: true }}
                transition={{ staggerChildren: 0.1, delayChildren: 0.6 }}
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
                  onClick={() => setPriceRange({ min: 0, max: 30000 })}
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
            <motion.div 
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
