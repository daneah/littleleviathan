import Vue from 'vue'
import Meta from 'vue-meta'
import Router from 'vue-router'
import Home from '@/views/Home'

Vue.use(Router)
Vue.use(Meta)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/press',
      name: 'press',
      component: () => import(/* webpackChunkName: 'press' */ '@/views/Press'),
    },
    {
      path: '/about',
      name: 'about',
      component: () => import(/* webpackChunkName: 'press' */ '@/views/About'),
    },
    {
      path: '/music',
      name: 'music',
      component: () => import(/* webpackChunkName: 'press' */ '@/views/Music'),
    },
    {
      path: '*',
      name: 'notfound',
      component: () => import(/* webpackChunkName: 'notfound' */ '@/views/NotFound'),
    },
  ],
})
