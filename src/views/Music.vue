<template>
  <main>
    <h1>Music</h1>
    <ul class="albums">
      <li
        class="album"
        v-for="album in albums"
        :key="album.title"
      >
        <div class="cover-image">
          <img
            :src="`/img/${album.coverImage}`"
            alt=""
          >
        </div>
        <div class="album__metadata">
          <h2>{{ album.title }}</h2>
          <p class="album__description">
            {{ album.description }}
          </p>
          <ul class="purchase-links">
            <li>
              <a
                :href="`https://itunes.apple.com/album/${album.appleMusicLink}`"
                title="Listen on Apple Music"
              >
                <FontAwesome
                  icon="music"
                  alt="Apple Music"
                />
              </a>
            </li>
            <li>
              <a
                :href="`https://soundcloud.com/littleleviathanmusic/sets/${album.soundcloudSet}`"
                title="Listen on SoundCloud"
              >
                <FontAwesome
                  :icon="['fab', 'soundcloud']"
                  alt="SoundCloud"
                />
              </a>
            </li>
            <li>
              <a
                :href="`https://littleleviathan.bandcamp.com/album/${album.bandcampId}`"
                title="Listen on Bandcamp"
              >
                <FontAwesome
                  :icon="['fab', 'bandcamp']"
                  alt="Bandcamp"
                />
              </a>
            </li>
            <li>
              <a
                :href="`https://open.spotify.com/album/${album.spotifyId}`"
                title="Listen on Spotify"
              >
                <FontAwesome
                  :icon="['fab', 'spotify']"
                  alt="Spotify"
                />
              </a>
            </li>
          </ul>
        </div>
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
  display: flex;
  flex-direction: column;
  justify-content: center;
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

  a {
    padding: .75rem;

    svg {
      transition: transform 0.25s cubic-bezier(0.68, -0.75, 0.265, 1.75);
    }

    &:hover svg {
      transform: scale(1.2);
    }
  }
}

.cover-image {
  display: flex;
  flex-direction: column;
  justify-content: center;

  img {
    max-width: 100%;
  }
}
</style>
