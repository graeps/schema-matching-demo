<!-- Core component of the interactive section. Takes two schemas and their mapping results.
Creates a vue-flow graph with two features:
1' two tables can get manually matched.
2' by click on button, results can be compared to the given matching results.-->
<template>
  <VueFlow
    v-model:edges="edges"
    fit-view-on-init
    :pan-on-drag="false"
    :pan-on-scroll="false"
    :auto-pan-on-connect="false"
    :auto-pan-on-node-drag="false"
    :zoom-on-scroll="false"
    :zoom-on-pinch="false"
    :zoom-on-double-click="false"
    :nodes="nodes"
    :nodes-draggable="false"
    :nodes-connectable="nodesConnectable"
    :connection-radius="50"
    :connection-mode="ConnectionMode.Loose"
    :max-zoom="1.5"
    :min-zoom="0.5"
    delete-key-code="false"
    @connect="onConnect"
  >
    <!-- Background with dots.-->
    <Background variant="dots" />

    <!-- Custom nodes and edges. -->
    <template #node-custom-bottom="{ label }">
      <CustomNodeBottom :label="label" />
    </template>
    <template #node-custom-top="{ label }">
      <CustomNodeTop :label="label" />
    </template>
    <template #node-title="{ label }">
      <TitleNode :label="label" />
    </template>
    <template #node-vertical="{ label }">
      <vertical-title-node :label="label" />
    </template>
    <template #connection-line="{ sourceX, sourceY, targetX, targetY, sourcePosition, targetPosition }">
      <SnapConnectionLine
        :source-x="sourceX"
        :source-y="sourceY"
        :target-x="targetX"
        :target-y="targetY"
        :source-position="sourcePosition"
        :target-position="targetPosition"
        :color="strokeColorPlayer"
      />
    </template>
    <template #edge-player="{ id, sourceX, sourceY, targetX, targetY, sourcePosition, targetPosition }">
      <CustomConnectionLine
        :id="id"
        :source-x="sourceX"
        :source-y="sourceY"
        :target-x="targetX"
        :target-y="targetY"
        :target-position="targetPosition"
        :source-position="sourcePosition"
        :color="strokeColorPlayer"
      />
    </template>
    <template #edge-intersec="{ id, sourceX, sourceY, targetX, targetY, sourcePosition, targetPosition }">
      <CustomConnectionLine
        :id="id"
        :source-x="sourceX"
        :source-y="sourceY"
        :target-x="targetX"
        :target-y="targetY"
        :target-position="targetPosition"
        :source-position="sourcePosition"
        :color="strokeColorIntersec"
      />
    </template>
    <template #edge-calc="{ id, sourceX, sourceY, targetX, targetY, sourcePosition, targetPosition }">
      <CustomConnectionLine
        :id="id"
        :source-x="sourceX"
        :source-y="sourceY"
        :target-x="targetX"
        :target-y="targetY"
        :target-position="targetPosition"
        :source-position="sourcePosition"
        :color="strokeColorCalc"
      />
    </template>
    <template #edge-hide="{ id, sourceX, sourceY, targetX, targetY, sourcePosition, targetPosition }">
      <CustomConnectionLine
        :id="id"
        :source-x="sourceX"
        :source-y="sourceY"
        :target-x="targetX"
        :target-y="targetY"
        :target-position="targetPosition"
        :source-position="sourcePosition"
        :color="strokeColorHide"
      />
    </template>

    <!-- Panel with button to undo last edge added. -->
    <undo-panel v-if="showUndoPanel" @delete-edge="deleteLastEdgeAdded"></undo-panel>

    <!-- Info panel to show comparison between manual matching and given matching. -->
    <venn-diagram
      v-if="showResults"
      :common-matches="String(commonFoundMatches)"
      :found-matches="String(foundByPlayer)"
      :calc-matches="String(foundByTool)"
      class="results-panel"
      @hover-left="handleHoverLeft"
      @hover-right="handleHoverRight"
      @hover-intersection="handleHoverIntersection"
      @no-hover="handleNoHover"
    />
  </VueFlow>
