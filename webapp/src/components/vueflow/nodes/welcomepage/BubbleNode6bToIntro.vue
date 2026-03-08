<template>
  <div class="text-bold node-container column justify-center items-center">
    <div class="row">
      <div class="">Einführung</div>
    </div>
    <div class="pulse" style="position: relative; padding: 10px">
      <Handle type="source" style="height: 15px; width: 15px; background-color: yellow" :position="Position.Bottom" />
    </div>
  </div>
</template>

<script setup>
import { Handle, Position } from "@vue-flow/core"
</script>

<style scoped>
.node-container {
  height: 150px;
  width: 150px;
  background-image: url("../../../../assets/scads-corp-design/bubbles/bubble-violet-1.png");
  background-size: contain;
  background-repeat: no-repeat;
  color: yellow;
  font-family: "Barlow", bold, sans-serif;
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
