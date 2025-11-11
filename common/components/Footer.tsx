
import React from 'react';
import { Link } from 'react-router-dom';

const Footer: React.FC = () => {
  return (
    <footer className="bg-gray-800 text-white">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-8">
          <div className="lg:col-span-2">
            <h3 className="text-xl font-bold text-blue-400 mb-4">CÔNG TY CỔ PHẦN TÂN THÀNH CÔNG</h3>
            <p className="text-gray-300">
              Chuyên cung cấp các giải pháp tư vấn, thiết kế và quản lý dự án xây dựng hàng đầu Việt Nam.
            </p>
          </div>
          <div>
            <h4 className="font-semibold text-lg mb-4">Liên kết nhanh</h4>
            <ul className="space-y-2">
              <li><Link to="/gioi-thieu" className="hover:text-blue-400 transition-colors">Về chúng tôi</Link></li>
              <li><Link to="/du-an" className="hover:text-blue-400 transition-colors">Dự án</Link></li>
              <li><Link to="/blog" className="hover:text-blue-400 transition-colors">Blog</Link></li>
              <li><Link to="/lien-he" className="hover:text-blue-400 transition-colors">Liên hệ</Link></li>
            </ul>
          </div>
          <div>
            <h4 className="font-semibold text-lg mb-4">Thông tin liên hệ</h4>
            <ul className="space-y-2 text-gray-300">
              <li className="flex items-start">
                <span className="mt-1 mr-2">&#x1f4cd;</span>
                <span>Tầng 5, Tòa nhà ABC, 123 Đường XYZ, Quận 1, TP. Hồ Chí Minh</span>
              </li>
              <li className="flex items-center">
                <span className="mr-2">&#x260e;</span>
                <a href="tel:+84976447766" className="hover:text-blue-400 transition-colors">(028) 38 123 456</a>
              </li>
              <li className="flex items-center">
                <span className="mr-2">&#x2709;</span>
                <a href="mailto:info@tanthanhcongjsc.com" className="hover:text-blue-400 transition-colors">info@tanthanhcongjsc.com</a>
              </li>
            </ul>
          </div>
        </div>
      </div>
      <div className="bg-gray-900 py-4 text-center text-gray-400 text-sm">
        <p>&copy; {new Date().getFullYear()} Tân Thành Công JSC. All rights reserved.</p>
      </div>
    </footer>
  );
};

export default Footer;
