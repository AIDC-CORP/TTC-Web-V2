import React, { useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import articlesData from './data/blog.json';
import { Article, GalleryImage, LangKey } from '../../types';
import { getCurrentLangKey } from '../../common/utils/i18nUtils';
import { viDateToISO } from '../../common/utils/dateUtils';
import Seo from '../../common/components/Seo';
import ArticleContent from './components/ArticleContent';
import ArticleGallery from './components/ArticleGallery';
import Lightbox, { LightboxImage } from './components/Lightbox';

const articles = articlesData as Article[];
const SITE_URL = 'https://tanthanhcongjsc.com';
const SITE_NAME = 'Tân Thành Công JSC';

const captionFor = (image: GalleryImage | undefined, lang: LangKey): string =>
  image?.caption?.[lang] || image?.caption?.vi || '';

const buildExcerpt = (content: string): string =>
  content
    .replace(/\[IMAGE:.*?\]/g, '')
    .replace(/##?\s/g, '')
    .replace(/\n+/g, ' ')
    .trim()
    .substring(0, 160);

const ArticleDetailPage: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const { t, i18n } = useTranslation();
  const [lightboxIndex, setLightboxIndex] = useState<number | null>(null);

  const article = articles.find((a) => a.id === id);
  const currentLang = getCurrentLangKey(i18n.language);
  const localizedContent = article ? (article[currentLang] || article.vi) : null;

  if (!article || !localizedContent) {
    return (
      <div className="container mx-auto px-4 py-20 text-center">
        <h1 className="text-3xl font-bold">{t('article.notFound')}</h1>
        <p className="mt-4">{t('article.notFoundText')}</p>
        <Link to="/blog" className="mt-8 inline-block bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition">
          {t('article.backToBlog')}
        </Link>
      </div>
    );
  }

  const canonical = `${SITE_URL}/blog/${article.id}`;
  const excerpt = buildExcerpt(localizedContent.content);
  const isoDate = viDateToISO(article.date);
  const imageUrl = article.thumbnail.startsWith('http')
    ? article.thumbnail
    : `${SITE_URL}${article.thumbnail}`;

  const galleryCaption = (image: GalleryImage) => captionFor(image, currentLang);

  const lightboxImages: LightboxImage[] = (article.gallery || []).map((img) => ({
    src: img.src,
    caption: galleryCaption(img),
  }));

  const jsonLd = [
    {
      '@context': 'https://schema.org',
      '@type': 'BlogPosting',
      headline: localizedContent.title,
      description: excerpt,
      image: imageUrl,
      datePublished: isoDate,
      dateModified: isoDate,
      inLanguage: currentLang,
      mainEntityOfPage: { '@type': 'WebPage', '@id': canonical },
      author: { '@type': 'Organization', name: SITE_NAME },
      publisher: {
        '@type': 'Organization',
        name: SITE_NAME,
        logo: { '@type': 'ImageObject', url: `${SITE_URL}/logo-tab.png` },
      },
    },
    {
      '@context': 'https://schema.org',
      '@type': 'BreadcrumbList',
      itemListElement: [
        { '@type': 'ListItem', position: 1, name: t('blog.breadcrumbHome'), item: SITE_URL },
        { '@type': 'ListItem', position: 2, name: t('blog.page.title'), item: `${SITE_URL}/blog` },
        { '@type': 'ListItem', position: 3, name: localizedContent.title },
      ],
    },
  ];

  return (
    <div className="bg-white py-16">
      <Seo
        title={localizedContent.title}
        description={excerpt}
        canonical={canonical}
        image={imageUrl}
        type="article"
        lang={currentLang}
        jsonLd={jsonLd}
      />

      <div className="container mx-auto px-4 max-w-3xl">
        {/* Breadcrumb */}
        <nav aria-label="Breadcrumb" className="text-sm text-gray-500 mb-6">
          <ol className="flex flex-wrap items-center gap-1">
            <li><Link to="/" className="hover:text-blue-600">{t('blog.breadcrumbHome')}</Link></li>
            <li aria-hidden="true">/</li>
            <li><Link to="/blog" className="hover:text-blue-600">{t('blog.page.title')}</Link></li>
            <li aria-hidden="true">/</li>
            <li className="text-gray-700 line-clamp-1" aria-current="page">{localizedContent.title}</li>
          </ol>
        </nav>

        <article>
          {/* Meta */}
          <div className="flex flex-wrap items-center gap-3 mb-3">
            {article.categories.map((cat) => (
              <span key={cat} className="text-xs font-semibold uppercase tracking-wide text-blue-600 bg-blue-50 px-3 py-1 rounded-full">
                {cat}
              </span>
            ))}
            {article.date && (
              <time dateTime={isoDate} className="text-sm text-gray-400">{article.date}</time>
            )}
          </div>

          {/* Title — H1 for SEO */}
          <h1 className="text-3xl md:text-4xl font-extrabold text-gray-900 leading-snug mb-6">
            {localizedContent.title}
          </h1>

          {/* Hero */}
          <img
            src={article.thumbnail}
            alt={localizedContent.title}
            className="w-full max-h-[500px] object-cover object-top rounded-2xl shadow-lg mb-8"
          />

          {/* Body */}
          <div className="text-gray-700 leading-relaxed text-base">
            <ArticleContent content={localizedContent.content} />
          </div>

          {/* Event gallery */}
          {article.gallery && article.gallery.length > 0 && (
            <ArticleGallery
              images={article.gallery}
              lang={currentLang}
              title={t('article.gallery')}
              onImageClick={setLightboxIndex}
            />
          )}
        </article>

        {/* Back link */}
        <div className="mt-12 pt-8 border-t border-gray-200">
          <Link to="/blog" className="inline-flex items-center gap-1 text-blue-600 hover:underline text-sm font-medium">
            ← {t('article.backToBlog')}
          </Link>
        </div>
      </div>

      <Lightbox
        images={lightboxImages}
        index={lightboxIndex}
        onClose={() => setLightboxIndex(null)}
        onNavigate={setLightboxIndex}
      />
    </div>
  );
};

export default ArticleDetailPage;
