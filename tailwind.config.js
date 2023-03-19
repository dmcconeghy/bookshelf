/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: "jit",
  content: [
    "./**/*.{html,js,j2}",
  ],
  darkMode: 'class',
  plugins: [
    require("flowbite/plugin")
  ],
  theme: {
    extend: {},
  },
}
