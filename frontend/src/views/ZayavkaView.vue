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
      <div v-if="error" class="form-error">{{ error }}</div>
      <div v-if="success" class="form-success">Заявка успешно отправлена! Мы свяжемся с вами в ближайшее время.</div>
      <button type="submit" class="btn-submit" :disabled="submitting">
        {{ submitting ? 'Отправка...' : 'Отправить заявку' }}
      </button>
    </form>
  </section>
</template>

<script setup>
import { reactive, ref } from 'vue'

const apiBase = (import.meta.env.VITE_API_URL || '').replace(/\/\s*$/, '')
const form = reactive({
  name: '',
  phone: '',
  email: '',
  date: '',
  message: '',
})
const submitting = ref(false)
const success = ref(false)
const error = ref('')

async function onSubmit() {
  if (submitting.value) return
  
  submitting.value = true
  success.value = false
  error.value = ''
  
  try {
    const formData = new FormData()
    formData.append('name', form.name)
    formData.append('phone', form.phone)
    if (form.email) formData.append('email', form.email)
    if (form.date) formData.append('date', form.date)
    if (form.message) formData.append('message', form.message)
    
    const res = await fetch(`${apiBase}/api/zayavka/`, {
      method: 'POST',
      body: formData,
    })
    
    const data = await res.json()
    
    if (res.ok && data.success) {
      success.value = true
      form.name = ''
      form.phone = ''
      form.email = ''
      form.date = ''
      form.message = ''
    } else {
      error.value = data.error || 'Ошибка отправки заявки'
    }
  } catch (e) {
    error.value = 'Ошибка соединения с сервером'
  } finally {
    submitting.value = false
  }
}
</script>
