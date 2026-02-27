import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'home', component: HomeView },
    { path: '/catalog', name: 'catalog', component: () => import('../views/CatalogView.vue') },
    { path: '/catalog/:id', name: 'film', component: () => import('../views/FilmDetailView.vue') },
    { path: '/news', name: 'news', component: () => import('../views/NewsView.vue') },
    { path: '/zayavka', name: 'zayavka', component: () => import('../views/ZayavkaView.vue') },
  ],
})

export default router
