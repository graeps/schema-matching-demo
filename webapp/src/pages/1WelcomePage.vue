<!-- Easy introduction on schema matching made with vue-flow. Travel from node to node on a graph.
On the very end you can decide weather to try the schema matching tool directly or first read the introduction.-->
<template>
  <q-page style="width: 100%; height: 100%">
    <div :class="backgroundClass" class="flow-container">
      <transition>
        <VueFlow
          v-if="showGraph"
          :nodes="nodes"
          :edges="edges"
          :default-viewport="{ zoom: 1.9, x: 380, y: -1120 }"
          :pan-on-drag="false"
          :pan-on-scroll="false"
          :auto-pan-on-connect="false"
          :auto-pan-on-node-drag="false"
          :zoom-on-scroll="false"
          :zoom-on-pinch="false"
          :zoom-on-double-click="false"
          :nodes-draggable="false"
          :nodes-connectable="false"
          :min-zoom="0.1"
        >
          <template #node-start="{}">
            <bubble-node1 />
          </template>
          <template #node-welcome="{}">
            <bubble-node2 @activate-edge="activateEdgeAfterAnimation" />
          </template>
          <template #node-explain="{}">
            <bubble-node3 />
          </template>
          <template #node-game="{}">
            <bubble-node4 ref="bubbleNode4Ref" @activate-edge="activateEdgeAfterPuzzle" />
          </template>
          <template #node-tool-1="{}">
            <bubble-node5a />
          </template>
          <template #node-tool-2="{}">
            <bubble-node5b />
          </template>
          <template #node-end="{}">
            <bubble-node6 />
          </template>
          <template #node-enda="{}">
            <bubble-node6a />
          </template>
          <template #node-endb="{}">
            <bubble-node6b />
          </template>
          <template #node-graphic="{}">
            <graphic-node />
          </template>
          <template #node-question1="{}">
            <question-node1 />
          </template>
          <template #node-question2="{}">
            <question-node2 />
          </template>
          <template #node-question3="{}">
            <question-node3 />
          </template>

          <template
            #edge-transition="{
              source,
              id,
              target,
              sourceX,
              sourceY,
              targetX,
              targetY,
              sourcePosition,
              targetPosition,
              data,
            }"
          >
            <transition-edge
              :id="id"
              :source="source"
              :target="target"
              :source-x="sourceX"
              :source-y="sourceY"
              :target-x="targetX"
              :target-y="targetY"
              :target-position="targetPosition"
              :source-position="sourcePosition"
              :data="data"
            />
          </template>
          <template
            #edge-transition-slow="{
              source,
              id,
              target,
              sourceX,
              sourceY,
              targetX,
              targetY,
              sourcePosition,
              targetPosition,
              data,
            }"
          >
            <transition-edge-slow
              :id="id"
              :source="source"
              :target="target"
              :source-x="sourceX"
              :source-y="sourceY"
              :target-x="targetX"
              :target-y="targetY"
              :target-position="targetPosition"
              :source-position="sourcePosition"
              :data="data"
            />
          </template>
          <template
            #edge-transition-fade-out="{
              source,
              id,
              target,
              sourceX,
              sourceY,
              targetX,
              targetY,
              sourcePosition,
              targetPosition,
              data,
            }"
          >
            <transition-edge-fade-out
              :id="id"
              :source="source"
              :target="target"
              :source-x="sourceX"
              :source-y="sourceY"
              :target-x="targetX"
              :target-y="targetY"
              :target-position="targetPosition"
              :source-position="sourcePosition"
              :data="data"
              @fade-out="changeBackgroundColor"
            />
          </template>
        </VueFlow>
      </transition>
    </div>
  </q-page>
</template>

<script setup>
// Technical imports.
import { onBeforeUnmount, onMounted, ref } from 'vue'
import { useVueFlow, VueFlow } from '@vue-flow/core'

