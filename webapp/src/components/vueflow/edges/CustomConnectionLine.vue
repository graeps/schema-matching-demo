<template>
  <g>
    <path fill="none" :stroke="props.color" :stroke-width="props.width" :d="path[0]" />
  </g>
</template>

<script setup>
import { getBezierPath } from "@vue-flow/core"
import { computed } from "vue"

const props = defineProps({
  sourceX: {
    type: Number,
    required: true,
  },
  sourceY: {
    type: Number,
    required: true,
  },
  targetX: {
    type: Number,
    required: true,
  },
  targetY: {
    type: Number,
    required: true,
  },
  sourcePosition: {
    type: String,
    required: true,
  },
  targetPosition: {
    type: String,
    required: true,
  },
  color: {
    type: String,
    required: true,
  },
  width: {
    type: String,
    required: false,
    default: "10",
  },
})

const path = computed(() => {
  const { sourceX, sourceY, targetX, targetY, sourcePosition, targetPosition } = props
  return getBezierPath({ sourceX, sourceY, sourcePosition, targetX, targetY, targetPosition, curvature: 0 })
})
</script>
