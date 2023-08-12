<script setup lang="ts">
import { useHead } from '@unhead/vue'

import PurchaseLink from '../components/PurchaseLink.vue'
import { useAlbumStore } from '../stores/albums'

const albums = useAlbumStore()

const PAGE_TITLE = 'Music'
const PAGE_DESCRIPTION = 'Albums, recordings, and music videos by Little Leviathan'

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

const getImageUrl = (path: string) => {
  return new URL(`../assets/${path}`, import.meta.url).href
}
</script>

<template>
  <main>
    <h1>Music</h1>
    <ul class="albums">
      <li class="album" v-for="album in albums.albums" :key="album.title">
        <div class="cover-image">
          <img :src="getImageUrl(album.coverImage)" :alt="`Album cover for ${album.title}`" />
        </div>
        <div class="album__metadata">
          <h2>{{ album.title }}</h2>
          <p class="album__description">
            {{ album.description }}
          </p>
          <ul class="purchase-links">
            <li>
              <PurchaseLink
                icon="music"
                :href="`https://itunes.apple.com/album/${album.appleMusicLink}`"
                service="Apple Music"
              />
            </li>
            <li>
              <PurchaseLink
                service="SoundCloud"
                :href="`https://soundcloud.com/littleleviathanmusic/sets/${album.soundcloudSet}`"
                :icon="['fab', 'soundcloud']"
              />
            </li>
            <li>
              <PurchaseLink
                service="Bandcamp"
                :href="`https://littleleviathan.bandcamp.com/album/${album.bandcampId}`"
                :icon="['fab', 'bandcamp']"
              />
            </li>
            <li>
              <PurchaseLink
                :icon="['fab', 'spotify']"
                :href="`https://open.spotify.com/album/${album.spotifyId}`"
                service="Spotify"
              />
            </li>
          </ul>
        </div>
      </li>
    </ul>
  </main>
</template>

<style lang="scss" scoped>
h1 {
  text-align: center;
}

.albums {
  margin-top: 0;
}

.album {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-gap: 5rem;

  @media (max-width: 700px) {
    grid-template-columns: 1fr;
    grid-gap: 2rem;
  }
}

.album__metadata {
  align-self: center;
}

.album__description {
  text-align: left;
  margin-top: 0;
}

.purchase-links {
  list-style: none;
  margin-left: -0.75rem;
  font-size: var(--text-xl);

  li {
    margin: 0;
    display: inline-block;
  }
}

.cover-image {
  align-self: center;
  justify-self: end;

  img {
    max-width: 100%;
  }
}
</style>
