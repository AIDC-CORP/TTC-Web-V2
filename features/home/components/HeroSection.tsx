import React, { useEffect, useMemo, useState } from 'react';
import { Link } from 'react-router-dom';
import { motion } from 'framer-motion';
import { useTranslation } from 'react-i18next';

const HeroSection: React.FC = () => {
  const { t } = useTranslation();
  const heroImages = useMemo(
    () => [
      'https://onetouchmedia.vn/wp-content/uploads/2019/11/05.jpg',
      'https://www.hancorp.com.vn/wp-content/uploads/2021/09/xay-dung-nha-xuong-1.jpg',
      'https://th.bing.com/th/id/R.e425a6042568905d49d624e2014ee0e1?rik=GJ6X%2fPLxAYh0Pg&riu=http%3a%2f%2fwww.beatexpharm.com.vn%2fstorage%2fuserfiles%2fimages%2fdu-an-cong-ty-cp-duoc-pham-quoc-te-dolexphar-1-1.jpg&ehk=jVEqUMAwJAshsPW4M30g%2bbUyDhcB7KJAXEHxdkwb6Qk%3d&risl=&pid=ImgRaw&r=0',
    ],
    []
  );
  const [currentIndex, setCurrentIndex] = useState(0);

  useEffect(() => {
    const intervalId = window.setInterval(() => {
      setCurrentIndex((prev) => (prev + 1) % heroImages.length);
    }, 5000);
    return () => window.clearInterval(intervalId);
  }, [heroImages.length]);

  return (
    <motion.section 
      className="relative min-h-[100vh] h-[100vh] text-white overflow-hidden"
      initial={{ opacity: 0, y: 50 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.8 }}
    >
      <div className="absolute inset-0">
        {heroImages.map((src, index) => (
          <div
            key={src}
            className={`absolute inset-0 bg-cover bg-center transition-opacity duration-[1200ms] ease-in-out ${index === currentIndex ? 'opacity-100' : 'opacity-0'}`}
            style={{ backgroundImage: `url('${src}')` }}
          />
        ))}
        <div className="absolute inset-0 bg-gradient-to-br from-[#0f172a]/80 via-[#1e3a8a]/60 to-[#1d4ed8]/40"></div>
      </div>
      <div className="relative container mx-auto px-4 h-full flex flex-col justify-center items-start text-left">
        <span className="uppercase tracking-[0.30em] text-blue-180/90 mb-6 text-sm md:text-base">{t('home.hero.badge')}</span>
        <h1 className="text-4xl md:text-6xl lg:text-7xl font-extrabold leading-tight mb-6 max-w-4xl">
          {t('home.hero.title')}
        </h1>
        <p className="text-base md:text-xl max-w-3xl mb-10 text-blue-100">
          {t('home.hero.description')}
        </p>
        <Link
          to="/lien-he"
          className="inline-flex items-center gap-3 bg-red-600 hover:bg-red-700 text-white font-semibold py-3 px-6 rounded-xl text-lg transition duration-300 shadow-sm"
        >
          <span>{t('common.contactConsultation')}</span>
          <span className="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-white">
            <span className="text-blue-600 text-xl leading-none">✓</span>
          </span>
        </Link>
      </div>
    </motion.section>
  );
};

export default HeroSection;