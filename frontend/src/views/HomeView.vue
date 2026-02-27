<template>
  <div>
    <section class="hero">
      <div class="hero-placeholder">
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
import { ref, onMounted } from 'vue'

const defaultCards = [
  { title: 'Каталог фильмов', image: null, link: '/catalog' },
  { title: 'Оставить заявку', image: null, link: '/zayavka' },
  { title: 'Про помещение', image: null, link: '#' },
  { title: 'Про планетарий', image: null, link: '#' },
]

const cards = ref([...defaultCards])

onMounted(async () => {
  try {
    const apiBase = (import.meta.env.VITE_API_URL || '').replace(/\/$/, '')
    const res = await fetch(`${apiBase}/api/menu-cards/`)
    if (res.ok) {
      const data = await res.json()
      if (data.cards && data.cards.length > 0) {
        cards.value = data.cards
      }
    }
  } catch (_) {}
})
</script>
