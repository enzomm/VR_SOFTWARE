import path from "path";
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import tailwind from "tailwindcss";
import autoprefixer from "autoprefixer";

// Exports the Vite configuration using the 'defineConfig' function.
export default defineConfig({
  css: {
    postcss: {
      plugins: [tailwind(), autoprefixer()], // PostCSS plugin settings: Tailwind CSS and Autoprefixer.
    },
  },
  plugins: [vue()], // Adds the Vue plugin to Vite.
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"), // Creates a shortcut '@' that points to the 'src' folder.
    },
  },
  server: {
    host: 'localhost', // Sets the host address of the development server. Replace with your local IP if necessary.
    port: 5173, // Sets the development server port.
  },
});
