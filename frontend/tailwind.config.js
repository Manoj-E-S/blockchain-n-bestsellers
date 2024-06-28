/** @type {import('tailwindcss').Config} */

export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        "darkBrown": "#2a190c",
        "brown": "#572f16",
        "gold": "#bc733f",
        "bronze": "#a16e4b",
        "cream": "#d4bfa5"
    },
    backgroundImage: {
      "stack": "url('assets/books-stack.jpg')",
      "stack1": "url('assets/books-stack1.jpg')",
      "library": "url('assets/library.jpg')"
    },
    fontFamily: {
      "gallient": ['"Gallient"', 'serif'],
      "raleway": ['"Raleway"', 'sans-serif'],
      "greatVibes": ['"Great Vibes"', 'cursive'],
    },
    boxShadow: {
      'customShadow': '4.6px 9.1px 9.1px rgba(0, 0, 0, 0.36)',
    },
  },
}
}
