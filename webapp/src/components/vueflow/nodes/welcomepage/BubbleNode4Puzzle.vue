<template>
  <div class="nodrag row justify-center">
    <div class="q-pb-lg q-pl-lg text-bold node-container2 row items-center justify-center">
      Füge Alices <br />und Bobs <br />
      Einkauflisten <br />zusammen!<br />
    </div>
    <puzzle-game ref="puzzleGameRef" @puzzle-finished="allowMoveOn" />
    <div class="column justify-center">
      <div class="q-pt-md text-bold node-container1 row items-center justify-center">
        <div class="q-pl-xl">
          Das ist ein bisschen,<br />
          wie ein Puzzle zu lösen.<br />
        </div>
        <div style="position: relative" class="q-pb-xl" :class="{ pulse: moveOn }">
          <Handle type="source" style="height: 15px; width: 15px; background-color: yellow" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { Handle } from "@vue-flow/core"
import { defineEmits, ref } from "vue"
import PuzzleGame from "components/puzzle/PuzzleGame.vue"

// Reference to PuzzleGame component
const puzzleGameRef = ref(null)
const moveOn = ref(false)

// Expose the reset function from PuzzleGame to parent
const resetPuzzleGame = () => {
  if (puzzleGameRef.value) {
    puzzleGameRef.value.reset()
  }
  moveOn.value = false
}

defineExpose({
  resetPuzzleGame,
})

const emit = defineEmits(["activate-edge"])
function allowMoveOn() {
  moveOn.value = true
  emit("activate-edge")
}
</script>

<style scoped>
.node-container1 {
  height: 300px;
  width: 300px;
  background-image: url("../../../../assets/scads-corp-design/bubbles/bubble-darkblue-4.svg");
  background-size: contain;
  background-repeat: no-repeat;
  color: yellow;
  font-family: "Barlow", bold, sans-serif;
}

.node-container2 {
  height: 300px;
  width: 300px;
  background-image: url("../../../../assets/scads-corp-design/bubbles/bubble-darkblue-5.svg");
  background-size: contain;
  background-repeat: no-repeat;
  color: yellow;
  font-family: "Barlow", bold, sans-serif;
}

@keyframes pulse {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.2);
  }
  100% {
    transform: scale(1);
  }
}

.pulse {
  animation: pulse 1.2s infinite;
}
</style>