</template>

<script setup>
// Functional import from vue.
import { computed, h, ref, watch } from "vue"

// Functional imports for vue-flow.
import { ConnectionMode, useVueFlow, VueFlow } from "@vue-flow/core"
import { Background } from "@vue-flow/background"

// Custom styled components for vue-flow.
import CustomNodeTop from "components/vueflow/nodes/demo/SingleColumnNodeTop.vue"
import CustomNodeBottom from "components/vueflow/nodes/demo/SingleColumnNodeBottom.vue"
import CustomConnectionLine from "components/vueflow/edges/CustomConnectionLine.vue"
import SnapConnectionLine from "components/vueflow/edges/SnappableConnectionLine.vue"
import TitleNode from "components/vueflow/nodes/demo/TitleNode.vue"
import VennDiagram from "components/vueflow/panels/ResultsPanel.vue"
import UndoPanel from "components/vueflow/panels/UndoPanel.vue"
import VerticalTitleNode from "components/vueflow/nodes/demo/VerticalTitleNode.vue"

// Component to generate single column markup table. Used to create the content of vue-flow nodes later.
import GenColumn from "./ColumnGen.vue"

// Functions to correctly update vue-flow.
const { addNodes, addEdges, removeEdges, fitView, onNodesInitialized } = useVueFlow()

const props = defineProps({
  // First table to show. Dictionary of form: {'title': title, 'schema': content_data}
  table1: {
    type: Object,
    required: true,
  },
  // Second table to show. Dictionary of form: {'title': title, 'schema': content_data}
  table2: {
    type: Object,
    required: true,
  },
})

// Layout of the tables and columns.
const columnWidth = 220
const columnWidthPx = columnWidth + "px"
const offsetX = 0
const offsetY = 0
const shiftY = 370

// Layout connection lines and nodes.
const strokeColorCalc = ref("#ff6f61")
const strokeColorIntersec = ref("#e96dff")
const strokeColorPlayer = ref("rgb(30,144,255)")
const strokeColorHide = ref("rgba(195,195,195,0.42)")

// Possible node types. First table is shown on the top, second table on the bottom.
const nodeTypes = ["custom-bottom", "custom-top"]

// Nodes and edges of the graph.
const edges = ref([])
const nodes = ref([])

// Store manually matched columns and automatically matched columns separately to compare them later.
const drawnEdges = ref([])
const calculatedEdges = ref([])

// Store comparison between manual and automatic match to show them in the results panel.
const commonFoundMatches = ref(0)
const foundByPlayer = ref(0)
const foundByTool = ref(0)

// Don't allow manual matches anymore after calculating the automatic matching.
const nodesConnectable = ref(true)

// Show undo panel only when undo is possible.
const showUndoPanel = computed(() => !showResults.value && drawnEdges.value.length > 0)

// Show the matching results while true.
const showResults = ref(false)

// Fit the viewport whenever nodes changes. Transition takes 1 sec.
onNodesInitialized(() => fitView({ duration: 1000 }))

// Function triggered when two nodes are connected manually. Specifies the ID in particular.
const onConnect = (params) => {
  console.log(params)
  // Manually assign an ID to the edge
  const newEdge = {
    id: `${params.source}-${params.target}`,
    source: params.source,
    target: params.target,
    type: "player",
  }
  //Check if the newEdge exists already
  if (!drawnEdges.value.some((existingEdge) => existingEdge.id === newEdge.id) && !drawnEdges.value.some((existingEdge) => existingEdge.id === `${params.target}-${params.source}`)) {
    //Add Edge to drawnEdges to compare later with calculatedEdges
    drawnEdges.value.push(newEdge)
    // Add edge to VueFlow
    addEdges([newEdge])
  }
}

// Function for undo panel. Deletes the last edge added, if possible.
const deleteLastEdgeAdded = () => {
  if (drawnEdges.value.length > 0) {
    const edgeId = drawnEdges.value.pop()
    removeEdges([edgeId])
  }
}

