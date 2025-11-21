
import React from 'react';
import { HashRouter, Routes, Route } from 'react-router-dom';
import MainLayout from './common/components/MainLayout';
import ErrorBoundary from './common/components/ErrorBoundary';
import HomePage from './features/home/HomePage';
import AboutPage from './features/about/AboutPage';
import ProjectsPage from './features/projects/ProjectsPage';
import ConsultingPage from './features/consulting/ConsultingPage';
import BlogPage from './features/blog/BlogPage';
import ContactPage from './features/contact/ContactPage';
import SearchResultsPage from './features/search/SearchResultsPage';

const App: React.FC = () => {
  return (
    <ErrorBoundary>
      <HashRouter>
        <Routes>
          <Route path="/" element={<MainLayout />}>
            <Route index element={<HomePage />} />
            <Route path="/gioi-thieu" element={<AboutPage />} />
            <Route path="/du-an" element={<ProjectsPage />} />
            <Route path="/tu-van" element={<ConsultingPage />} />
            <Route path="/blog" element={<BlogPage />} />
            <Route path="/lien-he" element={<ContactPage />} />
            <Route path="/tim-kiem" element={<SearchResultsPage />} />
          </Route>
        </Routes>
      </HashRouter>
    </ErrorBoundary>
  );
};

export default App;
