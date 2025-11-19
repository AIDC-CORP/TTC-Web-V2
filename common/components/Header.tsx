
import React, { useEffect, useRef, useState } from 'react';
import { Link, NavLink, useNavigate } from 'react-router-dom';
import { useTranslation } from 'react-i18next';

const NavItem: React.FC<{ to: string; children: React.ReactNode; onClick?: () => void }> = ({ to, children, onClick }) => {
  return (
    <NavLink
      to={to}
      onClick={onClick}
      className={({ isActive }) => {
        const baseClasses = 'py-2.5 px-6 rounded-lg text-lg font-medium transition-all duration-300 relative overflow-hidden group leading-tight';
        if (isActive) {
          return `${baseClasses} text-blue-600 font-semibold bg-blue-50 border-b-2 border-blue-600`;
        }
        return `${baseClasses} text-gray-700 hover:text-blue-600 hover:bg-blue-50/50 before:absolute before:bottom-0 before:left-0 before:w-0 before:h-0.5 before:bg-blue-600 before:transition-all before:duration-300 hover:before:w-full`;
      }}
    >
      <span className="relative z-10">{children}</span>
      {/* Glow effect on hover */}
      <span className="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-300 bg-gradient-to-r from-blue-500/10 via-blue-400/10 to-blue-500/10 blur-xl"></span>
    </NavLink>
  );
};

