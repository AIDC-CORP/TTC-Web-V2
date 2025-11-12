import React from 'react';
import { Link } from 'react-router-dom';
import { motion } from 'framer-motion';

const Criteria: React.FC = () => {
  return (
    <motion.section 
      className="py-16 md:py-24 bg-white"
      initial={{ opacity: 0, y: 50 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.8, delay: 1.0 }}
    >
      <div className="container mx-auto px-4 grid grid-cols-1 lg:grid-cols-2 gap-10 lg:gap-14 items-center">
        {/* Visual */}
        <div className="order-2 lg:order-1">
          <img
            src="https://tse3.mm.bing.net/th/id/OIP.5m-P9yD6n4RlLeY7Nr4ZhQHaE7?cb=ucfimgc2&rs=1&pid=ImgDetMain&o=7&rm=3"
            alt="Công trình tiêu biểu Tân Thành Công"
            className="w-full h-[480px] object-cover rounded-3xl shadow-xl"
          />
        </div>

        {/* Content */}
        <div className="order-1 lg:order-2">
          <span className="inline-flex items-center rounded-full bg-red-100 text-red-700 text-sm font-semibold px-4 py-2 mb-5">
            Quy trình làm việc của Tân Thành Công
          </span>
          <h2 className="text-3xl md:text-5xl font-extrabold leading-tight mb-5">
            Tiêu chí an toàn và bền vững
          </h2>
          <p className="text-gray-700 mb-6">
            Tân Thành Công cung cấp đầy đủ các dịch vụ thiết kế và xây dựng cho doanh nghiệp.
            Chúng tôi mang đến giải pháp toàn diện từ phân tích, tư vấn chiến lược đến triển khai thực tế,
            mở ra cơ hội phát triển cho mọi ý tưởng.
          </p>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-8">
            <div className="flex items-start gap-3">
              <span className="mt-1 inline-flex h-6 w-6 items-center justify-center rounded-full bg-green-100 text-green-600">✓</span>
              <div>Đảm bảo an toàn lao động</div>
            </div>
            <div className="flex items-start gap-3">
              <span className="mt-1 inline-flex h-6 w-6 items-center justify-center rounded-full bg-green-100 text-green-600">✓</span>
              <div>Vật liệu thân thiện môi trường</div>
            </div>
            <div className="flex items-start gap-3">
              <span className="mt-1 inline-flex h-6 w-6 items-center justify-center rounded-full bg-green-100 text-green-600">✓</span>
              <div>Phù hợp nhiều không gian và đối tượng sử dụng</div>
            </div>
            <div className="flex items-start gap-3">
              <span className="mt-1 inline-flex h-6 w-6 items-center justify-center rounded-full bg-green-100 text-green-600">✓</span>
              <div>Hoàn thiện nhanh chóng, hiệu quả</div>
            </div>
          </div>

          <div className="flex flex-col sm:flex-row items-start sm:items-center gap-4">
            <Link
              to="/lien-he"
              className="inline-flex items-center gap-3 bg-red-600 hover:bg-red-700 text-white font-semibold py-3 px-6 rounded-xl text-lg transition duration-300 shadow-sm"
            >
              <span>Liên hệ ngay</span>
              <span className="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-white">
                <span className="text-red-600 text-xl leading-none">☎</span>
              </span>
            </Link>
            <a href="tel:0976447766" className="text-blue-700 font-semibold">
              (+84) 0976-447-766
            </a>
          </div>
        </div>
      </div>
    </motion.section>
  );
};

export default Criteria;