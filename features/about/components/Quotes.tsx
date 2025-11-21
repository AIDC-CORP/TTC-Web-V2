import React from 'react';
import { motion } from 'framer-motion';
import { useTranslation } from 'react-i18next';

const Value: React.FC = () => {
  const { t, ready } = useTranslation();
  
  // Ensure translations are loaded before accessing
  if (!ready) {
    return null;
  }

  let values: { label: string; title: string; description: string }[] = [];
  try {
    const quotesData = t('about.quotes', { returnObjects: true });
    values = Array.isArray(quotesData) ? quotesData : [];
  } catch (error) {
    console.error('Error loading quotes translations:', error);
    values = [];
  }

  const quoteVariants = {
    hidden: { opacity: 0, y: 50, scale: 0.9 },
    visible: { opacity: 1, y: 0, scale: 1 }
  };

  return (
    <motion.div 
      className="grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-10"
      initial="hidden"
      whileInView="visible"
      viewport={{ once: true }}
      transition={{ staggerChildren: 0.15, delayChildren: 0.2 }}
    >
      {values.map((value, index) => (
        <motion.div
          key={index}
          className="relative bg-gradient-to-br from-blue-500 to-blue-600 rounded-3xl p-6 md:p-8 shadow-xl overflow-hidden group hover:shadow-2xl transition-shadow duration-300"
          variants={quoteVariants}
          transition={{ duration: 0.6 }}
          whileHover={{ 
            scale: 1.02, 
            transition: { duration: 0.3 }
          }}
        >
          {/* Decorative corner circle */}
          <div className="absolute -top-16 -right-16 w-40 h-40 bg-blue-400 rounded-full opacity-20 group-hover:opacity-30 transition-opacity"></div>

          {/* Quote mark icon */}
          <div className="text-4xl md:text-5xl text-white opacity-30 mb-3">‟</div>

          {/* Label badge */}
          <div className="inline-block mb-3 px-4 py-1.5 bg-white rounded-full">
            <span className="text-sm md:text-base font-bold text-blue-600">{value.label}</span>
          </div>

          {/* Content */}
          <h3 className="text-3xl md:text-4xl font-bold text-white mb-3 leading-tight relative z-10">
            {value.title}
          </h3>
          <p className="text-white text-base md:text-lg font-medium leading-relaxed relative z-10">
            {value.description}
          </p>

          {/* Closing quote mark */}
          <div className="absolute bottom-3 right-4 text-4xl md:text-5xl text-white opacity-20">‟</div>
        </motion.div>
      ))}
    </motion.div>
  );
};

export default Value;
