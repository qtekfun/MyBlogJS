---
title: "Configurando un proyecto Vue.js moderno"
author: "qtekfun"
date: "2025-08-18"
published: true
slug: "configurando-proyecto-vue-moderno"
excerpt: "Guía completa para configurar un proyecto Vue.js con las mejores prácticas y herramientas modernas."
tags: ["vue", "vite", "configuracion", "desarrollo"]
---

Configurar un proyecto Vue.js moderno puede parecer abrumador con tantas opciones disponibles. En este post te guío a través del proceso paso a paso.

## Herramientas esenciales

### Vite como bundler
Vite se ha convertido en mi herramienta favorita por su velocidad:

```bash
npm create vite@latest mi-proyecto -- --template vue
cd mi-proyecto
npm install
```

### ESLint y Prettier
Para mantener el código limpio y consistente:

```bash
npm install -D eslint prettier @vue/eslint-config-prettier
```

## Estructura de carpetas recomendada

```
src/
├── assets/          # Imágenes, iconos
├── components/      # Componentes reutilizables
├── composables/     # Lógica reutilizable
├── router/          # Configuración de rutas
├── stores/          # Estado global (Pinia)
├── views/           # Páginas/vistas
└── utils/           # Funciones auxiliares
```

## Configuración de Tailwind CSS

Tailwind CSS se integra perfectamente con Vite:

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

En `tailwind.config.js`:

```javascript
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts}'],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

## Vue Router para SPA

```bash
npm install vue-router@4
```

Configuración básica en `src/router/index.js`:

```javascript
import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/about', name: 'About', component: () => import('../views/About.vue') }
]

export default createRouter({
  history: createWebHistory(),
  routes
})
```

## Tips de productividad

1. **Usar Composition API**: Más flexible y reutilizable
2. **Crear composables**: Para lógica compartida
3. **Componentes pequeños**: Más fáciles de mantener
4. **TypeScript**: Para proyectos más grandes

## Próximos pasos

En el siguiente post hablaré sobre Pinia para el manejo de estado y cómo estructurar una aplicación más compleja.

¡Feliz codeo! 🚀
