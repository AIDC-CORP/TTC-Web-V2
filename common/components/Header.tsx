
import React, { useEffect, useRef, useState } from 'react';
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
  const [showHeader, setShowHeader] = useState(true);
  const lastScrollYRef = useRef(0);
  const navigate = useNavigate();

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    if (searchQuery.trim()) {
      navigate(`/tim-kiem?q=${encodeURIComponent(searchQuery.trim())}`);
      setSearchQuery('');
      setIsMenuOpen(false);
    }
  };

  useEffect(() => {
    const handleScroll = () => {
      const currentY = window.scrollY || 0;
      const lastY = lastScrollYRef.current;

      if (currentY < 10) {
        setShowHeader(true);
      } else if (currentY > lastY && currentY > 120) {
        // scrolling down and beyond threshold -> hide
        setShowHeader(false);
      } else if (currentY < lastY) {
        // scrolling up -> show
        setShowHeader(true);
      }

      lastScrollYRef.current = currentY;
    };

    window.addEventListener('scroll', handleScroll, { passive: true });
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <header className={`sticky top-0 z-50 transition-transform duration-300 ${showHeader ? 'translate-y-0' : '-translate-y-full'}`}>
      {/* Top contact bar */}
      <div className="hidden md:block bg-gray-900 text-gray-200 text-xs">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8 py-1 flex items-center justify-between">
          <div className="flex flex-wrap items-center gap-4">
            <span className="flex items-center gap-2">
              {/* location */}
              <svg xmlns="http://www.w3.org/2000/svg" className="h-3.5 w-3.5 text-red-500" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 2C8.686 2 6 4.686 6 8c0 4.5 6 12 6 12s6-7.5 6-12c0-3.314-2.686-6-6-6zm0 8.5A2.5 2.5 0 1 1 12 5a2.5 2.5 0 0 1 0 5.5z"/>
              </svg>
              Số 19N7B, KĐT Trung Hòa Nhân Chính, Quận Thanh Xuân, TP Hà Nội
            </span>
            <span className="flex items-center gap-2">
              {/* time */}
              <svg xmlns="http://www.w3.org/2000/svg" className="h-3.5 w-3.5 text-blue-400" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 2a10 10 0 1 0 .001 20.001A10 10 0 0 0 12 2zm.75 5a.75.75 0 0 0-1.5 0v5c0 .199.079.39.22.53l3 3a.75.75 0 1 0 1.06-1.06L12.75 11.5V7z"/>
              </svg>
              Giờ làm việc: 08:00 – 17:30
            </span>
            <a href="mailto:info@tanthanhcongjsc.com" className="flex items-center gap-2 hover:text-white transition-colors">
              {/* email */}
              <svg xmlns="http://www.w3.org/2000/svg" className="h-3.5 w-3.5 text-amber-400" viewBox="0 0 24 24" fill="currentColor">
                <path d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm0 2v.511l-8 5.333-8-5.333V6h16zM4 18V9.489l7.4 4.933a1 1 0 0 0 1.2 0L20 9.49V18H4z"/>
              </svg>
              info@tanthanhcongjsc.com
            </a>
          </div>
          <a href="tel:+84976447766" className="flex items-center gap-2.5 text-white">
            <span className="inline-flex items-center justify-center h-10 w-10 rounded-full bg-red-500">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="h-3.5 w-3.5">
                <path d="M1.5 4.5A3 3 0 014.5 1.5h2.172c.621 0 1.184.363 1.418.936l1.137 2.846a1.5 1.5 0 01-.37 1.648l-1.21 1.21a.75.75 0 00-.154.837c.59 1.331 1.64 2.88 3.168 4.407 1.527 1.528 3.076 2.578 4.407 3.168a.75.75 0 00.837-.154l1.21-1.21a1.5 1.5 0 011.648-.37l2.846 1.137c.573.234.936.797.936 1.418V19.5a3 3 0 01-3 3h-1.5C8.596 22.5 1.5 15.404 1.5 6V4.5z" />
              </svg>
            </span>
            <div className="leading-tight">
              <div className="text-[11px] text-gray-300">Hotline</div>
              <div className="font-semibold text-sm">(+84) 0976 447 766</div>
            </div>
          </a>
        </div>
      </div>

      {/* Main header */}
      <div className="bg-white/80 backdrop-blur-lg shadow-md">
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
      </div>
      
      {/* Mobile Menu */}
      <div className={`lg:hidden bg-white border-t border-gray-200 relative z-50 ${isMenuOpen ? 'block' : 'hidden'}`}>
        <nav className="container mx-auto px-4 py-4 flex flex-col gap-4">
          <NavItem to="/" onClick={() => setIsMenuOpen(false)}>Trang chủ</NavItem>
          <NavItem to="/gioi-thieu" onClick={() => setIsMenuOpen(false)}>Giới thiệu</NavItem>
          <NavItem to="/du-an" onClick={() => setIsMenuOpen(false)}>Dự án</NavItem>
          <NavItem to="/tu-van" onClick={() => setIsMenuOpen(false)}>Tư vấn</NavItem>
          <NavItem to="/blog" onClick={() => setIsMenuOpen(false)}>Blog</NavItem>
          <NavItem to="/lien-he" onClick={() => setIsMenuOpen(false)}>Liên hệ</NavItem>
          <form onSubmit={(e) => { handleSearch(e); setIsMenuOpen(false); }} className="w-full mt-2">
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