/**
 * Creates two tables in vue-flow, vertically one over each other, with connectable columns.
 * @param {string} headline - Headline above the graph.
 * @param {Object} table1 - Upper table as dictionary. Form: {'title': title, 'schema': content_data}
 * @param {Object} table2 - Lower table as dictionary. Form: {'title': title, 'schema': content_data}
 * @param {int} offsetX - X-coordinate of upper left corner.
 * @param {int} offsetY - Y-coordinate of upper left corner.
 * @param {int} distanceY - Vertical distance between the two tables in pixel.
 * @param {string} idPrefix - Optional prefix of IDs of nodes
 */
const createConnectableTables = (headline, table1, table2, offsetX, offsetY, distanceY, idPrefix = "") => {
  let columnY = offsetY + 50
  // Add headline of graph and titles of the tables as custom nodes.
  const headlineNode = {
    id: idPrefix + headline,
    label: headline,
    position: { x: offsetX + 2 * columnWidth - 200, y: offsetY - 20 },
    type: "title",
    class: "headline-node",
  }
  const titleNode1 = {
    id: idPrefix + "title1",
    label: table1.title,
    position: { x: offsetX, y: offsetY - 5 },
    type: "title",
    class: "title-node",
  }
  const titleNode2 = {
    id: idPrefix + "title2",
    label: table2.title,
    position: { x: offsetX, y: offsetY + distanceY + 235 },
    type: "title",
    class: "title-node",
  }
  const dbNode1 = {
    id: idPrefix + "db1",
    label: "DATENBANK I",
    position: { x: offsetX - 115, y: offsetY + 130 },
    type: "vertical",
  }
  const dbNode2 = {
    id: idPrefix + "db2",
    label: "DATENBANK II",
    position: { x: offsetX - 115, y: offsetY + 500 },
    type: "vertical",
  }
  addNodes([headlineNode, titleNode1, titleNode2, dbNode1, dbNode2])

  // Check if tables are valid and add schema nodes
  if (table1 && table1.schema && table2 && table2.schema) {
    const tables = [table1.schema, table2.schema]

    tables.forEach((table, index) => {
      let columnX = offsetX
      let nodeType = nodeTypes[index]

      Object.keys(table).forEach((key) => {
        // Generate a one column markup table as content of each node.
        const tableContent = h(GenColumn, { title: key, content: table[key] })
        // Create new node with dynamic unique ID
        const newNode = {
          id: idPrefix + `${index}${key}`,
          label: tableContent,
          position: { x: columnX, y: columnY },
          style: { width: columnWidthPx },
          type: nodeType,
        }
        addNodes(newNode)
        columnX += columnWidth
      })
      columnY += shiftY
    })
  } else {
    console.error("schema1 or schema2 props are missing or in wrong format")
  }
}

/**
 * Show the generated tables reactively depending on props.table1, props.table2 and layout choices.
 * These tables should be connected by the user.
 */
const showGeneratedData = () => {
  createConnectableTables("", props.table1, props.table2, offsetX, offsetY, shiftY)
}
watch(() => [props.table1, props.table2], showGeneratedData)

/**
 * Compares two arrays and returns how many elements are in both, or only one of them respectively.
 * @param arr1 - First array.
 * @param arr2 - Second array.
 * @returns {{commonElements: number, onlyInFirst: number, onlyInSecond: number}}
 */
function compareMatches(arr1, arr2) {
  let commonElements = 0
  let onlyInFirst = arr1.length
  let onlyInSecond = arr2.length
  arr1.forEach((item1) => {
    const existsInArr2 = arr2.some((item2) => item1.id === item2.id)

    // If it exists, update the edge.type
    if (existsInArr2) {
      commonElements++
    }
  })
  return {
    commonElements,
    onlyInFirst,
    onlyInSecond,
  }
}

/**
 * Adds a second graph to the plane, showing the results of the schema matching received by the parent component via props.matching.
 * Adds informativ results panel to the lower left corner.
 */
