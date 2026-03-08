<template>
  <Panel position="bottom-center" class="matcher-choice-panel q-pa-xl shadow-6">
    <div class="row justify-between">
      <q-btn icon="undo" class="primary-button" @click="() => emit('title')">Titelvergleich</q-btn>
      <q-btn icon="undo" class="primary-button" @click="() => emit('instance')">InstanzVergleich</q-btn>
      <q-btn icon="undo" class="primary-button" @click="() => emit('clustering')">Clustering</q-btn>
      <q-btn icon="undo" class="primary-button" @click="() => emit('classifier')">Klassifikator</q-btn>
    </div>
  </Panel>
</template>

<script setup>
import { defineEmits } from "vue"
import { Panel } from "@vue-flow/core"

// Definiere die Emit-Events
const emit = defineEmits(["title", "instance", "clustering", "classifier"])
</script>

<style scoped>
.matcher-choice-panel {
  background-color: rgba(140, 192, 218, 0.45);
  width: 80%;
}
</style>
