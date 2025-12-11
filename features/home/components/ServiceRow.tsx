import React, { useRef } from 'react';
import { useTranslation } from 'react-i18next';
import { services } from '../../../data/mockData';

const ServicesRow: React.FC = () => {
  const { t } = useTranslation();
  const trackRef = useRef<HTMLDivElement>(null);

  return (
    <div className="mt-10">
      {/* Desktop grid */}
      <div className="hidden lg:grid grid-cols-4 gap-6">
        {services.map((svc, idx) => (
          <article key={svc.id} className="group bg-white rounded-3xl overflow-hidden shadow-sm ring-1 ring-gray-100 hover:shadow-lg transition">
            <div className="relative">
              <img
                src={svc.image}
                alt={t(`services.items.${svc.id}.name`)}
                className="h-56 w-full object-cover"
              />
              <div className="absolute -bottom-8 right-6">
                <div className="h-14 w-14 rounded-full bg-red-600 text-white grid place-items-center shadow-lg">
                  <span className="text-xl">{idx % 3 === 0 ? '🛠️' : idx % 3 === 1 ? '⚙️' : '🏗️'}</span>
                </div>
              </div>
            </div>
            <div className="pt-10 px-6 pb-6">
              <div className="text-red-600 text-xs font-semibold tracking-widest uppercase mb-2">{t('services.category')}</div>
              <h3 className="text-lg font-bold mb-2 group-hover:text-blue-700 transition">{t(`services.items.${svc.id}.name`)}</h3>
              <p className="text-gray-600 text-sm leading-6">{t(`services.items.${svc.id}.summary`)}</p>
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
                alt={t(`services.items.${svc.id}.name`)}
                className="h-60 w-full object-cover"
              />
              <div className="absolute -bottom-8 right-6">
                <div className="h-14 w-14 rounded-full bg-red-600 text-white grid place-items-center shadow-lg">
                  <span className="text-xl">{idx % 3 === 0 ? '🛠️' : idx % 3 === 1 ? '⚙️' : '🏗️'}</span>
                </div>
              </div>
            </div>
            <div className="pt-10 px-6 pb-6">
              <div className="text-red-600 text-xs font-semibold tracking-widest uppercase mb-2">{t('services.category')}</div>
              <h3 className="text-lg font-bold mb-2">{t(`services.items.${svc.id}.name`)}</h3>
              <p className="text-gray-800 text-base leading-relaxed">{t(`services.items.${svc.id}.summary`)}</p>
            </div>
          </article>
        ))}
      </div>
    </div>
  );
};

export default ServicesRow;