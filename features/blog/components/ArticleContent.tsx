import React, { useMemo, useState } from 'react';
import Lightbox, { LightboxImage } from './Lightbox';

interface ContentPart {
  type: 'text' | 'image';
  content: string;
}

interface ParsedImage {
  filename: string;
  layout: string;
  caption: string;
}

const parseImageToken = (token: string): ParsedImage => {
  const segments = token.split(':');
  return {
    filename: segments[0],
    layout: segments[1] || 'full',
    caption: segments.slice(2).join(':') || '',
  };
};

const splitContent = (content: string): ContentPart[] => {
  if (!content) return [];
  const imageRegex = /\[IMAGE:(.*?)\]/g;
  const parts: ContentPart[] = [];
  let lastIndex = 0;
  let match: RegExpExecArray | null;

  while ((match = imageRegex.exec(content)) !== null) {
    if (match.index > lastIndex) {
      parts.push({ type: 'text', content: content.substring(lastIndex, match.index) });
    }
    parts.push({ type: 'image', content: match[1] });
    lastIndex = match.index + match[0].length;
  }
  if (lastIndex < content.length) {
    parts.push({ type: 'text', content: content.substring(lastIndex) });
  }
  return parts;
};

const imageClass = (layout: string): string => {
  switch (layout) {
    case 'center': return 'mx-auto max-h-72 object-contain rounded-xl shadow-md w-full';
    case 'wide': return 'mx-auto max-h-96 object-contain rounded-xl shadow-md w-full';
    case 'full':
    default: return 'w-full h-auto object-contain rounded-xl shadow-md';
  }
};

const wrapClass = (layout: string): string => {
  switch (layout) {
    case 'center': return 'my-8 max-w-lg mx-auto';
    case 'wide': return 'my-8 max-w-3xl mx-auto';
    default: return 'my-8';
  }
};

const renderTextBlock = (text: string, key: number) => (
  <div key={key}>
    {text.split('\n').map((line, lineIndex) => {
      if (line.startsWith('## ')) {
        return (
          <h2 key={lineIndex} className="text-2xl font-bold text-gray-800 mt-10 mb-4 border-l-4 border-blue-600 pl-4">
            {line.replace(/^## /, '')}
          </h2>
        );
      }
      if (line.startsWith('# ')) {
        return (
          <h2 key={lineIndex} className="text-2xl font-bold text-gray-800 mt-10 mb-4">
            {line.replace(/^# /, '')}
          </h2>
        );
      }
      if (line.startsWith('- ')) {
        return (
          <li key={lineIndex} className="text-gray-700 leading-relaxed mb-2 ml-6 list-disc">
            {line.replace(/^- /, '')}
          </li>
        );
      }
      if (line.trim()) {
        return (
          <p key={lineIndex} className="text-gray-700 leading-relaxed mb-4 text-base">
            {line}
          </p>
        );
      }
      return null;
    })}
  </div>
);

interface ArticleContentProps {
  content: string;
}

/**
 * Shared renderer for article body text + inline [IMAGE:file:layout:caption]
 * tokens (technical diagrams). Inline images open in a self-contained lightbox.
 */
const ArticleContent: React.FC<ArticleContentProps> = ({ content }) => {
  const [lightboxIndex, setLightboxIndex] = useState<number | null>(null);

  const parts = useMemo(() => splitContent(content), [content]);

  const inlineImages = useMemo<LightboxImage[]>(
    () =>
      parts
        .filter((p) => p.type === 'image')
        .map((p) => {
          const { filename, caption } = parseImageToken(p.content);
          return { src: `/blog-assets/${filename}`, caption };
        }),
    [parts]
  );

  let imageCounter = -1;

  return (
    <>
      {parts.map((part, index) => {
        if (part.type === 'text') {
          return renderTextBlock(part.content, index);
        }
        imageCounter += 1;
        const imgIndex = imageCounter;
        const { filename, layout, caption } = parseImageToken(part.content);
        return (
          <figure key={index} className={wrapClass(layout)}>
            <img
              src={`/blog-assets/${filename}`}
              alt={caption || `Hình ảnh bài viết ${imgIndex + 1}`}
              loading="lazy"
              decoding="async"
              className={`${imageClass(layout)} cursor-zoom-in`}
              onClick={() => setLightboxIndex(imgIndex)}
            />
            {caption && (
              <figcaption className="text-center text-sm text-gray-400 italic mt-2 px-4">
                {caption}
              </figcaption>
            )}
          </figure>
        );
      })}

      <Lightbox
        images={inlineImages}
        index={lightboxIndex}
        onClose={() => setLightboxIndex(null)}
        onNavigate={setLightboxIndex}
      />
    </>
  );
};

export default ArticleContent;
