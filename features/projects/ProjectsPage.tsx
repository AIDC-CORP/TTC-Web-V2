
import React, { useState, useMemo } from 'react';
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
      <div className="bg-white py-20">
        <div className="container mx-auto px-4 text-center">
          <h1 className="text-4xl md:text-5xl font-extrabold text-gray-800">Dự án của chúng tôi</h1>
          <p className="mt-4 text-lg text-gray-600">Năng lực và kinh nghiệm được chứng thực qua các công trình thực tế</p>
        </div>
      </div>

      <div className="container mx-auto px-4 py-16">
        <div className="lg:flex lg:gap-8">
          {/* Filters Sidebar */}
          <div className="lg:w-1/4 mb-8 lg:mb-0">
            {/* Category Filter */}
            <div className="mb-6">
              <h3 className="text-lg font-semibold text-gray-800 mb-4">Lọc theo danh mục</h3>
              <div className="flex flex-wrap gap-2">
                {categories.map(category => (
                  <button 
                    key={category} 
                    onClick={() => setFilter(category)}
                    className={`px-4 py-2 rounded-full font-semibold text-sm transition-colors duration-300 ${filter === category ? 'bg-blue-600 text-white' : 'bg-gray-200 text-gray-700 hover:bg-blue-200'}`}
                  >
                    {category}
                  </button>
                ))}
              </div>
            </div>

            {/* Region Filter */}
            <div className="mb-6">
              <h3 className="text-lg font-semibold text-gray-800 mb-4">Lọc theo vùng miền</h3>
              <div className="flex flex-wrap gap-2">
                {regions.map(region => (
                  <button
                    key={region}
                    onClick={() => setRegionFilter(region)}
                    className={`px-4 py-2 rounded-full font-semibold text-sm transition-colors duration-300 ${regionFilter === region ? 'bg-green-600 text-white' : 'bg-gray-200 text-gray-700 hover:bg-green-200'}`}
                  >
                    {region}
                  </button>
                ))}
              </div>
            </div>

            {/* Price Filter */}
            <div className="bg-gray-50 p-4 rounded-lg">
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
            </div>
          </div>

          {/* Projects Grid */}
          <div className="lg:w-3/4">
            <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-8">
              {filteredProjects.map(project => (
                <ProjectCard key={project.id} project={project} onClick={openProjectDialog} />
              ))}
            </div>

            {/* Recently Viewed */}
            {recentlyViewed.length > 0 && (
              <div className="mt-16">
                <h2 className="text-2xl font-bold text-gray-800 mb-8 text-center">Đã xem gần đây</h2>
                <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-8">
                  {recentlyViewed.map(project => (
                    <ProjectCard key={`recent-${project.id}`} project={project} onClick={openProjectDialog} />
                  ))}
                </div>
              </div>
            )}
          </div>
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
