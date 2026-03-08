<template>
  <div class="text-bold node-container column justify-center">
    <div style="position: relative; padding: 10px">
      <Handle
        type="source"
        style="height: 15px; width: 15px; background-color: yellow"
        :position="Position.Top"
      />
    </div>
    <div class="row justify-end">
      <div class="q-mr-xl q-pr-md text-right">
        Gelange hier rechts<br />
        zur Einführung...
      </div>
    </div>
    <div class="row justify-start">
      <div class="q-ml-xl q-pl-xl text-left q-mt-lg">
        ...oder probiere links <br />
        das Schema-Matching-Tool<br />
        direkt aus.
      </div>
    </div>
  </div>
</template>

<script setup>
import { Handle, Position } from '@vue-flow/core'
</script>

<style scoped>
.node-container {
  height: 400px;
  width: 400px;
  background-image: url('../../../../assets/scads-corp-design/bubbles/bubble-darkblue-2.svg');
  background-size: contain;
  background-repeat: no-repeat;
  color: yellow;
  font-family: 'Barlow', bold, sans-serif;
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
</style>
