
import React, { useState } from 'react';
import { Link, NavLink, useNavigate } from 'react-router-dom';

const NavItem: React.FC<{ to: string; children: React.ReactNode; onClick?: () => void }> = ({ to, children, onClick }) => {
  const activeClasses = 'text-blue-600 font-semibold';
  const inactiveClasses = 'text-gray-600 hover:text-blue-600 transition-colors';
  return (
    <NavLink
      to={to}
      onClick={onClick}
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
          <nav className="hidden lg:flex items-center space-x-2">
            <NavItem to="/">Trang chủ</NavItem>
            <NavItem to="/gioi-thieu">Giới thiệu</NavItem>
            <NavItem to="/du-an">Dự án</NavItem>
            <NavItem to="/tu-van">Tư vấn</NavItem>
            <NavItem to="/blog">Blog</NavItem>
            <NavItem to="/lien-he">Liên hệ</NavItem>
          </nav>
          
          <div className="hidden lg:block">
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
          <div className="lg:hidden">
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
      
      {/* Overlay */}
      {isMenuOpen && (
        <div
          className="fixed inset-0 bg-black bg-opacity-50 z-40 lg:hidden"
          onClick={() => setIsMenuOpen(false)}
        ></div>
      )}

      {/* Sidebar */}
      <div
        className={`fixed top-0 right-0 h-screen w-64 bg-white shadow-lg z-50 transform transition-transform duration-300 ease-in-out lg:hidden ${
          isMenuOpen ? 'translate-x-0' : 'translate-x-full'
        }`}
      >
        <div className="flex justify-between items-center p-4 border-b">
          <h2 className="text-lg font-semibold">Menu</h2>
          <button
            onClick={() => setIsMenuOpen(false)}
            className="text-gray-600 hover:text-blue-600 focus:outline-none"
          >
            <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        <nav className="flex flex-col space-y-4 px-6 py-8 overflow-y-auto h-full">
          <NavItem to="/" onClick={() => setIsMenuOpen(false)}>Trang chủ</NavItem>
          <NavItem to="/gioi-thieu" onClick={() => setIsMenuOpen(false)}>Giới thiệu</NavItem>
          <NavItem to="/du-an" onClick={() => setIsMenuOpen(false)}>Dự án</NavItem>
          <NavItem to="/tu-van" onClick={() => setIsMenuOpen(false)}>Tư vấn</NavItem>
          <NavItem to="/blog" onClick={() => setIsMenuOpen(false)}>Blog</NavItem>
          <NavItem to="/lien-he" onClick={() => setIsMenuOpen(false)}>Liên hệ</NavItem>
          <form onSubmit={(e) => { handleSearch(e); setIsMenuOpen(false); }} className="w-full mt-4">
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
    </header>
  );
};

export default Header;
