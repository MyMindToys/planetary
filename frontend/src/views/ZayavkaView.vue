<template>
  <section class="page-content">
    <h1>Оставить заявку</h1>
    <p>Заполните форму — мы свяжемся с вами и подберём программу и время для вашего мероприятия.</p>

    <form class="form" @submit.prevent="onSubmit">
      <div class="form-group">
        <label for="name">Имя *</label>
        <input type="text" id="name" v-model="form.name" placeholder="Ваше имя" required>
      </div>
      <div class="form-group">
        <label for="phone">Телефон *</label>
        <input type="tel" id="phone" v-model="form.phone" placeholder="+7 (___) ___-__-__" required>
      </div>
      <div class="form-group">
        <label for="email">Email</label>
        <input type="email" id="email" v-model="form.email" placeholder="example@mail.ru">
      </div>
      <div class="form-group">
        <label for="date">Желаемая дата</label>
        <input type="date" id="date" v-model="form.date">
      </div>
      <div class="form-group">
        <label for="message">Сообщение</label>
        <textarea id="message" v-model="form.message" placeholder="Опишите мероприятие, количество гостей, помещение..."></textarea>
      </div>
      <button type="submit" class="btn-submit">Отправить заявку</button>
    </form>
  </section>
</template>

<script setup>
import { reactive } from 'vue'

const form = reactive({
  name: '',
  phone: '',
  email: '',
  date: '',
  message: '',
})

function onSubmit() {
  // Пока только статика — отправка на бэк потом
  console.log('Form:', form)
}
</script>
