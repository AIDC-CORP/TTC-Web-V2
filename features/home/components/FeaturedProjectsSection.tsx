import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import projectsData from '../../projects/data/projects.json';
import ProjectCard from '../../projects/components/ProjectCard';
import ProjectDetailDialog from '../../projects/components/dialogs/ProjectDetailDialog';
import { motion } from 'framer-motion';
import { Project } from '../../../types';
import { useTranslation } from 'react-i18next';

const FeaturedProjectsSection: React.FC = () => {
  const { t } = useTranslation();
  const [selectedProject, setSelectedProject] = useState<Project | null>(null);
  const [isDialogOpen, setIsDialogOpen] = useState(false);

  const featuredProjects = projectsData.slice(0, 3).map(project => ({
    id: project.name.toLowerCase().replace(/\s+/g, '-').replace(/[^a-z0-9-]/g, ''),
    name: project.name,
    image: project.thumbnail_url || 'https://picsum.photos/400/300?random=1',
    summary: `${project.location_specific} - ${project.square}`,
    description: `Dự án tại ${project.location_specific}, diện tích ${project.square}, năm ${project.year}. Quản lý dự án: ${project.project_manager}`,
    investor: project.project_manager,
    executionTime: project.year,
    gallery: project.gallery_urls,
    category: t('home.projects.category'),
    location_specific: project.location_specific,
    square: project.square,
    project_manager: project.project_manager,
    year: project.year
  }));

  const handleProjectClick = (project: Project) => {
    setSelectedProject(project);
    setIsDialogOpen(true);
  };

  const handleCloseDialog = () => {
    setIsDialogOpen(false);
    setSelectedProject(null);
  };

  return (
    <>
      <motion.section 
        className="py-16 md:py-24 bg-white"
        initial={{ opacity: 0, y: 50 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8, delay: 0.4 }}
      >
        <div className="container mx-auto px-4">
          <h2 className="text-3xl md:text-4xl font-bold text-center mb-4">{t('home.projects.title')}</h2>
          <p className="text-center text-gray-600 max-w-3xl mx-auto mb-12 text-base md:text-lg font-medium leading-relaxed">{t('home.projects.description')}</p>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {featuredProjects.map(project => (
              <ProjectCard key={project.id} project={project} onClick={handleProjectClick} />
            ))}
          </div>
          <div className="text-center mt-12">
             <Link to="/du-an" className="text-blue-600 font-semibold hover:underline">
               {t('home.projects.viewAll')}
             </Link>
          </div>
          </div>
        </motion.section>
      <ProjectDetailDialog 
        project={selectedProject} 
        isOpen={isDialogOpen} 
        onClose={handleCloseDialog} 
      />
    </>
  );
};

export default FeaturedProjectsSection;