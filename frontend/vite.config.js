import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue_router from 'unplugin-vue-router/vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue_router(), vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
