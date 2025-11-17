import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { motion } from 'framer-motion';

const IntroSection: React.FC = () => {
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
              NĂM KINH NGHIỆM
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
            Tân Thành Công
          </span>
          <h2 className="text-3xl md:text-5xl font-extrabold leading-tight mb-5">
            Đối tác thiết kế và thi công nhà xưởng công nghiệp chuẩn quốc tế
          </h2>
          <p className="text-gray-700 mb-8 text-base md:text-lg font-medium leading-relaxed">
            Tân Thành Công JSC mang tới giải pháp tổng thể cho doanh nghiệp sản xuất và nhà đầu tư.
            Chúng tôi kết hợp kiến thức chuyên môn sâu, đội ngũ đa ngôn ngữ và quy trình quản trị hiện đại
            để đảm bảo dự án vận hành bền vững, an toàn và hiệu quả.
          </p>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
            <div className="flex items-start gap-3">
              <span className="mt-1 inline-flex h-6 w-6 items-center justify-center rounded-full bg-red-100 text-red-600">✓</span>
              <div>
                <div className="font-bold text-gray-900 text-base md:text-lg">Tổng thầu thiết kế & thi công</div>
                <p className="text-gray-600 text-base leading-relaxed">
                  Kết nối trọn chuỗi giá trị từ tư vấn ý tưởng, thiết kế kỹ thuật đến triển khai công trường chuẩn quốc tế.
                </p>
              </div>
            </div>
            <div className="flex items-start gap-3">
              <span className="mt-1 inline-flex h-6 w-6 items-center justify-center rounded-full bg-red-100 text-red-600">✓</span>
              <div>
                <div className="font-bold text-gray-900 text-base md:text-lg">Đồng hành cùng doanh nghiệp FDI</div>
                <p className="text-gray-600 text-base leading-relaxed">
                  Hiểu rõ yêu cầu của nhà đầu tư nước ngoài, tối ưu chi phí và tiến độ cho dự án công nghiệp tại Việt Nam.
                </p>
              </div>
            </div>
            <div className="flex items-start gap-3 sm:col-span-2">
              <span className="mt-1 inline-flex h-6 w-6 items-center justify-center rounded-full bg-red-100 text-red-600">✓</span>
              <div>
                <div className="font-bold text-gray-900 text-base md:text-lg">Giải pháp xanh & thông minh</div>
                <p className="text-gray-600 text-base leading-relaxed">
                  Ưu tiên công nghệ nhà thép tiền chế, tiết kiệm năng lượng và mở rộng linh hoạt cho nhà xưởng tương lai.
                </p>
              </div>
            </div>
          </div>

          <div className="mt-8 flex items-center gap-4">
            <Link
              to="/lien-he"
              className="inline-flex items-center gap-2 bg-red-600 hover:bg-red-700 text-white font-semibold py-3 px-6 rounded-xl transition duration-300 shadow-sm"
            >
              <span>Liên hệ ngay</span>
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