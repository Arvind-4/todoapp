export const plugins = [
    require('tailwindcss'),
    require('autoprefixer'),
    require('cssnano')({
        preset: 'default',
    }),
];