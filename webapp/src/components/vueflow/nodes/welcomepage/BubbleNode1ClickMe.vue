<template>
  <div class="text-bold text-center node-container column justify-center items-center">
    <div>Klick mich!</div>
    <div class="pulse q-pt-md">
      <Handle type="source" style="height: 15px; width: 15px; background-color: yellow" :position="Position.Bottom" />
    </div>
  </div>
</template>

<script setup>
import { Handle, Position } from "@vue-flow/core"
</script>

<style scoped>
@keyframes shake {
  0% {
    transform: translateX(0) rotate(0deg);
  }
  3% {
    transform: translateX(-1px) rotate(-1deg);
  }
  6% {
    transform: translateX(1px) rotate(1deg);
  }
  9% {
    transform: translateX(-1px) rotate(-1deg);
  }
  12% {
    transform: translateX(1px) rotate(1deg);
  }
  15% {
    transform: translateX(0) rotate(0deg);
  }
}

.node-container {
  height: 300px;
  width: 300px;
  background-image: url("../../../../assets/scads-corp-design/bubbles/bubble-darkblue-1.svg");
  background-size: contain;
  background-repeat: no-repeat;
  color: yellow;
  font-family: "Barlow", bold, sans-serif;
  animation: shake 5s infinite;
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
</style>
