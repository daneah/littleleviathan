import Vue from 'vue';
import Meta from 'vue-meta';
import Router from 'vue-router';
import Home from './views/Home.vue';

Vue.use(Router);
Vue.use(Meta);

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
      component: () => import(/* webpackChunkName: 'press' */ './views/Press.vue'),
    },
    {
      path: '/about',
      name: 'about',
      component: () => import(/* webpackChunkName: 'press' */ './views/About.vue'),
    },
    {
      path: '/music',
      name: 'music',
      component: () => import(/* webpackChunkName: 'press' */ './views/Music.vue'),
    },
    /*
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(// webpackChunkName: "about" // './views/About.vue'),
    },
    */
  ],
});
