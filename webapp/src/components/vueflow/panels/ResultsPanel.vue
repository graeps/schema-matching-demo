<template>
  <Panel position="bottom-left" class="panel-style shadow-5" @mouseenter="hideHint">
    <div class="text-h6 text-center q-mt-md">Ergebnisse</div>
    <div class="row justify-center items-center">
      <div class="svg-container" @mouseenter="emitEvent('no-hover')" @mouseleave="emitEvent('no-hover')">
        <div v-if="isIntersectionHovered">
          <q-tooltip v-model="isIntersectionHovered" class="shadow-1" style="background: #ed93fe" transition-hide="scale" anchor="bottom middle" self="top middle" :delay="2000">
            <div class="result-popup">
              Ihr habt {{ props.commonMatches }} <br />
              gemeinsame Matches.
            </div>
          </q-tooltip>
        </div>

        <svg :width="280 * scale" :height="200 * scale">
          <!-- Left Circle -->
          <circle
            :cx="100 * scale"
            :cy="100 * scale"
            :r="80 * scale"
            class="circle left"
            :class="[{ hovered: isLeftHovered }, { hide: isRightHovered || isIntersectionHovered }]"
            @mouseenter.stop="emitEvent('hover-left')"
            @mouseleave="emitEvent('no-hover')"
          />

          <!-- Right Circle -->
          <circle
            :cx="180 * scale"
            :cy="100 * scale"
            :r="80 * scale"
            class="circle right"
            :class="[{ hovered: isRightHovered }, { hide: isLeftHovered || isIntersectionHovered }]"
            @mouseenter.stop="emitEvent('hover-right')"
            @mouseleave="emitEvent('no-hover')"
          ></circle>

          <!-- Intersection using ClipPath -->
          <g>
            <clipPath id="clip-left">
              <circle :cx="100 * scale" :cy="100 * scale" :r="80 * scale" />
            </clipPath>
            <clipPath id="clip-right">
              <circle :cx="180 * scale" :cy="100 * scale" :r="80 * scale" />
            </clipPath>
            <!-- Intersection fill area -->
            <circle
              :cx="180 * scale"
              :cy="100 * scale"
              :r="80 * scale"
              clip-path="url(#clip-left)"
              class="intersection"
              :class="[{ hovered: isIntersectionHovered && !(isRightHovered || isLeftHovered) }, { hide: isRightHovered || isLeftHovered }]"
              @mouseenter.stop="emitEvent('hover-intersection')"
              @mouseleave="emitEvent('no-hover')"
            />
            <circle
              :cx="100 * scale"
              :cy="100 * scale"
              :r="80 * scale"
              clip-path="url(#clip-right)"
              class="intersection"
              :class="[{ hovered: isIntersectionHovered && !(isRightHovered || isLeftHovered) }, { hide: isRightHovered || isLeftHovered }]"
              @mouseenter.stop="emitEvent('hover-intersection')"
              @mouseleave="emitEvent('no-hover')"
            />
          </g>
        </svg>
        <div v-if="showBeforeHovered">
          <q-tooltip v-model="showBeforeHovered" anchor="top middle" self="bottom middle" class="shadow-1" style="background: #ed93fe">
            <div class="result-popup">
              Fahre mit der Maus <br />
              über das Diagramm.
            </div></q-tooltip
          >
        </div>
        <div v-if="isRightHovered">
          <q-tooltip v-model="isRightHovered" class="shadow-1" style="background: #ed93fe" transition-hide="scale" anchor="top right" self="bottom right">
            <div class="result-popup">
              Das Tool hat {{ props.calcMatches }} <br />
              Matches gefunden.
            </div>
          </q-tooltip>
        </div>
        <div v-if="isLeftHovered">
          <q-tooltip v-model="isLeftHovered" class="shadow-1" style="background: #ed93fe" transition-hide="scale" anchor="top left" self="bottom left">
            <div class="result-popup">
              Du hast {{ props.foundMatches }} <br />
              Matches gefunden.
            </div>
          </q-tooltip>
        </div>
      </div>
    </div>
  </Panel>
</template>

<script setup>
import { ref, defineProps } from "vue"
import { Panel } from "@vue-flow/core"

const props = defineProps({
  commonMatches: {
    type: String,
    required: true,
  },
  foundMatches: {
    type: String,
    required: true,
  },
  calcMatches: {
    type: String,
    required: true,
  },
})

const showBeforeHovered = ref(true)

const hideHint = () => (showBeforeHovered.value = false)

const scale = 0.8
// Define the emit function to send events to the parent
const emit = defineEmits(["no-hover", "hover-left", "hover-right", "hover-intersection"])

// Hover states for each element
const isLeftHovered = ref(false)
const isRightHovered = ref(false)
const isIntersectionHovered = ref(false)

// Emit event based on the hovered section
function emitEvent(eventType) {
  resetHover() // Reset all hover states
  if (eventType === "hover-left") {
    isLeftHovered.value = true
    isRightHovered.value = false
    isIntersectionHovered.value = false
  } else if (eventType === "hover-right") {
    isRightHovered.value = true
    isLeftHovered.value = false
    isIntersectionHovered.value = false
  } else if (eventType === "hover-intersection") {
    isIntersectionHovered.value = true
    isLeftHovered.value = false
    isRightHovered.value = false
  }
  if (eventType === "no-hover") {
    isLeftHovered.value = false
    isRightHovered.value = false
    isIntersectionHovered.value = false
  }
  // Emit the event to the parent
  emit(eventType)
}

// Reset hover state when the mouse leaves any of the areas
function resetHover() {
  isLeftHovered.value = false
  isRightHovered.value = false
  isIntersectionHovered.value = false
}
</script>

<style scoped>
.circle {
  transition:
    stroke 0.1s,
    fill 0.1s,
    stroke-width 0.1s;
  pointer-events: all;
}

.circle.left {
  fill: rgba(30, 144, 255, 0.34);
  stroke: rgba(1, 129, 255, 0.59);
  stroke-width: 2;
}

.circle.right {
  fill: rgba(255, 111, 97, 0.57);
  stroke: rgba(253, 48, 30, 0.62);
  stroke-width: 2;
}

/* Highlight the left circle border on hover */
.circle.left.hovered {
  fill: rgba(30, 144, 255, 0.82);
  stroke: rgb(1, 129, 255);
  stroke-width: 4;
}

/* Highlight the right circle border on hover */
.circle.right.hovered {
  fill: #ff6f61;
  stroke: #fd301e;
  stroke-width: 4;
}

/* Intersection area hover effect */
.intersection {
  fill: rgba(138, 43, 226, 0.09);
  stroke: #8a2be2;
  transition:
    fill 0.1s,
    stroke 0.1s,
    stroke-width 0.1s;
  stroke-width: 0;
  pointer-events: all;
}

.intersection.hovered {
  fill: rgba(138, 43, 226, 0.24);
  stroke: #8a2be2;
  stroke-width: 4;
}

.hide {
  fill: rgba(128, 128, 128, 0.35) !important;
  stroke: rgba(128, 128, 128, 0.51) !important;
}

.svg-container {
  position: relative;
}

.panel-style {
  background-color: rgba(179, 232, 155, 0.82);
  border: 2px solid #55ad2f;
  border-radius: 5px;
}

.result-popup {
  font-family: Barlow, sans-serif;
  font-size: 18px;
  color: black;
}
</style>
