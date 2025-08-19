import { ref, computed } from 'vue'
import fm from 'front-matter'

export function usePosts() {
  const posts = ref([])
  const loading = ref(false)
  const error = ref(null)

  const publishedPosts = computed(() =>
    posts.value.filter(post => post.published)
  )

  const sortedPosts = computed(() =>
    publishedPosts.value.sort((a, b) => new Date(b.date) - new Date(a.date))
  )

  const loadPosts = async () => {
    try {
      loading.value = true
      error.value = null

      const modules = import.meta.glob('/posts/*.md', { query: '?raw', import: 'default' })
      const loadedPosts = []

      for (const path in modules) {
        const content = await modules[path]()
        const slug = path.replace('/posts/', '').replace('.md', '')

        // Usar front-matter en lugar de gray-matter
        const { attributes: frontMatter, body: markdownContent } = fm(content)

        const post = {
          slug,
          title: frontMatter.title || 'Sin título',
          author: frontMatter.author || 'Anónimo',
          date: frontMatter.date || new Date().toISOString().split('T')[0],
          published: frontMatter.published !== false,
          excerpt: frontMatter.excerpt || '',
          tags: frontMatter.tags || [],
          content: markdownContent
        }

        loadedPosts.push(post)
      }

      posts.value = loadedPosts
    } catch (err) {
      error.value = err.message
      console.error('Error cargando posts:', err)
    } finally {
      loading.value = false
    }
  }

  const getPostBySlug = (slug) => {
    return posts.value.find(post => post.slug === slug)
  }

  return {
    posts,
    loading,
    error,
    publishedPosts,
    sortedPosts,
    loadPosts,
    getPostBySlug
  }
}