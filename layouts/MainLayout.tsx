
import React from 'react';
import { Outlet } from 'react-router-dom';
import Header from '../features/common/components/Header';
import Footer from '../features/common/components/Footer';

const MainLayout: React.FC = () => {
  return (
    <div className="flex flex-col min-h-screen bg-gray-50 text-gray-800">
      <Header />
      <main className="flex-grow">
        <Outlet />
      </main>
      <Footer />
    </div>
  );
};

export default MainLayout;
