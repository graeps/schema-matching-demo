<template>
  <div class="node-container shadow-2" :class="borderColor">
    <q-tooltip
      class="matcher-tooltip"
      :class="borderColor"
      anchor="top middle"
      self="bottom middle"
      :delay="200"
    >
      {{ props.data.tooltipText }}
    </q-tooltip>
    <div class="text-center matcher-subtitle">{{ props.data.title }}</div>
    <div class="text-center matcher-title">{{ props.data.subtitle }}</div>
    <q-separator class="q-my-sm" />

    <div class="text-center matcher-subtitle">
      {{ props.data.targetSimilarity }}
    </div>
    <div class="row justify-center q-pt-xs">
      <div class="text-center matcher-result">{{ matcherResult }}</div>
    </div>

    <Handle
      id="handle-1"
      type="target"
      :position="Position.Left"
      connectable="single"
      :is-valid-connection="isValidConnectionLeft"
    />
    <Handle
      id="handle-2"
      type="target"
      :position="Position.Right"
      connectable="single"
      :is-valid-connection="isValidConnectionRight"
    />
  </div>
</template>

<script setup>
import { Handle, Position, useNodeConnections } from '@vue-flow/core'
import { useInstanceMatcher } from 'components/vueflow/nodes/matcher/instanceMatcher'
import { useStringMatcher } from 'components/vueflow/nodes/matcher/stringMatcher'
import { useClusteringMatcher } from 'components/vueflow/nodes/matcher/clusteringMatcher.js'
import { useClassifierMatcher } from 'components/vueflow/nodes/matcher/classifierMatcher.js'

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

const connections = useNodeConnections({})

const stringMatcherResult = useStringMatcher(connections).compareTitlesResult
const instanceMatcherResult = useInstanceMatcher(connections).compareDataType
const clusteringMatcherResult = useClusteringMatcher(connections).compareCluster
const classifierMatcherResult = useClassifierMatcher(connections).compareClassifier

function isValidConnectionLeft(connection) {
  return props.data.validSourceLeft.includes(connection.source)
}

function isValidConnectionRight(connection) {
  return props.data.validSourceRight.includes(connection.source)
}

const resultsMap = {
  string: stringMatcherResult,
  instance: instanceMatcherResult,
  clustering: clusteringMatcherResult,
  classifier: classifierMatcherResult,
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
  height: 180px;
  width: 270px;
  color: black;
  transform: scale(0.8);
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
  height: 34px;
  width: 17px;
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
