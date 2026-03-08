<template>
  <div class="text-bold node-container column justify-center items-center">
    <div class="q-pb-lg q-pl-xl">
      Wir stellen ein<br />
      Tool vor, dass<br />
      dabei helfen kann. <br />
    </div>
    <div style="position: relative">
      <Handle class="pulse" type="source" style="height: 15px; width: 15px; background-color: yellow" :position="Position.Bottom" />
    </div>
  </div>
</template>

<script setup>
import { Handle, Position } from "@vue-flow/core"
</script>

<style scoped>
.node-container {
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
