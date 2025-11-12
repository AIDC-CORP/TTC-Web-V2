import React from 'react';
import { Link } from 'react-router-dom';
import ProjectCard from '../projects/components/ProjectCard';
import HeroSection from './components/HeroSection';
import ServicesRow from './components/ServiceRow';
import IntroSection from './components/IntroSection';
import FeaturedProjectsSection from './components/FeaturedProjectsSection';
import ServiceSection from './components/ServiceSection';
import LatestBlogsSection from './components/LatestBlogsSection';
import CalloutSection from './components/CalloutSection';
import Criteria from './components/CriteriaSection';
import PartnersSection from './components/PartnersSection';

const HomePage: React.FC = () => {
  return (
    <div>
      <HeroSection />

      <IntroSection />

      <FeaturedProjectsSection />

      <ServiceSection />

      <LatestBlogsSection />

      <PartnersSection />

      <CalloutSection />

      <Criteria />
    </div>
  );
};

export default HomePage;
