
import React, { useEffect, useMemo, useRef, useState } from 'react';
import { Link } from 'react-router-dom';
import { projects, services } from '../../data/mockData';
import ProjectCard from '../projects/components/ProjectCard';

const HomePage: React.FC = () => {
  const featuredProjects = projects.slice(0, 3);
  const heroImages = useMemo(
    () => [
      'https://onetouchmedia.vn/wp-content/uploads/2019/11/05.jpg',
      'https://www.hancorp.com.vn/wp-content/uploads/2021/09/xay-dung-nha-xuong-1.jpg',
      'https://th.bing.com/th/id/R.e425a6042568905d49d624e2014ee0e1?rik=GJ6X%2fPLxAYh0Pg&riu=http%3a%2f%2fwww.beatexpharm.com.vn%2fstorage%2fuserfiles%2fimages%2fdu-an-cong-ty-cp-duoc-pham-quoc-te-dolexphar-1-1.jpg&ehk=jVEqUMAwJAshsPW4M30g%2bbUyDhcB7KJAXEHxdkwb6Qk%3d&risl=&pid=ImgRaw&r=0',
    ],
    []
  );
  const [currentIndex, setCurrentIndex] = useState(0);
  const trackRef = useRef<HTMLDivElement>(null);

  const ServicesRow: React.FC = () => {
    return (
      <div className="mt-10">
        {/* Desktop grid */}
        <div className="hidden lg:grid grid-cols-4 gap-6">
          {services.map((svc, idx) => (
            <article key={svc.id} className="group bg-white rounded-3xl overflow-hidden shadow-sm ring-1 ring-gray-100 hover:shadow-lg transition">
              <div className="relative">
                <img
                  src={svc.image}
                  alt={svc.name}
                  className="h-56 w-full object-cover"
                />
                <div className="absolute -bottom-8 right-6">
                  <div className="h-14 w-14 rounded-full bg-red-600 text-white grid place-items-center shadow-lg">
                    <span className="text-xl">{idx % 3 === 0 ? '🛠️' : idx % 3 === 1 ? '⚙️' : '🏗️'}</span>
                  </div>
                </div>
              </div>
              <div className="pt-10 px-6 pb-6">
                <div className="text-red-600 text-xs font-semibold tracking-widest uppercase mb-2">Thiết kế xây dựng</div>
                <h3 className="text-lg font-bold mb-2 group-hover:text-blue-700 transition">{svc.name}</h3>
                <p className="text-gray-600 text-sm leading-6">{svc.summary}</p>
              </div>
            </article>
          ))}
        </div>

        {/* Mobile/Tablet carousel */}
        <div
          ref={trackRef}
          className="lg:hidden flex gap-6 overflow-x-auto snap-x snap-mandatory pb-2 [-ms-overflow-style:none] [scrollbar-width:none]"
          style={{ scrollbarWidth: 'none' }}
        >
          {services.map((svc, idx) => (
            <article key={svc.id} className="min-w-[85%] sm:min-w-[60%] snap-start bg-white rounded-3xl overflow-hidden shadow-sm ring-1 ring-gray-100">
              <div className="relative">
                <img
                  src={svc.image}
                  alt={svc.name}
                  className="h-60 w-full object-cover"
                />
                <div className="absolute -bottom-8 right-6">
                  <div className="h-14 w-14 rounded-full bg-red-600 text-white grid place-items-center shadow-lg">
                    <span className="text-xl">{idx % 3 === 0 ? '🛠️' : idx % 3 === 1 ? '⚙️' : '🏗️'}</span>
                  </div>
                </div>
              </div>
              <div className="pt-10 px-6 pb-6">
                <div className="text-red-600 text-xs font-semibold tracking-widest uppercase mb-2">Thiết kế xây dựng</div>
                <h3 className="text-lg font-bold mb-2">{svc.name}</h3>
                <p className="text-gray-600 text-sm">{svc.summary}</p>
              </div>
            </article>
          ))}
        </div>
      </div>
    );
  };

  useEffect(() => {
    const intervalId = window.setInterval(() => {
      setCurrentIndex((prev) => (prev + 1) % heroImages.length);
    }, 5000);
    return () => window.clearInterval(intervalId);
  }, [heroImages.length]);

  return (
    <div>
      {/* Hero Section */}
      <section className="relative min-h-[100vh] h-[100vh] text-white overflow-hidden">
        <div className="absolute inset-0">
          {heroImages.map((src, index) => (
            <div
              key={src}
              className={`absolute inset-0 bg-cover bg-center transition-opacity duration-[1200ms] ease-in-out ${index === currentIndex ? 'opacity-100' : 'opacity-0'}`}
              style={{ backgroundImage: `url('${src}')` }}
            />
          ))}
          <div className="absolute inset-0 bg-gradient-to-br from-[#0f172a]/80 via-[#1e3a8a]/60 to-[#1d4ed8]/40"></div>
        </div>
        <div className="relative container mx-auto px-4 h-full flex flex-col justify-center items-start text-left">
          <span className="uppercase tracking-[0.30em] text-blue-180/90 mb-6 text-sm md:text-base">NHÀ THÉP TIỀN CHẾ</span>
          <h1 className="text-4xl md:text-6xl lg:text-7xl font-extrabold leading-tight mb-6 max-w-4xl">
            TÂN THÀNH CÔNG JSC
          </h1>
          <p className="text-base md:text-xl max-w-3xl mb-10 text-blue-100">
            Tư vấn chuyên nghiệp, thi công nhanh chóng, công nghệ tiêu chuẩn Quốc tế luôn được Tân Thành Công đặt lên hàng đầu.
          </p>
          <Link
            to="/tu-van"
            className="inline-flex items-center gap-3 bg-red-600 hover:bg-red-700 text-white font-semibold py-3 px-6 rounded-xl text-lg transition duration-300 shadow-sm"
          >
            <span>Liên Hệ Tư Vấn</span>
            <span className="inline-flex items-center justify-center w-8 h-8 rounded-lg bg-white">
              <span className="text-blue-600 text-xl leading-none">✓</span>
            </span>
          </Link>
        </div>
      </section>



      {/* Industrial Solutions Intro Section */}
      <section className="py-16 md:py-24 bg-white">
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
              <div className="text-red-600 font-extrabold text-6xl md:text-7xl mt-4 leading-none">10+</div>
            </div>

            {/* Overlapped images */}
            <div className="relative">
              <img
                src="https://udl.kizuna.vn/photos/2020/05/28/c3fea20d60a652af993d14925ca1e3c6.jpg"
                alt="Nhà xưởng công nghiệp"
                className="w-full h-72 sm:h-96 object-cover rounded-3xl shadow-md"
              />
              <img
                src="https://www.tanthanhcongjsc.com/wp-content/uploads/2022/10/chat-luong-600x386.jpg "
                alt="Kỹ sư công trường"
                className="absolute -top-8 -left-8 w-44 h-32 sm:w-64 sm:h-44 object-cover rounded-3xl shadow-lg border-8 border-white"
              />
            </div>
          </div>

          {/* Content side */}
          <div>
            <span className="inline-block text-xs md:text-sm font-semibold tracking-widest uppercase bg-red-100 text-red-700 px-4 py-2 rounded-full mb-5">
              Tân Thành Công
            </span>
            <h2 className="text-3xl md:text-5xl font-extrabold leading-tight mb-5">
              Đối tác thiết kế và thi công nhà xưởng công nghiệp chuẩn quốc tế
            </h2>
            <p className="text-gray-700 mb-8">
              Tân Thành Công JSC mang tới giải pháp tổng thể cho doanh nghiệp sản xuất và nhà đầu tư.
              Chúng tôi kết hợp kiến thức chuyên môn sâu, đội ngũ đa ngôn ngữ và quy trình quản trị hiện đại
              để đảm bảo dự án vận hành bền vững, an toàn và hiệu quả.
            </p>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
              <div className="flex items-start gap-3">
                <span className="mt-1 inline-flex h-6 w-6 items-center justify-center rounded-full bg-red-100 text-red-600">✓</span>
                <div>
                  <div className="font-semibold text-gray-900">Tổng thầu thiết kế & thi công</div>
                  <p className="text-gray-600 text-sm">
                    Kết nối trọn chuỗi giá trị từ tư vấn ý tưởng, thiết kế kỹ thuật đến triển khai công trường chuẩn quốc tế.
                  </p>
                </div>
              </div>
              <div className="flex items-start gap-3">
                <span className="mt-1 inline-flex h-6 w-6 items-center justify-center rounded-full bg-red-100 text-red-600">✓</span>
                <div>
                  <div className="font-semibold text-gray-900">Đồng hành cùng doanh nghiệp FDI</div>
                  <p className="text-gray-600 text-sm">
                    Hiểu rõ yêu cầu của nhà đầu tư nước ngoài, tối ưu chi phí và tiến độ cho dự án công nghiệp tại Việt Nam.
                  </p>
                </div>
              </div>
              <div className="flex items-start gap-3 sm:col-span-2">
                <span className="mt-1 inline-flex h-6 w-6 items-center justify-center rounded-full bg-red-100 text-red-600">✓</span>
                <div>
                  <div className="font-semibold text-gray-900">Giải pháp xanh & thông minh</div>
                  <p className="text-gray-600 text-sm">
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
                className="inline-flex items-center gap-3 text-blue-700 font-semibold"
              >
                <span className="inline-flex items-center justify-center w-10 h-10 rounded-full bg-blue-100">☎</span>
                <span>(+84) 0976-447-766</span>
              </a>
            </div>
          </div>
        </div>
      </section>

      {/* Featured Projects Section */}
      <section className="py-16 md:py-24 bg-white">
        <div className="container mx-auto px-4">
          <h2 className="text-3xl md:text-4xl font-bold text-center mb-4">Dự án Tiêu biểu</h2>
          <p className="text-center text-gray-600 max-w-2xl mx-auto mb-12">Chúng tôi tự hào đã góp phần vào thành công của nhiều dự án lớn, khẳng định năng lực và uy tín.</p>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {featuredProjects.map(project => (
              <ProjectCard key={project.id} project={project} />
            ))}
          </div>
          <div className="text-center mt-12">
             <Link to="/du-an" className="text-blue-600 font-semibold hover:underline">
               Xem tất cả dự án &rarr;
             </Link>
          </div>
        </div>
      </section>

      {/* Services Section */}
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


      {/* Callout: Bạn cần tư vấn xây dựng nhà xưởng? */}
      <section className="py-12 md:py-16 bg-white">
        <div className="container mx-auto px-4">
          <div className="rounded-2xl bg-gradient-to-r from-blue-600 to-indigo-600 text-white p-8 md:p-10 flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
            <div>
              <h3 className="text-2xl md:text-3xl font-bold mb-2">Bạn cần tư vấn xây dựng nhà xưởng?</h3>
              <p className="text-blue-50">Cách nhanh nhất, vui lòng liên hệ trực tiếp với tư vấn viên qua các kênh sau.</p>
            </div>
            <div className="flex flex-wrap gap-3">
              <a href="https://zalo.me/" target="_blank" rel="noreferrer" className="bg-white text-blue-700 font-semibold py-2.5 px-5 rounded-full transition hover:bg-blue-50">Chat Zalo</a>
              <a href="https://m.me/" target="_blank" rel="noreferrer" className="bg-white/10 text-white font-semibold py-2.5 px-5 rounded-full transition hover:bg-white/20">Chat Messenger</a>
              <a href="tel:0976447766" className="bg-white/10 text-white font-semibold py-2.5 px-5 rounded-full transition hover:bg-white/20">Gọi 0976 447 766</a>
            </div>
          </div>
        </div>
      </section>

      {/* Stats: Chúng tôi có gì? (red overlay section) */}
      <section className="relative py-16 md:py-24">
        {/* Background image + red overlay */}
        <div
          className="absolute inset-0 bg-cover bg-center"
          style={{
            backgroundImage: "url('https://tse3.mm.bing.net/th/id/OIP.5m-P9yD6n4RlLeY7Nr4ZhQHaE7?cb=ucfimgc2&rs=1&pid=ImgDetMain&o=7&rm=3')",
            backgroundAttachment: 'fixed',
          }}
        />
        <div className="absolute inset-0 bg-blue-600/40" />

        <div className="relative container mx-auto px-4">
          <h2 className="text-3xl md:text-4xl font-bold text-center text-white mb-12">Chúng tôi có gì?</h2>

          {/* Team capability stats */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 text-white mb-16">
            <div className="bg-white/10 rounded-2xl p-8 text-center backdrop-blur-sm">
              <div className="text-5xl font-extrabold leading-none">20+</div>
              <div className="mt-2 text-lg font-semibold opacity-95">Kiến trúc sư</div>
              <div className="mt-3 text-sm opacity-90">Thiết kế kết cấu, kiến trúc công trình hiện đại.</div>
            </div>
            <div className="bg-white/10 rounded-2xl p-8 text-center backdrop-blur-sm">
              <div className="text-5xl font-extrabold leading-none">40+</div>
              <div className="mt-2 text-lg font-semibold opacity-95">Kỹ sư xây dựng</div>
              <div className="mt-3 text-sm opacity-90">Giám sát thi công, quản lý chất lượng.</div>
            </div>
            <div className="bg-white/10 rounded-2xl p-8 text-center backdrop-blur-sm">
              <div className="text-5xl font-extrabold leading-none">10+</div>
              <div className="mt-2 text-lg font-semibold opacity-95">Chuyên gia tư vấn viên</div>
              <div className="mt-3 text-sm opacity-90">Phân tích và hỗ trợ khách hàng doanh nghiệp.</div>
            </div>
          </div>

          {/* Highlight criteria */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-10 text-white">
            <div className="bg-white/5 rounded-2xl p-8 backdrop-blur-sm">
              <h3 className="text-2xl font-bold mb-3">Công nghệ</h3>
              <p className="opacity-95">Áp dụng nhà thép tiền chế hiện đại.</p>
            </div>
            <div className="bg-white/5 rounded-2xl p-8 backdrop-blur-sm">
              <h3 className="text-2xl font-bold mb-3">Thiết bị</h3>
              <p className="opacity-95">Máy móc hiện đại – vận hành bởi công nhân tay nghề bậc 7/7.</p>
            </div>
            <div className="bg-white/5 rounded-2xl p-8 backdrop-blur-sm">
              <h3 className="text-2xl font-bold mb-3">Tầm nhìn</h3>
              <p className="opacity-95">Đội ngũ kỹ sư nhiều năm kinh nghiệm, hướng tới chuẩn quốc tế.</p>
            </div>
            <div className="bg-white/5 rounded-2xl p-8 backdrop-blur-sm">
              <h3 className="text-2xl font-bold mb-3">Định hướng</h3>
              <p className="opacity-95">Lấy sự hài lòng của khách hàng làm mục tiêu.</p>
            </div>
          </div>
        </div>
      </section>

      {/* TTC: Tiêu chí an toàn và bền vững (moved to bottom) */}
      <section className="py-16 md:py-24 bg-white">
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
      </section>
    </div>
  );
};

export default HomePage;
