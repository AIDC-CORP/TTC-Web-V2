import React from 'react';
import { motion } from 'framer-motion';

const Cards: React.FC = () => {
  const cardVariants = {
    hidden: { opacity: 0, y: 50 },
    visible: { opacity: 1, y: 0 }
  };

  return (
    <motion.div 
      className="w-full"
      initial="hidden"
      whileInView="visible"
      viewport={{ once: true }}
      transition={{ staggerChildren: 0.2 }}
    >
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8 md:gap-10">
        {/* Sứ mệnh Card */}
        <motion.div 
          className="group relative bg-gradient-to-br from-blue-50 to-indigo-100 p-8 md:p-10 rounded-2xl shadow-lg hover:shadow-2xl transition-all duration-500 transform hover:-translate-y-2 border border-blue-100 hover:border-blue-200"
          variants={cardVariants}
          transition={{ duration: 0.6 }}
          whileHover={{ y: -8, transition: { duration: 0.3 } }}
        >
          <div className="absolute -top-4 left-1/2 transform -translate-x-1/2">
            <div className="w-12 h-12 bg-gradient-to-r from-blue-500 to-blue-600 rounded-full flex items-center justify-center shadow-lg">
              <svg className="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
            </div>
          </div>
          <div className="pt-6 text-center">
            <h3 className="text-3xl md:text-4xl font-bold text-blue-700 mb-6 group-hover:text-blue-800 transition-colors duration-300">Sứ mệnh</h3>
            <p className="text-gray-700 text-base md:text-lg font-medium leading-relaxed group-hover:text-gray-800 transition-colors duration-300">
              Cung cấp các giải pháp kỹ thuật ưu việt, an toàn và hiệu quả, góp phần vào sự phát triển bền vững của ngành xây dựng và xã hội.
            </p>
          </div>
        </motion.div>

        {/* Tầm nhìn Card */}
        <motion.div 
          className="group relative bg-gradient-to-br from-purple-50 to-pink-100 p-8 md:p-10 rounded-2xl shadow-lg hover:shadow-2xl transition-all duration-500 transform hover:-translate-y-2 border border-purple-100 hover:border-purple-200"
          variants={cardVariants}
          transition={{ duration: 0.6 }}
          whileHover={{ y: -8, transition: { duration: 0.3 } }}
        >
          <div className="absolute -top-4 left-1/2 transform -translate-x-1/2">
            <div className="w-12 h-12 bg-gradient-to-r from-purple-500 to-purple-600 rounded-full flex items-center justify-center shadow-lg">
              <svg className="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
              </svg>
            </div>
          </div>
          <div className="pt-6 text-center">
            <h3 className="text-3xl md:text-4xl font-bold text-purple-700 mb-6 group-hover:text-purple-800 transition-colors duration-300">Tầm nhìn</h3>
            <p className="text-gray-700 text-base md:text-lg font-medium leading-relaxed group-hover:text-gray-800 transition-colors duration-300">
              Trở thành đối tác tin cậy hàng đầu trong lĩnh vực tư vấn và quản lý dự án xây dựng tại Việt Nam và vươn tầm khu vực.
            </p>
          </div>
        </motion.div>

        {/* Giá trị cốt lõi Card */}
        <motion.div 
          className="group relative bg-gradient-to-br from-green-50 to-emerald-100 p-8 md:p-10 rounded-2xl shadow-lg hover:shadow-2xl transition-all duration-500 transform hover:-translate-y-2 border border-green-100 hover:border-green-200"
          variants={cardVariants}
          transition={{ duration: 0.6 }}
          whileHover={{ y: -8, transition: { duration: 0.3 } }}
        >
          <div className="absolute -top-4 left-1/2 transform -translate-x-1/2">
            <div className="w-12 h-12 bg-gradient-to-r from-green-500 to-green-600 rounded-full flex items-center justify-center shadow-lg">
              <svg className="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
              </svg>
            </div>
          </div>
          <div className="pt-6 text-center">
            <h3 className="text-3xl md:text-4xl font-bold text-green-700 mb-6 group-hover:text-green-800 transition-colors duration-300">Giá trị cốt lõi</h3>
            <p className="text-gray-700 text-base md:text-lg font-medium leading-relaxed group-hover:text-gray-800 transition-colors duration-300">
              Uy tín - Chuyên nghiệp - Sáng tạo - Tận tâm. Đây là kim chỉ nam cho mọi hoạt động của chúng tôi.
            </p>
          </div>
        </motion.div>
      </div>
    </motion.div>
  );
};

export default Cards;
