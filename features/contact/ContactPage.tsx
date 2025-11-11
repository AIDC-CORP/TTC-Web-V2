
import React from 'react';
import FormSection from './components/FormSection';
import MapSection from './components/MapSection';

const ContactPage: React.FC = () => {
  return (
    <div>
        <div className="bg-white py-20">
            <div className="container mx-auto px-4 text-center">
                <h1 className="text-4xl md:text-5xl font-extrabold text-gray-800">Liên hệ với chúng tôi</h1>
                <p className="mt-4 text-lg text-gray-600">Chúng tôi luôn sẵn sàng lắng nghe và tư vấn giải pháp cho bạn.</p>
            </div>
        </div>

        <div className="container mx-auto px-4 py-16">
            <div className="grid lg:grid-cols-2 gap-12">
                <FormSection />
                <MapSection />
            </div>
        </div>
    </div>
  );
};

export default ContactPage;
