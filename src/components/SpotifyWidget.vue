<script setup lang="ts">
interface SpotifyWidgetProps {
  artistId: string
}

defineProps<SpotifyWidgetProps>()
</script>

<template>
  <iframe
    style="border-radius: 12px"
    :src="`https://open.spotify.com/embed/artist/${artistId}`"
    width="100%"
    height="352"
    frameBorder="0"
    allowfullscreen
    allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
    loading="lazy"
  ></iframe>
</template>
