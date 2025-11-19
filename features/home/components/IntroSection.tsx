import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { motion } from 'framer-motion';
import { useTranslation } from 'react-i18next';

const IntroSection: React.FC = () => {
  const { t } = useTranslation();
  const [count, setCount] = useState(0);

  useEffect(() => {
    const timer = setInterval(() => {
      setCount(prev => prev < 10 ? prev + 1 : 10);
    }, 100);
    return () => clearInterval(timer);
  }, []);

  return (
    <motion.section 
      className="py-16 md:py-24 bg-white"
      initial={{ opacity: 0, x: -50 }}
      animate={{ opacity: 1, x: 0 }}
      transition={{ duration: 0.8, delay: 0.2 }}
    >
      <div className="container mx-auto px-4 grid grid-cols-1 md:grid-cols-2 gap-10 md:gap-14 items-center">
        {/* Visual side */}
        <div className="relative pl-14 md:pl-24">
          {/* Vertical badge */}
          <div className="hidden sm:flex flex-col items-center absolute top-1/2 -translate-y-1/2 -left-2 md:-left-6">
            <div
              className="text-gray-800 font-bold tracking-wider bg-white rounded-full shadow px-3 py-2 text-sm"
              style={{ writingMode: 'vertical-rl', transform: 'rotate(180deg)' }}
            >
              {t('intro.experienceBadge')}
            </div>
            <div className="text-red-600 font-extrabold text-6xl md:text-7xl mt-4 leading-none">{count}+</div>
          </div>

          {/* Overlapped images */}
          <div className="relative">
            <img
              src="introsection2.jpg"
              alt="Nhà xưởng công nghiệp"
              className="w-full h-72 sm:h-96 object-cover rounded-3xl shadow-md"
            />
            <img
              src="introsection1.jpg"
              alt="Kỹ sư công trường"
              className="absolute -top-8 -left-8 w-44 h-32 sm:w-64 sm:h-44 object-cover rounded-3xl shadow-lg border-8 border-white"
            />
          </div>
        </div>

        {/* Content side */}
        <div>
          <span className="inline-block text-sm md:text-base font-bold tracking-widest uppercase bg-red-100 text-red-700 px-4 py-2 rounded-full mb-5">
            {t('intro.tag')}
          </span>
          <h2 className="text-3xl md:text-5xl font-extrabold leading-tight mb-5">
            {t('intro.title')}
          </h2>
          <p className="text-gray-700 mb-8 text-base md:text-lg font-medium leading-relaxed">
            {t('intro.description')}
          </p>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
            <div className="flex items-start gap-3">
              <span className="mt-1 inline-flex h-6 w-6 items-center justify-center rounded-full bg-red-100 text-red-600">✓</span>
              <div>
                <div className="font-bold text-gray-900 text-base md:text-lg">{t('intro.feature1.title')}</div>
                <p className="text-gray-600 text-base leading-relaxed">
                  {t('intro.feature1.description')}
                </p>
              </div>
            </div>
            <div className="flex items-start gap-3">
              <span className="mt-1 inline-flex h-6 w-6 items-center justify-center rounded-full bg-red-100 text-red-600">✓</span>
              <div>
                <div className="font-bold text-gray-900 text-base md:text-lg">{t('intro.feature2.title')}</div>
                <p className="text-gray-600 text-base leading-relaxed">
                  {t('intro.feature2.description')}
                </p>
              </div>
            </div>
            <div className="flex items-start gap-3 sm:col-span-2">
              <span className="mt-1 inline-flex h-6 w-6 items-center justify-center rounded-full bg-red-100 text-red-600">✓</span>
              <div>
                <div className="font-bold text-gray-900 text-base md:text-lg">{t('intro.feature3.title')}</div>
                <p className="text-gray-600 text-base leading-relaxed">
                  {t('intro.feature3.description')}
                </p>
              </div>
            </div>
          </div>

          <div className="mt-8 flex items-center gap-4">
            <Link
              to="/lien-he"
              className="inline-flex items-center gap-2 bg-red-600 hover:bg-red-700 text-white font-semibold py-3 px-6 rounded-xl transition duration-300 shadow-sm"
            >
              <span>{t('intro.ctaButton')}</span>
            </Link>
            <a
              href="tel:0976447766"
              className="inline-flex items-center gap-3 text-blue-700 font-bold text-base md:text-lg"
            >
              <span className="inline-flex items-center justify-center w-10 h-10 rounded-full bg-blue-100">☎</span>
              <span>(+84) 0976-447-766</span>
            </a>
          </div>
        </div>
      </div>
    </motion.section>
  );
};

export default IntroSection;