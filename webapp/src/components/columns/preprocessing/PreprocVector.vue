<template>
  <!-- Horizontal Liste für wordEmbedding -->
  <q-markup-table
    bordered
    class="no-pointer-events"
    dense
    :separator="'vertical'"
    :table-layout="'fixed'"
  >
    <thead>
      <tr>
        <th class="text-center title">Word Embedding des Titles</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="text-left">[ {{ props.wordEmbedding.join(', ') }}, ... ]</td>
      </tr>
    </tbody>
  </q-markup-table>

  <!-- Horizontal Liste für feature vector -->
  <q-markup-table
    bordered
    class="no-pointer-events q-mt-md"
    dense
    :separator="'vertical'"
    :table-layout="'fixed'"
  >
    <thead>
      <tr>
        <th class="text-center title">Vektordarstellung der Meta-Daten</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="text-left">[ {{ props.featureVector.join(', ') }}, ... ]</td>
      </tr>
    </tbody>
  </q-markup-table>
</template>

<script setup>
const props = defineProps({
  featureVector: { type: Array, required: true },
  wordEmbedding: { type: Array, required: true },
})
</script>

<style>
.title {
  font-family: 'Barlow', sans-serif;
  font-size: 11pt !important;
}
td {
  transition: background-color 0.5s ease !important;
}
</style>
