
import React from 'react';
import { Link } from 'react-router-dom';
import { Project } from '../../../types';

interface ProjectCardProps {
  project: Project;
}

const ProjectCard: React.FC<ProjectCardProps> = ({ project }) => {
  return (
    <div className="bg-white rounded-lg shadow-lg overflow-hidden transform hover:-translate-y-2 transition-transform duration-300 group">
      <Link to={`/du-an/${project.id}`}>
        <div className="relative">
          <img src={project.image} alt={project.name} className="w-full h-56 object-cover" />
          <div className="absolute inset-0 bg-black bg-opacity-20 group-hover:bg-opacity-40 transition-opacity duration-300"></div>
           <div className="absolute bottom-0 left-0 bg-blue-600 text-white px-3 py-1 text-sm font-semibold rounded-tr-lg">
              {project.category}
            </div>
        </div>
        <div className="p-6">
          <h3 className="text-xl font-bold text-gray-800 mb-2 group-hover:text-blue-600 transition-colors">{project.name}</h3>
          <p className="text-gray-600 text-sm line-clamp-3">{project.summary}</p>
        </div>
      </Link>
    </div>
  );
};

export default ProjectCard;
