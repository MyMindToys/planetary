<template>
  <section class="page-content page-content--news-detail">
    <div v-if="loading" class="news-detail news-detail--loading">Загрузка...</div>
    <div v-else-if="item" class="news-detail">
      <router-link to="/news" class="news-detail__back">← К новостям</router-link>
      <article>
        <h1 class="news-detail__title">{{ item.title }}</h1>
        <p class="news-detail__date">{{ formatDate(item.date) }}</p>
        <p v-if="item.excerpt" class="news-detail__excerpt">{{ item.excerpt }}</p>
        <div v-if="item.body" class="news-detail__body" v-html="item.body"></div>
        <div v-else-if="item.excerpt" class="news-detail__body"><p>{{ item.excerpt }}</p></div>

        <section v-if="item.gallery?.length" class="news-detail__gallery">
          <h2 class="news-detail__gallery-title">Галерея</h2>
          <div class="news-detail__gallery-grid">
            <figure v-for="(img, i) in item.gallery" :key="i" class="news-detail__gallery-item">
              <img :src="img.url" :alt="img.caption || ''" loading="lazy">
              <figcaption v-if="img.caption">{{ img.caption }}</figcaption>
            </figure>
          </div>
        </section>
      </article>
    </div>
    <div v-else class="news-detail">Новость не найдена.</div>
  </section>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const apiBase = (import.meta.env.VITE_API_URL || '').replace(/\/\s*$/, '')
const item = ref(null)
const loading = ref(true)

function formatDate(iso) {
  if (!iso) return ''
  const d = new Date(iso)
  return d.toLocaleDateString('ru-RU', { day: 'numeric', month: 'long', year: 'numeric' })
}

async function fetchNews() {
  const id = route.params.id
  if (!id) return
  loading.value = true
  item.value = null
  try {
    const r = await fetch(`${apiBase}/api/news/${id}/`)
    if (r.ok) item.value = await r.json()
  } catch (_) {}
  loading.value = false
}

onMounted(fetchNews)
watch(() => route.params.id, fetchNews)
</script>
