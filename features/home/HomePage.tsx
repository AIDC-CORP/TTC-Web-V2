import React from 'react';
import { motion } from 'framer-motion';
import HeroSection from './components/HeroSection';
import IntroSection from './components/IntroSection';
import FeaturedProjectsSection from './components/FeaturedProjectsSection';
import ServiceSection from './components/ServiceSection';
import LatestBlogsSection from './components/LatestBlogsSection';
import PartnersSection from './components/PartnersSection';
import CalloutSection from './components/CalloutSection';
import Criteria from './components/CriteriaSection';
import { FactoryAnatomySection } from './components/FactoryAnatomySection';
import Seo from '../../common/components/Seo';

const SITE_URL = 'https://tanthanhcongjsc.com';

const HomePage: React.FC = () => {
  const jsonLd = [
    {
      '@context': 'https://schema.org',
      '@type': 'Organization',
      name: 'Tân Thành Công JSC',
      url: SITE_URL,
      logo: `${SITE_URL}/logo-tab.png`,
      description: 'Giải pháp tích hợp cho dự án nhà máy và công trình công nghiệp tại Việt Nam.',
      address: {
        '@type': 'PostalAddress',
        addressLocality: 'Hà Nội',
        addressCountry: 'VN',
      },
    },
    {
      '@context': 'https://schema.org',
      '@type': 'WebSite',
      name: 'Tân Thành Công JSC',
      url: SITE_URL,
      potentialAction: {
        '@type': 'SearchAction',
        target: `${SITE_URL}/tim-kiem?q={search_term_string}`,
        'query-input': 'required name=search_term_string',
      },
    },
  ];

  return (
    <div>
      <Seo
        title="Trang chủ"
        description="Tân Thành Công JSC - Giải pháp tích hợp cho dự án nhà máy và công trình công nghiệp tại Việt Nam. Tư vấn, thiết kế, thi công và bảo trì."
        canonical={`${SITE_URL}/`}
        image={`${SITE_URL}/logo_aidc.png`}
        lang="vi"
        jsonLd={jsonLd}
      />
      <HeroSection />

      <motion.div
        initial={{ opacity: 0, y: 50 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: "-100px" }}
        transition={{ duration: 0.8, ease: "easeOut" }}
      >
        <IntroSection />
      </motion.div>

      <motion.div
        initial={{ opacity: 0, y: 50 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: "-100px" }}
        transition={{ duration: 0.8, ease: "easeOut", delay: 0.1 }}
      >
        <FeaturedProjectsSection />
      </motion.div>

      <motion.div
        initial={{ opacity: 0, y: 50 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: "-100px" }}
        transition={{ duration: 0.8, ease: "easeOut", delay: 0.2 }}
      >
        <ServiceSection />
      </motion.div>

      {/* <motion.div
        initial={{ opacity: 0, y: 50 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: "-100px" }}
        transition={{ duration: 0.8, ease: "easeOut", delay: 0.25 }}
      >
        <FactoryAnatomySection />
      </motion.div> */}

      <motion.div
        initial={{ opacity: 0, y: 50 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: "-100px" }}
        transition={{ duration: 0.8, ease: "easeOut", delay: 0.3 }}
      >
        <LatestBlogsSection />
      </motion.div>

      <motion.div
        initial={{ opacity: 0, y: 50 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: "-100px" }}
        transition={{ duration: 0.8, ease: "easeOut", delay: 0.4 }}
      >
        <PartnersSection />
      </motion.div>

      <motion.div
        initial={{ opacity: 0, y: 50 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: "-100px" }}
        transition={{ duration: 0.8, ease: "easeOut", delay: 0.5 }}
      >
        <CalloutSection />
      </motion.div>

      <motion.div
        initial={{ opacity: 0, y: 50 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, margin: "-100px" }}
        transition={{ duration: 0.8, ease: "easeOut", delay: 0.6 }}
      >
        <Criteria />
      </motion.div>
    </div>
  );
};

export default HomePage;
