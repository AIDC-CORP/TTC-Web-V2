import React, { useEffect, useState } from 'react';
import { motion, useAnimation } from 'framer-motion';

interface AnimatedCounterProps {
  value: number;
  suffix?: string;
  duration?: number;
}

const AnimatedCounter: React.FC<AnimatedCounterProps> = ({
  value,
  suffix = '',
  duration = 2000
}) => {
  const [count, setCount] = useState(0);
  const controls = useAnimation();

  useEffect(() => {
    const startAnimation = async () => {
      await controls.start({
        count: value,
        transition: {
          duration: duration / 1000,
          ease: "easeOut"
        }
      });
    };

    startAnimation();
  }, [value, duration, controls]);

  return (
    <motion.div
      animate={controls}
      initial={{ count: 0 }}
      onUpdate={(latest) => setCount(Math.floor(latest.count))}
    >
      {count.toLocaleString()}{suffix}
    </motion.div>
  );
};

const Stats: React.FC = () => {
  const titleVariants = {
    hidden: { opacity: 0, y: 30 },
    visible: { opacity: 1, y: 0 }
  };

  const statVariants = {
    hidden: { opacity: 0, scale: 0.8 },
    visible: { opacity: 1, scale: 1 }
  };

  return (
    <>
      <motion.h2
        className="text-4xl font-bold text-center text-gray-800 mb-12 bg-gradient-to-r from-blue-600 to-blue-800 bg-clip-text text-transparent"
        initial="hidden"
        whileInView="visible"
        viewport={{ once: true }}
        variants={titleVariants}
        transition={{ duration: 0.6 }}
      >
        CHÚNG TÔI CÓ GÌ?
      </motion.h2>
      <motion.div
        className="grid grid-cols-1 md:grid-cols-3 gap-8 text-center mb-16"
        initial="hidden"
        whileInView="visible"
        viewport={{ once: true }}
        transition={{ staggerChildren: 0.1, delayChildren: 0.3 }}
      >
        <motion.div
          className="bg-gradient-to-br from-blue-50 to-blue-100 p-8 rounded-xl shadow-md hover:shadow-xl transform hover:-translate-y-2 transition-all duration-300"
          variants={statVariants}
          transition={{ duration: 0.5 }}
          whileHover={{ y: -8, transition: { duration: 0.3 } }}
        >
          <div className="mb-4">
            <svg className="w-12 h-12 mx-auto text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
            </svg>
          </div>
          <div className="text-5xl font-bold text-blue-600 mb-2">
            <AnimatedCounter value={20} />
          </div>
          <div className="text-lg font-semibold text-gray-700">KIẾN TRÚC SƯ</div>
        </motion.div>
        <motion.div
          className="bg-gradient-to-br from-blue-50 to-blue-100 p-8 rounded-xl shadow-md hover:shadow-xl transform hover:-translate-y-2 transition-all duration-300"
          variants={statVariants}
          transition={{ duration: 0.5 }}
          whileHover={{ y: -8, transition: { duration: 0.3 } }}
        >
          <div className="mb-4">
            <svg className="w-12 h-12 mx-auto text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
            </svg>
          </div>
          <div className="text-5xl font-bold text-blue-600 mb-2">
            <AnimatedCounter value={40} />
          </div>
          <div className="text-lg font-semibold text-gray-700">KỸ SƯ XÂY DỰNG</div>
        </motion.div>
        <motion.div
          className="bg-gradient-to-br from-blue-50 to-blue-100 p-8 rounded-xl shadow-md hover:shadow-xl transform hover:-translate-y-2 transition-all duration-300"
          variants={statVariants}
          transition={{ duration: 0.5 }}
          whileHover={{ y: -8, transition: { duration: 0.3 } }}
        >
          <div className="mb-4">
            <svg className="w-12 h-12 mx-auto text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m8 0V8a2 2 0 01-2 2H8a2 2 0 01-2-2V6m8 0H8m0 0V4m0 2v2m0-2h8" />
            </svg>
          </div>
          <div className="text-5xl font-bold text-blue-600 mb-2">
            <AnimatedCounter value={10} />
          </div>
          <div className="text-lg font-semibold text-gray-700">CHUYÊN GIA VẤN VIÊN</div>
        </motion.div>
        <motion.div
          className="bg-gradient-to-br from-blue-50 to-blue-100 p-8 rounded-xl shadow-md hover:shadow-xl transform hover:-translate-y-2 transition-all duration-300"
          variants={statVariants}
          transition={{ duration: 0.5 }}
          whileHover={{ y: -8, transition: { duration: 0.3 } }}
        >
          <div className="mb-4">
            <svg className="w-12 h-12 mx-auto text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
          </div>
          <div className="text-5xl font-bold text-blue-600 mb-2">
            <AnimatedCounter value={150} suffix="+" />
          </div>
          <div className="text-lg font-semibold text-gray-700">DỰ ÁN</div>
        </motion.div>
        <motion.div
          className="bg-gradient-to-br from-blue-50 to-blue-100 p-8 rounded-xl shadow-md hover:shadow-xl transform hover:-translate-y-2 transition-all duration-300"
          variants={statVariants}
          transition={{ duration: 0.5 }}
          whileHover={{ y: -8, transition: { duration: 0.3 } }}
        >
          <div className="mb-4">
            <svg className="w-12 h-12 mx-auto text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.5-9a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0z" />
            </svg>
          </div>
          <div className="text-5xl font-bold text-blue-600 mb-2">
            <AnimatedCounter value={100} suffix="+" />
          </div>
          <div className="text-lg font-semibold text-gray-700">NHÂN VIÊN</div>
        </motion.div>
        <motion.div
          className="bg-gradient-to-br from-blue-50 to-blue-100 p-8 rounded-xl shadow-md hover:shadow-xl transform hover:-translate-y-2 transition-all duration-300"
          variants={statVariants}
          transition={{ duration: 0.5 }}
          whileHover={{ y: -8, transition: { duration: 0.3 } }}
        >
          <div className="mb-4">
            <svg className="w-12 h-12 mx-auto text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
            </svg>
          </div>
          <div className="text-5xl font-bold text-blue-600 mb-2">
            <AnimatedCounter value={1000} suffix="+" />
          </div>
          <div className="text-lg font-semibold text-gray-700">KHÁCH HÀNG</div>
        </motion.div>
      </motion.div>
    </>
  );
};

export default Stats;
