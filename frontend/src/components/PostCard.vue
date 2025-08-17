<template>
  <!-- Aquí irá tu HTML -->
  <div class="bg-white rounded-lg shadow p-6">
    <!-- Usar las props directamente con post.propiedad -->
    <h3>{{ post.title }}</h3>
    <p>{{ post.excerpt }}</p>
    <span>{{ post.date }}</span>
  </div>
</template>

<script setup>
  <!-- Aquí irá tu lógica de Vue -->
  import { computed } from 'vue'
  const props = defineProps({
    post: {
      type: Object,
      required: true
    }
  })
</script>

<style scoped>
  <!-- Aquí irán tus estilos personalizados (si necesitas) -->
</style>
