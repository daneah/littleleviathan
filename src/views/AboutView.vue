<script setup lang="ts">
import { useHead } from '@unhead/vue'

const PAGE_TITLE = 'About'
const PAGE_DESCRIPTION = 'Biography for Little Leviathan'

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
    <h1>About</h1>
    <p>
      Dane Hillard is a man of many interests, of which music has been one of the most enduring. His
      tastes have changed dramatically over the years, but the album Little Leviathan is a snapshot
      of where his tastes have settled in recent years. Inspired by folk and indie
      singer/songwriters such as Iron & Wine, The Shins, Alexi Murdoch, and more, Little Leviathan
      is a collection of work about love, loss, and finding meaning in both.
    </p>
  </main>
</template>

<style lang="scss" scoped>
main {
  text-align: center;
}

p {
  text-align: left;
  margin-left: auto;
  margin-right: auto;
}
</style>
