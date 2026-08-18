import path from 'path';
import { defineConfig, loadEnv } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig(({ mode }) => {
    const env = loadEnv(mode, '.', '');
    return {
      server: {
        port: 3000,
        host: '0.0.0.0',
      },
      preview: {
        port: 3001,
        host: '0.0.0.0',
      },
      plugins: [react()],
      define: {
        'process.env.API_KEY': JSON.stringify(env.GEMINI_API_KEY),
        'process.env.GEMINI_API_KEY': JSON.stringify(env.GEMINI_API_KEY)
      },
      resolve: {
        alias: {
          '@': path.resolve(__dirname, '.'),
        }
      },
      build: {
        rollupOptions: {
          output: {
            manualChunks: undefined,
            entryFileNames: 'assets/js/[name]-[hash].js',
            chunkFileNames: 'assets/js/[name]-[hash].js',
            assetFileNames: (assetInfo) => {
              if (/\.(css)$/.test(assetInfo.name || '')) {
                return 'assets/css/[name]-[hash][extname]';
              }
              if (/\.(png|jpe?g|gif|svg|webp|ico)$/.test(assetInfo.name || '')) {
                return 'assets/images/[name]-[hash][extname]';
              }
              return 'assets/[name]-[hash][extname]';
            },
          },
        },
      },
    };
});
