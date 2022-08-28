/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./tauron/templates/**/*.html",
    "./tauron/static/src/**/*.js",
    "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms')
  ],
}
