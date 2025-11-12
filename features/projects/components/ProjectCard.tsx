
import React from 'react';
import { Link } from 'react-router-dom';
import { motion } from 'framer-motion';
import { Project } from '../../../types';

interface ProjectCardProps {
  project: Project;
  onClick?: (project: Project) => void;
}

const ProjectCard: React.FC<ProjectCardProps> = ({ project, onClick }) => {
  const handleClick = () => {
    if (onClick) {
      onClick(project);
    }
  };

  const CardContent = () => (
    <motion.div 
      style={{ height: '400px' }}
      className="bg-white rounded-lg shadow-lg overflow-hidden transform hover:-translate-y-2 transition-transform duration-300 group cursor-pointer flex flex-col"
      whileHover={{ 
        y: -8, 
        transition: { duration: 0.3, ease: "easeOut" }
      }}
      whileTap={{ scale: 0.98 }}
    >
      <div className="relative">
        <motion.img 
          src={project.image} 
          alt={project.name} 
          className="w-full h-56 object-cover" 
          whileHover={{ scale: 1.05 }}
          transition={{ duration: 0.3 }}
        />
        <motion.div 
          className="absolute inset-0 bg-black bg-opacity-20 group-hover:bg-opacity-40 transition-opacity duration-300"
          whileHover={{ opacity: 0.6 }}
        ></motion.div>
         <div 
           className="absolute bottom-0 left-0 bg-blue-600 text-white px-3 py-1 text-sm font-semibold rounded-tr-lg"
         >
            {project.category}
          </div>
      </div>
      <div 
        className="p-6 flex-1 flex flex-col"
      >
        <h3 
          className="text-xl font-bold text-gray-800 mb-2 group-hover:text-blue-600 transition-colors"
        >
          {project.name}
        </h3>
        <p 
          className="text-gray-600 text-sm line-clamp-3 flex-1"
        >
          {project.summary}
        </p>
      </div>
    </motion.div>
  );

  if (onClick) {
    return (
      <div onClick={handleClick}>
        <CardContent />
      </div>
    );
  }

  return (
    <Link to={`/du-an/${project.id}`}>
      <CardContent />
    </Link>
  );
};

export default ProjectCard;
