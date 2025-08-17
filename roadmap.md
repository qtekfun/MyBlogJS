# Plan de Proyecto: Blog Personal con Vue, Tailwind y Node.js

Este documento describe los pasos y requisitos para construir un blog personal estático como proyecto de aprendizaje. El stack tecnológico incluye Vue.js para el frontend, Tailwind CSS para el diseño, y Node.js para un script de gestión de contenidos. El blog se desplegará en GitHub Pages.

## Fases del Proyecto

El desarrollo se divide en fases priorizadas para asegurar un progreso incremental y organizado.

---

### Fase 1: El Esqueleto del Proyecto (Lo Mínimo Viable)

**Meta:** Tener una base funcional del blog, donde se puedan listar y visualizar artículos.

1.  **Configuración del Entorno de Desarrollo**
    * **Objetivo:** Crear el proyecto e instalar las dependencias principales.
    * **Acciones:**
        * Inicializar un nuevo proyecto con Vite y Vue: `npm create vite@latest`.
        * Instalar y configurar Tailwind CSS siguiendo la [guía oficial para Vite](https://tailwindcss.com/docs/guides/vite).
        * Instalar `vue-router` para la gestión de rutas: `npm install vue-router`.

2.  **Estructura del Contenido y Datos de Prueba**
    * **Objetivo:** Definir cómo se almacenarán los artículos.
    * **Acciones:**
        * Crear una carpeta en la raíz del proyecto llamada `/posts`.
        * Crear 2-3 archivos de ejemplo con la extensión `.md` (Markdown).
        * Cada archivo debe contener una sección de metadatos *Front Matter* y el contenido.

    * **Ejemplo de `mi-primer-post.md`:**
        ```markdown
        ---
        title: "Mi Primer Post"
        author: "Tu Nombre"
        date: "2025-08-17"
        published: true
        ---

        Este es el contenido de mi primer post, escrito en **Markdown**.
        Permite usar listas, enlaces y todo lo que Markdown soporta.
        ```

3.  **Página Principal (Home): Listado de Posts**
    * **Objetivo:** Leer los archivos Markdown y mostrar una lista de posts en la página de inicio.
    * **Acciones:**
        * Instalar `gray-matter` para parsear el Front Matter: `npm install gray-matter`.
        * En el componente de la página principal (`views/Home.vue`), crear una lógica para leer los archivos de `/posts` durante el proceso de build.
        * Parsear cada archivo para extraer sus metadatos y contenido.
        * Crear un array con los datos de todos los posts y ordenarlo por fecha (de más reciente a más antiguo).
        * En la plantilla HTML, iterar sobre el array para renderizar una tarjeta (`div`) por cada post, mostrando su título y fecha.

4.  **Rutas y Vista de Post Individual**
    * **Objetivo:** Permitir la navegación a una página que muestre el contenido completo de un post.
    * **Acciones:**
        * Configurar `vue-router` para manejar rutas dinámicas como `/post/:slug`. El `slug` puede ser el nombre del archivo.
        * Crear un nuevo componente `views/Post.vue`.
        * Este componente recibirá el `slug` de la URL, buscará el post correspondiente, y mostrará su `title`, `author`, `date` y `content`.
        * Instalar `markdown-it` para renderizar el contenido Markdown como HTML: `npm install markdown-it`.

---

### Fase 2: Estilo, Diseño y Páginas Estáticas

**Meta:** Aplicar un diseño coherente y añadir páginas de contenido estático.

1.  **Diseño y Componentes con Tailwind CSS**
    * **Objetivo:** Crear una interfaz de usuario atractiva y reutilizable.
    * **Acciones:**
        * Diseñar las tarjetas de los posts en la página principal con un estilo limpio, añadiendo efectos `hover`.
        * Estilizar la vista del post individual. Usar el plugin `@tailwindcss/typography` para dar formato profesional al contenido del artículo.
        * Crear un componente `Navbar.vue` para la navegación.
        * Implementar el menú de navegación: fijo en la parte superior izquierda en escritorio y un menú lateral ocultable (menú hamburguesa) para dispositivos móviles.

2.  **Crear la Página "About Me"**
    * **Objetivo:** Añadir una página estática con información sobre el autor.
    * **Acciones:**
        * Crear un nuevo componente `views/About.vue`.
        * Añadir la ruta estática `/about` en `vue-router` apuntando al nuevo componente.
        * Añadir el enlace "About Me" en el componente `Navbar.vue`.

---

### Fase 3: El Script de Gestión de Contenidos

**Meta:** Crear una herramienta de línea de comandos (CLI) para gestionar los posts de forma sencilla.

1.  **Preparación del Script Interactivo**
    * **Objetivo:** Configurar la base para el script de gestión en Node.js.
    * **Acciones:**
        * Crear una carpeta `/scripts` y dentro un archivo `manage.js`.
        * Instalar las dependencias necesarias para el script:
            * `inquirer`: Para crear prompts interactivos en la terminal.
            * `fs-extra`: Para facilitar las operaciones con el sistema de archivos.

2.  **Funcionalidad 1: Crear un Nuevo Post**
    * **Objetivo:** Automatizar la creación de nuevos archivos de artículo.
    * **Acciones:**
        * Usar `inquirer` para preguntar al usuario el `título` y `autor` del post.
        * Generar automáticamente un `slug` a partir del título (ej: `mi-nuevo-post`).
        * Generar la fecha actual y establecer `published: false` por defecto.
        * Crear un nuevo archivo `.md` en `/posts` con el `slug` como nombre y el Front Matter pre-rellenado.

3.  **Funcionalidad 2: Gestionar Visibilidad y Programación**
    * **Objetivo:** Modificar el estado de un post (publicado, borrador, programado).
    * **Acciones:**
        * El script debe listar todos los posts existentes.
        * El usuario podrá elegir un post y cambiar el valor de `published` a `true`/`false`.
        * El usuario podrá establecer o modificar el campo `date` para programar un post para el futuro.
        * **Lógica de "Programación"**: El blog solo mostrará posts donde `published: true` y `date` sea una fecha pasada. Esto se evalúa en el momento de construir el sitio.

---

### Fase 4: Funcionalidades Avanzadas y Despliegue

**Meta:** Añadir la búsqueda y publicar el blog en internet.

1.  **Barra de Búsqueda**
    * **Objetivo:** Permitir a los usuarios buscar artículos desde el cliente.
    * **Acciones:**
        * **Paso de compilación:** Crear un script que genere un archivo `search-index.json` en la carpeta `/public` durante el build. Este archivo contendrá un array con el `title`, `slug` y `content` de cada post.
        * **Frontend:**
            * Crear un componente de búsqueda en Vue.
            * Al montarse, el componente hará `fetch` del archivo `search-index.json`.
            * Instalar `fuse.js` (`npm install fuse.js`) para implementar una búsqueda "fuzzy" (difusa) que filtre los resultados a medida que el usuario escribe.

2.  **Despliegue en GitHub Pages**
    * **Objetivo:** Publicar el blog estático de forma gratuita y automatizada.
    * **Acciones:**
        * Crear un repositorio en GitHub y subir el código.
        * Configurar `vite.config.js` para establecer la `base` correcta para GitHub Pages.
        * Crear un workflow de **GitHub Actions** en `.github/workflows/deploy.yml`.
        * El workflow debe automatizar los siguientes pasos en cada `push` a la rama `main`:
            1.  Hacer checkout del código.
            2.  Instalar dependencias con `npm install`.
            3.  Construir el proyecto con `npm run build`.
            4.  Desplegar el contenido de la carpeta `/dist` resultante a la rama `gh-pages`.
        * Activar GitHub Pages en la configuración del repositorio para que sirva el contenido desde la rama `gh-pages`.
