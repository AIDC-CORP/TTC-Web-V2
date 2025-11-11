
import React, { useState, useMemo } from 'react';
import { projects } from '../../data/mockData';
import ProjectCard from './components/ProjectCard';

const ProjectsPage: React.FC = () => {
  const [filter, setFilter] = useState('Tất cả');
  
  const categories = useMemo(() => ['Tất cả', ...Array.from(new Set(projects.map(p => p.category)))], []);

  const filteredProjects = useMemo(() => {
    if (filter === 'Tất cả') {
      return projects;
    }
    return projects.filter(project => project.category === filter);
  }, [filter]);

  return (
    <div>
      <div className="bg-white py-20">
        <div className="container mx-auto px-4 text-center">
          <h1 className="text-4xl md:text-5xl font-extrabold text-gray-800">Dự án của chúng tôi</h1>
          <p className="mt-4 text-lg text-gray-600">Năng lực và kinh nghiệm được chứng thực qua các công trình thực tế</p>
        </div>
      </div>

      <div className="container mx-auto px-4 py-16">
        <div className="flex justify-center mb-12 flex-wrap gap-2">
            {categories.map(category => (
                 <button 
                    key={category} 
                    onClick={() => setFilter(category)}
                    className={`px-6 py-2 rounded-full font-semibold transition-colors duration-300 ${filter === category ? 'bg-blue-600 text-white' : 'bg-gray-200 text-gray-700 hover:bg-blue-200'}`}
                >
                    {category}
                 </button>
            ))}
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {filteredProjects.map(project => (
            <ProjectCard key={project.id} project={project} />
          ))}
        </div>
      </div>
    </div>
  );
};

export default ProjectsPage;
