<!-- Puzzle game used on 1WelcomePage.vue. -->
<template>
  <div class="column main-container" style="height: 510px">
    <!--  Upper shopping list with drop zones. Show before puzzle is solved.  -->
    <div class="puzzle-container-top inset-shadow rounded-borders column justify-center items-center" :class="[{ 'bg-default-yellow': bgDefault }, { 'bg-mistake-red': !bgDefault }]">
      <transition name="fade">
        <div v-if="showAlicesList">
          <div class="text-center">Alices Einkaufsliste</div>
          <div class="row nowrap">
            <div v-for="piece in pieces1" :key="piece.id" class="column">
              <img class="img-container-top" :class="{ shake: isShaking }" :src="piece.src" alt="Drop zone piece" />
              <div class="column" :class="{ shake: isShaking }" @drop="onDrop($event, piece.id)" @dragenter.prevent @dragover.prevent>
                <img v-if="movedPieces.find((moved) => moved.id === piece.id)" class="img-container-moved" :src="movedPieces.find((moved) => moved.id === piece.id).src" alt="Moved drop zone piece" />
                <img v-else class="img-container-filler" :src="fillerPieces[piece.id].src" alt="Default drop zone piece" />
              </div>
            </div>
          </div>
        </div>
      </transition>
      <!-- Merged shopping lists. Show after puzzle is solved. -->
      <transition name="fade">
        <div v-if="showCommonList">
          <div class="text-center">Alices & Bobs Einkaufsliste</div>
          <div class="row nowrap">
            <img class="img-container-list" src="../../assets/puzzle/puzzle-complete.png" alt="Puzzle Image" />
          </div>
        </div>
      </transition>
    </div>
    <!-- Congratulation message. Show after puzzle is solved.-->
    <transition name="fade">
      <div v-if="showCongratulations" class="row justify-center">
        <div class="congratulations-msg text-center self-center inset-shadow q-my-md q-pa-md col-4">Sehr gut!</div>
      </div>
    </transition>
    <!--  Lower shopping list. Show before puzzle is solved.  -->
    <transition name="fade">
      <div
        v-if="showBobsList"
        class="puzzle-container-bottom inset-shadow-down rounded-borders column justify-center items-center q-my-sm"
        :class="[{ 'bg-default-yellow': bgDefault }, { 'bg-mistake-red': !bgDefault }]"
      >
        <div class="text-weight-bold">Bobs Einkaufsliste</div>
        <div class="row nowrap">
          <div v-for="piece in pieces2" :key="piece.id" class="img-wrapper" @dragover.prevent @dragstart="startDrag($event, piece.id)">
            <img class="img-container-bottom drag-el" :src="piece.src" alt="Draggable piece" />
          </div>
        </div>
      </div>
    </transition>
    <!-- Button to merge lists. Show after puzzle has been completed-->
    <transition name="fade">
      <div v-if="puzzleCompleted && showBobsList" class="row justify-center">
        <q-btn class="pulse-btn blue-bg blue-border text-yellow shadow-1" size="md" label="Daten verbinden!" @click="mergeLists" />
      </div>
    </transition>
  </div>
</template>

<script setup>
// Functional import from vue.
import { computed, defineEmits, ref } from "vue"

// Importing the individual pieces of the puzzle.
import piece1Tongue from "assets/puzzle/puzzle-piece-1-2.png"
import piece1Groove from "assets/puzzle/puzzle-piece-1-1.png"
import piece3Tongue from "assets/puzzle/puzzle-piece-2-2.png"
import piece2Groove from "assets/puzzle/puzzle-piece-2-1.png"
import piece5Tongue from "assets/puzzle/puzzle-piece-3-2.png"
import piece3Groove from "assets/puzzle/puzzle-piece-3-1.png"
import piece1Filler from "assets/puzzle/puzzle-filler-1.png"
import piece2Filler from "assets/puzzle/puzzle-filler-2.png"
import piece3Filler from "assets/puzzle/puzzle-filler-3.png"

// Handle background color. Turns red if player makes misstake.
const bgDefault = ref(true)

// Handle shaking animation when merging.
const isShaking = ref(false)

// Handle congratulations message.
const showCongratulations = ref(false)

// Drop zone pieces (non-draggable).
const pieces1 = ref([
  { id: "0", src: piece1Groove },
  { id: "1", src: piece2Groove },
  { id: "2", src: piece3Groove },
])
// Draggable pieces.
const pieces2 = ref([
  { id: "2", src: piece5Tongue },
  { id: "0", src: piece1Tongue },
  { id: "1", src: piece3Tongue },
])

const movedPieces = ref([])

const fillerPieces = ref([
  { id: "0", src: piece1Filler },
  { id: "1", src: piece2Filler },
  { id: "2", src: piece3Filler },
])

const puzzleCompleted = computed(() => movedPieces.value.length === 3)
const showBobsList = ref(true)
const showAlicesList = ref(true)
const showCommonList = ref(false)

const mergeLists = () => {
  showBobsList.value = false
  isShaking.value = true
  setTimeout(() => {
    showAlicesList.value = false
  }, 1000)
  setTimeout(() => {
    showCommonList.value = true
    isShaking.value = false
  }, 1900)
  setTimeout(() => {
    showCongratulations.value = true
    onPuzzleFinished()
  }, 2900)
}

const startDrag = (event, pieceID) => {
  event.dataTransfer.dropEffect = "move"
  event.dataTransfer.effectAllowed = "move"
  event.dataTransfer.setData("pieceID", pieceID)
}

