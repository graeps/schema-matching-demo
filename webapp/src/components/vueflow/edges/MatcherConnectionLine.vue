<template>
  <g>
    <circle :cx="targetX" :cy="targetY" fill="#fff" :r="7" :stroke="props.color" :stroke-width="props.circleWidth" />
    <path class="vue-flow__connection animated" fill="none" :stroke="props.color" :stroke-width="props.strokeWidth" :d="path[0]" />
  </g>
</template>

<script setup>
import { getBezierPath, Position } from "@vue-flow/core"
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
  strokeWidth: {
    type: String,
    required: false,
    default: "10",
  },
  circleWidth: {
    type: String,
    require: false,
    default: "8.5",
  },
})

const path = computed(() => {
  const { sourceX, sourceY, targetX, targetY, sourcePosition } = props
  let targetPosition = Position.Right
  if (sourcePosition === "right") {
    targetPosition = Position.Left
  }

  // Access the value of the ref when passing to getBezierPath
  return getBezierPath({
    sourceX,
    sourceY,
    targetX,
    targetY,
    sourcePosition, // Access the value
    targetPosition, // Access the value
    curvature: 0,
  })
})
</script>
