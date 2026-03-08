<template>
  <VueFlow
    :zoom-on-double-click="false"
    :zoom-on-scroll="false"
    :pan-on-drag="false"
    :nodes-draggable="false"
    :nodes-connectable="false"
    :nodes="[...nodesConfig1, ...nodesConfig2]"
    :edges="[...edgesConfig1, ...edgesConfig2]"
    fit-view-on-init
  >
    <template #node-matcher="{ label, id, data }">
      <MatcherNode :id="id" :label="label" :data="data" />
    </template>
    <template #node-data="{ data, id }">
      <DataNode :id="id" :data="data" />
    </template>
    <template #node-combiner="{ data, id }">
      <CombinerNode :id="id" :data="data" />
    </template>
    <template #node-selector="{ data, id }">
      <SelectorNode :id="id" :data="data" />
    </template>
    <template #node-column="{ data, id }">
      <ColumnNode :id="id" :data="data" />
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
      #edge-combiner="{ id, sourceX, sourceY, targetX, targetY, sourcePosition, targetPosition }"
    >
      <MatcherEdge
        :id="id"
        :source-x="sourceX"
        :source-y="sourceY"
        :target-x="targetX"
        :target-y="targetY"
        :source-position="sourcePosition"
        :target-position="targetPosition"
        color="grey"
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
        !showRemoveBtn
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
        !showRemoveBtn
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
        !showRemoveBtn
      />
    </template>
    <template
      #edge-match="{ id, sourceX, sourceY, targetX, targetY, sourcePosition, targetPosition }"
    >
      <MatcherEdge
        :id="id"
        :source-x="sourceX"
        :source-y="sourceY"
        :target-x="targetX"
        :target-y="targetY"
        :source-position="sourcePosition"
        :target-position="targetPosition"
        color="#01FB32FF"
        !showRemoveBtn
      />
    </template>
    <template
      #edge-no-match="{ id, sourceX, sourceY, targetX, targetY, sourcePosition, targetPosition }"
    >
      <MatcherEdge
        :id="id"
        :source-x="sourceX"
        :source-y="sourceY"
        :target-x="targetX"
        :target-y="targetY"
        :source-position="sourcePosition"
        :target-position="targetPosition"
        color="red"
        !showRemoveBtn
      />
    </template>
    <Panel position="top-right">
      Wähle eine Konfiguration:
      <div class="q-gutter-sm">
        <q-option-group
          v-model="toggleConfig"
          :options="[
            { label: 'Config 1', value: false },
            { label: 'Config 2', value: true },
          ]"
          type="radio"
          color="white"
        />
      </div>
    </Panel>
  </VueFlow>
</template>
<script setup>
import { Panel, VueFlow } from '@vue-flow/core'
import { ref, watch } from 'vue'

import MatcherNode from 'components/vueflow/nodes/combiner/MatcherNodeDense.vue'
import SelectorNode from 'components/vueflow/nodes/combiner/SelectorNode.vue'
import DataNode from 'components/vueflow/nodes/matcher/DataNode.vue'
import CombinerNode from 'components/vueflow/nodes/combiner/CombinerNode.vue'
import ColumnNode from 'components/vueflow/nodes/combiner/RawColumnNode.vue'
import MatcherConnectionLine from 'components/vueflow/edges/MatcherConnectionLine.vue'
import MatcherEdge from 'components/vueflow/edges/MatcherEdge.vue'
import TitleNodeLarge from 'components/vueflow/nodes/demo/TitleNodeLarge.vue'

const yOffset = 200
const xOffset = 200

const xFirstCol = 450
const xSecondCol = xFirstCol + xOffset
const xThirdCol = xFirstCol + 2 * xOffset
const xForthCol = xFirstCol + 3 * xOffset
const yFirstRow = 30
const ySecondRow = yFirstRow + yOffset
const yThirdRow = yFirstRow + 2 * yOffset
const yForthRow = yFirstRow + 3 * yOffset

const xData = 400
const yData = 0
const dataDistance = 280 + 280

const toggleConfig = ref(false)

