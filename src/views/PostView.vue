<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50">
    <!-- Loading state -->
    <div v-if="loading" class="max-w-4xl mx-auto px-4 py-16">
      <div class="text-center">
        <p class="text-gray-600">Cargando post...</p>
      </div>
    </div>

    <!-- Error state -->
    <div v-else-if="error" class="max-w-4xl mx-auto px-4 py-16">
      <div class="bg-red-50 border border-red-200 rounded-lg p-6">
        <h2 class="text-red-800 font-bold mb-2">Post no encontrado</h2>
        <p class="text-red-600">{{ error }}</p>
        <router-link 
          to="/" 
          class="inline-block mt-4 text-blue-600 hover:text-blue-800 font-medium"
        >
          ← Volver al inicio
        </router-link>
      </div>
    </div>

    <!-- Post content -->
    <article v-else-if="post" class="max-w-4xl mx-auto px-4 py-8">
      <!-- Back button -->
      <router-link 
        to="/" 
        class="inline-flex items-center text-blue-600 hover:text-blue-800 font-medium mb-8 transition-colors"
      >
        <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
        </svg>
        Volver al blog
      </router-link>

      <!-- Post header -->
      <header class="bg-white rounded-xl shadow-lg p-8 mb-8">
        <h1 class="text-4xl font-bold text-gray-900 mb-4">{{ post.title }}</h1>
        
        <!-- Meta info -->
        <div class="flex flex-wrap items-center gap-4 text-sm text-gray-600 mb-6">
          <div class="flex items-center">
            <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path>
            </svg>
            {{ post.author }}
          </div>
          <div class="flex items-center">
            <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path>
            </svg>
            {{ formatDate(post.date) }}
          </div>
          <div class="flex items-center">
            <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
            {{ readingTime }} min lectura
          </div>
        </div>

        <!-- Tags -->
        <div v-if="post.tags && post.tags.length > 0" class="flex flex-wrap gap-2">
          <span 
            v-for="tag in post.tags" 
            :key="tag"
            class="bg-blue-50 text-blue-700 text-sm px-3 py-1 rounded-full font-medium"
          >
            #{{ tag }}
          </span>
        </div>
      </header>

      <!-- Post content -->
      <div class="bg-white rounded-xl shadow-lg p-8">
        <div 
          class="prose prose-lg max-w-none prose-headings:text-gray-900 prose-p:text-gray-700 prose-a:text-blue-600 prose-strong:text-gray-900"
          v-html="renderedContent"
        ></div>
      </div>

      <!-- Navigation -->
      <nav class="mt-12 border-t pt-8">
        <div class="flex justify-between items-center">
          <div v-if="previousPost">
            <p class="text-sm text-gray-500 mb-1">Post anterior</p>
            <router-link 
              :to="`/post/${previousPost.slug}`"
              class="text-blue-600 hover:text-blue-800 font-medium"
            >
              {{ previousPost.title }}
            </router-link>
          </div>
          <div v-if="nextPost" class="text-right">
            <p class="text-sm text-gray-500 mb-1">Siguiente post</p>
            <router-link 
              :to="`/post/${nextPost.slug}`"
              class="text-blue-600 hover:text-blue-800 font-medium"
            >
              {{ nextPost.title }}
            </router-link>
          </div>
        </div>
      </nav>
    </article>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { usePosts } from '@/composables/usePosts'
import MarkdownIt from 'markdown-it'

// Inicializar route, router y composable
const route = useRoute()
const router = useRouter()
const { posts, loading, error, loadPosts, getPostBySlug } = usePosts()

const post = ref(null)

// Configurar markdown-it
const md = new MarkdownIt({
  html: true,        // Permitir HTML
  linkify: true,     // Convertir URLs en links
  typographer: true  // Mejorar comillas y guiones
})

// Computed actualizado:
const renderedContent = computed(() => {
  if (!post.value) return ''
  // Convertir Markdown a HTML
  return md.render(post.value.content)
})

const readingTime = computed(() => {
  if (!post.value) return 0
  const wordsPerMinute = 200
  const wordCount = post.value.content.split(' ').length
  return Math.ceil(wordCount / wordsPerMinute)
})

const currentIndex = computed(() => {
  if (!post.value) return -1
  return posts.value.findIndex(p => p.slug === post.value.slug)
})

const previousPost = computed(() => {
  const index = currentIndex.value
  return index > 0 ? posts.value[index - 1] : null
})

const nextPost = computed(() => {
  const index = currentIndex.value
  return index < posts.value.length - 1 ? posts.value[index + 1] : null
})

// Methods
const formatDate = (dateString) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('es-ES', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}

const loadPost = async () => {
  const slug = route.params.slug
  
  if (posts.value.length === 0) {
    await loadPosts()
  }
  
  const foundPost = getPostBySlug(slug)
  if (foundPost) {
    post.value = foundPost
  } else {
    error.value = `Post "${slug}" no encontrado`
  }
}

// Watchers
watch(() => route.params.slug, loadPost)

// Lifecycle
onMounted(loadPost)
</script>

<style scoped>
/* Estilos mejorados para el contenido del post */
.prose {
  font-size: 1.1rem;
  line-height: 1.8;
  color: #374151;
}

.prose h1, .prose h2, .prose h3, .prose h4 {
  color: #111827;
  font-weight: 700;
  margin-top: 2.5rem;
  margin-bottom: 1.5rem;
  line-height: 1.2;
}

.prose h1 { 
  font-size: 2.5rem;
}

.prose h2 { 
  font-size: 2rem;
  border-bottom: 2px solid #e5e7eb;
  padding-bottom: 0.5rem;
}

.prose h3 { 
  font-size: 1.5rem;
}

.prose h4 { 
  font-size: 1.25rem;
}

.prose p {
  margin-bottom: 1.5rem;
  text-align: justify;
}

.prose ul, .prose ol {
  margin-bottom: 1.5rem;
  padding-left: 2rem;
}

.prose li {
  margin-bottom: 0.5rem;
}

.prose blockquote {
  border-left: 4px solid #3b82f6;
  background-color: #f8fafc;
  padding: 1rem 1.5rem;
  margin: 2rem 0;
  font-style: italic;
  border-radius: 0.5rem;
}

.prose code {
  background-color: #f1f5f9;
  color: #e11d48;
  padding: 0.25rem 0.5rem;
  border-radius: 0.375rem;
  font-size: 0.9rem;
  font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
  font-weight: 600;
}

.prose pre {
  background-color: #1e293b;
  color: #e2e8f0;
  padding: 1.5rem;
  border-radius: 0.75rem;
  overflow-x: auto;
  margin: 2rem 0;
  line-height: 1.5;
}

.prose pre code {
  background: transparent;
  color: inherit;
  padding: 0;
  font-weight: normal;
}

.prose strong {
  font-weight: 700;
  color: #111827;
}

.prose a {
  color: #2563eb;
  text-decoration: underline;
  text-underline-offset: 2px;
}

.prose a:hover {
  color: #1d4ed8;
  text-decoration-thickness: 2px;
}

.prose img {
  max-width: 100%;
  height: auto;
  border-radius: 0.5rem;
  margin: 2rem 0;
}
</style>