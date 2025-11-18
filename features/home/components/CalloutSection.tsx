import React from 'react';
import { motion } from 'framer-motion';
import { useTranslation } from 'react-i18next';

const CalloutSection: React.FC = () => {
  const { t } = useTranslation();
  
  return (
    <motion.section 
      className="py-12 md:py-16 bg-white"
      initial={{ opacity: 0, scale: 0.9 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ duration: 0.8, delay: 0.8 }}
    >
      <div className="container mx-auto px-4">
        <div className="rounded-2xl bg-gradient-to-r from-blue-600 to-indigo-600 text-white p-8 md:p-10 flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
          <div>
            <h3 className="text-2xl md:text-3xl font-bold mb-2">{t('home.callout.title')}</h3>
            <p className="text-blue-50">{t('home.callout.description')}</p>
          </div>
          <div className="flex flex-wrap gap-3">
            <a href="https://zalo.me/" target="_blank" rel="noreferrer" className="bg-white text-blue-700 font-semibold py-2.5 px-5 rounded-full transition hover:bg-blue-50">{t('common.chatZalo')}</a>
            <a href="https://m.me/" target="_blank" rel="noreferrer" className="bg-white/10 text-white font-semibold py-2.5 px-5 rounded-full transition hover:bg-white/20">{t('common.chatMessenger')}</a>
            <a href="tel:0976447766" className="bg-white/10 text-white font-semibold py-2.5 px-5 rounded-full transition hover:bg-white/20">{t('home.callout.call')}</a>
          </div>
        </div>
      </div>
    </motion.section>
  );
};

export default CalloutSection;