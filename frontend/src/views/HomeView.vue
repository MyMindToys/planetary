<template>
  <div>
    <section class="hero">
      <div v-if="banners.length" class="hero-carousel">
        <div class="hero-carousel__track" :style="{ transform: `translateX(-${currentIndex * 100}%)` }">
          <div v-for="banner in banners" :key="banner.id" class="hero-carousel__slide">
            <img :src="banner.image" alt="Баннер" class="hero-carousel__img">
          </div>
        </div>
        <button v-if="banners.length > 1" @click="prevSlide" class="hero-carousel__btn hero-carousel__btn--prev">‹</button>
        <button v-if="banners.length > 1" @click="nextSlide" class="hero-carousel__btn hero-carousel__btn--next">›</button>
        <div v-if="banners.length > 1" class="hero-carousel__dots">
          <button v-for="(banner, i) in banners" :key="banner.id" @click="currentIndex = i" :class="['hero-carousel__dot', { 'hero-carousel__dot--active': i === currentIndex }]"></button>
        </div>
      </div>
      <div v-else class="hero-placeholder">
        <p>Место для карусели или баннера</p>
      </div>
    </section>

    <section class="buttons-section">
      <div class="buttons-grid">
        <template v-for="(card, i) in cards" :key="i">
          <router-link v-if="card.link && card.link !== '#' && card.link.startsWith('/')" :to="card.link" class="card-btn">
            <img v-if="card.image" :src="card.image" :alt="card.title">
            <div v-else class="card-btn__img"></div>
            <span>{{ card.title }}</span>
          </router-link>
          <a v-else :href="card.link || '#'" class="card-btn">
            <img v-if="card.image" :src="card.image" :alt="card.title">
            <div v-else class="card-btn__img"></div>
            <span>{{ card.title }}</span>
          </a>
        </template>
      </div>
    </section>

    <section class="about">
      <div class="about-inner">
        <h2 class="about-title">Мобильный планетарий Калейдоскоп</h2>
        <div class="about-block">
          <p>
            «Калейдоскоп» — это современный мобильный планетарий, который привозит звёздное небо к вам.
            Мы проводим полнокупольные программы для школ, детских садов, праздников и корпоративных мероприятий.
          </p>
          <p>
            Надувной купол, профессиональное оборудование и увлекательные фильмы о космосе, природе и науке
            создают эффект полного погружения. Подходит для помещений от 30 м² и аудитории до 50 человек.
          </p>
        </div>
        <div class="about-block">
          <p>
            Выберите программу в каталоге или оставьте заявку — мы подберём время и формат под ваше мероприятие.
          </p>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const defaultCards = [
  { title: 'Каталог фильмов', image: null, link: '/catalog' },
  { title: 'Оставить заявку', image: null, link: '/zayavka' },
  { title: 'Про помещение', image: null, link: '#' },
  { title: 'Про планетарий', image: null, link: '#' },
]

const cards = ref([...defaultCards])
const banners = ref([])
const currentIndex = ref(0)
let carouselInterval = null

function nextSlide() {
  currentIndex.value = (currentIndex.value + 1) % banners.value.length
}

function prevSlide() {
  currentIndex.value = (currentIndex.value - 1 + banners.value.length) % banners.value.length
}

onMounted(async () => {
  const apiBase = (import.meta.env.VITE_API_URL || '').replace(/\/$/, '')
  try {
    const [cardsRes, bannersRes] = await Promise.all([
      fetch(`${apiBase}/api/menu-cards/`),
      fetch(`${apiBase}/api/banners/`),
    ])
    if (cardsRes.ok) {
      const data = await cardsRes.json()
      if (data.cards && data.cards.length > 0) {
        cards.value = data.cards
      }
    }
    if (bannersRes.ok) {
      const data = await bannersRes.json()
      if (data.banners && data.banners.length > 0) {
        banners.value = data.banners
        if (banners.value.length > 1) {
          carouselInterval = setInterval(nextSlide, 5000)
        }
      }
    }
  } catch (_) {}
})

onUnmounted(() => {
  if (carouselInterval) clearInterval(carouselInterval)
})
</script>
