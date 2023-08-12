<script setup lang="ts">
import { useHead } from '@unhead/vue'
import { RouterLink } from 'vue-router'

const PAGE_TITLE = 'Page Not Found'
const PAGE_DESCRIPTION = 'This page does not exist'

useHead({
  title: PAGE_TITLE,
  meta: [
    {
      name: 'description',
      content: PAGE_DESCRIPTION
    },
    {
      property: 'og:description',
      content: PAGE_DESCRIPTION
    }
  ]
})
</script>

<template>
  <main>
    <h1>Lost at sea!</h1>

    <p>The page you requested could not be found.</p>
    <RouterLink :to="{ name: 'home' }"> Go back home </RouterLink>
  </main>
</template>

<style lang="scss" scoped>
main {
  text-align: center;
}

p {
  margin: 1rem auto;
}
</style>
