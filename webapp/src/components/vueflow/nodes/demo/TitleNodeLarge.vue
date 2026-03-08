<template>
  <div class="text-box text-center">
    {{ props.label }}
  </div>
</template>

<script setup>
import { defineProps } from 'vue'

const props = defineProps({
  label: {
    type: String,
    required: true,
  },
})
</script>
<style scoped>
.text-box {
  font-family: 'Barlow', bold, sans-serif;
  color: #004b6f;
  font-size: 18pt;
}
</style>
