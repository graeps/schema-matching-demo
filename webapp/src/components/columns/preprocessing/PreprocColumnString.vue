<template>
  <q-markup-table
    bordered
    class="no-pointer-events"
    dense
    :separator="'vertical'"
    :table-layout="'fixed'"
  >
    <tbody>
      <tr>
        <td class="text-right indicator">title</td>
        <td :class="{ highlight1: connectedToMatcher1 }" class="text-right">{{ props.title }}</td>
      </tr>
      <tr>
        <td class="text-right indicator">data type</td>
        <td :class="{ highlight2: connectedToMatcher2 }" class="text-right">string</td>
      </tr>
      <tr>
        <td class="text-right indicator">num_instances</td>
        <td :class="{ highlight2: connectedToMatcher2 }" class="text-right">
          {{ props.numInstances }}
        </td>
      </tr>
      <tr>
        <td class="text-right indicator">avg_length</td>
        <td :class="{ highlight2: connectedToMatcher2 }" class="text-right">
          {{ props.avgLength }}
        </td>
      </tr>
      <tr>
        <td class="text-right indicator">frac_upper</td>
        <td :class="{ highlight2: connectedToMatcher2 }" class="text-right">
          {{ props.fracUpper }}
        </td>
      </tr>
      <tr>
        <td class="text-right indicator">frac_letters</td>
        <td :class="{ highlight2: connectedToMatcher2 }" class="text-right">
          {{ props.fracLetters }}
        </td>
      </tr>
    </tbody>
  </q-markup-table>
</template>
<script setup>
const props = defineProps({
  id: { type: String, required: true },
  title: { type: String, required: true },
  numInstances: { type: String, required: true },
  avgLength: { type: String, required: true },
  fracUpper: { type: String, required: true },
  fracLetters: { type: String, required: true },
  connectedToMatcher1: { type: Boolean, required: true },
  connectedToMatcher2: { type: Boolean, required: true },
})
</script>

<style scoped>
.indicator {
  font-family: 'Barlow', sans-serif;
}
td {
  transition: background-color 0.5s ease !important;
}
</style>
