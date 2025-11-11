
import React from 'react';

const AboutPage: React.FC = () => {
  return (
    <div className="bg-white">
       <div className="relative bg-blue-700 text-white py-20 md:py-32">
        <div className="container mx-auto px-4 text-center">
          <h1 className="text-4xl md:text-5xl font-extrabold">Về Tân Thành Công</h1>
          <p className="mt-4 text-lg md:text-xl text-blue-200">Hành trình kiến tạo những giá trị bền vững</p>
        </div>
      </div>

      <div className="container mx-auto px-4 py-16 md:py-24">
        <div className="grid md:grid-cols-2 gap-12 items-center">
            <div>
                <img src="https://picsum.photos/seed/aboutus/800/600" alt="Đội ngũ Tân Thành Công" className="rounded-lg shadow-2xl"/>
            </div>
            <div>
                <h2 className="text-3xl font-bold text-gray-800 mb-4">Câu chuyện của chúng tôi</h2>
                <p className="text-gray-600 leading-relaxed mb-4">
                    Được thành lập từ năm 2010, Tân Thành Công khởi đầu với một đội ngũ kỹ sư tâm huyết và khát vọng mang đến những công trình chất lượng cao cho Việt Nam. Trải qua hơn một thập kỷ phát triển, chúng tôi đã không ngừng nỗ lực, đổi mới và vươn lên trở thành một trong những công ty tư vấn xây dựng uy tín hàng đầu.
                </p>
                <p className="text-gray-600 leading-relaxed">
                    Sự thành công của chúng tôi được xây dựng trên nền tảng chuyên môn vững chắc, tinh thần trách nhiệm và sự tin tưởng của Quý khách hàng, đối tác.
                </p>
            </div>
        </div>

        <div className="mt-20 md:mt-32">
            <div className="grid grid-cols-1 md:grid-cols-3 gap-10 text-center">
                <div className="bg-gray-50 p-8 rounded-lg shadow-md">
                    <h3 className="text-2xl font-bold text-blue-600 mb-3">Sứ mệnh</h3>
                    <p className="text-gray-600">Cung cấp các giải pháp kỹ thuật ưu việt, an toàn và hiệu quả, góp phần vào sự phát triển bền vững của ngành xây dựng và xã hội.</p>
                </div>
                 <div className="bg-gray-50 p-8 rounded-lg shadow-md">
                    <h3 className="text-2xl font-bold text-blue-600 mb-3">Tầm nhìn</h3>
                    <p className="text-gray-600">Trở thành đối tác tin cậy hàng đầu trong lĩnh vực tư vấn và quản lý dự án xây dựng tại Việt Nam và vươn tầm khu vực.</p>
                </div>
                 <div className="bg-gray-50 p-8 rounded-lg shadow-md">
                    <h3 className="text-2xl font-bold text-blue-600 mb-3">Giá trị cốt lõi</h3>
                    <p className="text-gray-600">Uy tín - Chuyên nghiệp - Sáng tạo - Tận tâm. Đây là kim chỉ nam cho mọi hoạt động của chúng tôi.</p>
                </div>
            </div>
        </div>
      </div>
    </div>
  );
};

export default AboutPage;
