<template>
  <section class="page-content page-content--catalog">
    <h1>Каталог фильмов</h1>
    <p class="catalog-intro">Полнокупольные программы для мобильного планетария. Подходят для детей и взрослых.</p>

    <div class="catalog-layout">
      <aside class="catalog-filters">
        <div class="catalog-filters__block">
          <h3 class="catalog-filters__title">Категория</h3>
          <label class="catalog-filters__check">
            <input type="checkbox" :checked="isAllSelected('categories')" @change="toggleAll('categories', $event.target.checked)">
            Все
          </label>
          <label v-for="opt in filterOptions.categories" :key="'cat-' + opt" class="catalog-filters__check">
            <input type="checkbox" :value="opt" v-model="selectedCategories">
            {{ opt }}
          </label>
        </div>
        <div class="catalog-filters__block">
          <h3 class="catalog-filters__title">Жанр</h3>
          <label class="catalog-filters__check">
            <input type="checkbox" :checked="isAllSelected('genres')" @change="toggleAll('genres', $event.target.checked)">
            Все
          </label>
          <label v-for="opt in filterOptions.genres" :key="'gen-' + opt" class="catalog-filters__check">
            <input type="checkbox" :value="opt" v-model="selectedGenres">
            {{ opt }}
          </label>
        </div>
        <div class="catalog-filters__block">
          <h3 class="catalog-filters__title">Тип контента</h3>
          <label class="catalog-filters__check">
            <input type="checkbox" :checked="isAllSelected('content_types')" @change="toggleAll('content_types', $event.target.checked)">
            Все
          </label>
          <label v-for="opt in filterOptions.content_types" :key="'ct-' + opt" class="catalog-filters__check">
            <input type="checkbox" :value="opt" v-model="selectedContentTypes">
            {{ opt }}
          </label>
        </div>
        <div class="catalog-filters__block">
          <h3 class="catalog-filters__title">Возраст</h3>
          <div class="catalog-filters__age">
            <label class="catalog-filters__age-label">
              от
              <input type="number" min="0" max="21" placeholder="—" v-model.number="selectedAgeMin">
            </label>
            <label class="catalog-filters__age-label">
              до
              <input type="number" min="0" max="21" placeholder="—" v-model.number="selectedAgeMax">
            </label>
          </div>
        </div>
      </aside>

      <div class="catalog-main">
        <div class="catalog-grid">
          <FilmCard v-for="film in filteredFilms" :key="film.id" :film="film" />
        </div>
        <p class="catalog-cta">
          Хотите заказать показ? <router-link to="/zayavka">Оставьте заявку</router-link> — мы подберём программу под ваше мероприятие.
        </p>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import FilmCard from '../components/FilmCard.vue'

const apiBase = (import.meta.env.VITE_API_URL || '').replace(/\/\s*$/, '')
const films = ref([])
const filterOptions = ref({ categories: [], genres: [], content_types: [] })
const selectedCategories = ref([])
const selectedGenres = ref([])
const selectedContentTypes = ref([])
const selectedAgeMin = ref(null)
const selectedAgeMax = ref(null)

const filteredFilms = computed(() => {
  let list = films.value
  if (selectedCategories.value.length) {
    list = list.filter(f => (f.categories || []).some(c => selectedCategories.value.includes(c)))
  }
  if (selectedGenres.value.length) {
    list = list.filter(f => (f.genres || []).some(g => selectedGenres.value.includes(g)))
  }
  if (selectedContentTypes.value.length) {
    list = list.filter(f => (f.content_types || []).some(t => selectedContentTypes.value.includes(t)))
  }
  const ageMin = selectedAgeMin.value != null && selectedAgeMin.value !== '' ? Number(selectedAgeMin.value) : null
  const ageMax = selectedAgeMax.value != null && selectedAgeMax.value !== '' ? Number(selectedAgeMax.value) : null
  if (ageMin != null || ageMax != null) {
    list = list.filter(f => {
      const fMin = f.age_rating_min != null ? f.age_rating_min : 0
      const fMax = f.age_rating_max != null ? f.age_rating_max : 99
      if (ageMin != null && ageMax != null) {
        return fMin <= ageMax && fMax >= ageMin
      }
      if (ageMin != null) return fMax >= ageMin
      return fMin <= ageMax
    })
  }
  return list
})

function isAllSelected(group) {
  const opts = filterOptions.value[group] || []
  const sel = group === 'categories' ? selectedCategories : group === 'genres' ? selectedGenres : selectedContentTypes
  return opts.length === 0 || sel.value.length === 0
}

function toggleAll(group, checked) {
  const opts = filterOptions.value[group] || []
  if (group === 'categories') selectedCategories.value = checked ? [...opts] : []
  else if (group === 'genres') selectedGenres.value = checked ? [...opts] : []
  else selectedContentTypes.value = checked ? [...opts] : []
}

onMounted(async () => {
  try {
    const [filmsRes, filtersRes] = await Promise.all([
      fetch(`${apiBase}/api/films/`),
      fetch(`${apiBase}/api/catalog-filters/`),
    ])
    const filmsData = await filmsRes.json()
    const filtersData = await filtersRes.json()
    if (filmsData.films?.length) films.value = filmsData.films
    if (filtersData.categories) filterOptions.value.categories = filtersData.categories
    if (filtersData.genres) filterOptions.value.genres = filtersData.genres
    if (filtersData.content_types) filterOptions.value.content_types = filtersData.content_types
  } catch (_) {}
})
</script>
