<template>
  <div class="text-bold node-container column justify-center items-center">
    <div class="">Ausprobieren</div>
    <div class="pulse" style="position: relative; padding: 10px">
      <Handle type="source" style="height: 15px; width: 15px; background-color: yellow" :position="Position.Bottom" />
    </div>
    <div style="width: 50px; height: 40px"></div>
  </div>
</template>

<script setup>
import { Handle, Position } from "@vue-flow/core"
</script>

<style scoped>
.node-container {
  height: 150px;
  width: 150px;
  background-image: url("../../../../assets/scads-corp-design/bubbles/bubble-turquoise-1.png");
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
  animation-delay: 0.6s;
}
</style>
