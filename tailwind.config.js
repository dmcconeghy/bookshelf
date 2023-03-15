/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: "jit",
  content: [
    "./**/*.{html,js,j2}",
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require("flowbite/plugin")
  ],
}