// Import transition edges to travel from node to node.
import TransitionEdge from 'components/vueflow/edges/TransitionEdge.vue'
import TransitionEdgeSlow from 'components/vueflow/edges/TransitionEdgeSlow.vue'
import TransitionEdgeFadeOut from 'components/vueflow/edges/TransitionEdgeFadeOut.vue'

// The nodes.
import BubbleNode1 from 'components/vueflow/nodes/welcomepage/BubbleNode1ClickMe.vue'
import BubbleNode2 from 'components/vueflow/nodes/welcomepage/BubbleNode2Animation.vue'
import BubbleNode3 from 'components/vueflow/nodes/welcomepage/BubbleNode3Explanation.vue'
import BubbleNode4 from 'components/vueflow/nodes/welcomepage/BubbleNode4Puzzle.vue'
import BubbleNode5a from 'components/vueflow/nodes/welcomepage/BubbleNode5aTool.vue'
import BubbleNode5b from 'components/vueflow/nodes/welcomepage/BubbleNode5bTool.vue'
import BubbleNode6 from 'components/vueflow/nodes/welcomepage/BubbleNode6End.vue'
import BubbleNode6a from 'components/vueflow/nodes/welcomepage/BubbleNode6aToDemo.vue'
import BubbleNode6b from 'components/vueflow/nodes/welcomepage/BubbleNode6bToIntro.vue'
import GraphicNode from 'components/vueflow/nodes/welcomepage/BgGraphicNode.vue'
import QuestionNode1 from 'components/vueflow/nodes/welcomepage/QuestionNode1.vue'
import QuestionNode2 from 'components/vueflow/nodes/welcomepage/QuestionNode2.vue'
import QuestionNode3 from 'components/vueflow/nodes/welcomepage/QuestionNode3.vue'

// Functions from vue-flow to react on changes.
const { onPaneReady, fitView, findEdge } = useVueFlow()

const nodes = ref([
  {
    id: '1',
    position: { x: 80, y: 684 },
    type: 'start',
    zIndex: 100,
  },
  {
    id: '2',
    position: { x: 1642, y: 822 },
    type: 'welcome',
    zIndex: 100,
    selectable: true,
  },
  {
    id: '3',
    position: { x: 261, y: 1682 },
    type: 'explain',
    zIndex: 100,
  },
  {
    id: '4',
    position: { x: -550, y: 2832 },
    type: 'game',
    zIndex: 101,
    selectable: true,
  },
  {
    id: '5a',
    position: { x: 1955, y: 2438 },
    type: 'tool-1',
    zIndex: 100,
  },
  {
    id: '5b',
    position: { x: 2219, y: 2384 },
    type: 'tool-2',
    zIndex: 100,
  },
  {
    id: '6',
    position: { x: 560, y: 3786 },
    type: 'end',
    zIndex: 100,
  },
  {
    id: '6a',
    position: { x: 430, y: 4050 },
    type: 'enda',
    zIndex: 100,
  },
  {
    id: '6b',
    position: { x: 985, y: 4030 },
    type: 'endb',
    zIndex: 100,
  },
  {
    id: 'exit1',
    position: { x: -1918, y: 4786 },
    type: 'default',
    zIndex: 100,
  },
  {
    id: 'exit2',
    position: { x: 3518, y: 4786 },
    type: 'default',
    zIndex: 100,
  },
  {
    id: 'q1',
    position: { x: 2105, y: 2987 },
    type: 'question1',
    zIndex: 100,
    selectable: false,
  },
  {
    id: 'q2',
    position: { x: 1514, y: 2991 },
    type: 'question2',
    zIndex: 100,
    selectable: false,
  },
  {
    id: 'q3',
    position: { x: 1153, y: 3444 },
    type: 'question3',
    zIndex: 100,
    selectable: false,
  },
  {
    id: 'g1',
    position: { x: -776, y: 242 },
    type: 'graphic',
    zIndex: 0,
    selectable: false,
  },
])