// Handle the drop event in the drop zone
const onDrop = (event, dropzone) => {
  const pieceID = event.dataTransfer.getData("pieceID") // Get the ID of the dragged piece
  const pieceIndex = pieces2.value.findIndex((item) => item.id === pieceID)

  // If piece exists in pieces2, add it to movedPieces and remove it from pieces2
  if (pieceIndex !== -1 && pieceID === dropzone) {
    const pieceToMove = pieces2.value[pieceIndex] // Get the piece object
    movedPieces.value.push(pieceToMove) // Add the piece to movedPieces
    pieces2.value.splice(pieceIndex, 1) // Remove the piece from pieces2
  }
  if (pieceIndex !== -1 && pieceID !== dropzone) {
    bgDefault.value = false
    setTimeout(() => {
      bgDefault.value = true
    }, 400)
  }
}

// Reset everything. Exposed to parent component.
const reset = () => {
  showBobsList.value = true
  showAlicesList.value = true
  showCommonList.value = false
  bgDefault.value = true
  isShaking.value = false
  movedPieces.value = []
  pieces2.value = [
    { id: "2", src: piece5Tongue },
    { id: "0", src: piece1Tongue },
    { id: "1", src: piece3Tongue },
  ]
}

// Expose the reset function
defineExpose({
  reset,
})

// Emit event when puzzle is finished to allow to step forward.
const emit = defineEmits(["puzzle-finished"])
function onPuzzleFinished() {
  emit("puzzle-finished")
}
</script>

<style scoped>
.main-container {
  font-family: "Barlow", bold, sans-serif;
}

.img-container-top {
  margin-right: -5px;
  margin-left: -5px;
  margin-top: -20px;
  width: 90px;
  height: 115px;
  position: relative;
  z-index: 2;
}

.img-container-filler {
  margin-right: -5px;
  margin-left: -5px;
  margin-top: -25px;
  width: 90px;
  height: 115px;
}

.img-container-moved {
  margin-right: -5px;
  margin-left: -5px;
  margin-top: -25px;
  width: 90px;
  height: 115px;
  z-index: 2;
  position: relative;
}

.img-container-bottom {
  margin-right: -5px;
  margin-left: -5px;
  width: 90px;
  height: 115px;
}

.img-container-list {
  width: 260px;
  height: 115px;
}

@keyframes rotate {
  0% {
    transform: rotate(-1deg);
  }
  50% {
    transform: rotate(1deg);
  }
  100% {
    transform: rotate(-1deg);
  }
}

.img-wrapper {
  animation: rotate 2s infinite;
}

.img-wrapper:nth-child(1) {
  animation-delay: 0s;
}

.img-wrapper:nth-child(2) {
  animation-delay: -0.9s;
}

.img-wrapper:nth-child(3) {
  animation-delay: -1.3s;
}

.puzzle-container-top {
  width: 355px;
  height: 250px;
  padding: 10px;
  border-radius: 100px;
}
.puzzle-container-bottom {
  width: 355px;
  height: 200px;
  padding: 10px;
  border-radius: 100px;
}

.bg-default-yellow {
  background: #e8e58d;
}

.bg-mistake-red {
  background: #ff6f61;
}

.drag-el {
  cursor: grab;
  transition: transform 0.1s ease;
}

.drag-el:hover {
  transform: scale(1.02);
}

/* Fade transition styles for both enter and leave */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.7s ease;
}
.fade-enter-from {
  opacity: 0;
}
.fade-enter-to {
  opacity: 1;
}
.fade-leave-from {
  opacity: 1;
}
.fade-leave-to {
  opacity: 0;
}

@keyframes pulseHighlight {
  0% {
    box-shadow: 0 0 5px rgba(255, 255, 0, 0);
    border-color: #1e90ff;
  }
  50% {
    box-shadow: 0 0 10px rgba(255, 255, 0, 0.6);
    border-color: yellow;
  }
  100% {
    box-shadow: 0 0 5px rgba(255, 255, 0, 0);
    border-color: #1e90ff;
  }
}

.pulse-btn {
  animation: pulseHighlight 2s infinite;
  transition:
    background-color 0.3s ease,
    border-color 0.3s ease;
}

@keyframes shake {
  0% {
    transform: translateX(0) rotate(0deg);
  }
  20% {
    transform: translateX(-1px) rotate(-1deg);
  }
  40% {
    transform: translateX(1px) rotate(1deg);
  }
  60% {
    transform: translateX(-1px) rotate(-1deg);
  }
  80% {
    transform: translateX(1px) rotate(1deg);
  }
  100% {
    transform: translateX(0) rotate(0deg);
  }
}

.shake {
  animation: shake 2s infinite;
}

.shake:nth-child(1) {
  animation-delay: 0s;
}
.shake:nth-child(2) {
  animation-delay: -0.2s;
}
.shake:nth-child(3) {
  animation-delay: -0.6s;
}
.shake:nth-child(4) {
  animation-delay: -0.3s;
}
.shake:nth-child(5) {
  animation-delay: -0.7s;
}
.shake:nth-child(6) {
  animation-delay: -0.9s;
}

.congratulations-msg {
  background-color: #d450aa;
  border: 1px solid #ad2f85;
  border-radius: 40px;
  font-family: "Barlow", sans-serif;
  font-size: 18px;
  color: yellow;
}
</style>
