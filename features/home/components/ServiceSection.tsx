import React from 'react';
import ServicesRow from './ServiceRow';
import { motion } from 'framer-motion';
import { useTranslation } from 'react-i18next';

const ServiceSection: React.FC = () => {
  const { t } = useTranslation();
  
  return (
    <motion.section 
      className="py-20 md:py-28 bg-gray-50"
      initial={{ opacity: 0, x: 50 }}
      animate={{ opacity: 1, x: 0 }}
      transition={{ duration: 0.8, delay: 0.6 }}
    >
      <div className="container mx-auto px-4">
        {/* Header */}
        <div className="flex flex-col md:flex-row md:items-start md:justify-between gap-8">
          <div className="max-w-3xl">
            <span className="inline-flex items-center rounded-full bg-red-100 text-red-700 text-sm font-semibold px-4 py-2 mb-4">
              {t('home.services.badge')}
            </span>
            <h2 className="text-3xl md:text-5xl font-extrabold leading-tight">
              {t('home.services.title')}
              <br className="hidden md:block" /> {t('home.services.titleLine2')}
            </h2>
          </div>

          <div className="md:max-w-2xl text-gray-600 md:text-lg font-medium leading-relaxed">
            <p>
              {t('home.services.description')}
            </p>
          </div>
        </div>

        {/* Cards row (carousel) */}
        <ServicesRow />
      </div>
    </motion.section>
  );
};

export default ServiceSection;