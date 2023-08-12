<script setup lang="ts">
import { useHead } from '@unhead/vue'

const PAGE_TITLE = 'Press'
const PAGE_DESCRIPTION = 'Coverage and praise for Little Leviathan'

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
    <h1>Press</h1>
    <a href="https://themerestidea.blogspot.com/2015/04/" target="_blank" rel="noopener">
      An Interview with Little Leviathan
    </a>
  </main>
</template>

<style lang="scss" scoped>
main {
  text-align: center;
}
</style>
