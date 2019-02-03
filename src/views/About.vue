<template>
  <main>
    <h1>About</h1>
    <p>
      Dane Hillard is a man of many interests, of which music has been one of the most enduring.
      His tastes have changed dramatically over the years,
      but the album Little Leviathan is a snapshot of where his tastes have settled in recent years.
      Inspired by folk and indie singer/songwriters
      such as Iron & Wine, The Shins, Alexi Murdoch, and more,
      Little Leviathan is a collection of work about love, loss, and finding meaning in both.
    </p>
  </main>
</template>

<script>
const PAGE_TITLE = 'About';
const PAGE_DESCRIPTION = 'Little Leviathan | News, tour, info, music, photos, videos, and more.';

export default {
  name: 'About',
  metaInfo: {
    title: 'About',
    meta: [
      {
        property: 'og:title',
        content: PAGE_TITLE,
        vmid: 'og:title',
      },
      {
        property: 'og:url',
        content: 'https://littleleviathan.com/about',
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
};
</script>

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