const nodesConfig1 = ref([
  {
    id: 'c1-data-diagnose',
    position: { x: xData, y: yData },
    type: 'column',
    data: {
      entity: 'Diagnose',
      handlePosition: 'right',
    },
  },
  {
    id: 'c1-data-diagnosis',
    position: { x: xData + dataDistance, y: yData },
    type: 'column',
    data: {
      entity: 'Diagnosis',
      handlePosition: 'left',
    },
  },
  {
    id: 'c1-matcher1',
    position: { x: xFirstCol, y: yThirdRow },
    type: 'matcher',
    data: {
      matcherType: 'string',
      title: 'Matcher 1',
      subtitle: 'String-Vergleich',
    },
  },
  {
    id: 'c1-matcher2',
    position: { x: xSecondCol, y: yForthRow },
    type: 'matcher',
    data: {
      matcherType: 'instance',
      title: 'Matcher 2',
      subtitle: 'Instance-Vergleich',
    },
  },
  {
    id: 'c1-matcher3',
    position: { x: xThirdCol, y: yForthRow },
    type: 'matcher',
    data: {
      matcherType: 'clustering',
      title: 'Matcher 3',
      subtitle: 'Clustering',
    },
  },
  {
    id: 'c1-matcher4',
    position: { x: xForthCol, y: yForthRow },
    type: 'matcher',
    data: {
      matcherType: 'classifier',
      title: 'Matcher 4',
      subtitle: 'Classifier',
    },
  },
  {
    id: 'c1-combiner1',
    position: { x: xThirdCol, y: yThirdRow },
    type: 'combiner',
    data: {
      combinerType: 'average',
      title: 'Combiner 1',
    },
  },
  {
    id: 'c1-combiner2',
    position: { x: xSecondCol, y: ySecondRow },
    type: 'combiner',
    data: {
      combinerType: 'max',
      title: 'Combiner 2',
    },
  },
  {
    id: 'c1-selector1',
    position: { x: xSecondCol - 25, y: yFirstRow },
    type: 'selector',
    data: {
      selectorType: 'threshold',
      title: 'Selector 1',
      subtitle: 'Threshold Selector',
      config: 'config1',
    },
  },
])

const edgesConfig1 = ref([
  {
    id: 'c1-matcher2-combiner1',
    targetHandle: 'handle-1',
    source: 'c1-matcher2',
    target: 'c1-combiner1',
    type: 'matcher2',
    animated: true,
    selectable: true,
  },
  {
    id: 'c1-matcher3-combiner1',
    targetHandle: 'handle-1',
    source: 'c1-matcher3',
    target: 'c1-combiner1',
    type: 'matcher3',
    animated: true,
    selectable: true,
  },
  {
    id: 'c1-matcher4-combiner1',
    targetHandle: 'handle-1',
    source: 'c1-matcher4',
    target: 'c1-combiner1',
    type: 'matcher4',
    animated: true,
    selectable: true,
  },
  {
    id: 'c1-combiner1-combiner2',
    sourceHandle: 'handle-2',
    targetHandle: 'handle-1',
    source: 'c1-combiner1',
    target: 'c1-combiner2',
    type: 'combiner',
    animated: true,
    selectable: true,
  },
  {
    id: 'c1-matcher1-combiner2',
    targetHandle: 'handle-1',
    source: 'c1-matcher1',
    target: 'c1-combiner2',
    type: 'matcher1',
    animated: true,
    selectable: true,
  },
  {
    id: 'c1-combiner2-selector1',
    targetHandle: 'handle-1',
    sourceHandle: 'handle-2',
    source: 'c1-combiner2',
    target: 'c1-selector1',
    type: 'combiner',
    animated: true,
    selectable: true,
  },
  {
    id: 'c1-data1-data2',
    source: 'c1-data-diagnosis',
    target: 'c1-data-diagnose',
    type: 'match',
  },
])

