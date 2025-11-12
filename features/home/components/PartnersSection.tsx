import React from 'react';
import { motion } from 'framer-motion';

const PartnersSection: React.FC = () => {
  const partners = [
    { name: 'Alo', logo: '/alo-logo.png' },
    { name: 'Diều Phương', logo: '/dieuphuong-logo.png' },
    { name: 'Food', logo: '/Food-logo.png' },
    { name: 'AIDC', logo: '/aidc_logo.png' },
    { name: 'Par5', logo: '/par5.png' },
    { name: 'Y2Y', logo: '/y2y.png' },
  ];

  return (
    <motion.section 
      className="py-20 md:py-28 bg-white overflow-hidden"
      initial={{ opacity: 0, y: 50 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.8, delay: 0.2 }}
    >
      <div className="container mx-auto px-4">
        {/* Header */}
        <div className="text-center mb-16">
          <span className="inline-flex items-center rounded-full bg-red-100 text-red-700 text-sm font-semibold px-4 py-2 mb-4">
            ĐỐI TÁC CỦA CHÚNG TÔI
          </span>
          <h2 className="text-3xl md:text-5xl font-extrabold leading-tight">
            Các đối tác chiến lược
          </h2>
          <p className="mt-4 text-gray-600 max-w-2xl mx-auto">
            Chúng tôi tự hào hợp tác với những thương hiệu hàng đầu trong ngành
          </p>
        </div>

        {/* Logo Carousel */}
        <div className="relative">
          {/* Scrolling Logo Strip */}
          <motion.div
            className="flex gap-12 items-center"
            animate={{
              x: ['0%', '-50%'],
            }}
            transition={{
              duration: 20,
              repeat: Infinity,
              ease: 'linear',
            }}
          >
            {/* Double the logos for seamless loop */}
            {[...partners, ...partners].map((partner, index) => (
              <div
                key={`${partner.name}-${index}`}
                className="flex-shrink-0 w-48 h-32 bg-gray-100 rounded-lg flex items-center justify-center p-4 hover:grayscale-0 transition-all duration-300"
              >
                <img
                  src={partner.logo}
                  alt={partner.name}
                  className="w-full h-full object-contain"
                />
              </div>
            ))}
          </motion.div>
        </div>
      </div>
    </motion.section>
  );
};

export default PartnersSection;
