<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50">
    <!-- Hero Header -->
    <header class="relative overflow-hidden bg-white shadow-lg">
      <div class="absolute inset-0 bg-gradient-to-r from-blue-600 to-purple-600 opacity-10"></div>
      <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div class="text-center">
          <h1 class="text-5xl md:text-6xl font-extrabold text-gray-900 mb-4">
            Qtekfun's
            <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-purple-600"
              >Site</span
            >
          </h1>
          <p class="text-xl text-gray-600 max-w-2xl mx-auto">
            Explorando tecnología, ideas y experiencias digitales
          </p>
        </div>
      </div>
    </header>

    <!-- Main Content -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div class="grid gap-8 md:gap-12">
        <!-- Featured Post -->
        <div
          class="bg-white rounded-2xl shadow-xl overflow-hidden hover:shadow-2xl transition-shadow duration-300"
        >
          <div class="p-8 md:p-12">
            <div class="flex items-center mb-4">
              <div class="h-2 w-2 bg-green-500 rounded-full mr-3"></div>
              <span class="text-sm font-medium text-green-600">Featured Post</span>
            </div>
            <h2 class="text-3xl font-bold text-gray-900 mb-6">My thoughts are expected here</h2>
            <p class="text-lg text-gray-600 leading-relaxed mb-8">
              More soon. Stay tuned for exciting content about technology, development, and digital
              experiences.
            </p>
            <button
              class="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-lg text-white bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 transition-all duration-200"
            >
              Read More
              <svg class="ml-2 h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M17 8l4 4m0 0l-4 4m4-4H3"
                ></path>
              </svg>
            </button>
          </div>
        </div>

        <!-- Posts Recientes -->
        <section>
          <h2 class="text-2xl font-bold text-gray-900 mb-8">Posts Recientes</h2>

          <div class="space-y-6">
            <PostCard
              v-for="post in sortedPosts"
              :key="post.slug"
              :post="post"
              :featured="index === 0"
            />
          </div>
        </section>
      </div>
    </main>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import PostCard from './PostCard.vue'
import { usePosts } from '@/composables/usePosts'

// Usar el composable
const { posts, loading, error, sortedPosts, loadPosts } = usePosts()

// Cargar posts cuando se monte el componente
onMounted(() => {
  loadPosts()
})
</script>
