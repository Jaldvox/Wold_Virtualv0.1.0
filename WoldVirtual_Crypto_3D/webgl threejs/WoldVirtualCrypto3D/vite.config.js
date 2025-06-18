import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    open: true,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true
      },
      '/ws': {
        target: 'ws://localhost:8000',
        ws: true
      }
    },
  },
  build: {
    outDir: 'dist',
    sourcemap: true,
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src/frontend'),
      '@components': path.resolve(__dirname, './src/frontend/components'),
      '@hooks': path.resolve(__dirname, './src/frontend/hooks'),
      '@utils': path.resolve(__dirname, './src/frontend/utils'),
      '@assets': path.resolve(__dirname, './src/frontend/assets'),
      '@styles': path.resolve(__dirname, './src/frontend/styles')
    },
  },
})