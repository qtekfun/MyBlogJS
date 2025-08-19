<template>
  <div
    class="min-h-screen w-full bg-gradient-to-br from-blue-50 to-white-50 overflow-x-hidden"
  >
    <!-- Hero Header -->
    <header class="relative overflow-hidden bg-white shadow-lg">
      <div class="absolute inset-0 bg-gradient-to-r from-blue-600 to-white-600 opacity-10"></div>
      <div class="relative max-w-full mx-auto px-4 sm:px-6 lg:px-8 py-8 sm:py-12 lg:py-16">
        <div class="text-center">
          <h1
            class="text-3xl sm:text-4xl md:text-5xl lg:text-6xl font-extrabold text-gray-900 mb-3 sm:mb-4"
          >
            Qtekfun's
            <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-white-600"
              >Site</span
            >
          </h1>
          <p class="text-base sm:text-lg md:text lg:text-xl text-gray-600 mx-auto">
            Explorando tecnología, ideas y experiencias digitales
          </p>
        </div>
      </div>
    </header>

    <!-- Main Content -->
    <main class="max-w-full mx-auto px-4 sm:px-6 lg:px-8 py-6 sm:py-8 lg:py-12">
      <div class="grid gap-6 sm:gap-8 lg:gap-12">
        <!-- Featured Post - responsive -->
          <div
            v-if="sortedPosts.length > 0"
            class="bg-white rounded-xl sm:rounded-2xl shadow-xl overflow-hidden hover:shadow-2xl transition-shadow duration-300 mx-[25%] mx-auto"
          >
          <div class="p-4 sm:p-6 lg:p-8 xl:p-12">
            <div class="flex items-center mb-3 sm:mb-4">
              <div class="h-2 w-2 bg-blue-500 rounded-full mr-2 sm:mr-3"></div>
              <span class="text-xs sm:text-sm font-medium text-blue-600">Featured Post</span>
            </div>
            <h2 class="text-xl sm:text-2xl lg:text-3xl font-bold text-gray-900 mb-4 sm:mb-6">
              {{ sortedPosts[0].title }}
            </h2>
            <p class="text-sm sm:text-base lg:text-lg text-gray-600 leading-relaxed mb-6 sm:mb-8">
              {{ sortedPosts[0].excerpt }}
            </p>
            <router-link
              :to="`/post/${sortedPosts[0].slug}`"
              class="inline-flex items-center px-4 sm:px-6 py-2 sm:py-3 border border-transparent text-sm sm:text-base font-medium rounded-lg text-white bg-blue-50 from-blue-600 to-white-600 hover:from-blue-700 hover:to-white-700 transition-all duration-200"
            >
              Read More
              <svg
                class="ml-2 h-4 w-4 sm:h-5 sm:w-5"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M17 8l4 4m0 0l-4 4m4-4H3"
                ></path>
              </svg>
            </router-link>
          </div>
        </div>

        <!-- Posts Recientes - responsive grid -->
        <section v-if="!loading && !error">
          <h2 class="text-xl sm:text-2xl font-bold text-gray-900 mb-6 sm:mb-8 px-2 sm:px-0">
            Posts Recientes
          </h2>

          <!-- Grid responsive: 1 col en móvil, 2 en tablet, 3 en desktop -->
          <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4 sm:gap-6 lg:gap-8">
            <PostCard
              v-for="post in sortedPosts.slice(1)"
              :key="post.slug"
              :post="post"
              :featured="false"
            />
          </div>
        </section>

        <!-- Loading state -->
        <div v-if="loading" class="text-center py-8 sm:py-12">
          <div class="inline-flex items-center px-4 py-2 text-sm font-medium text-gray-600">
            <svg
              class="animate-spin -ml-1 mr-3 h-4 w-4 sm:h-5 sm:w-5"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
            >
              <circle
                class="opacity-25"
                cx="12"
                cy="12"
                r="10"
                stroke="currentColor"
                stroke-width="4"
              ></circle>
              <path
                class="opacity-75"
                fill="currentColor"
                d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
              ></path>
            </svg>
            Cargando posts...
          </div>
        </div>

        <!-- Error state -->
        <div v-if="error" class="text-center py-8 sm:py-12">
          <div class="bg-red-50 border border-red-200 rounded-lg p-4 sm:p-6 max-w-md mx-auto">
            <p class="text-red-600 text-sm sm:text-base">Error: {{ error }}</p>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import PostCard from './PostCard.vue'
import { usePosts } from '@/composables/usePosts'

// Usar el composable
const { loading, error, sortedPosts, loadPosts } = usePosts()

// Cargar posts cuando se monte el componente
onMounted(() => {
  loadPosts()
})
</script>
