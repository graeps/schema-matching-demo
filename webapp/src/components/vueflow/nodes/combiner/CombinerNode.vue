<template>
  <div class="node-container shadow-2">
    <div class="row">
      <div class="col-6 offset-md-3 text-center combiner-subtitle">{{ props.data.title }}</div>
    </div>
    <div class="text-center combiner-title q-mb-xs">{{ subtitle[props.data.combinerType] }}</div>
    <div class="row justify-center">
      <div class="text-center combiner-result">{{ combinerResult[props.data.combinerType] }}</div>
    </div>
    <q-tooltip class="combiner-tooltip" anchor="top middle" self="bottom middle" :delay="200">
      {{ tooltipText[props.data.combinerType] }}
    </q-tooltip>
    <Handle id="handle-1" type="target" :position="Position.Bottom" />
    <Handle id="handle-2" type="source" :position="Position.Top" />
  </div>
</template>

<script setup>
import { Handle, Position } from '@vue-flow/core'

import { defineProps } from 'vue'

const props = defineProps({
  id: {
    type: String,
    required: true,
  },
  data: {
    type: Object,
    required: true,
  },
})

const combinerResult = {
  max: 0.88,
  min: 0.48,
  average: Math.round(((0.48 + 1.0 + 0.91) / 3) * 100.0) / 100.0,
}

const tooltipText = {
  max: 'Dieser Combiner gibt das Maximum der Eingabewerte zurück.',
  min: 'Dieser Combiner gibt das Minimum der Eingabewerte zurück.',
  average: 'Dieser Combiner bildet das arithmetische Mittel der Eingabewerte.',
}

const subtitle = {
  max: 'Max. Combiner',
  min: 'Min. Combiner',
  average: 'Average Combiner',
}
</script>

<style scoped>
.node-container {
  border-style: solid;
  border-radius: 40px;
  height: 140px;
  width: 230px;
  color: black;
  transform: scale(0.8);
  padding: 5px;
  border-color: gray;
  background-color: #e8e7e7;
}

.combiner-title {
  font-family: 'Barlow', sans-serif;
  color: #004b6f;
  font-size: 18pt;
}

.combiner-subtitle {
  font-family: 'Barlow', sans-serif;
  color: #000000;
  font-size: 14pt;
}

.combiner-result {
  width: fit-content;
  height: fit-content;
  padding: 0.2em 0.6em;
  font-family: 'Courier New', monospace;
  background-color: #f4f4f4;
  border: 1px solid #ccc;
  border-radius: 17px;
  box-shadow: 1px 1px 4px rgba(0, 0, 0, 0.1);
  color: #004b6f;
  font-size: 14pt;
}

.vue-flow__handle {
  height: 15px;
  width: 35px;
  border-radius: 4px;
  background-color: darkred;
}
</style>

<style>
.combiner-tooltip {
  border-style: solid;
  border-width: 1px;
  color: rgb(15 23 42);
  box-shadow: rgba(29, 29, 29, 0.46) 2px 2px 5px 1px;
  font-size: 10pt;
  white-space: pre-line;
  text-align: justify;
  border-color: gray;
  background-color: #e8e7e7;
}
</style>
