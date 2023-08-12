<script setup lang="ts">
interface PurchaseLinkProps {
  href: string
  service: string
  icon: string | object
}

defineProps<PurchaseLinkProps>()
</script>

<template>
  <a :href="href" :title="`Listen on ${service}`">
    <font-awesome-icon :icon="icon" :alt="service" />
  </a>
</template>

<style lang="scss" scoped>
a {
  padding: 0.75rem;

  svg {
    transition: transform 0.25s cubic-bezier(0.68, -0.75, 0.265, 1.75);
  }

  &:hover svg {
    transform: scale(1.5);
  }
}
</style>
