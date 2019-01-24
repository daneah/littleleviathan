<template>
  <main>
    <img
      class="hero"
      src="/img/whale.png"
      alt="Little Leviathan whale"
    >
  </main>
</template>

<script>
const PAGE_TITLE = 'Little Leviathan';
const PAGE_DESCRIPTION = 'Little Leviathan | News, tour, info, music, photos, videos, and more.';

export default {
  name: 'Home',
  metaInfo: {
    titleTemplate: PAGE_TITLE,
    meta: [
      {
        property: 'og:title',
        content: PAGE_TITLE,
        vmid: 'og:title',
      },
      {
        property: 'og:url',
        content: 'https://littleleviathan.com',
        vmid: 'og:url',
      },
      {
        name: 'description',
        content: PAGE_DESCRIPTION,
        vmid: 'description',
      },
      {
        name: 'og:description',
        content: PAGE_DESCRIPTION,
        vmid: 'og:description',
      },
    ],
  },
};
</script>

<style lang="scss" scoped>
.hero {
  display: block;
  margin: 5rem auto;
  animation: wobble 2s ease-in-out infinite alternate;
  max-width: 100%;
}

@keyframes wobble {
  from {
    transform: translateY(-7px);
  }

  to {
    transform: translateY(3px);
  }
}
</style>
