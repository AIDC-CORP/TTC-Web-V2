import React, { useCallback, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { useTranslation } from 'react-i18next';

export interface LightboxImage {
  src: string;
  caption?: string;
}

interface LightboxProps {
  images: LightboxImage[];
  index: number | null;
  onClose: () => void;
  onNavigate: (index: number) => void;
}

const Lightbox: React.FC<LightboxProps> = ({ images, index, onClose, onNavigate }) => {
  const { t } = useTranslation();
  const isOpen = index !== null && index >= 0 && index < images.length;

  const goPrev = useCallback(() => {
    if (index === null) return;
    onNavigate((index - 1 + images.length) % images.length);
  }, [index, images.length, onNavigate]);

  const goNext = useCallback(() => {
    if (index === null) return;
    onNavigate((index + 1) % images.length);
  }, [index, images.length, onNavigate]);

  useEffect(() => {
    if (!isOpen) return;

    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') onClose();
      else if (e.key === 'ArrowLeft') goPrev();
      else if (e.key === 'ArrowRight') goNext();
    };

    document.addEventListener('keydown', onKey);
    const prevOverflow = document.body.style.overflow;
    document.body.style.overflow = 'hidden';

    return () => {
      document.removeEventListener('keydown', onKey);
      document.body.style.overflow = prevOverflow;
    };
  }, [isOpen, onClose, goPrev, goNext]);

  const current = isOpen ? images[index as number] : null;
  const showNav = images.length > 1;

  return (
    <AnimatePresence>
      {isOpen && current && (
        <motion.div
          className="fixed inset-0 z-[60] flex items-center justify-center bg-black/90 backdrop-blur-sm"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          transition={{ duration: 0.25 }}
          onClick={onClose}
          role="dialog"
          aria-modal="true"
        >
          <button
            onClick={onClose}
            aria-label={t('article.closeImage')}
            className="absolute top-4 right-4 z-10 text-white/80 hover:text-white text-4xl leading-none w-12 h-12 flex items-center justify-center"
          >
            ×
          </button>

          {showNav && (
            <button
              onClick={(e) => { e.stopPropagation(); goPrev(); }}
              aria-label={t('article.prevImage')}
              className="absolute left-2 md:left-6 z-10 text-white/70 hover:text-white text-5xl w-12 h-16 flex items-center justify-center"
            >
              ‹
            </button>
          )}

          <motion.figure
            key={index}
            className="max-w-6xl w-full px-4 flex flex-col items-center"
            initial={{ opacity: 0, scale: 0.96 }}
            animate={{ opacity: 1, scale: 1 }}
            exit={{ opacity: 0, scale: 0.96 }}
            transition={{ duration: 0.25 }}
            onClick={(e) => e.stopPropagation()}
          >
            <img
              src={current.src}
              alt={current.caption || ''}
              className="max-h-[80vh] w-auto max-w-full object-contain rounded-lg shadow-2xl"
            />
            {current.caption && (
              <figcaption className="mt-4 text-center text-sm text-white/80 italic max-w-3xl px-4">
                {current.caption}
              </figcaption>
            )}
            {showNav && (
              <span className="mt-2 text-xs text-white/50">
                {(index as number) + 1} / {images.length}
              </span>
            )}
          </motion.figure>

          {showNav && (
            <button
              onClick={(e) => { e.stopPropagation(); goNext(); }}
              aria-label={t('article.nextImage')}
              className="absolute right-2 md:right-6 z-10 text-white/70 hover:text-white text-5xl w-12 h-16 flex items-center justify-center"
            >
              ›
            </button>
          )}
        </motion.div>
      )}
    </AnimatePresence>
  );
};

export default Lightbox;
