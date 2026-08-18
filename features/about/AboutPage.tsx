
import React from 'react';
import { motion } from 'framer-motion';
import { useTranslation } from 'react-i18next';
import Value from './components/Quotes';
import Cards from './components/Cards';
import Stats from './components/Stats';
import Seo from '../../common/components/Seo';

const AboutPage: React.FC = () => {
  const { t, ready } = useTranslation();
  
  // Show loading state if translations aren't ready
  if (!ready) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-white">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto"></div>
          <p className="mt-4 text-gray-600">Đang tải...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="bg-white">
      <Seo
        title="Giới thiệu"
        description="Tìm hiểu về Tân Thành Công JSC - Đội ngũ chuyên nghiệp với hơn 10 năm kinh nghiệm trong lĩnh vực tư vấn, thiết kế và thi công nhà máy công nghiệp."
        canonical="https://tanthanhcongjsc.com/gioi-thieu"
        image="https://tanthanhcongjsc.com/about.png"
        lang="vi"
      />
      <div className="relative bg-cover bg-center text-white py-24 md:py-40 overflow-hidden" style={{ backgroundImage: `url('/about.png')` }}>
        {/* Overlay for better text readability */}
        <div className="absolute inset-0 bg-black bg-opacity-50"></div>
        
        {/* Decorative background elements */}
        <div className="absolute inset-0 opacity-10">
          <div className="absolute top-10 left-10 w-72 h-72 bg-white rounded-full blur-3xl"></div>
          <div className="absolute bottom-10 right-10 w-96 h-96 bg-blue-300 rounded-full blur-3xl"></div>
        </div>
        
        {/* Content */}
        <motion.div 
          className="container mx-auto px-4 text-center relative z-10"
          initial={{ opacity: 0, y: 50 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, ease: "easeOut" }}
        >
          <motion.div 
            className="inline-block mb-6 px-4 py-2 bg-blue-500 rounded-full text-base font-bold tracking-wide"
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.6, delay: 0.2 }}
          >
            {t('about.hero.tag')}
          </motion.div>
          <motion.h1 
            className="text-5xl md:text-6xl lg:text-7xl font-extrabold mb-6 leading-tight tracking-tight animate-fade-in"
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.4 }}
          >
            {t('about.hero.title')}
          </motion.h1>
          <motion.div 
            className="w-20 h-1 bg-gradient-to-r from-blue-300 to-blue-100 mx-auto mb-6 rounded-full"
            initial={{ scaleX: 0 }}
            animate={{ scaleX: 1 }}
            transition={{ duration: 0.6, delay: 0.8 }}
          />
          <motion.p 
            className="mt-6 text-xl md:text-3xl text-blue-100 max-w-3xl mx-auto font-medium leading-relaxed animate-fade-in-delayed"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 1.0 }}
          >
            {t('about.hero.subtitle')}
          </motion.p>
          <motion.p 
            className="mt-6 text-lg md:text-xl text-blue-200 max-w-2xl mx-auto opacity-90 font-medium leading-relaxed"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 1.2 }}
          >
            {t('about.hero.experience')}
          </motion.p>
        </motion.div>
      </div>

      <div className="container mx-auto px-4 py-16 md:py-24">
        <motion.div 
          className="grid md:grid-cols-2 gap-12 md:gap-16 items-center"
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8 }}
        >
          <motion.div
            initial={{ opacity: 0, x: -50 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.8, delay: 0.2 }}
          >
            <img src="/about1.jpg" alt="Đội ngũ Tân Thành Công" className="rounded-lg shadow-2xl"/>
          </motion.div>
          <motion.div
            initial={{ opacity: 0, x: 50 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.8, delay: 0.4 }}
            className="md:pl-8"
          >
            <h2 className="text-4xl md:text-5xl md:whitespace-nowrap font-bold text-gray-800 mb-6 leading-tight">{t('about.story.title')}</h2>
            <p className="text-gray-700 text-base md:text-lg font-medium leading-relaxed mb-6">
              {t('about.story.paragraph1')}
            </p>
            <p className="text-gray-600 text-base md:text-lg font-medium leading-relaxed">
              {t('about.story.paragraph2')}
            </p>
          </motion.div>
        </motion.div>

        <motion.div
          className="mt-20 md:mt-32"
          initial={{ opacity: 0, y: 50 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8, delay: 0.6 }}
        >
          <Cards />
        </motion.div>

        <motion.div 
          className="mt-20 md:mt-32"
          initial={{ opacity: 0, y: 50 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8, delay: 0.8 }}
        >
          <Stats />
          <Value />
        </motion.div>
      </div>
    </div>
  );
};

export default AboutPage;
