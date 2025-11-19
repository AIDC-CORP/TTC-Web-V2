import React, { useState } from 'react';
import { useTranslation } from 'react-i18next';

const FormSection: React.FC = () => {
  const { t } = useTranslation();
  const [formData, setFormData] = useState({ name: '', phone: '', email: '', message: '' });
  const [errors, setErrors] = useState<{ [key: string]: string }>({});
  const [isSubmitted, setIsSubmitted] = useState(false);

  const validate = () => {
    const newErrors: { [key: string]: string } = {};
    if (!formData.name.trim()) newErrors.name = t('contact.form.errors.name');
    if (!formData.phone.trim() && !formData.email.trim()) {
        newErrors.phone = t('contact.form.errors.phoneOrEmail');
        newErrors.email = t('contact.form.errors.phoneOrEmail');
    }
    if (formData.email && !/^\S+@\S+\.\S+$/.test(formData.email)) {
        newErrors.email = t('contact.form.errors.invalidEmail');
    }
    if (formData.phone && !/^\d{10,}$/.test(formData.phone)) {
        newErrors.phone = t('contact.form.errors.invalidPhone');
    }
    if (!formData.message.trim()) newErrors.message = t('contact.form.errors.message');
    
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
      <h2 className="text-2xl font-bold mb-6">{t('contact.form.title')}</h2>
      {isSubmitted ? (
        <div className="bg-green-100 border-l-4 border-green-500 text-green-700 p-4 rounded-md" role="alert">
          <p className="font-bold">{t('contact.form.success.title')}</p>
          <p>{t('contact.form.success.message')}</p>
        </div>
      ) : (
        <form onSubmit={handleSubmit} noValidate>
          <div className="mb-4">
            <label htmlFor="name" className="block text-gray-700 font-medium mb-2">{t('contact.form.nameLabel')} *</label>
            <input type="text" id="name" name="name" value={formData.name} onChange={handleChange} className={`w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 ${errors.name ? 'border-red-500 focus:ring-red-400' : 'border-gray-300 focus:ring-blue-400'}`} />
            {errors.name && <p className="text-red-500 text-sm mt-1">{errors.name}</p>}
          </div>
          <div className="grid md:grid-cols-2 gap-4 mb-4">
            <div>
              <label htmlFor="phone" className="block text-gray-700 font-medium mb-2">{t('contact.form.phoneLabel')}</label>
              <input type="tel" id="phone" name="phone" value={formData.phone} onChange={handleChange} className={`w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 ${errors.phone ? 'border-red-500 focus:ring-red-400' : 'border-gray-300 focus:ring-blue-400'}`} />
              {errors.phone && <p className="text-red-500 text-sm mt-1">{errors.phone}</p>}
            </div>
            <div>
              <label htmlFor="email" className="block text-gray-700 font-medium mb-2">{t('contact.form.emailLabel')}</label>
              <input type="email" id="email" name="email" value={formData.email} onChange={handleChange} className={`w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 ${errors.email ? 'border-red-500 focus:ring-red-400' : 'border-gray-300 focus:ring-blue-400'}`} />
              {errors.email && <p className="text-red-500 text-sm mt-1">{errors.email}</p>}
            </div>
          </div>
          <div className="mb-6">
            <label htmlFor="message" className="block text-gray-700 font-medium mb-2">{t('contact.form.messageLabel')} *</label>
            <textarea id="message" name="message" rows={5} value={formData.message} onChange={handleChange} className={`w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 ${errors.message ? 'border-red-500 focus:ring-red-400' : 'border-gray-300 focus:ring-blue-400'}`}></textarea>
            {errors.message && <p className="text-red-500 text-sm mt-1">{errors.message}</p>}
          </div>
          <button type="submit" className="w-full bg-blue-600 text-white font-bold py-3 px-6 rounded-lg hover:bg-blue-700 transition-colors">{t('contact.form.submitButton')}</button>
        </form>
      )}
    </div>
  );
};

export default FormSection;