<template>
  <iframe
    :src="`https://open.spotify.com/follow/1/?uri=spotify:artist:${artistId}&size=basic&theme=light&show-count=0`"
    :title="`Follow ${artistName} on Spotify`"
    width="93"
    height="25"
    scrolling="no"
    frameborder="0"
    style="border:none; overflow:hidden;"
    allowtransparency="true"
  />
</template>

<script>
export default {
  name: 'SpotifyWidget',
  props: {
    artistId: {
      type: String,
      required: true,
    },
    artistName: {
      type: String,
      required: true,
    },
  },
  data () {
    return {}
  },
};
</script>
