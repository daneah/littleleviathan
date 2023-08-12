<script setup lang="ts">
import SpotifyWidget from '../components/SpotifyWidget.vue'
import whale from '../assets/whale.png'
</script>

<template>
  <main>
    <img class="hero" :src="whale" alt="Little Leviathan whale" />
    <SpotifyWidget artist-id="5rp7W2bKUyN8uB4KntE38x" />
  </main>
</template>

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
