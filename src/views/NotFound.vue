<template>
  <main>
    <h1>Lost at sea!</h1>

    <p>
      The page you requested could not be found.
    </p>
    <router-link
      :to="{ name: 'home' }"
    >
      Go back home
    </router-link>
  </main>
</template>

<script>
const PAGE_TITLE = 'Page Not Found'
const PAGE_DESCRIPTION = 'This page does not exist'

export default {
  name: 'NotFound',
  metaInfo: {
    title: 'Page Not Found',
    meta: [
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
      {
        property: 'og:title',
        content: `${PAGE_TITLE} | Little Leviathan`,
        vmid: 'og:title',
      },
    ],
  },
}
</script>

<style lang="scss" scoped>
main {
  text-align: center;
}

p {
  margin: 1rem auto;
}
</style>
