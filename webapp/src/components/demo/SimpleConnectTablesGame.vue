<!-- Connect the tables game. Builds to tables in vue-flow which can get manually connected with the mouse. Choice can be checked on correctness.-->
<template>
  <div class="text-h6 text-center q-mt-md">Verbinde die äquivalenten Spalten!</div>
  <VueFlow
    :pan-on-drag="true"
    :pan-on-scroll="false"
    :auto-pan-on-connect="false"
    :auto-pan-on-node-drag="false"
    :zoom-on-scroll="false"
    :zoom-on-pinch="false"
    :zoom-on-double-click="false"
    :nodes="nodes"
    :edges="edges"
    :nodes-draggable="false"
    :nodes-connectable="true"
    :connection-radius="50"
    :connection-mode="ConnectionMode.Loose"
    auto-connect
    @connect="onConnect"
  >
    <template #node-custom-bottom="{ label }">
      <CustomNodeBottom :label="label" />
    </template>
    <template #node-custom-top="{ label }">
      <CustomNodeTop :label="label" />
    </template>
    <template #node-vertical="{ label }">
      <vertical-title-node :label="label" />
    </template>
    <template #node-title="{ label }">
      <title-node :label="label" />
    </template>
    <template #connection-line="{ sourceX, sourceY, targetX, targetY, sourcePosition, targetPosition }">
      <SnapConnectionLine :source-x="sourceX" :source-y="sourceY" :target-x="targetX" :target-y="targetY" :source-position="sourcePosition" :target-position="targetPosition" :color="strokeColor1" />
    </template>
    <template #edge-custom="{ id, sourceX, sourceY, targetX, targetY, sourcePosition, targetPosition }">
      <CustomConnectionLine
        :id="id"
        :source-x="sourceX"
        :source-y="sourceY"
        :target-x="targetX"
        :target-y="targetY"
        :source-position="sourcePosition"
        :target-position="targetPosition"
        :color="strokeColor3"
      />
    </template>
    <template #edge-default="{ id, sourceX, sourceY, targetX, targetY, sourcePosition, targetPosition }">
      <CustomConnectionLine
        :id="id"
        :source-x="sourceX"
        :source-y="sourceY"
        :target-x="targetX"
        :target-y="targetY"
        :source-position="sourcePosition"
        :target-position="targetPosition"
        :color="strokeColor2"
      />
    </template>
    <Panel position="bottom-right">
      <q-btn class="text-black primary-button" style="padding: 10px" @click="onSolve">Überprüfen</q-btn>
    </Panel>
  </VueFlow>
</template>

<script setup>
import { ConnectionMode, Panel, useVueFlow, VueFlow } from "@vue-flow/core"
import { ref } from "vue"

import CustomNodeTop from "components/vueflow/nodes/demo/SingleColumnNodeTop.vue"
import CustomNodeBottom from "components/vueflow/nodes/demo/SingleColumnNodeBottom.vue"
import VerticalTitleNode from "components/vueflow/nodes/demo/VerticalTitleNode.vue"
import CustomConnectionLine from "components/vueflow/edges/CustomConnectionLine.vue"
import SnapConnectionLine from "components/vueflow/edges/SnappableConnectionLine.vue"
import TitleNode from "components/vueflow/nodes/demo/TitleNode.vue"

import SingleColumn11 from "components/columns/patientdata/SingleColumnPatientenId.vue"
import SingleColumn12 from "components/columns/patientdata/SingleColumnVorname.vue"
import SingleColumn13 from "components/columns/patientdata/SingleColumnNameGerman.vue"
import SingleColumn14 from "components/columns/patientdata/SingleColumnGeburtsdatum.vue"
import SingleColumn15 from "components/columns/patientdata/SingleColumnDiagnose.vue"
import SingleColumn16 from "components/columns/patientdata/SingleColumnBlutdruck.vue"
import SingleColumn21 from "components/columns/patientdata/SingleColumnPid.vue"
import SingleColumn22 from "components/columns/patientdata/SingleColumnNameEnglish.vue"
import SingleColumn23 from "components/columns/patientdata/SingleColumnSex.vue"
import SingleColumn24 from "components/columns/patientdata/SingleColumnAge.vue"
import SingleColumn25 from "components/columns/patientdata/SingleColumnDiagnosis.vue"
import SingleColumn26 from "components/columns/patientdata/SingleColumnBloodPressure.vue"

const { addEdges, onPaneReady, fitView } = useVueFlow()

const table1y = 0
const table2y = table1y + 370
const tablex = 70
const columnWidth = 165
const columnWidthPx = columnWidth + "px"

