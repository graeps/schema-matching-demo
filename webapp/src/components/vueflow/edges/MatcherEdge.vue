<template>
  <g>
    <path fill="none" :stroke="props.color" stroke-width="10" :d="path[0]" />
  </g>
  <!-- Use the `EdgeLabelRenderer` to escape the SVG world of edges and render your own custom label in a `<div>` ctx -->
  <EdgeLabelRenderer>
    <div
      :style="{
        pointerEvents: 'all',
        position: 'absolute',
        transform: `translate(-50%, -50%) translate(${path[1]}px,${path[2]}px)`,
      }"
      class="nodrag nopan"
    >
      <q-btn
        v-if="props.showRemoveBtn"
        size="sm"
        icon="close"
        class="edgebutton no-padding"
        round
        @click="removeEdges(id)"
        :style="{ '--edge-color': props.color }"
      />
    </div>
  </EdgeLabelRenderer>
</template>

<script setup>
import { EdgeLabelRenderer, getBezierPath, useVueFlow } from '@vue-flow/core'
import { computed } from 'vue'

const { removeEdges } = useVueFlow()

const props = defineProps({
  id: {
    type: String,
    required: true,
  },
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
  data: {
    type: Object,
    required: false,
    default: null,
  },
  markerEnd: {
    type: String,
    required: false,
    default: '',
  },
  style: {
    type: Object,
    required: false,
    default: null,
  },
  color: {
    type: String,
    required: true,
  },
  showRemoveBtn: {
    type: Boolean,
    required: false,
  },
})

const path = computed(() => getBezierPath(props))
</script>

<style scoped>
.edgebutton {
  border-radius: 90px;
  cursor: pointer;
  background-color: rgba(250, 224, 224, 0.84);
}

.edgebutton:hover {
  transform: scale(1.1);
  transition: all ease 0.5s;
  box-shadow: 0 0 0 4px var(--edge-color);
  background-color: rgb(250, 224, 224);
}
</style>
