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
          <FilmCard v-for="film in films" :key="film.id" :film="film" />
        </div>
        <div v-if="totalPages > 1" class="catalog-pagination">
          <button @click="goToPage(currentPage - 1)" :disabled="currentPage === 1" class="catalog-pagination__btn">‹</button>
          <button v-for="p in visiblePages" :key="p" @click="goToPage(p)" :class="['catalog-pagination__btn', { 'catalog-pagination__btn--active': p === currentPage }]">{{ p }}</button>
          <button @click="goToPage(currentPage + 1)" :disabled="currentPage === totalPages" class="catalog-pagination__btn">›</button>
        </div>
        <p class="catalog-cta">
          Хотите заказать показ? <router-link to="/zayavka">Оставьте заявку</router-link> — мы подберём программу под ваше мероприятие.
        </p>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import FilmCard from '../components/FilmCard.vue'

const apiBase = (import.meta.env.VITE_API_URL || '').replace(/\/\s*$/, '')
const films = ref([])
const filterOptions = ref({ categories: [], genres: [], content_types: [] })
const selectedCategories = ref([])
const selectedGenres = ref([])
const selectedContentTypes = ref([])
const selectedAgeMin = ref(null)
const selectedAgeMax = ref(null)
const currentPage = ref(1)
const totalPages = ref(0)
const total = ref(0)
const loading = ref(false)

const visiblePages = computed(() => {
  const pages = []
  const maxVisible = 7
  let start = Math.max(1, currentPage.value - Math.floor(maxVisible / 2))
  let end = Math.min(totalPages.value, start + maxVisible - 1)
  if (end - start < maxVisible - 1) {
    start = Math.max(1, end - maxVisible + 1)
  }
  for (let i = start; i <= end; i++) {
    pages.push(i)
  }
  return pages
})

async function loadFilms() {
  loading.value = true
  try {
    const params = new URLSearchParams()
    params.append('page', currentPage.value.toString())
    params.append('page_size', '16')
    if (selectedCategories.value.length) {
      selectedCategories.value.forEach(c => params.append('categories', c))
    }
    if (selectedGenres.value.length) {
      selectedGenres.value.forEach(g => params.append('genres', g))
    }
    if (selectedContentTypes.value.length) {
      selectedContentTypes.value.forEach(t => params.append('content_types', t))
    }
    if (selectedAgeMin.value != null && selectedAgeMin.value !== '') {
      params.append('age_min', selectedAgeMin.value.toString())
    }
    if (selectedAgeMax.value != null && selectedAgeMax.value !== '') {
      params.append('age_max', selectedAgeMax.value.toString())
    }
    
    const res = await fetch(`${apiBase}/api/films/?${params}`)
    const data = await res.json()
    if (data.films) {
      films.value = data.films
      total.value = data.total || 0
      totalPages.value = data.total_pages || 0
    }
  } catch (_) {}
  loading.value = false
}

function goToPage(page) {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page
    loadFilms()
  }
}

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
    const filtersRes = await fetch(`${apiBase}/api/catalog-filters/`)
    const filtersData = await filtersRes.json()
    if (filtersData.categories) filterOptions.value.categories = filtersData.categories
    if (filtersData.genres) filterOptions.value.genres = filtersData.genres
    if (filtersData.content_types) filterOptions.value.content_types = filtersData.content_types
    await loadFilms()
  } catch (_) {}
})

// Перезагружаем при изменении фильтров
watch([selectedCategories, selectedGenres, selectedContentTypes, selectedAgeMin, selectedAgeMax], () => {
  currentPage.value = 1
  loadFilms()
})
</script>
