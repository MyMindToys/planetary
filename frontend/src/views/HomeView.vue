<template>
  <div>
    <section class="hero">
      <div class="hero-placeholder">
        <p>Место для карусели или баннера</p>
      </div>
    </section>

    <section class="buttons-section">
      <div class="buttons-grid">
        <router-link to="/catalog" class="card-btn">
          <img src="/img/2026-01-31_09-29-06.png" alt="Каталог фильмов">
          <span>Каталог фильмов</span>
        </router-link>
        <router-link to="/zayavka" class="card-btn">
          <img src="/img/2026-01-31_09-29-21.png" alt="Оставить заявку">
          <span>Оставить заявку</span>
        </router-link>
        <a href="#" class="card-btn">
          <img src="/img/2026-01-31_09-29-46.png" alt="Про помещение">
          <span>Про помещение</span>
        </a>
        <a href="#" class="card-btn">
          <img src="/img/2026-01-31_09-29-54.png" alt="Про планетарий">
          <span>Про планетарий</span>
        </a>
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
</script>
