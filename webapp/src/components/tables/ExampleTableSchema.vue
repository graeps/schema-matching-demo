<!-- Markup table which emits events to parent component when hovering over individual columns. -->
<template>
  <q-markup-table bordered dense flat :separator="'vertical'">
    <thead>
      <tr>
        <th class="text-right table-title" :class="{ hovered: isHovered1 }" @mouseover.stop="emitEvent('hover-column-1')" @mouseleave="emitEvent('no-hover')">Patienten-ID</th>
        <th class="text-right table-title" :class="{ hovered: isHovered2 }" @mouseover.stop="emitEvent('hover-column-2')" @mouseleave="emitEvent('no-hover')">Name</th>
        <th class="text-right table-title" :class="{ hovered: isHovered3 }" @mouseover.stop="emitEvent('hover-column-3')" @mouseleave="emitEvent('no-hover')">Geburtsdatum</th>
        <th class="text-right table-title" :class="{ hovered: isHovered4 }" @mouseover.stop="emitEvent('hover-column-4')" @mouseleave="emitEvent('no-hover')">Blutdruck</th>
      </tr>
    </thead>
    <tbody>
      <tr class="q-tr--no-hover">
        <td class="text-right table-content" :class="{ hovered: isHovered1 }" @mouseover.stop="emitEvent('hover-column-1')" @mouseleave="emitEvent('no-hover')">1</td>
        <td class="text-right table-content" :class="{ hovered: isHovered2 }" @mouseover.stop="emitEvent('hover-column-2')" @mouseleave="emitEvent('no-hover')">Schmidt</td>
        <td class="text-right table-content" :class="{ hovered: isHovered3 }" @mouseover.stop="emitEvent('hover-column-3')" @mouseleave="emitEvent('no-hover')">03.04.1983</td>
        <td class="text-right table-content" :class="{ hovered: isHovered4 }" @mouseover.stop="emitEvent('hover-column-4')" @mouseleave="emitEvent('no-hover')">hoch</td>
      </tr>
      <tr class="q-tr--no-hover">
        <td class="text-right table-content" :class="{ hovered: isHovered1 }" @mouseover.stop="emitEvent('hover-column-1')" @mouseleave="emitEvent('no-hover')">2</td>
        <td class="text-right table-content" :class="{ hovered: isHovered2 }" @mouseover.stop="emitEvent('hover-column-2')" @mouseleave="emitEvent('no-hover')">Wagner</td>
        <td class="text-right table-content" :class="{ hovered: isHovered3 }" @mouseover.stop="emitEvent('hover-column-3')" @mouseleave="emitEvent('no-hover')">17.12.2001</td>
        <td class="text-right table-content" :class="{ hovered: isHovered4 }" @mouseover.stop="emitEvent('hover-column-4')" @mouseleave="emitEvent('no-hover')">normal</td>
      </tr>
      <tr class="q-tr--no-hover">
        <td class="text-right table-content" :class="{ hovered: isHovered1 }" @mouseover.stop="emitEvent('hover-column-1')" @mouseleave="emitEvent('no-hover')">3</td>
        <td class="text-right table-content" :class="{ hovered: isHovered2 }" @mouseover.stop="emitEvent('hover-column-2')" @mouseleave="emitEvent('no-hover')">Kowalski</td>
        <td class="text-right table-content" :class="{ hovered: isHovered3 }" @mouseover.stop="emitEvent('hover-column-3')" @mouseleave="emitEvent('no-hover')">06.10.1958</td>
        <td class="text-right table-content" :class="{ hovered: isHovered4 }" @mouseover.stop="emitEvent('hover-column-4')" @mouseleave="emitEvent('no-hover')">hoch</td>
      </tr>
      <tr class="q-tr--no-hover">
        <td class="text-right table-content" :class="{ hovered: isHovered1 }" @mouseover.stop="emitEvent('hover-column-1')" @mouseleave="emitEvent('no-hover')">...</td>
        <td class="text-right table-content" :class="{ hovered: isHovered2 }" @mouseover.stop="emitEvent('hover-column-2')" @mouseleave="emitEvent('no-hover')">...</td>
        <td class="text-right table-content" :class="{ hovered: isHovered3 }" @mouseover.stop="emitEvent('hover-column-3')" @mouseleave="emitEvent('no-hover')">...</td>
        <td class="text-right table-content" :class="{ hovered: isHovered4 }" @mouseover.stop="emitEvent('hover-column-4')" @mouseleave="emitEvent('no-hover')">...</td>
      </tr>
    </tbody>
  </q-markup-table>
</template>

<script setup>
import { ref } from "vue"

const emit = defineEmits(["no-hover", "hover-column-1", "hover-column-2", "hover-column-3", "hover-column-4"])

const isHovered1 = ref(false)
const isHovered2 = ref(false)
const isHovered3 = ref(false)
const isHovered4 = ref(false)

function emitEvent(eventType) {
  if (eventType === "hover-column-1") {
    isHovered1.value = true
  }
  if (eventType === "hover-column-2") {
    isHovered2.value = true
  }
  if (eventType === "hover-column-3") {
    isHovered3.value = true
  }
  if (eventType === "hover-column-4") {
    isHovered4.value = true
  }
  if (eventType === "no-hover") {
    isHovered1.value = false
    isHovered2.value = false
    isHovered3.value = false
    isHovered4.value = false
  }
  emit(eventType)
}
</script>

<style scoped>
.hovered {
  background: rgba(215, 81, 241, 0.11);
}
</style>
