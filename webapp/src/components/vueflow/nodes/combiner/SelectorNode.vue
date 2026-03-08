<template>
  <div
    class="node-container shadow-2"
    :class="props.data.config === 'config1' ? 'green-node' : 'red-node'"
  >
    <div class="text-center selector-subtitle">{{ props.data.title }}</div>
    <div class="text-center selector-title q-mb-xs">{{ props.data.subtitle }}</div>
    <div class="row justify-center">
      <div class="text-center selector-result">{{ selectorResult[props.data.config] }}</div>
    </div>
    <q-tooltip class="selector-tooltip" anchor="top middle" self="bottom middle" :delay="200">
      Dieser Selector entscheidet sich dafür, dass ein Match zwischen <br />
      zwei Spalten aus Datenbank I und Datenbank II vorliegt, <br />
      sobald ein vordefinierter Schwellwert überschritten wird. <br />
      Hier haben wir in beiden Konfigurationen 0.5 gewählt.
    </q-tooltip>
    <Handle id="handle-1" type="target" :position="Position.Bottom" />
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

const selectorResult = {
  config1: '0.88 > 0.5 MATCH!',
  config2: '0.48 < 0.5',
}
</script>

<style scoped>
.node-container {
  border-style: solid;
  border-radius: 40px;
  border-width: 8px;
  height: 150px;
  width: 280px;
  color: black;
  transform: scale(0.8);
  padding: 5px;
  white-space: pre-line;
}

.red-node {
  border-color: red;
  background-color: #ffdbdb;
}

.green-node {
  border-color: #01fb32;
  background-color: #d1ffda;
}

.selector-title {
  font-family: 'Barlow', sans-serif;
  color: #004b6f;
  font-size: 18pt;
}

.selector-subtitle {
  font-family: 'Barlow', sans-serif;
  color: #000000;
  font-size: 14pt;
}

.selector-result {
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
.selector-tooltip {
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