const edges = ref([
  {
    id: '1-2',
    source: '1',
    target: '2',
    type: 'transition',
    zIndex: 9999,
    data: { active: true },
  },
  {
    id: '2-3',
    source: '2',
    target: '3',
    type: 'transition',
    zIndex: 9999,
    data: { active: false },
  },
  {
    id: '3-4',
    source: '3',
    target: '4',
    type: 'transition',
    zIndex: 9999,
    data: { active: true },
  },
  {
    id: '4-5a',
    source: '4',
    target: '5a',
    type: 'transition',
    zIndex: 9999,
    data: { active: false },
  },
  {
    id: '5b-6',
    source: '5b',
    target: '6',
    type: 'transition-slow',
    zIndex: 9999,
    data: { active: true },
  },
  {
    id: '6a-exit1',
    source: '6a',
    target: 'exit1',
    type: 'transition-fade-out',
    zIndex: 9999,
    data: { active: true, path: '/try-it' },
  },
  {
    id: '6b-exit2',
    source: '6b',
    target: 'exit2',
    type: 'transition-fade-out',
    zIndex: 9999,
    data: { active: true, path: '/intro' },
  },
])

// Focus the first node at the beginning.
onPaneReady(() =>
  fitView({
    nodes: ['1'],
    duration: 1500,
    padding: 0.3,
  }),
)

// Ref and function to trigger reset function in PuzzleGame.vue component.
const bubbleNode4Ref = ref(null)
const resetPuzzleGame = () => {
  if (bubbleNode4Ref.value) {
    bubbleNode4Ref.value.resetPuzzleGame()
  }
}

// Ref and function to trigger reset function in node 2/animation node component.
const bubbleNode2Ref = ref(null)
const resetSchemaAnimation = () => {
  if (bubbleNode2Ref.value) {
    bubbleNode2Ref.value.resetAnimation()
  }
}

// Allow stepping forward.
function activateEdgeAfterAnimation() {
  findEdge('2-3').data.active = true
}
function activateEdgeAfterPuzzle() {
  findEdge('4-5a').data.active = true
}
function deactivateEdges() {
  findEdge('2-3').data.active = false
  findEdge('4-5').data.active = false
}

// Restart the whole landing page and focus start node after 120sec of mouse inactivity
const inactive = ref(false)
let timeoutId = null

const startInactivityTimer = () => {
  timeoutId = setTimeout(() => {
    inactive.value = true
    resetSchemaAnimation()
    resetPuzzleGame()
    deactivateEdges()
    fitView({
      nodes: ['1'],
      duration: 8000,
      padding: 0.3,
    })
  }, 120000)
}

const resetInactivityTimer = () => {
  inactive.value = false
  clearTimeout(timeoutId)
  startInactivityTimer()
}

onMounted(() => {
  window.addEventListener('mousemove', resetInactivityTimer)
  startInactivityTimer()
})

// Remove the event listener when the component is unmounted
onBeforeUnmount(() => {
  window.removeEventListener('mousemove', resetInactivityTimer)
  clearTimeout(timeoutId) // Clear the timer if component is unmounted
})

// Reactive state to control the background color class
const backgroundClass = ref('bg-black') // Default class is black

const changeBackgroundColor = () => {
  backgroundClass.value = 'bg-white' // Change to white background when fading out
  showGraph.value = false
}

// Handle fade out at the very end.
const showGraph = ref(true)
</script>

<style>
@import '../../node_modules/@vue-flow/core/dist/style.css';
@import '../../node_modules/@vue-flow/core/dist/theme-default.css';

.flow-container {
  height: calc(100vh - 60px);
}

.bg-black {
  background: black;
  transition: background-color 4s ease-in-out;
}

.bg-white {
  background: whitesmoke;
  transition: background-color 4s ease-in-out;
}
.v-enter-active,
.v-leave-active {
  transition: opacity 1.5s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}
</style>
