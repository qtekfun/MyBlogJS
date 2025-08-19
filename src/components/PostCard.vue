<template>
  <article class="bg-white rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 overflow-hidden border border-gray-100">
    <!-- Header con tag featured si es el primer post -->
    <div v-if="featured" class="bg-gradient-to-r from-blue-600 to-purple-600 px-6 py-2">
      <span class="text-white text-sm font-medium">✨ Featured Post</span>
    </div>
    
    <!-- Contenido principal -->
    <div class="p-6">
      <!-- Título -->
      <h3 class="text-xl font-bold text-gray-900 mb-3 hover:text-blue-600 transition-colors cursor-pointer">
        {{ post.title }}
      </h3>
      
      <!-- Excerpt -->
      <p class="text-gray-600 leading-relaxed mb-4 line-clamp-2">
        {{ post.excerpt }}
      </p>
      
      <!-- Tags -->
      <div v-if="post.tags && post.tags.length > 0" class="flex flex-wrap gap-2 mb-4">
        <span 
          v-for="tag in post.tags.slice(0, 3)" 
          :key="tag"
          class="inline-block bg-blue-50 text-blue-700 text-xs px-2 py-1 rounded-full font-medium"
        >
          #{{ tag }}
        </span>
        <span 
          v-if="post.tags.length > 3" 
          class="inline-block bg-gray-100 text-gray-600 text-xs px-2 py-1 rounded-full"
        >
          +{{ post.tags.length - 3 }} más
        </span>
      </div>
      
      <!-- Footer con fecha y CTA -->
      <div class="flex items-center justify-between pt-4 border-t border-gray-100">
        <div class="flex items-center text-sm text-gray-500">
          <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path>
          </svg>
          {{ formatDate(post.date) }}
        </div>
        
        <router-link 
          :to="`/post/${post.slug}`"
          class="inline-flex items-center text-blue-600 hover:text-blue-800 font-medium text-sm transition-colors"
        >
          Leer más
          <svg class="w-4 h-4 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path>
          </svg>
        </router-link>
      </div>
    </div>
  </article>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  post: {
    type: Object,
    required: true
  },
  featured: {
    type: Boolean,
    default: false
  }
})

// Formatear fecha de manera más legible
const formatDate = (dateString) => {
  const date = new Date(dateString)
  return date.toLocaleDateString('es-ES', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>