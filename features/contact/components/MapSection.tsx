import React from 'react';
import { useTranslation } from 'react-i18next';

const MapSection: React.FC = () => {
  const { t } = useTranslation();

  const openGoogleMaps = () => {
    const latitude = 21.005076;
    const longitude = 105.801285;
    const url = `https://www.google.com/maps?q=${latitude},${longitude}`;
    window.open(url, '_blank');
  };

  return (
    <div>
      <h2 className="text-2xl font-bold mb-6">{t('contact.map.directContact')}</h2>
      <ul className="space-y-4 text-gray-700 text-lg">
        <li className="flex items-start">
          <span className="mt-1 mr-3 text-blue-600">&#x1f4cd;</span>
          <div>
            <h3 className="font-semibold">{t('contact.map.addressLabel')}</h3>
            <p>{t('header.address')}</p>
          </div>
        </li>
        <li className="flex items-start">
          <span className="mt-1 mr-3 text-blue-600">&#x260e;</span>
          <div>
            <h3 className="font-semibold">{t('header.hotline')}</h3>
            <a href="tel:+84976447766" className="hover:text-blue-600 transition-colors">(0976) 447 766</a>
          </div>
        </li>
        <li className="flex items-start">
          <span className="mt-1 mr-3 text-blue-600">&#x2709;</span>
          <div>
            <h3 className="font-semibold">{t('contact.map.emailLabel')}</h3>
            <a href="mailto:info@tanthanhcongjsc.com" className="hover:text-blue-600 transition-colors">info@tanthanhcongjsc.com</a>
          </div>
        </li>
      </ul>
      <div className="mt-8 rounded-lg overflow-hidden shadow-lg">
                <iframe src="https://www.google.com/maps?q=21.005076,105.801285&z=16&output=embed" width="100%" height="300" style={{border:0}} allowFullScreen={true} loading="lazy" referrerPolicy="no-referrer-when-downgrade"></iframe>
      </div>
      <button onClick={openGoogleMaps} className="mt-4 bg-blue-600 text-white font-bold py-2 px-4 rounded-lg hover:bg-blue-700 transition-colors">
        {t('contact.map.openMapButton')}
      </button>
    </div>
  );
};

export default MapSection;
