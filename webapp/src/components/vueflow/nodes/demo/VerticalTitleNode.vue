<template>
  <div class="rotate-text">
    {{ props.label }}
  </div>
</template>

<script setup>
import { defineProps } from "vue"

const props = defineProps({
  label: {
    type: String,
    required: true,
  },
})
</script>

<style scoped>
.rotate-text {
  font-family: "Barlow", bold, sans-serif;
  rotate: -90deg;
  font-size: 25px;
  color: #004b6f;
}
</style>
