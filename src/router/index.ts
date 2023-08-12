import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/HomeView.vue')
    },
    {
      path: '/press',
      name: 'press',
      component: () => import('../views/PressView.vue')
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/music',
      name: 'music',
      component: () => import('../views/MusicView.vue')
    },
    {
      path: '/:pathMatch(.*)',
      name: 'notfound',
      component: () => import('../views/NotFoundView.vue')
    }
  ]
})

export default router
