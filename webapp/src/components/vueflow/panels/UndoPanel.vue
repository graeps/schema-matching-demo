<template>
  <Panel position="top-left">
    <q-btn icon="undo" class="primary-button" @click="deleteEdge" />
  </Panel>
</template>

<script setup>
import { defineEmits } from "vue"
import { Panel } from "@vue-flow/core"

const emit = defineEmits(["delete-edge"])

const deleteEdge = () => {
  emit("delete-edge")
}
</script>
