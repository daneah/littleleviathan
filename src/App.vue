<script setup lang="ts">
import { RouterLink, RouterView, useRoute } from 'vue-router'
import { useHead } from '@unhead/vue'
import wordmark from './assets/little-leviathan-wordmark.png'
import whale from './assets/whale.png'

const route = useRoute()
const PAGE_DESCRIPTION = 'Little Leviathan | News, tour, info, music, photos, videos, and more.'

useHead({
  titleTemplate: '%s | Little Leviathan',
  link: [
    {
      rel: 'canonical',
      href: () => `https://littleleviathan${route.fullPath}`
    }
  ],
  meta: [
    {
      name: 'description',
      content: PAGE_DESCRIPTION
    },
    {
      property: 'og:description',
      content: PAGE_DESCRIPTION
    },
    {
      property: 'og:url',
      content: () => `https://littleleviathan.com${route.fullPath}${route.fullPath ? '/' : ''}`
    },
    {
      property: 'og:image',
      content: whale
    }
  ]
})
</script>

<template>
  <div>
    <nav>
      <RouterLink to="/">
        <img :src="wordmark" alt="Little Leviathan" />
      </RouterLink>

      <ul>
        <li>
          <RouterLink to="/music"> Music </RouterLink>
        </li>
        <li>
          <RouterLink to="/about"> About </RouterLink>
        </li>
        <li>
          <RouterLink to="/press"> Press </RouterLink>
        </li>
      </ul>
    </nav>

    <RouterView v-slot="{ Component }">
      <Transition name="slide-down">
        <component :is="Component" />
      </Transition>
    </RouterView>
  </div>
</template>

<style lang="scss">
@import './assets/main.scss';

body {
  background-color: var(--light-blue);
}

a {
  text-decoration: none;
  color: var(--dark-blue);

  &:hover {
    color: var(--very-dark-blue);
    text-decoration: underline;
  }
}

nav {
  text-align: center;

  ul {
    list-style: none;

    li {
      display: inline-block;
      padding: 1rem;
      font-size: var(--text-xl);
      font-weight: 300;
    }
  }

  img {
    display: block;
    margin: 0 auto;
    max-width: 100%;
  }
}

.slide-down-enter-active {
  opacity: 0;
  transform: translateY(50px);
  transition:
    opacity 0.5s,
    transform 0.5s;
}

.slide-down-enter,
.slide-down-enter-to {
  opacity: 1;
  transform: translateY(0px);
}
</style>
