<template>
  <div class="text-bold node-container row justify-center items-center">
    <div class="q-pb-xl">
      Schema Matching verbindet <br />
      Daten aus verschieden Quellen <br />
      zu einer großen Datenbank. <br />
    </div>
    <div class="pulse" style="position: relative">
      <Handle type="source" style="height: 15px; width: 15px; background-color: yellow" :position="Position.Right" />
    </div>
  </div>
</template>

<script setup>
import { Handle, Position } from "@vue-flow/core"
</script>

<style scoped>
.node-container {
  height: 400px;
  width: 400px;
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
