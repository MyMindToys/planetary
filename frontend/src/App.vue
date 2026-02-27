<template>
  <div class="app">
    <header class="header">
      <div class="header-inner">
        <router-link to="/" class="logo">Калейдоскоп</router-link>
        <nav class="nav">
          <router-link to="/">Главная</router-link>
          <router-link to="/catalog">Каталог фильмов</router-link>
          <router-link to="/news">Новости</router-link>
          <router-link to="/zayavka">Оставить заявку</router-link>
        </nav>
        <div class="contacts">
          <a href="tel:+79001234567">+7 (900) 123-45-67</a>
        </div>
      </div>
    </header>

    <main>
      <router-view />
    </main>

    <footer class="footer">
      <div class="footer-inner">
        <p>© Мобильный планетарий Калейдоскоп</p>
        <p><a href="tel:+79001234567">+7 (900) 123-45-67</a></p>
      </div>
    </footer>
  </div>
</template>

<script setup>
</script>
