<template>
  <main>
    <h1>Music</h1>
    <ul class="albums">
      <li
        class="album"
        v-for="album in albums"
        :key="album.title"
      >
        <div class="album__metadata">
          <h2>{{ album.title }}</h2>
          <p class="album__description">
            {{ album.description }}
          </p>
          <ul class="purchase-links">
            <li>
              <a :href="`https://itunes.apple.com/album/${album.appleMusicLink}`">
                Apple Music
              </a>
            </li>
            <li>
              <a :href="`https://soundcloud.com/littleleviathanmusic/sets/${album.soundcloudSet}`">
                SoundCloud
              </a>
            </li>
            <li>
              <a :href="`https://littleleviathan.bandcamp.com/album/${album.bandcampId}`">
                Bandcamp
              </a>
            </li>
            <li>
              <a :href="`https://open.spotify.com/album/${album.spotifyId}`">
                Spotify
              </a>
            </li>
          </ul>
        </div>
        <img
          class="cover-image"
          :src="`/img/${album.coverImage}`"
          alt=""
        >
      </li>
    </ul>
  </main>
</template>

<script>
import { mapState } from 'vuex';

const PAGE_TITLE = 'Music';
const PAGE_DESCRIPTION = 'Little Leviathan | News, tour, info, music, photos, videos, and more.';

export default {
  name: 'Music',
  computed: {
    ...mapState({
      albums: state => state.albums,
    }),
  },
  mounted() {
    console.log(this.albums);
  },
  metaInfo: {
    title: 'Music',
    meta: [
      {
        property: 'og:title',
        content: PAGE_TITLE,
        vmid: 'og:title',
      },
      {
        property: 'og:url',
        content: 'https://littleleviathan.com/music',
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
main {
  text-align: center;
}

.albums {
  margin-top: 0;
}

.album {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-gap: 1rem;
}

.album__metadata {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  justify-content: center;

  h2 {
    text-align: right;
  }
}

.album__description {
  text-align: left;
  margin-top: 0;
}

.purchase-links {
  list-style: none;
  margin-top: 0;

  li {
    padding: var(--space-xs);
    display: inline-block;
  }
}

.cover-image {
  max-width: 400px;
  margin: 0 auto;
}
</style>
