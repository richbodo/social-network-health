<script setup>
import { useNav } from '@slidev/client'
const nav = useNav()
</script>

<template>
  <!-- SNH logo, upper-left of every slide except the title slide -->
  <img
    v-if="nav.currentPage.value !== 1"
    src="/snh-logo.svg"
    alt=""
    class="absolute top-4 left-5 w-11 opacity-90 z-10 pointer-events-none"
  />
</template>
