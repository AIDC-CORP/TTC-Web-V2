import React, { useState, useEffect } from 'react';
import { SiZalo } from 'react-icons/si';
import { FaFacebookMessenger } from 'react-icons/fa';
import { MdCall } from 'react-icons/md';
import { IoArrowUp } from 'react-icons/io5';

const FloatingButtons: React.FC = () => {
  const [isVisible, setIsVisible] = useState(false);

  // Show scroll-to-top button when user scrolls down
  useEffect(() => {
    const toggleVisibility = () => {
      if (window.pageYOffset > 300) {
        setIsVisible(true);
      } else {
        setIsVisible(false);
      }
    };

    window.addEventListener('scroll', toggleVisibility);
    return () => window.removeEventListener('scroll', toggleVisibility);
  }, []);

  const scrollToTop = () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  };

  const phoneNumber = '+84976447766'; // From footer contact info
  const zaloUrl = `https://zalo.me/0976447766`;

  return (
    <div className="fixed bottom-6 right-6 z-50 flex flex-col space-y-3">
      {/* Zalo Button */}
      <a
        href={zaloUrl}
        target="_blank"
        rel="noopener noreferrer"
        className="w-12 h-12 bg-blue-500 hover:bg-blue-600 text-white rounded-full flex items-center justify-center shadow-lg transition-all duration-300 hover:scale-110"
        title="Liên hệ qua Zalo"
      >
        <SiZalo className="w-6 h-6" />
      </a>

      {/* Messenger Button */}
      <a
        href="https://www.messenger.com/t/100010515335344"
        target="_blank"
        rel="noopener noreferrer"
        className="w-12 h-12 bg-blue-500 hover:bg-blue-600 text-white rounded-full flex items-center justify-center shadow-lg transition-all duration-300 hover:scale-110"
        title="Liên hệ qua Messenger"
      >
        <FaFacebookMessenger className="w-6 h-6" />
      </a>

      {/* Phone Button */}
      <a
        href={`tel:${phoneNumber}`}
        className="w-12 h-12 bg-green-500 hover:bg-green-600 text-white rounded-full flex items-center justify-center shadow-lg transition-all duration-300 hover:scale-110"
        title="Gọi điện"
      >
        <MdCall className="w-6 h-6" />
      </a>

      {/* Scroll to Top Button */}
      {isVisible && (
        <button
          onClick={scrollToTop}
          className="w-12 h-12 bg-gray-600 hover:bg-gray-700 text-white rounded-full flex items-center justify-center shadow-lg transition-all duration-300 hover:scale-110"
          title="Lên đầu trang"
        >
          <IoArrowUp className="w-6 h-6" />
        </button>
      )}
    </div>
  );
};

export default FloatingButtons;