const showMatching = (matching) => {
  calculatedEdges.value.forEach((oldEdge) => {
    const existsInDrawnEdges = drawnEdges.value.some((drawnEdge) => drawnEdge.id === oldEdge.id)
    if (!existsInDrawnEdges) {
      removeEdges([oldEdge])
    }
  })
  if (process.env.DEV) {
    console.log("matching results", matching)
  }
  if (!Array.isArray(matching)) {
    console.error("props.matching is not an array")
    return
  }
  calculatedEdges.value = matching.map((pair) => ({
    id: `${pair[0]}-${pair[1]}`,
    source: pair[0],
    target: pair[1],
    type: "calc",
  }))

  const result = compareMatches(drawnEdges.value, calculatedEdges.value)
  commonFoundMatches.value = result.commonElements
  foundByPlayer.value = result.onlyInFirst
  foundByTool.value = result.onlyInSecond

  // Filter out edges that already exist in the edges array
  const newEdges = calculatedEdges.value.filter((newEdge) => !drawnEdges.value.some((existingEdge) => existingEdge.id === newEdge.id))
  // Add only the unique edges to the edges array
  if (newEdges.length > 0) {
    addEdges(newEdges) // Your existing function to add edges
  }

  showResults.value = true
  nodesConnectable.value = false
}

// Clear the graph. Is exposed to parent component since it has to be triggered when new data is generated via AttributeGen.vue.
const clearAll = () => {
  showResults.value = false
  nodesConnectable.value = true
  drawnEdges.value = []
  calculatedEdges.value = []
  edges.value = []
  nodes.value = []
}

/** Handle the interaction of the results panel with the vue-flow graph.
 * Edges get highlighted depending on which part of the venn diagramm in the results panel is hovered.
 */
function handleNoHover() {
  edges.value.forEach((edge) => {
    const existsInDrawnEdges = drawnEdges.value.some((drawnEdge) => drawnEdge.id === edge.id)
    if (existsInDrawnEdges) {
      edge.type = "player"
    } else {
      edge.type = "calc"
    }
  })
}

function handleHoverLeft() {
  edges.value.forEach((edge) => {
    const existsInDrawnEdges = drawnEdges.value.some((drawnEdge) => drawnEdge.id === edge.id)
    if (existsInDrawnEdges) {
      edge.type = "player"
      edge.zIndex = 1
    } else {
      edge.type = "hide"
      edge.zIndex = 0
    }
  })
}

function handleHoverRight() {
  edges.value.forEach((edge) => {
    const existsInCalcEdges = calculatedEdges.value.some((calcEdge) => calcEdge.id === edge.id)
    // If it exists, update the edge.type
    if (existsInCalcEdges) {
      edge.type = "calc" // Set the type to "drawn"
      edge.zIndex = 1
    } else {
      edge.type = "hide"
      edge.zIndex = 0
    }
  })
}

function handleHoverIntersection() {
  edges.value.forEach((edge) => {
    const existsInDrawnEdges = drawnEdges.value.some((drawnEdge) => drawnEdge.id === edge.id)
    const existsInCalcEdges = calculatedEdges.value.some((calcEdge) => calcEdge.id === edge.id)
    // If it exists, update the edge.type
    if (existsInDrawnEdges && existsInCalcEdges) {
      edge.type = "intersec" // Set the type to "drawn"
      edge.zIndex = 1
    } else {
      edge.type = "hide"
      edge.zIndex = 0
    }
  })
}

// Expose these functions to the parent component.
defineExpose({ showMatching, clearAll })
</script>

<style>
@import "../../../node_modules/@vue-flow/core/dist/style.css";
@import "../../../node_modules/@vue-flow/core/dist/theme-default.css";

.title-node {
  background: #8cc0da80;
  border: 2px solid #8cc0da;
  border-radius: 10px;
  padding: 15px;
  font-size: 20px;
  width: 310px;
}

.headline-node {
  background: rgba(255, 255, 255, 0.5);
  padding: 0;
  border: 0;
  font-size: 40px;
  width: 800px;
}
</style>