const Header: React.FC = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');
  const [showHeader, setShowHeader] = useState(true);
  const { t, i18n } = useTranslation();
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
      <div className="hidden md:block bg-blue-900 text-gray-200 text-sm">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8 py-1 flex items-center justify-between">
          <div className="flex flex-wrap items-center gap-4">
            <span className="flex items-center gap-2">
              {/* location */}
              <svg xmlns="http://www.w3.org/2000/svg" className="h-3.5 w-3.5 text-red-500" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 2C8.686 2 6 4.686 6 8c0 4.5 6 12 6 12s6-7.5 6-12c0-3.314-2.686-6-6-6zm0 8.5A2.5 2.5 0 1 1 12 5a2.5 2.5 0 0 1 0 5.5z"/>
              </svg>
              {t('header.address')}
            </span>
            <span className="flex items-center gap-2">
              {/* time */}
              <svg xmlns="http://www.w3.org/2000/svg" className="h-3.5 w-3.5 text-blue-400" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 2a10 10 0 1 0 .001 20.001A10 10 0 0 0 12 2zm.75 5a.75.75 0 0 0-1.5 0v5c0 .199.079.39.22.53l3 3a.75.75 0 1 0 1.06-1.06L12.75 11.5V7z"/>
              </svg>
              {t('header.workingHours')}
            </span>
            <a href="mailto:info@tanthanhcongjsc.com" className="flex items-center gap-2 hover:text-white transition-colors">
              {/* email */}
              <svg xmlns="http://www.w3.org/2000/svg" className="h-3.5 w-3.5 text-amber-400" viewBox="0 0 24 24" fill="currentColor">
                <path d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm0 2v.511l-8 5.333-8-5.333V6h16zM4 18V9.489l7.4 4.933a1 1 0 0 0 1.2 0L20 9.49V18H4z"/>
              </svg>
              info@tanthanhcongjsc.com
            </a>
          </div>

          <div className="flex items-center gap-4">
            <a href="tel:+84976447766" className="flex items-center gap-2 text-white hover:opacity-90 transition-opacity duration-200">
              <span className="inline-flex items-center justify-center h-8 w-8 rounded-full bg-red-500 shadow-sm hover:shadow transition-shadow duration-200">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" className="h-3.5 w-3.5">
                  <path d="M1.5 4.5A3 3 0 014.5 1.5h2.172c.621 0 1.184.363 1.418.936l1.137 2.846a1.5 1.5 0 01-.37 1.648l-1.21 1.21a.75.75 0 00-.154.837c.59 1.331 1.64 2.88 3.168 4.407 1.527 1.528 3.076 2.578 4.407 3.168a.75.75 0 00.837-.154l1.21-1.21a1.5 1.5 0 011.648-.37l2.846 1.137c.573.234.936.797.936 1.418V19.5a3 3 0 01-3 3h-1.5C8.596 22.5 1.5 15.404 1.5 6V4.5z" />
                </svg>
              </span>
              <div className="leading-tight">
                <div className="text-[10px] text-gray-300">{t('header.hotline')}</div>
                <div className="font-semibold text-sm">(+84) 0976 447 766</div>
              </div>
            </a>
            <div className="flex items-center gap-2 text-sm">
              <button onClick={() => i18n.changeLanguage('vi')} className={`px-2 py-1 rounded-md transition-colors ${i18n.language === 'vi' ? 'bg-blue-600 text-white' : 'hover:bg-blue-800'}`}>VI</button>
              <span className="text-gray-500">|</span>
              <button onClick={() => i18n.changeLanguage('en')} className={`px-2 py-1 rounded-md transition-colors ${i18n.language === 'en' ? 'bg-blue-600 text-white' : 'hover:bg-blue-800'}`}>EN</button>
            </div>
          </div>
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
            <NavItem to="/">{t('nav.home')}</NavItem>
            <NavItem to="/gioi-thieu">{t('nav.about')}</NavItem>
            <NavItem to="/du-an">{t('nav.projects')}</NavItem>
            <NavItem to="/tu-van">{t('nav.consulting')}</NavItem>
            <NavItem to="/blog">{t('nav.blog')}</NavItem>
            <NavItem to="/lien-he">{t('nav.contact')}</NavItem>
          </nav>
          
          <div className="hidden lg:block">
            <form onSubmit={handleSearch} className="relative">
              <input
                type="text"
                placeholder={t('header.searchPlaceholder')}
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="w-48 pl-3 pr-10 py-2 border border-gray-300 rounded-full focus:outline-none focus:ring-1 focus:ring-blue-500 focus:border-blue-500 transition-all text-sm shadow-sm"
              />
              <button 
                type="submit" 
                className="absolute right-1 top-1/2 -translate-y-1/2 w-7 h-7 bg-blue-600 text-white rounded-full flex items-center justify-center hover:bg-blue-700 transition-colors duration-200"
              >
                <svg xmlns="http://www.w3.org/2000/svg" className="h-3.5 w-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg>
              </button>
            </form>
          </div>

          {/* Mobile Menu Button */}
          <div className="lg:hidden">
            <button
              onClick={() => setIsMenuOpen(!isMenuOpen)}
              className="w-10 h-10 bg-gradient-to-r from-blue-600 to-blue-700 text-white rounded-lg flex items-center justify-center hover:from-blue-700 hover:to-blue-800 shadow-md hover:shadow-lg transition-all duration-300 transform hover:scale-105 active:scale-95 focus:outline-none relative group"
            >
              <svg 
                xmlns="http://www.w3.org/2000/svg" 
                className={`h-6 w-6 transition-all duration-300 ${isMenuOpen ? 'rotate-90' : ''}`} 
                fill="none" 
                viewBox="0 0 24 24" 
                stroke="currentColor" 
                strokeWidth={2.5}
              >
                {isMenuOpen ? (
                  <path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" />
                ) : (
                  <path strokeLinecap="round" strokeLinejoin="round" d="M4 6h16M4 12h16m-7 6h7" />
                )}
              </svg>
              {/* Ripple effect */}
              <span className="absolute inset-0 rounded-lg bg-white opacity-0 group-active:opacity-20 group-active:animate-ping"></span>
            </button>
          </div>
        </div>
        </div>
      </div>
      
      {/* Mobile Menu */}
      <div className={`lg:hidden bg-white border-t border-gray-300 relative z-50 ${isMenuOpen ? 'block' : 'hidden'}`}>
        <nav className="container mx-auto px-4 py-4 flex flex-col gap-4">
          <NavItem to="/" onClick={() => setIsMenuOpen(false)}>{t('nav.home')}</NavItem>
          <NavItem to="/gioi-thieu" onClick={() => setIsMenuOpen(false)}>{t('nav.about')}</NavItem>
          <NavItem to="/du-an" onClick={() => setIsMenuOpen(false)}>{t('nav.projects')}</NavItem>
          <NavItem to="/tu-van" onClick={() => setIsMenuOpen(false)}>{t('nav.consulting')}</NavItem>
          <NavItem to="/blog" onClick={() => setIsMenuOpen(false)}>{t('nav.blog')}</NavItem>
          <NavItem to="/lien-he" onClick={() => setIsMenuOpen(false)}>{t('nav.contact')}</NavItem>
          <form onSubmit={(e) => { handleSearch(e); setIsMenuOpen(false); }} className="w-full mt-2 relative">
            <input
              type="text"
              placeholder={t('header.searchPlaceholder')}
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="w-full pl-3 pr-10 py-2 border border-gray-300 rounded-full focus:outline-none focus:ring-1 focus:ring-blue-500 focus:border-blue-500 transition-all text-sm shadow-sm"
            />
            <button 
              type="submit" 
              className="absolute right-1 top-1/2 -translate-y-1/2 w-7 h-7 bg-blue-600 text-white rounded-full flex items-center justify-center hover:bg-blue-700 transition-colors duration-200"
            >
              <svg xmlns="http://www.w3.org/2000/svg" className="h-3.5 w-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg>
            </button>
          </form>
        </nav>
      </div>
    </header>
  );
};

export default Header;
