/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        agro: {
          50: '#f2f9f0',
          100: '#e1f2dd',
          200: '#c5e5be',
          300: '#9ed394',
          400: '#72ba65',
          500: '#4e9f40',
          600: '#3c8130',
          700: '#306627',
          800: '#2a5123',
          900: '#24441f',
          950: '#0f250c',
        },
        earth: {
          50: '#fbf8f4',
          100: '#f5efe6',
          200: '#eadecd',
          300: '#d9c5ab',
          400: '#c4a683',
          500: '#b48d64',
          600: '#a37754',
          700: '#885f44',
          800: '#6f4f3c',
          900: '#5b4133',
        },
      },
    },
  },
  plugins: [],
}
