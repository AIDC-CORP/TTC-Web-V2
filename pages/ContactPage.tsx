
import React, { useState } from 'react';

const ContactPage: React.FC = () => {
  const [formData, setFormData] = useState({ name: '', phone: '', email: '', message: '' });
  const [errors, setErrors] = useState<{ [key: string]: string }>({});
  const [isSubmitted, setIsSubmitted] = useState(false);

  const validate = () => {
    const newErrors: { [key: string]: string } = {};
    if (!formData.name.trim()) newErrors.name = 'Vui lòng nhập họ tên';
    if (!formData.phone.trim() && !formData.email.trim()) {
        newErrors.phone = 'Vui lòng nhập SĐT hoặc Email';
        newErrors.email = 'Vui lòng nhập SĐT hoặc Email';
    }
    if (formData.email && !/^\S+@\S+\.\S+$/.test(formData.email)) {
        newErrors.email = 'Email không hợp lệ';
    }
    if (formData.phone && !/^\d{10,}$/.test(formData.phone)) {
        newErrors.phone = 'Số điện thoại không hợp lệ';
    }
    if (!formData.message.trim()) newErrors.message = 'Vui lòng nhập nội dung tin nhắn';
    
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (validate()) {
      console.log('Form submitted:', formData);
      setIsSubmitted(true);
      setFormData({ name: '', phone: '', email: '', message: '' });
      setTimeout(() => setIsSubmitted(false), 5000);
    }
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

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
                <div>
                    <h2 className="text-2xl font-bold mb-6">Gửi yêu cầu tư vấn</h2>
                    {isSubmitted ? (
                        <div className="bg-green-100 border-l-4 border-green-500 text-green-700 p-4 rounded-md" role="alert">
                            <p className="font-bold">Gửi liên hệ thành công!</p>
                            <p>Chúng tôi sẽ phản hồi bạn sớm nhất.</p>
                        </div>
                    ) : (
                        <form onSubmit={handleSubmit} noValidate>
                            <div className="mb-4">
                                <label htmlFor="name" className="block text-gray-700 font-medium mb-2">Họ và tên *</label>
                                <input type="text" id="name" name="name" value={formData.name} onChange={handleChange} className={`w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 ${errors.name ? 'border-red-500 focus:ring-red-400' : 'border-gray-300 focus:ring-blue-400'}`} />
                                {errors.name && <p className="text-red-500 text-sm mt-1">{errors.name}</p>}
                            </div>
                            <div className="grid md:grid-cols-2 gap-4 mb-4">
                                <div>
                                    <label htmlFor="phone" className="block text-gray-700 font-medium mb-2">Số điện thoại</label>
                                    <input type="tel" id="phone" name="phone" value={formData.phone} onChange={handleChange} className={`w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 ${errors.phone ? 'border-red-500 focus:ring-red-400' : 'border-gray-300 focus:ring-blue-400'}`} />
                                    {errors.phone && <p className="text-red-500 text-sm mt-1">{errors.phone}</p>}
                                </div>
                                 <div>
                                    <label htmlFor="email" className="block text-gray-700 font-medium mb-2">Email</label>
                                    <input type="email" id="email" name="email" value={formData.email} onChange={handleChange} className={`w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 ${errors.email ? 'border-red-500 focus:ring-red-400' : 'border-gray-300 focus:ring-blue-400'}`} />
                                    {errors.email && <p className="text-red-500 text-sm mt-1">{errors.email}</p>}
                                </div>
                            </div>
                            <div className="mb-6">
                                <label htmlFor="message" className="block text-gray-700 font-medium mb-2">Nội dung tin nhắn *</label>
                                <textarea id="message" name="message" rows={5} value={formData.message} onChange={handleChange} className={`w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 ${errors.message ? 'border-red-500 focus:ring-red-400' : 'border-gray-300 focus:ring-blue-400'}`}></textarea>
                                {errors.message && <p className="text-red-500 text-sm mt-1">{errors.message}</p>}
                            </div>
                            <button type="submit" className="w-full bg-blue-600 text-white font-bold py-3 px-6 rounded-lg hover:bg-blue-700 transition-colors">Gửi đi</button>
                        </form>
                    )}
                </div>
                <div>
                    <h2 className="text-2xl font-bold mb-6">Thông tin liên hệ trực tiếp</h2>
                     <ul className="space-y-4 text-gray-700 text-lg">
                        <li className="flex items-start">
                            <span className="mt-1 mr-3 text-blue-600">&#x1f4cd;</span>
                            <div>
                                <h3 className="font-semibold">Địa chỉ</h3>
                                <p>Tầng 5, Tòa nhà ABC, 123 Đường XYZ, Quận 1, TP. Hồ Chí Minh</p>
                            </div>
                        </li>
                        <li className="flex items-start">
                            <span className="mt-1 mr-3 text-blue-600">&#x260e;</span>
                            <div>
                                <h3 className="font-semibold">Hotline</h3>
                                <a href="tel:+842838123456" className="hover:text-blue-600 transition-colors">(028) 38 123 456</a>
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
                         <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3919.447913364969!2d106.70133181529813!3d10.77699599232076!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x31752f49a37a726f%3A0x47b87612c22938a1!2zVMOyYSBuaMOgIEJpdGV4Y28!5e0!3m2!1svi!2s!4v1654321098765!5m2!1svi!2s" width="100%" height="300" style={{border:0}} allowFullScreen={true} loading="lazy" referrerPolicy="no-referrer-when-downgrade"></iframe>
                    </div>
                </div>
            </div>
        </div>
    </div>
  );
};

export default ContactPage;
