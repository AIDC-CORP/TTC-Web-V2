
import React, { useEffect } from 'react';
import { Outlet, useLocation } from 'react-router-dom';
import Header from './Header';
import Footer from './Footer';
import FloatingButtons from './FloatingButtons';

const MainLayout: React.FC = () => {
  const location = useLocation();
  
  useEffect(() => {
    // Scroll to top when route changes
    window.scrollTo(0, 0);
  }, [location.pathname]);
  
  return (
    <div className="flex flex-col min-h-screen bg-gray-50 text-gray-800">
      <Header />
      <main className="flex-grow">
        <Outlet key={location.pathname} />
      </main>
      <Footer />
      <FloatingButtons />
    </div>
  );
};

export default MainLayout;
