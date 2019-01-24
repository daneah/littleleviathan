<template>
  <div id="app">
    <nav>
      <router-link to="/">
        <img
          src="/img/little-leviathan-wordmark.png"
          alt="Little Leviathan"
        >
      </router-link>

      <ul>
        <li>
          <router-link to="/music">
            Music
          </router-link>
        </li>
        <li>
          <router-link to="/about">
            About
          </router-link>
        </li>
        <li>
          <router-link to="/press">
            Press
          </router-link>
        </li>
      </ul>

      <SpotifyWidget artist-id="5rp7W2bKUyN8uB4KntE38x" />
    </nav>

    <transition name="slide-down">
      <router-view />
    </transition>
  </div>
</template>

<script>
import SpotifyWidget from '@/components/SpotifyWidget.vue';

export default {
  name: 'App',
  components: {
    SpotifyWidget,
  },
  metaInfo() {
    return {
      title: 'GIVE ME A TITLE',
      titleTemplate: chunk => `${chunk} | Little Leviathan`,
      meta: [
        {
          property: 'og:title',
          content: 'GIVE ME A TITLE',
          vmid: 'og:title',
        },
        {
          property: 'og:url',
          content: 'GIVE ME A URL',
          vmid: 'og:url',
        },
        {
          property: 'description',
          content: 'GIVE ME A DESCRIPTION',
          vmid: 'og:description',
        },
      ],
    };
  },
};
</script>

<style lang="scss">
@import '@/main.scss';

body {
  background-color: var(--light-blue);
}

a {
  text-decoration: none;
  color: var(--dark-blue);

  &:hover {
    color: var(--very-dark-blue);
    text-decoration: underline;
  }
}

nav {
  text-align: center;

  ul {
    list-style: none;

    li {
      display: inline-block;
      padding: 1rem;
      font-size: var(--text-lg);
      font-weight: 300;
    }
  }

  img {
    display: block;
    margin: 0 auto;
    max-width: 100%;
  }
}

.slide-down-enter-active {
  transition: opacity 0.5s, transform 0.5s;
}

.slide-down-enter,
.slide-down-leave-to {
  opacity: 0;
  transform: translateY(50px);
}
</style>
