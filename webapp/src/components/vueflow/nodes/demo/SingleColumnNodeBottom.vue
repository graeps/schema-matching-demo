<template>
  <div>
    <Handle type="source" :position="Position.Bottom" style="height: 50px; width: 90px; border: 2px solid #55ad2f; background-color: #b3e89b" />
    <component :is="props.label" />
  </div>
</template>

<script setup>
import { Position, Handle } from "@vue-flow/core"
import { defineProps } from "vue"

const props = defineProps({
  label: {
    type: Object,
    required: true,
  },
})
</script>
