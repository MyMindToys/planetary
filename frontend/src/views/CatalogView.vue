<template>
  <section class="page-content page-content--catalog">
    <h1>Каталог фильмов</h1>
    <p>Полнокупольные программы для мобильного планетария. Подходят для детей и взрослых.</p>

    <div class="catalog-grid">
      <article v-for="film in films" :key="film.title" class="catalog-card">
        <div class="catalog-card__img" :style="film.cover ? { backgroundImage: `url(${film.cover})` } : {}"></div>
        <div class="catalog-card__body">
          <h2 class="catalog-card__title"><a href="#">{{ film.title }}</a></h2>
          <p class="catalog-card__desc">{{ filmDesc(film) }}</p>
        </div>
      </article>
    </div>

    <p class="catalog-cta">
      Хотите заказать показ? <router-link to="/zayavka">Оставьте заявку</router-link> — мы подберём программу под ваше мероприятие.
    </p>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const apiBase = (import.meta.env.VITE_API_URL || '').replace(/\/\s*$/, '')
const films = ref([])

function filmDesc(film) {
  const parts = []
  if (film.content_types?.length) parts.push(film.content_types.join(', '))
  if (film.genres?.length) parts.push(film.genres.join(', '))
  if (film.duration_minutes) parts.push(`${film.duration_minutes} мин`)
  const age = ageStr(film.age_rating_min, film.age_rating_max)
  if (age) parts.push(age)
  const line = parts.join(' · ')
  return line ? `${line}. ${film.description || ''}`.trim() : (film.description || '')
}

function ageStr(min, max) {
  if (min != null && max != null) return `${min}+–${max}+`
  if (min != null) return `${min}+`
  if (max != null) return `до ${max}+`
  return ''
}

onMounted(async () => {
  try {
    const r = await fetch(`${apiBase}/api/films/`)
    const data = await r.json()
    if (data.films?.length) films.value = data.films
  } catch (_) {}
})
</script>
