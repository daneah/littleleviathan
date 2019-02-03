<template>
  <main>
    <h1>Press</h1>
    <a
      href="https://themerestidea.blogspot.com/2015/04/"
      target="_blank"
      rel="noopener"
    >
      An Interview with Little Leviathan
    </a>
  </main>
</template>

<script>
const PAGE_TITLE = 'Press'
const PAGE_DESCRIPTION = 'Little Leviathan | News, tour, info, music, photos, videos, and more.'

export default {
  name: 'Press',
  metaInfo: {
    title: 'Press',
    meta: [
      {
        property: 'og:title',
        content: PAGE_TITLE,
        vmid: 'og:title',
      },
      {
        property: 'og:url',
        content: 'https://littleleviathan.com/press',
        vmid: 'og:url',
      },
      {
        name: 'description',
        content: PAGE_DESCRIPTION,
        vmid: 'description',
      },
      {
        property: 'og:description',
        content: PAGE_DESCRIPTION,
        vmid: 'og:description',
      },
    ],
  },
}
</script>

<style lang="scss" scoped>
main {
  text-align: center;
}
</style>
