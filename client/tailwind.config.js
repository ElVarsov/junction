/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  presets: [require("nativewind/preset")],
  theme: {
    extend: {},
    colors: {
      primary: "#1450F5",
    },
  },
  future: {
    hoverOnlyWhenSupported: true,
  },
  plugins: [],
};
