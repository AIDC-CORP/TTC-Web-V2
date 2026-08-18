import React from 'react';
import { motion } from 'framer-motion';
import { useTranslation } from 'react-i18next';
import { GalleryImage, LangKey } from '../../../types';

interface ArticleGalleryProps {
  images: GalleryImage[];
  lang: LangKey;
  title: string;
  onImageClick: (index: number) => void;
}

const captionFor = (image: GalleryImage, lang: LangKey): string =>
  image.caption?.[lang] || image.caption?.vi || '';

const ArticleGallery: React.FC<ArticleGalleryProps> = ({ images, lang, title, onImageClick }) => {
  const { t } = useTranslation();
  if (!images.length) return null;

  return (
    <section className="mt-12" aria-label={title}>
      <h2 className="text-2xl font-bold text-gray-900 mb-6 border-l-4 border-blue-600 pl-4">
        {title}
      </h2>
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
        {images.map((image, index) => {
          const caption = captionFor(image, lang);
          return (
            <motion.figure
              key={image.src}
              className="group cursor-pointer m-0"
              whileHover={{ y: -4 }}
              transition={{ duration: 0.25 }}
              onClick={() => onImageClick(index)}
            >
              <div className="relative overflow-hidden rounded-xl shadow-md aspect-[3/2]">
                <img
                  src={image.src}
                  alt={caption || t('article.galleryImageAlt', { n: index + 1 })}
                  loading="lazy"
                  decoding="async"
                  className="w-full h-full object-cover transition-transform duration-300 group-hover:scale-105"
                />
                <div className="absolute inset-0 bg-black/0 group-hover:bg-black/20 transition-colors duration-300" />
              </div>
              {caption && (
                <figcaption className="mt-2 text-sm text-gray-500 italic leading-snug">
                  {caption}
                </figcaption>
              )}
            </motion.figure>
          );
        })}
      </div>
    </section>
  );
};

export default ArticleGallery;
