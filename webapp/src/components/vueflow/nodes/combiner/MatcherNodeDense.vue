<template>
  <div class="node-container shadow-2" :class="borderColor">
    <div class="text-center matcher-subtitle">{{ props.data.title }}</div>
    <div class="text-center matcher-title q-mb-xs">{{ props.data.subtitle }}</div>
    <div class="row justify-center">
      <div class="text-center matcher-result">{{ matcherResult }}</div>
    </div>

    <Handle
      id="handle-1"
      type="target"
      :position="Position.Top"
      connectable="single"
      :is-valid-connection="isValidConnectionLeft"
    />
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

const resultsMap = {
  string: '0.88',
  instance: '0.48',
  clustering: '1.0',
  classifier: '0.91',
}

const matcherResult = resultsMap[props.data.matcherType]

const borderColorMap = {
  string: 'matcher-string',
  instance: 'matcher-instance',
  clustering: 'matcher-clustering',
  classifier: 'matcher-classifier',
}

const borderColor = borderColorMap[props.data.matcherType]
</script>

<script>
export default {
  inheritAttrs: false,
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
}

.matcher-title {
  font-family: 'Barlow', sans-serif;
  color: #004b6f;
  font-size: 18pt;
}

.matcher-subtitle {
  font-family: 'Barlow', sans-serif;
  color: #000000;
  font-size: 14pt;
}

.matcher-result {
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

<style lang="scss">
.matcher-string {
  border-color: $highlight1;
  background-color: $highlight1Light;
}
.matcher-instance {
  border-color: $highlight2;
  background-color: $highlight2Light;
}
.matcher-clustering {
  border-color: $highlight3;
  background-color: $highlight3Light;
}
.matcher-classifier {
  border-color: $highlight4;
  background-color: $highlight4Light;
}

.matcher-tooltip {
  border-style: solid;
  border-width: 1px;
  color: rgb(15 23 42);
  box-shadow: rgba(29, 29, 29, 0.46) 2px 2px 5px 1px;
  font-size: 10pt;
  white-space: pre-line;
  text-align: justify;
}
</style>
