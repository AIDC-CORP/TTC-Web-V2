import React from 'react';

const MapSection: React.FC = () => {
  const openGoogleMaps = () => {
    const latitude = 21.005076;
    const longitude = 105.801285;
    const url = `https://www.google.com/maps?q=${latitude},${longitude}`;
    window.open(url, '_blank');
  };

  return (
    <div>
      <h2 className="text-2xl font-bold mb-6">Thông tin liên hệ trực tiếp</h2>
      <ul className="space-y-4 text-gray-700 text-lg">
        <li className="flex items-start">
          <span className="mt-1 mr-3 text-blue-600">&#x1f4cd;</span>
          <div>
            <h3 className="font-semibold">Địa chỉ</h3>
            <p>Tầng 5, Số 19N7B, KĐT Trung Hòa Nhân Chính, Quận Thanh Xuân, TP Hà Nội</p>
          </div>
        </li>
        <li className="flex items-start">
          <span className="mt-1 mr-3 text-blue-600">&#x260e;</span>
          <div>
            <h3 className="font-semibold">Hotline</h3>
            <a href="tel:+84976447766" className="hover:text-blue-600 transition-colors">(0976) 447 766</a>
          </div>
        </li>
        <li className="flex items-start">
          <span className="mt-1 mr-3 text-blue-600">&#x2709;</span>
          <div>
            <h3 className="font-semibold">Email</h3>
            <a href="mailto:info@tanthanhcongjsc.com" className="hover:text-blue-600 transition-colors">info@tanthanhcongjsc.com</a>
          </div>
        </li>
      </ul>
      <div className="mt-8 rounded-lg overflow-hidden shadow-lg">
                <iframe src="https://www.google.com/maps?q=21.005076,105.801285&z=16&output=embed" width="100%" height="300" style={{border:0}} allowFullScreen={true} loading="lazy" referrerPolicy="no-referrer-when-downgrade"></iframe>
      </div>
      <button onClick={openGoogleMaps} className="mt-4 bg-blue-600 text-white font-bold py-2 px-4 rounded-lg hover:bg-blue-700 transition-colors">
        Mở bản đồ lớn
      </button>
    </div>
  );
};

export default MapSection;