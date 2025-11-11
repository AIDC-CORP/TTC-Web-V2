
import React from 'react';
import { Link } from 'react-router-dom';
import { projects, services } from '../data/mockData';
import ProjectCard from '../features/projects/components/ProjectCard';
import ServiceCard from '../features/home/components/ServiceCard';

const HomePage: React.FC = () => {
  const featuredProjects = projects.slice(0, 3);

  return (
    <div>
      {/* Hero Section */}
      <section className="relative h-[60vh] md:h-[70vh] bg-cover bg-center text-white" style={{ backgroundImage: `url('https://picsum.photos/seed/hero/1920/1080')` }}>
        <div className="absolute inset-0 bg-black bg-opacity-50"></div>
        <div className="relative container mx-auto px-4 h-full flex flex-col justify-center items-center text-center">
          <h1 className="text-4xl md:text-6xl font-extrabold leading-tight mb-4 animate-fade-in-down">Kiến Tạo Giá Trị Bền Vững</h1>
          <p className="text-lg md:text-xl max-w-3xl mb-8 animate-fade-in-up">Tân Thành Công - Đồng hành cùng bạn trên mọi công trình, mang đến giải pháp xây dựng tối ưu và hiệu quả.</p>
          <Link to="/du-an" className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-8 rounded-full text-lg transition duration-300 transform hover:scale-105 animate-fade-in-up">
            Khám phá Dự án
          </Link>
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
      <section className="py-16 md:py-24 bg-gray-50">
        <div className="container mx-auto px-4">
          <h2 className="text-3xl md:text-4xl font-bold text-center mb-12">Dịch vụ của Chúng tôi</h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
            {services.map(service => (
              <ServiceCard key={service.id} service={service} />
            ))}
          </div>
        </div>
      </section>
    </div>
  );
};

export default HomePage;
