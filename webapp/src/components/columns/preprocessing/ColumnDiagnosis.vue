<template>
  <q-markup-table
    class="no-pointer-events"
    bordered
    dense
    :separator="'vertical'"
    :style="{ background: props.whiteBg ? 'white' : 'rgb(231, 231, 255)' }"
  >
    <thead>
      <tr>
        <th class="text-center title" :class="{ largeTitle: props.largeFont }">Diagnosis</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="text-right" :class="{ large: props.largeFont }">hypertension</td>
      </tr>
      <tr>
        <td class="text-right" :class="{ large: props.largeFont }">asthma</td>
      </tr>
      <tr>
        <td class="text-right" :class="{ large: props.largeFont }">migraine</td>
      </tr>
      <tr>
        <td class="text-right" :class="{ large: props.largeFont }">...</td>
      </tr>
    </tbody>
  </q-markup-table>
</template>

<script setup>
const props = defineProps({
  whiteBg: Boolean,
  largeFont: { type: Boolean, required: false, default: false },
})
</script>

<style scoped>
.title {
  font-family: 'Barlow', sans-serif;
  font-size: 11pt !important;
}
.largeTitle {
  font-size: 16pt !important;
}
.large {
  font-size: 14pt !important;
}
</style>
