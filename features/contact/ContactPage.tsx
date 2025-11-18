
import React from 'react';
import { useTranslation } from 'react-i18next';
import FormSection from './components/FormSection';
import MapSection from './components/MapSection';

const ContactPage: React.FC = () => {
  const { t } = useTranslation();
  
  return (
    <div className="min-h-screen bg-gray-50">
        <div className="bg-white py-20">
            <div className="container mx-auto px-4 text-center">
                <h1 className="text-4xl md:text-5xl font-extrabold text-gray-800">{t('contactPage.title')}</h1>
                <p className="mt-4 text-lg text-gray-600">{t('contactPage.subtitle')}</p>
            </div>
        </div>

        <div className="container mx-auto px-4 py-20 -mt-12">
            <div className="grid lg:grid-cols-2 gap-8">
                <div className="bg-white shadow-xl rounded-2xl p-8 transform hover:scale-105 transition-transform duration-300">
                    <div className="flex items-center mb-6">
                        <div className="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center mr-4">
                            <svg className="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
                            </svg>
                        </div>
                        <h2 className="text-2xl font-bold text-gray-800">{t('contactPage.sendMessage')}</h2>
                    </div>
                    <FormSection />
                </div>
                <div className="bg-white shadow-xl rounded-2xl p-8 transform hover:scale-105 transition-transform duration-300">
                    <div className="flex items-center mb-6">
                        <div className="w-12 h-12 bg-green-100 rounded-full flex items-center justify-center mr-4">
                            <svg className="w-6 h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                            </svg>
                        </div>
                        <h2 className="text-2xl font-bold text-gray-800">{t('contactPage.ourLocation')}</h2>
                    </div>
                    <MapSection />
                </div>
            </div>
        </div>
    </div>
  );
};

export default ContactPage;
