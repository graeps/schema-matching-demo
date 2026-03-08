<template>
  <div class="text-bold node-container row items-center justify-center">
    <div class="col">
      <div class="circle-text">
        <transition name="fade">
          <svg v-if="moveOn" viewBox="0 0 200 200">
            <!-- Upper half text: "Schema matching?" -->
            <path id="upperPath" fill="transparent" d="M 20,100 A 100,65 0 0 1 180,100" />
            <text>
              <textPath href="#upperPath" startOffset="32%">Klick mich!</textPath>
            </text>

            <!-- Lower half text: "Klick mich!" -->
            <path id="lowerPath" fill="transparent" d="M 20,110 A 100,65 0 0 0 180,110" />
            <text>
              <textPath href="#lowerPath" startOffset="37%"></textPath>
            </text>
          </svg>
        </transition>
        <!-- Handle element positioned in the center -->
        <div :class="{ pulse: moveOn }" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%)">
          <Handle type="source" style="height: 15px; width: 15px; background-color: yellow; border-radius: 50%" :position="Position.Left" />
        </div>
      </div>
    </div>
    <div class="column">
      <div class="col text-center q-mt-xl q-mb-md text-h5" style="color: yellow">Schema Matching!</div>

      <div class="container q-mb-md">
        <transition name="fade">
          <div v-if="showButton" class="col center-content">
            <q-btn rounded class="shadow-5 main-btn softPulse" label="Was ist das?" size="md" @click="startSequence"></q-btn>
          </div>
        </transition>
        <!-- First Image (Left) -->
        <transition name="fade">
          <div v-show="showFirstImage" :class="['col', { 'move-to-right': moveImageRight }, 'start-content']" style="left: 0">
            <img src="../../../../assets/diagrams/data-pic-1.png" alt="First" class="image-style" />
          </div>
        </transition>

        <!-- Second Image (Right) -->
        <transition name="fade">
          <div v-show="showSecondImage" :class="['col', { 'move-to-left': moveImageLeft }, 'end-content']" style="right: 0">
            <img src="../../../../assets/diagrams/data-pic-2.png" alt="Second" class="image-style" />
          </div>
        </transition>

        <!-- Third Image (Center) -->
        <transition name="fade">
          <div v-show="showThirdImage" :class="['col', { 'move-to-right': moveThirdImage }, 'center-content']">
            <img src="../../../../assets/diagrams/data-pic-3.png" alt="Third" class="image-style-2" />
          </div>
        </transition>
        <transition name="fade">
          <div v-show="moreDetails" class="col column center-content text-h6" style="color: yellow">Mehr erfahren?</div>
        </transition>
        <!-- Third Image (Center) -->
        <transition name="fade">
          <div v-show="moveOn" class="col column center-left q-pt-xl" style="rotate: 20deg; color: yellow">
            <q-icon name="keyboard_double_arrow_left" size="xl"></q-icon>
          </div>
        </transition>
      </div>
    </div>
    <div class="col-3 col-md-3"></div>
  </div>
</template>

<script setup>
import { ref, defineEmits } from "vue"
import { Handle, Position } from "@vue-flow/core"

const showButton = ref(true)
const showFirstImage = ref(false)
const showSecondImage = ref(false)
const showThirdImage = ref(false)
const moveImageRight = ref(false)
const moveImageLeft = ref(false)
const moveThirdImage = ref(false)
const moreDetails = ref(false)
const moveOn = ref(false)

const startSequence = () => {
  // Fade out the button
  showButton.value = false

  // Fade in the first image after 0.5 sec
  setTimeout(() => {
    showFirstImage.value = true
  }, 1000)

  // Fade in the second image after 1.5 sec
  setTimeout(() => {
    showSecondImage.value = true
  }, 2500)
  // Move images to center after 2.5 seconds
  setTimeout(() => {
    moveImageRight.value = true
    moveImageLeft.value = true
  }, 3700)

  // Show the third image after images fade out (after 3.5 sec)
  setTimeout(() => {
    showFirstImage.value = false
    showSecondImage.value = false
    showThirdImage.value = true
  }, 5700)
  setTimeout(() => {
    moveThirdImage.value = true
  }, 7500)
  setTimeout(() => {
    moreDetails.value = true
  }, 9000)
  setTimeout(() => {
    moveOn.value = true
    allowMoveOn()
  }, 10500)
}

const resetAnimation = () => {
  showButton.value = true
  showFirstImage.value = false
  showSecondImage.value = false
  showThirdImage.value = false
  moveImageRight.value = false
  moveImageLeft.value = false
  moreDetails.value = false
  moveOn.value = false
}

// Expose the reset function
defineExpose({
  resetAnimation,
})

const emit = defineEmits(["activate-edge"])
function allowMoveOn() {
  emit("activate-edge")
}
</script>

<style scoped>
.node-container {
  height: 600px;
  width: 600px;
  background-image: url("../../../../assets/scads-corp-design/bubbles/bubble-darkblue-6.svg");
  background-size: contain;
  background-repeat: no-repeat;
}

.circle-text {
  width: 200px; /* Adjust as necessary */
  height: 200px;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}

.circle-text svg {
  width: 100%;
  height: 100%;
}

.circle-text text {
  font-size: 12px;
  font-weight: bold;
  fill: rgb(255, 255, 0); /* Text color */
}

@keyframes pulse {
  0% {
    transform: scale(1); /* Normalgröße, keine Rotation */
  }
  50% {
    transform: scale(1.2); /* Größer und um 45 Grad gedreht */
  }
  100% {
    transform: scale(1); /* Zurück zur Normalgröße und Rotation */
  }
}

.pulse {
  animation: pulse 1.2s infinite;
}

@keyframes softPulse {
  0% {
    transform: scale(1); /* Normalgröße, keine Rotation */
  }
  50% {
    transform: scale(1.05); /* Größer und um 45 Grad gedreht */
  }
  100% {
    transform: scale(1); /* Zurück zur Normalgröße und Rotation */
  }
}

.softPulse {
  animation: softPulse 1.2s infinite;
}

.main-btn {
  background-color: #d450aa;
  border: #ad2f85;
  font-family: "Barlow", sans-serif;
  font-size: 20px;
  color: yellow;
}

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

.container {
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  width: 300px;
  height: 120px;
}

.start-content {
  position: absolute;
  left: 0; /* Stick to the left */
}

.center-content {
  position: absolute;
  left: 50%;
  transform: translateX(-50%); /* Center horizontally */
}

.end-content {
  position: absolute;
  right: 0; /* Stick to the right */
}

.move-to-right {
  transform: translateX(95%); /* Move the first image from left to center */
  transition:
    transform 1.5s ease-in-out,
    opacity 1s ease-in-out;
}

.move-to-left {
  transform: translateX(-95%); /* Move the first image from left to center */
  transition:
    transform 1.5s ease-in-out,
    opacity 1s ease-in-out;
}

.image-style {
  max-width: 100px;
  max-height: 100px;
  transition:
    transform 1.5s ease-in-out,
    opacity 1s ease-in-out;
}

.image-style-2 {
  max-width: 110px;
  max-height: 110px;
  transition:
    transform 1.5s ease-in-out,
    opacity 1s ease-in-out;
}
</style>