const strokeColor1 = ref("#8CC0DA")
const strokeColor2 = ref("#8CC0DA")
const strokeColor3 = ref("#8CC0DA")

const nodes = ref([
  {
    id: "1",
    label: SingleColumn11,
    position: { x: tablex, y: table1y },
    style: { width: columnWidthPx },
    type: "custom-bottom",
  },
  {
    id: "2",
    label: SingleColumn12,
    position: { x: tablex + columnWidth, y: table1y },
    style: { width: columnWidthPx },
    type: "custom-bottom",
  },
  {
    id: "3",
    label: SingleColumn13,
    position: { x: tablex + 2 * columnWidth, y: table1y },
    style: { width: columnWidthPx },
    type: "custom-bottom",
  },
  {
    id: "4",
    label: SingleColumn14,
    position: { x: tablex + 3 * columnWidth, y: table1y },
    style: { width: columnWidthPx },
    type: "custom-bottom",
  },
  {
    id: "5",
    label: SingleColumn15,
    position: { x: tablex + 4 * columnWidth, y: table1y },
    style: { width: columnWidthPx },
    type: "custom-bottom",
  },
  {
    id: "6",
    label: SingleColumn16,
    position: { x: tablex + 5 * columnWidth, y: table1y },
    style: { width: columnWidthPx },
    type: "custom-bottom",
  },
  {
    id: "7",
    label: SingleColumn22,
    position: { x: tablex, y: table2y },
    style: { width: columnWidthPx },
    type: "custom-top",
    zIndex: 1,
  },
  {
    id: "8",
    label: SingleColumn25,
    position: { x: tablex + columnWidth, y: table2y },
    style: { width: columnWidthPx },
    type: "custom-top",
    zIndex: 1,
  },
  {
    id: "9",
    label: SingleColumn23,
    position: { x: tablex + 2 * columnWidth, y: table2y },
    style: { width: columnWidthPx },
    type: "custom-top",
  },
  {
    id: "10",
    label: SingleColumn26,
    position: { x: tablex + 3 * columnWidth, y: table2y },
    style: { width: columnWidthPx },
    type: "custom-top",
  },
  {
    id: "11",
    label: SingleColumn21,
    position: { x: tablex + 4 * columnWidth, y: table2y },
    style: { width: columnWidthPx },
    type: "custom-top",
  },
  {
    id: "12",
    label: SingleColumn24,
    position: { x: tablex + 5 * columnWidth, y: table2y },
    style: { width: columnWidthPx },
    type: "custom-top",
  },
  {
    id: "db1",
    label: "DATENBANK I",
    position: { x: tablex - 110, y: table1y + 75 },
    type: "vertical",
  },
  {
    id: "db2",
    label: "DATENBANK II",
    position: { x: tablex - 110, y: table2y + 75 },
    type: "vertical",
  },
  {
    id: "title1",
    label: "Patientendaten",
    position: { x: tablex, y: table1y - 55 },
    type: "title",
    class: "title-node",
    zIndex: -1,
  },
  {
    id: "title2",
    label: "Patient Data",
    position: { x: tablex, y: table2y + 185 },
    type: "title",
    class: "title-node",
    zIndex: -1,
  },
])

const edges = ref([
  {
    id: "e1-11",
    source: "1",
    target: "11",
    type: "custom",
  },
])

function onConnect(params) {
  addEdges([params])
}

function onSolve() {
  const newEdges = [
    {
      id: "vorname",
      source: "2",
      target: "7",
      type: "custom",
    },
    {
      id: "name",
      source: "3",
      target: "7",
      type: "custom",
    },
    {
      id: "date",
      source: "4",
      target: "12",
      type: "custom",
    },
    {
      id: "diagnosis",
      source: "5",
      target: "8",
      type: "custom",
    },
    {
      id: "bmi",
      source: "6",
      target: "10",
      type: "custom",
    },
  ]
  const uniqueEdges = newEdges.filter((edge) => !edges.value.some((existingEdge) => existingEdge.id === edge.id))
  addEdges(uniqueEdges)
  strokeColor2.value = "#ff6f61"
  strokeColor3.value = "#7cfa46"
}

onPaneReady(() =>
  fitView({
    nodes: ["1", "6", "7", "12"],
    duration: 1500,
    padding: 0.2,
  })
)
</script>

<style>
@import "../../../node_modules/@vue-flow/core/dist/style.css";
@import "../../../node_modules/@vue-flow/core/dist/theme-default.css";

.title-node {
  background: #8cc0da80;
  border: 1px solid grey;
  border-radius: 10px;
  padding: 15px;
  font-size: 20px;
  width: 310px;
}
</style>
