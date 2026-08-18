import React from 'react';

interface JsonLd {
  [key: string]: unknown;
}

interface SeoProps {
  title: string;
  description?: string;
  canonical?: string;
  image?: string;
  type?: 'website' | 'article';
  lang?: string;
  jsonLd?: JsonLd | JsonLd[];
  siteName?: string;
}

const DEFAULT_SITE = 'Tân Thành Công JSC';

/**
 * Renders document head tags. React 19 hoists <title>/<meta>/<link> to <head>
 * automatically, so no manual DOM manipulation is needed.
 */
const Seo: React.FC<SeoProps> = ({
  title,
  description,
  canonical,
  image,
  type = 'website',
  lang,
  jsonLd,
  siteName = DEFAULT_SITE,
}) => {
  const fullTitle = title.includes(siteName) ? title : `${title} | ${siteName}`;
  const blocks = jsonLd ? (Array.isArray(jsonLd) ? jsonLd : [jsonLd]) : [];

  if (lang && typeof document !== 'undefined') {
    document.documentElement.lang = lang;
  }

  return (
    <>
      <title>{fullTitle}</title>
      {description && <meta name="description" content={description} />}
      {canonical && <link rel="canonical" href={canonical} />}

      <meta property="og:title" content={fullTitle} />
      {description && <meta property="og:description" content={description} />}
      <meta property="og:type" content={type} />
      {canonical && <meta property="og:url" content={canonical} />}
      {image && <meta property="og:image" content={image} />}
      <meta property="og:site_name" content={siteName} />

      <meta name="twitter:card" content={image ? 'summary_large_image' : 'summary'} />
      <meta name="twitter:title" content={fullTitle} />
      {description && <meta name="twitter:description" content={description} />}
      {image && <meta name="twitter:image" content={image} />}

      {blocks.map((block, index) => (
        <script
          key={index}
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(block) }}
        />
      ))}
    </>
  );
};

export default Seo;
