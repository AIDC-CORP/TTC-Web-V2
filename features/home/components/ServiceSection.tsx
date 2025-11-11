import React from 'react';
import ServicesRow from './ServiceRow';

const ServiceSection: React.FC = () => {
  return (
    <section className="py-20 md:py-28 bg-gray-50">
      <div className="container mx-auto px-4">
        {/* Header */}
        <div className="flex flex-col md:flex-row md:items-start md:justify-between gap-8">
          <div className="max-w-3xl">
            <span className="inline-flex items-center rounded-full bg-red-100 text-red-700 text-sm font-semibold px-4 py-2 mb-4">
              DỊCH VỤ CỦA CHÚNG TÔI
            </span>
            <h2 className="text-3xl md:text-5xl font-extrabold leading-tight">
              Cung cấp các giải pháp
              <br className="hidden md:block" /> thiết kế xây dựng
            </h2>
          </div>

          <div className="md:max-w-xl text-gray-600">
            <p>
            Tân Thành Công mang đến giải pháp toàn diện trong thiết kế và thi công nhà xưởng công nghiệp. Với đội ngũ kỹ sư và chuyên gia giàu kinh nghiệm, chúng tôi cung cấp dịch vụ tư vấn, thiết kế, và thi công trọn gói, đảm bảo tiến độ, chất lượng và tính an toàn cho từng công trình. Tân Thành Công luôn hướng đến việc tối ưu chi phí và hiện thực hóa mọi ý tưởng xây dựng của khách hàng bằng những giải pháp kỹ thuật tiên tiến và hiệu quả.
      
            </p>
          </div>
        </div>

        {/* Cards row (carousel) */}
        <ServicesRow />
      </div>
    </section>
  );
};

export default ServiceSection;