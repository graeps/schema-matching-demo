<!-- Navigation button with two directions: up and down. Used to jump between pages-->
<template>
  <div class="row justify-center" style="width: 100%">
    <div class="column">
      <div class="col text-barlow text-center q-mb-xs">
        {{ label }}
      </div>
      <q-btn
        class="shadow-2 bg-white"
        style="color: #004b6f"
        padding="xs lg"
        rounded
        size="md"
        :icon="icon"
        :to="link"
      ></q-btn>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  // link where to jump to
  label: {
    type: String,
    required: false,
    default: '',
  },
  link: {
    type: String,
    required: true,
  },
  // two possible directions strings: "up" and "down"
  direction: {
    type: String,
    required: true,
  },
})

// set icon depending on direction
const icon = computed(() => {
  if (props.direction === 'up') {
    return 'keyboard_double_arrow_up'
  } else if (props.direction === 'down') {
    return 'keyboard_double_arrow_down'
  } else {
    return null
  }
})
</script>
