
import React, { useState } from 'react';
import { Link, NavLink, useNavigate } from 'react-router-dom';

const NavItem: React.FC<{ to: string; children: React.ReactNode }> = ({ to, children }) => {
  const activeClasses = 'text-blue-600 font-semibold';
  const inactiveClasses = 'text-gray-600 hover:text-blue-600 transition-colors';
  return (
    <NavLink
      to={to}
      className={({ isActive }) => `${isActive ? activeClasses : inactiveClasses} py-2 px-3 rounded-md`}
    >
      {children}
    </NavLink>
  );
};

const Header: React.FC = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');
  const navigate = useNavigate();

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    if (searchQuery.trim()) {
      navigate(`/tim-kiem?q=${encodeURIComponent(searchQuery.trim())}`);
      setSearchQuery('');
      setIsMenuOpen(false);
    }
  };

  return (
    <header className="bg-white/80 backdrop-blur-lg shadow-md sticky top-0 z-50">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-20">
          <div className="flex-shrink-0">
            <Link to="/" className="flex items-center">
              <img 
                src="/logo-ttc-removebg-DNXrVdJp.png" 
                alt="Tân Thành Công JSC" 
                className="h-12 w-auto"
              />
            </Link>
          </div>

          {/* Desktop Navigation */}
          <nav className="hidden md:flex items-center space-x-2">
            <NavItem to="/">Trang chủ</NavItem>
            <NavItem to="/gioi-thieu">Giới thiệu</NavItem>
            <NavItem to="/du-an">Dự án</NavItem>
            <NavItem to="/tu-van">Tư vấn</NavItem>
            <NavItem to="/blog">Blog</NavItem>
            <NavItem to="/lien-he">Liên hệ</NavItem>
          </nav>
          
          <div className="hidden md:block">
            <form onSubmit={handleSearch} className="relative">
              <input
                type="text"
                placeholder="Tìm kiếm..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="w-48 pl-4 pr-10 py-2 border rounded-full focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all"
              />
              <button type="submit" className="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 hover:text-blue-600">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg>
              </button>
            </form>
          </div>

          {/* Mobile Menu Button */}
          <div className="md:hidden">
            <button
              onClick={() => setIsMenuOpen(!isMenuOpen)}
              className="text-gray-600 hover:text-blue-600 focus:outline-none"
            >
              <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                {isMenuOpen ? (
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                ) : (
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16m-7 6h7" />
                )}
              </svg>
            </button>
          </div>
        </div>
      </div>
      
      {/* Mobile Menu */}
      {isMenuOpen && (
        <div className="md:hidden bg-white pb-4">
          <nav className="flex flex-col items-center space-y-2 px-4">
            <NavItem to="/">Trang chủ</NavItem>
            <NavItem to="/gioi-thieu">Giới thiệu</NavItem>
            <NavItem to="/du-an">Dự án</NavItem>
            <NavItem to="/tu-van">Tư vấn</NavItem>
            <NavItem to="/blog">Blog</NavItem>
            <NavItem to="/lien-he">Liên hệ</NavItem>
            <form onSubmit={handleSearch} className="w-full mt-4">
              <input
                type="text"
                placeholder="Tìm kiếm..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="w-full px-4 py-2 border rounded-full focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </form>
          </nav>
        </div>
      )}
    </header>
  );
};

export default Header;
