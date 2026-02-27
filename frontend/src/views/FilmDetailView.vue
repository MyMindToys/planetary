<template>
  <section class="page-content page-content--film">
    <div v-if="loading" class="film-detail film-detail--loading">Загрузка...</div>
    <div v-else-if="film" class="film-detail">
      <router-link to="/catalog" class="film-detail__back">← В каталог</router-link>
      <div class="film-detail__top">
        <div class="film-detail__cover" :style="coverStyle">
          <span v-if="film.is_new" class="film-detail__badge">Новинка</span>
        </div>
        <div class="film-detail__info">
          <h1 class="film-detail__title">{{ film.title }}</h1>
          <dl v-if="metaList.length" class="film-detail__meta">
            <template v-for="item in metaList" :key="item.label">
              <dt>{{ item.label }}</dt>
              <dd>{{ item.value }}</dd>
            </template>
          </dl>
          <p v-if="film.description" class="film-detail__desc">{{ film.description }}</p>
        </div>
      </div>
    </div>
    <div v-else class="film-detail">Фильм не найден.</div>
  </section>
</template>

<script setup>
import { ref, computed, watch, onMounted } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const apiBase = (import.meta.env.VITE_API_URL || '').replace(/\/\s*$/, '')
const film = ref(null)
const loading = ref(true)

const coverStyle = computed(() => {
  if (film.value?.cover) return { backgroundImage: `url(${film.value.cover})` }
  return {}
})

function ageStr(min, max) {
  if (min != null && max != null) return `${min}+ – ${max}+`
  if (min != null) return `${min}+`
  if (max != null) return `до ${max}+`
  return ''
}

const metaList = computed(() => {
  if (!film.value) return []
  const list = []
  if (film.value.content_types?.length)
    list.push({ label: 'Тип контента', value: film.value.content_types.join(', ') })
  if (film.value.genres?.length)
    list.push({ label: 'Жанр', value: film.value.genres.join(', ') })
  if (film.value.categories?.length)
    list.push({ label: 'Категория', value: film.value.categories.join(', ') })
  if (film.value.duration_minutes)
    list.push({ label: 'Длительность', value: `${film.value.duration_minutes} мин` })
  const age = ageStr(film.value.age_rating_min, film.value.age_rating_max)
  if (age) list.push({ label: 'Возраст', value: age })
  return list
})

async function fetchFilm() {
  const id = route.params.id
  if (!id) return
  loading.value = true
  film.value = null
  try {
    const r = await fetch(`${apiBase}/api/films/${id}/`)
    if (r.ok) film.value = await r.json()
  } catch (_) {}
  loading.value = false
}

onMounted(fetchFilm)
watch(() => route.params.id, fetchFilm)
</script>
