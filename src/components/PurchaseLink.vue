<template>
  <a
    :href="href"
    :title="`Listen on ${service}`"
  >
    <FontAwesome
      :icon="icon"
      :alt="service"
    />
  </a>
</template>

<script>
export default {
  name: 'PurchaseLink',
  props: {
    href: {
      type: String,
      required: true,
    },
    service: {
      type: String,
      required: true,
    },
    icon: {
      type: [String, Object],
      required: true,
    },
  },
};
</script>

<style lang="scss" scoped>
a {
  padding: .75rem;

  svg {
    transition: transform 0.25s cubic-bezier(0.68, -0.75, 0.265, 1.75);
  }

  &:hover svg {
    transform: scale(1.5);
  }
}
</style>
