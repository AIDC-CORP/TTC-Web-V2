import React from 'react';
import { Link } from 'react-router-dom';
import { projects } from '../../../data/mockData';
import ProjectCard from '../../projects/components/ProjectCard';

const FeaturedProjectsSection: React.FC = () => {
  const featuredProjects = projects.slice(0, 3);

  return (
    <section className="py-16 md:py-24 bg-white">
      <div className="container mx-auto px-4">
        <h2 className="text-3xl md:text-4xl font-bold text-center mb-4">Dự án Tiêu biểu</h2>
        <p className="text-center text-gray-600 max-w-2xl mx-auto mb-12">Chúng tôi tự hào đã góp phần vào thành công của nhiều dự án lớn, khẳng định năng lực và uy tín.</p>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {featuredProjects.map(project => (
            <ProjectCard key={project.id} project={project} />
          ))}
        </div>
        <div className="text-center mt-12">
           <Link to="/du-an" className="text-blue-600 font-semibold hover:underline">
             Xem tất cả dự án &rarr;
           </Link>
        </div>
      </div>
    </section>
  );
};

export default FeaturedProjectsSection;