const nodesConfig2 = ref([
  {
    id: 'c2-data-diagnose',
    position: { x: xData, y: yData },
    type: 'column',
    data: {
      entity: 'Diagnose',
      handlePosition: 'right',
    },
  },
  {
    id: 'c2-data-diagnosis',
    position: { x: xData + dataDistance, y: yData },
    type: 'column',
    data: {
      entity: 'Diagnosis',
      handlePosition: 'left',
    },
  },
  {
    id: 'c2-matcher1',
    position: { x: xFirstCol - xOffset / 2, y: yThirdRow },
    type: 'matcher',
    data: {
      matcherType: 'string',
      title: 'Matcher 1',
      subtitle: 'String-Vergleich',
    },
  },
  {
    id: 'c2-matcher2',
    position: { x: xSecondCol - xOffset / 2, y: yThirdRow },
    type: 'matcher',
    data: {
      matcherType: 'instance',
      title: 'Matcher 2',
      subtitle: 'Instance-Vergleich',
    },
  },
  {
    id: 'c2-matcher3',
    position: { x: xThirdCol - xOffset / 2, y: yThirdRow },
    type: 'matcher',
    data: {
      matcherType: 'clustering',
      title: 'Matcher 3',
      subtitle: 'Clustering',
    },
  },
  {
    id: 'c2-matcher4',
    position: { x: xForthCol - xOffset / 2, y: yThirdRow },
    type: 'matcher',
    data: {
      matcherType: 'classifier',
      title: 'Matcher 4',
      subtitle: 'Classifier',
    },
  },
  {
    id: 'c2-combiner1',
    position: { x: xSecondCol, y: ySecondRow },
    type: 'combiner',
    data: {
      combinerType: 'min',
      title: 'Combiner 1',
    },
  },
  {
    id: 'c2-selector1',
    position: { x: xSecondCol - 25, y: yFirstRow },
    type: 'selector',
    data: {
      selectorType: 'threshold',
      title: 'Selector 1',
      subtitle: 'Threshold Selector',
      config: 'config2',
    },
  },
])

const edgesConfig2 = ref([
  {
    id: 'c2-matcher1-combiner1',
    targetHandle: 'handle-1',
    source: 'c2-matcher1',
    target: 'c2-combiner1',
    type: 'matcher1',
    animated: true,
    selectable: true,
  },
  {
    id: 'c2-matcher2-combiner1',
    targetHandle: 'handle-1',
    source: 'c2-matcher2',
    target: 'c2-combiner1',
    type: 'matcher2',
    animated: true,
    selectable: true,
  },
  {
    id: 'c2-matcher3-combiner1',
    targetHandle: 'handle-1',
    source: 'c2-matcher3',
    target: 'c2-combiner1',
    type: 'matcher3',
    animated: true,
    selectable: true,
  },
  {
    id: 'c2-matcher4-combiner1',
    targetHandle: 'handle-1',
    source: 'c2-matcher4',
    target: 'c2-combiner1',
    type: 'matcher4',
    animated: true,
    selectable: true,
  },
  {
    id: 'c2-combiner1-selector1',
    targetHandle: 'handle-1',
    sourceHandle: 'handle-2',
    source: 'c2-combiner1',
    target: 'c2-selector1',
    type: 'combiner',
    animated: true,
    selectable: true,
  },
])

nodesConfig2.value = nodesConfig2.value.map((node) => ({ ...node, hidden: !toggleConfig.value }))
edgesConfig2.value = edgesConfig2.value.map((edge) => ({ ...edge, hidden: !toggleConfig.value }))

watch(toggleConfig, () => {
  nodesConfig1.value = nodesConfig1.value.map((node) => ({ ...node, hidden: toggleConfig.value }))
  edgesConfig1.value = edgesConfig1.value.map((edge) => ({ ...edge, hidden: toggleConfig.value }))
  nodesConfig2.value = nodesConfig2.value.map((node) => ({ ...node, hidden: !toggleConfig.value }))
  edgesConfig2.value = edgesConfig2.value.map((edge) => ({ ...edge, hidden: !toggleConfig.value }))
})
</script>

<style scoped>
.vue-flow__panel {
  background-color: rgba(5, 24, 52, 0.65);
  padding: 10px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
  color: white;
  font-size: 12px;
  font-family: Barlow, sans-serif;
}
</style>
