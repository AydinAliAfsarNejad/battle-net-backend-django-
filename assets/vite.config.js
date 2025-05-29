import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'
export default defineConfig({
  plugins: [
    tailwindcss(),
  ],
})
module.exports = {
  theme: {
    extend: {
      screens: {
        'custom-lg': '1450px',
      },
    },
  },
}
