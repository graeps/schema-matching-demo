<!-- Connect the tables game. Builds to tables in vue-flow which can get manually connected with the mouse. Choice can be checked on correctness.-->
<template>
  <VueFlow
    :zoom-on-double-click="false"
    :zoom-on-scroll="false"
    :pan-on-drag="false"
    :nodes-draggable="false"
    :nodes="nodes"
    :edges="edges"
    :nodes-connectable="true"
    :connection-radius="50"
    fit-view-on-init
    @connect="onConnect"
  >
    <template #node-matcher="{ label, id, data }">
      <MatcherNodeTitle :id="id" :label="label" :data="data" />
    </template>
    <template #node-data="{ data, id }">
      <DataNode :id="id" :data="data" />
    </template>
    <template #node-title="{ id, label }">
      <TitleNodeLarge :id="id" :label="label" />
    </template>
    <template
      #connection-line="{ sourceX, sourceY, targetX, targetY, sourcePosition, targetPosition }"
    >
      <MatcherConnectionLine
        :source-x="sourceX"
        :source-y="sourceY"
        :target-x="targetX"
        :target-y="targetY"
        :source-position="sourcePosition"
        :target-position="targetPosition"
        color="lightgrey"
      />
    </template>
    <template
      #edge-matcher1="{ id, sourceX, sourceY, targetX, targetY, sourcePosition, targetPosition }"
    >
      <MatcherEdge
        :id="id"
        :source-x="sourceX"
        :source-y="sourceY"
        :target-x="targetX"
        :target-y="targetY"
        :source-position="sourcePosition"
        :target-position="targetPosition"
        color="#ff6f61"
        show-remove-btn
      />
    </template>
    <template
      #edge-matcher2="{ id, sourceX, sourceY, targetX, targetY, sourcePosition, targetPosition }"
    >
      <MatcherEdge
        :id="id"
        :source-x="sourceX"
        :source-y="sourceY"
        :target-x="targetX"
        :target-y="targetY"
        :source-position="sourcePosition"
        :target-position="targetPosition"
        color="#e96dff"
        show-remove-btn
      />
    </template>
    <template
      #edge-matcher3="{ id, sourceX, sourceY, targetX, targetY, sourcePosition, targetPosition }"
    >
      <MatcherEdge
        :id="id"
        :source-x="sourceX"
        :source-y="sourceY"
        :target-x="targetX"
        :target-y="targetY"
        :source-position="sourcePosition"
        :target-position="targetPosition"
        color="#FAC05E"
        show-remove-btn
      />
    </template>
    <template
      #edge-matcher4="{ id, sourceX, sourceY, targetX, targetY, sourcePosition, targetPosition }"
    >
      <MatcherEdge
        :id="id"
        :source-x="sourceX"
        :source-y="sourceY"
        :target-x="targetX"
        :target-y="targetY"
        :source-position="sourcePosition"
        :target-position="targetPosition"
        color="#4AA6FDFF"
        show-remove-btn
      />
    </template>
  </VueFlow>
</template>

<script setup>
import { useVueFlow, VueFlow } from '@vue-flow/core'
import { ref } from 'vue'

import MatcherNodeTitle from 'components/vueflow/nodes/matcher/MatcherNode.vue'
import DataNode from 'components/vueflow/nodes/matcher/DataNode.vue'
import MatcherConnectionLine from 'components/vueflow/edges/MatcherConnectionLine.vue'
import MatcherEdge from 'components/vueflow/edges/MatcherEdge.vue'
import TitleNodeLarge from 'components/vueflow/nodes/demo/TitleNodeLarge.vue'
import PreprocColumnDate from 'components/columns/preprocessing/PreprocColumnDate.vue'
import PreprocColumnString from 'components/columns/preprocessing/PreprocColumnString.vue'
import PreprocColumnNumber from 'components/columns/preprocessing/PreprocColumnNumber.vue'

const { addEdges } = useVueFlow()

const onConnect = (params) => {
  const edgeType = `matcher${params.target.charAt(params.target.length - 1)}`

  const newEdge = {
    id: `${params.source}-${params.target}`,
    source: params.source,
    target: params.target,
    targetHandle: params.targetHandle,
    type: edgeType, // Set type dynamically
    animated: true,
    selectable: true,
  }

  addEdges([newEdge])
}

const xDistance = 450
const yDistance = 250

const xMatcherPos = 20
const yMatcherPos = -130
const yOffset = 180

