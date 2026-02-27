<template>
  <section class="page-content page-content--catalog">
    <h1>Каталог фильмов</h1>
    <p>Полнокупольные программы для мобильного планетария. Подходят для детей и взрослых.</p>

    <div class="catalog-grid">
      <article v-for="film in films" :key="film.title" class="catalog-card">
        <div class="catalog-card__img"></div>
        <div class="catalog-card__body">
          <h2 class="catalog-card__title"><a href="#">{{ film.title }}</a></h2>
          <p class="catalog-card__desc">{{ film.desc }}</p>
        </div>
      </article>
    </div>

    <p class="catalog-cta">
      Хотите заказать показ? <router-link to="/zayavka">Оставьте заявку</router-link> — мы подберём программу под ваше мероприятие.
    </p>
  </section>
</template>

<script setup>
const films = [
  { title: 'Космическая одиссея', desc: 'Для всей семьи · 25 мин · 6+. Полнокупольное путешествие по Солнечной системе.' },
  { title: 'Звёздное небо над нами', desc: 'Образовательная · 30 мин · 8+. Узнайте, как устроено небо и что видят астрономы.' },
  { title: 'Путешествие к планетам', desc: 'Детская программа · 20 мин · 4+. Приключение для самых маленьких зрителей.' },
  { title: 'Тёмная материя', desc: 'Научно-популярная · 35 мин · 12+. Загадки Вселенной и современная астрофизика.' },
  { title: 'Сказки звёздного неба', desc: 'Для малышей · 15 мин · 3+. Добрые истории под куполом планетария.' },
  { title: 'Рождённые звёздами', desc: 'Для всей семьи · 28 мин · 6+. Как рождаются звёзды и планеты.' },
]
</script>
