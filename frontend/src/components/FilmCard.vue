<template>
  <article class="film-card">
    <router-link :to="{ name: 'film', params: { id: film.id } }" class="film-card__link">
      <div class="film-card__cover" :style="coverStyle">
        <span v-if="film.is_new" class="film-card__badge">Новинка</span>
      </div>
      <div class="film-card__body">
        <h2 class="film-card__title">{{ film.title }}</h2>
        <p v-if="metaLine" class="film-card__meta">{{ metaLine }}</p>
      </div>
    </router-link>
  </article>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  film: {
    type: Object,
    required: true,
  },
})

const coverStyle = computed(() => {
  if (props.film.cover) {
    return { backgroundImage: `url(${props.film.cover})` }
  }
  return {}
})

function ageStr(min, max) {
  if (min != null && max != null) return `${min}+ – ${max}+`
  if (min != null) return `${min}+`
  if (max != null) return `до ${max}+`
  return ''
}

const metaLine = computed(() => {
  const parts = []
  if (props.film.content_types?.length) parts.push(props.film.content_types.join(', '))
  if (props.film.genres?.length) parts.push(props.film.genres.join(', '))
  if (props.film.duration_minutes) parts.push(`${props.film.duration_minutes} мин`)
  const age = ageStr(props.film.age_rating_min, props.film.age_rating_max)
  if (age) parts.push(age)
  return parts.join(' · ')
})
</script>