const nodes = ref([
  {
    id: 'heading1',
    label: 'Datenbank I',
    position: { x: -xDistance + 65, y: -70 },
    type: 'title',
  },
  {
    id: 'heading2',
    label: 'Datenbank II',
    position: { x: xDistance + 65, y: -70 },
    type: 'title',
  },
  {
    id: 'data1-1',
    label: 'data1-1',
    position: { x: -xDistance, y: 0 },
    type: 'data',
    data: {
      entity: 'Geburtsdatum',
      dataToShow: PreprocColumnDate,
      preprocProps: {
        id: 't1_c4',
        dataType: 'date',
        title: 'Geburtsdatum',
        numInstances: '3.485',
        minDate: '24.02.1938',
        maxDate: '3.03.2017',
      },
      handlePosition: 'right',
    },
  },
  {
    id: 'data1-2',
    label: 'data1-2',
    position: { x: -xDistance, y: yDistance },
    type: 'data',
    data: {
      entity: 'Diagnose',
      dataToShow: PreprocColumnString,
      preprocProps: {
        id: 't1_c5',
        dataType: 'string',
        title: 'Diagnose',
        numInstances: '3.485',
        avgLength: '14.6',
        fracUpper: '0.16',
        fracLetters: '0.6',
      },
      handlePosition: 'right',
    },
  },
  {
    id: 'data2-1',
    label: 'data2-1',
    position: { x: xDistance, y: 0 },
    type: 'data',
    data: {
      entity: 'Diagnosis',
      dataToShow: PreprocColumnString,
      preprocProps: {
        id: 't2_c6',
        dataType: 'string',
        title: 'Diagnosis',
        numInstances: '24.304',
        avgLength: '8.0',
        fracUpper: '0.0',
        fracLetters: '1.0',
      },
      handlePosition: 'left',
    },
  },
  {
    id: 'data2-2',
    label: 'data2-2',
    position: { x: xDistance, y: yDistance },
    type: 'data',
    data: {
      entity: 'PID',
      dataToShow: PreprocColumnNumber,
      preprocProps: {
        id: 't2_c1',
        dataType: 'number',
        title: 'PID',
        numInstances: '24.304',
        minValue: '1',
        maxValue: '24.304',
        avgValue: '12.152',
      },
      handlePosition: 'left',
    },
  },
  {
    id: 'matcher1',
    position: { x: xMatcherPos, y: yMatcherPos },
    type: 'matcher',
    data: {
      validSourceLeft: ['data1-1', 'data1-2'],
      validSourceRight: ['data2-1', 'data2-2'],
      matcherType: 'string',
      title: 'Matcher 1',
      subtitle: 'String-Vergleich',
      targetSimilarity: 'Ähnlichkeit Titel:',
      tooltipText:
        'Dieser Matcher gibt den Anteil der in beiden Titeln \n vorkommenden Buchstaben zurück. \n\n' +
        'Zum Beispiel teilen sich die Titel "Diagnose" und \n "diagnosis" ' +
        'sieben der insgesamt acht vorkommenden \n Buchstaben, ' +
        'woraus sich ein Score von 7/8≈0.88 ergibt.',
    },
  },
  {
    id: 'matcher2',
    position: { x: xMatcherPos, y: yMatcherPos + yOffset },
    type: 'matcher',
    data: {
      validSourceLeft: ['data1-1', 'data1-2'],
      validSourceRight: ['data2-1', 'data2-2'],
      matcherType: 'instance',
      title: 'Matcher 2',
      subtitle: 'Instance-Vergleich',
      targetSimilarity: 'Ähnlichkeit Meta-Daten:',
      tooltipText:
        'Dieser Matcher prüft, ob zweimal der selbe Datentyp vorliegt.\n' +
        'Falls das der Fall ist, wird ein Similarity-Score durch Vergleich \nder Meta-Daten berechnet.',
    },
  },
  {
    id: 'matcher3',
    position: { x: xMatcherPos, y: yMatcherPos + 2 * yOffset },
    type: 'matcher',
    data: {
      validSourceLeft: ['data1-1', 'data1-2'],
      validSourceRight: ['data2-1', 'data2-2'],
      matcherType: 'clustering',
      title: 'Matcher 3',
      subtitle: 'Clustering',
      targetSimilarity: 'Im selben Cluster?:',
      tooltipText:
        'Dieser Matcher beruht auf der räumlichen Distanz der Vektoren.\n' +
        'Die Vektoren zweier Spalten, die nah aneinander sind landen im\n selben Cluster und bekommen einen hohen Score.',
    },
  },
  {
    id: 'matcher4',
    position: { x: xMatcherPos, y: yMatcherPos + 3 * yOffset },
    type: 'matcher',
    data: {
      validSourceLeft: ['data1-1', 'data1-2'],
      validSourceRight: ['data2-1', 'data2-2'],
      matcherType: 'classifier',
      title: 'Matcher 4',
      subtitle: 'Classifier',
      targetSimilarity: 'Match nach NN?:',
      tooltipText:
        'Dieser Matcher berechnet mit Hilfe eines neuronalen Netzes (NN)\n' +
        'die Wahrscheinlichkeit, dass zwei Vektoren zu semantisch äquivalenten\n' +
        'Spalten gehören. Das NN wurde zuvor auf gelabelten Datenbanken trainiert.',
    },
  },
])

const edges = ref([
  {
    id: 'diagnose-matcher1',
    targetHandle: 'handle-1',
    source: 'data1-2',
    target: 'matcher1',
    type: 'matcher1',
    animated: true,
    selectable: true,
  },
  {
    id: 'matcher1-diagnosis',
    targetHandle: 'handle-2',
    source: 'data2-1',
    target: 'matcher1',
    type: 'matcher1',
    animated: true,
    selectable: true,
  },
])
</script>

<style>
@import '../../../node_modules/@vue-flow/core/dist/style.css';
@import '../../../node_modules/@vue-flow/core/dist/theme-default.css';
</style>
