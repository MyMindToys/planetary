<template>
  <section class="page-content page-content--news">
    <h1>Новости</h1>
    <p class="news-intro">Актуальные события и анонсы мобильного планетария «Калейдоскоп».</p>

    <ul class="news-list">
      <li v-for="item in news" :key="item.id" class="news-item">
        <router-link :to="{ name: 'newsDetail', params: { id: item.id } }" class="news-item__link">
          <h2 class="news-title">{{ item.title }}</h2>
          <p class="news-date">{{ formatDate(item.date) }}</p>
          <p class="news-excerpt">{{ item.excerpt }}</p>
          <span class="news-item__more">Читать полностью →</span>
        </router-link>
      </li>
    </ul>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const apiBase = (import.meta.env.VITE_API_URL || '').replace(/\/\s*$/, '')
const news = ref([])

function formatDate(iso) {
  if (!iso) return ''
  const d = new Date(iso)
  return d.toLocaleDateString('ru-RU', { day: 'numeric', month: 'long', year: 'numeric' })
}

onMounted(async () => {
  try {
    const r = await fetch(`${apiBase}/api/news/`)
    const data = await r.json()
    if (data.news?.length) news.value = data.news
  } catch (_) {}
})
</script>
