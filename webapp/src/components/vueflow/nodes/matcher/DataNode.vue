<template>
  <div class="">
    <Handle type="source" :position="handlePosition" />
    <component
      :is="props.data.dataToShow"
      v-bind="{
        ...props.data.preprocProps,
        connectedToMatcher1,
        connectedToMatcher2,
        connectedToMatcher3,
        connectedToMatcher4,
      }"
    />
    <q-markup-table
      bordered
      class="no-pointer-events"
      dense
      :separator="'vertical'"
      :table-layout="'fixed'"
    >
      <tbody>
        <tr>
          <td class="text-right indicator">Vektor</td>
          <td
            :class="[
              { highlight3: connectedToMatcher3 && !connectedToMatcher4 },
              { highlight4: !connectedToMatcher3 && connectedToMatcher4 },
              { stripes: connectedToMatcher3 && connectedToMatcher4 },
            ]"
            class="text-right"
          >
            {{ vectorPropsMap[props.data.entity] }}
          </td>
        </tr>
      </tbody>
    </q-markup-table>
  </div>
</template>

<script setup>
import { Handle, Position, useNodeConnections, useNodesData } from '@vue-flow/core'
import { computed, defineProps } from 'vue'

const props = defineProps({
  id: {
    type: String,
    required: true,
  },
  data: {
    type: Array,
    required: true,
  },
})

const handlePosition = computed(() => {
  if (props.data.handlePosition === 'left') {
    return Position.Left
  } else {
    return Position.Right
  }
})

const vectorPropsMap = {
  Diagnose: '[0.52, --, 0.34, 0.69, 0.56, ...]',
  Geburtsdatum: '[0.87, 0.34, 0.56, --, 0.92, ...]',
  Diagnosis: '[0.64, --, 0.45, 0.23, 0.89, ...]',
  PID: '[0.52, 0.18, --, 0.77, 0.34, ...]',
}

const connections = useNodeConnections({})
const targetTitle = useNodesData(() => connections.value.map((connection) => connection.target))

const connectedToMatcher1 = computed(() => targetTitle.value.some((node) => node.id === 'matcher1'))
const connectedToMatcher2 = computed(() => targetTitle.value.some((node) => node.id === 'matcher2'))
const connectedToMatcher3 = computed(() => targetTitle.value.some((node) => node.id === 'matcher3'))
const connectedToMatcher4 = computed(() => targetTitle.value.some((node) => node.id === 'matcher4'))
</script>

<style scoped>
.node-container {
  border-style: solid;
  border-radius: 5px;
  border-color: rgba(140, 192, 218, 0.45);
}

.vue-flow__handle {
  height: 30px;
  width: 25px;
  background-color: darkred;
  border-radius: 4px;
}
.indicator {
  font-family: 'Barlow', sans-serif;
}
.subtitle {
  font-family: 'Barlow', sans-serif;
  color: #004b6f;
  font-size: 12pt;
}
td {
  transition: background-color 0.5s ease !important;
}
</style>
