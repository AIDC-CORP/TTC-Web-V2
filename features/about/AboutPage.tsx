
import React from 'react';
import Value from './components/Value';

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
        <div className="container mx-auto px-4 text-center relative z-10">
          <div className="inline-block mb-6 px-4 py-2 bg-blue-500 rounded-full text-sm font-semibold tracking-wide">
            Giới thiệu về công ty
          </div>
          <h1 className="text-5xl md:text-6xl lg:text-7xl font-extrabold mb-6 leading-tight animate-fade-in">
            Về Tân Thành Công
          </h1>
          <div className="w-20 h-1 bg-gradient-to-r from-blue-300 to-blue-100 mx-auto mb-6 rounded-full"></div>
          <p className="mt-6 text-lg md:text-2xl text-blue-100 max-w-3xl mx-auto font-light leading-relaxed animate-fade-in-delayed">
            Hành trình kiến tạo những giá trị bền vững
          </p>
          <p className="mt-4 text-base md:text-lg text-blue-200 max-w-2xl mx-auto opacity-90">
            Hơn 15 năm kinh nghiệm trong lĩnh vực tư vấn và quản lý dự án xây dựng
          </p>
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

        <div className="mt-20 md:mt-32">
            <h2 className="text-4xl font-bold text-center text-gray-800 mb-12">CHÚNG TÔI CÓ GÌ?</h2>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-8 text-center mb-16">
                <div className="bg-blue-50 p-8 rounded-lg shadow-md">
                    <div className="text-4xl font-bold text-blue-600 mb-2">20</div>
                    <div className="text-lg font-semibold text-gray-700">KIẾN TRÚC SƯ</div>
                </div>
                <div className="bg-blue-50 p-8 rounded-lg shadow-md">
                    <div className="text-4xl font-bold text-blue-600 mb-2">40</div>
                    <div className="text-lg font-semibold text-gray-700">KỸ SƯ XÂY DỰNG</div>
                </div>
                <div className="bg-blue-50 p-8 rounded-lg shadow-md">
                    <div className="text-4xl font-bold text-blue-600 mb-2">10</div>
                    <div className="text-lg font-semibold text-gray-700">CHUYÊN GIA VẤN VIÊN</div>
                </div>
            </div>

            <Value />
        </div>
      </div>
    </div>
  );
};

export default AboutPage;
