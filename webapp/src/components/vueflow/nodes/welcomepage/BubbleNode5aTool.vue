<template>
  <div class="node-container column justify-center items-center">
    <div class="text-center q-pb-sm">Das war einfach!</div>
    <div class="text-left q-pb-xl">
      Bei großen Datenmenge <br />
      kann es aber schnell<br />
      unübersichtlich werden. <br />
    </div>
    <div style="position: relative">
      <Handle type="source" style="height: 10px; width: 10px; background-color: yellow" :position="Position.Left" />
    </div>
  </div>
</template>

<script setup>
import { Handle, Position } from "@vue-flow/core"
</script>

<style scoped>
.node-container {
  height: 370px;
  width: 370px;
  background-image: url("../../../../assets/scads-corp-design/bubbles/bubble-darkblue-3.svg");
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
