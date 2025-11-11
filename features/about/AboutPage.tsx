
import React from 'react';
import { motion } from 'framer-motion';
import Value from './components/Quotes';
import Cards from './components/Cards';
import Stats from './components/Stats';

const AboutPage: React.FC = () => {
  return (
    <div className="bg-white">
      <div className="relative bg-cover bg-center text-white py-24 md:py-40 overflow-hidden" style={{ backgroundImage: `url('https://picsum.photos/seed/construction-hero/1920/1080')` }}>
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
            className="inline-block mb-6 px-4 py-2 bg-blue-500 rounded-full text-sm font-semibold tracking-wide"
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.6, delay: 0.2 }}
          >
            Giới thiệu về công ty
          </motion.div>
          <motion.h1 
            className="text-5xl md:text-6xl lg:text-7xl font-extrabold mb-6 leading-tight animate-fade-in"
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.4 }}
          >
            Về Tân Thành Công
          </motion.h1>
          <motion.div 
            className="w-20 h-1 bg-gradient-to-r from-blue-300 to-blue-100 mx-auto mb-6 rounded-full"
            initial={{ scaleX: 0 }}
            animate={{ scaleX: 1 }}
            transition={{ duration: 0.6, delay: 0.8 }}
          />
          <motion.p 
            className="mt-6 text-lg md:text-2xl text-blue-100 max-w-3xl mx-auto font-light leading-relaxed animate-fade-in-delayed"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 1.0 }}
          >
            Hành trình kiến tạo những giá trị bền vững
          </motion.p>
          <motion.p 
            className="mt-4 text-base md:text-lg text-blue-200 max-w-2xl mx-auto opacity-90"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 1.2 }}
          >
            Hơn 15 năm kinh nghiệm trong lĩnh vực tư vấn và quản lý dự án xây dựng
          </motion.p>
        </motion.div>
      </div>

      <div className="container mx-auto px-4 py-16 md:py-24">
        <motion.div 
          className="grid md:grid-cols-2 gap-12 items-center"
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
            <img src="https://picsum.photos/seed/aboutus/800/600" alt="Đội ngũ Tân Thành Công" className="rounded-lg shadow-2xl"/>
          </motion.div>
          <motion.div
            initial={{ opacity: 0, x: 50 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.8, delay: 0.4 }}
          >
            <h2 className="text-3xl font-bold text-gray-800 mb-4">Câu chuyện của chúng tôi</h2>
            <p className="text-gray-600 leading-relaxed mb-4">
              Được thành lập từ năm 2010, Tân Thành Công khởi đầu với một đội ngũ kỹ sư tâm huyết và khát vọng mang đến những công trình chất lượng cao cho Việt Nam. Trải qua hơn một thập kỷ phát triển, chúng tôi đã không ngừng nỗ lực, đổi mới và vươn lên trở thành một trong những công ty tư vấn xây dựng uy tín hàng đầu.
            </p>
            <p className="text-gray-600 leading-relaxed">
              Sự thành công của chúng tôi được xây dựng trên nền tảng chuyên môn vững chắc, tinh thần trách nhiệm và sự tin tưởng của Quý khách hàng, đối tác.
            </p>
          </motion.div>
        </motion.div>

        <motion.div
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
