<template>
  <div class="node-container">
    <q-tooltip :anchor="anchorPosition" :self="position" class="no-padding shadow-2 preprocTooltip">
      <div>
        <component
          :is="PreprocColumnString"
          v-bind="{
            connectedToMatcher1,
            connectedToMatcher2,
            ...preprocProps[props.data.entity],
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
              <td class="text-right stripes">
                {{ vectorPropsMap[entity] }}
              </td>
            </tr>
          </tbody>
        </q-markup-table>
      </div></q-tooltip
    >
    <Handle type="source" :position="handlePosition" />
    <component :is="column" :whiteBg="true" :largeFont="true" />
  </div>
</template>

<script setup>
import { Handle, Position } from '@vue-flow/core'
import { computed, defineProps } from 'vue'
import SingleColumnDiagnose from 'components/columns/preprocessing/ColumnDiagnose.vue'
import SingleColumnDiagnosis from 'components/columns/preprocessing/ColumnDiagnosis.vue'
import PreprocColumnString from 'components/columns/preprocessing/PreprocColumnString.vue'

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

const entity = props.data.entity
const connectedToMatcher1 = true
const connectedToMatcher2 = true
const largeFont = true

console.log('largeFont RawColumn', largeFont)

const preprocPropsDiagnose = {
  id: 't1_c5',
  dataType: 'string',
  title: 'Diagnose',
  numInstances: '3.485',
  avgLength: '6.3',
  fracUpper: '0.16',
  fracLetters: '1.0',
}

const preprocPropsDiagnosis = {
  id: 't2_c6',
  dataType: 'string',
  title: 'Diagnosis',
  numInstances: '24.304',
  avgLength: '8.0',
  fracUpper: '0.09',
  fracLetters: '0.36',
}

const preprocProps = {
  Diagnose: preprocPropsDiagnose,
  Diagnosis: preprocPropsDiagnosis,
}

const anchorPosition = computed(() => {
  if (entity === 'Diagnose') {
    return 'center left'
  } else {
    return 'center right'
  }
})

const position = computed(() => {
  if (entity === 'Diagnose') {
    return 'center right'
  } else {
    return 'center left'
  }
})

const handlePosition = computed(() => {
  if (props.data.handlePosition === 'left') {
    return Position.Left
  } else {
    return Position.Right
  }
})

const column = computed(() => {
  if (entity === 'Diagnose') {
    return SingleColumnDiagnose
  } else {
    return SingleColumnDiagnosis
  }
})

const vectorPropsMap = {
  Diagnose: '[0.52, --, 0.34, 0.69, 0.56, ...]',
  Diagnosis: '[0.64, --, 0.45, 0.23, 0.89, ...]',
}
</script>

<style scoped>
.node-container {
  scale: 1;
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

.rawColumn .q-markup-table {
  background-color: white !important;
}
</style>
