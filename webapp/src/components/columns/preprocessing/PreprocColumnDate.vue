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
        <td class="text-right indicator">data_type</td>
        <td :class="{ highlight2: connectedToMatcher2 }" class="text-right">date</td>
      </tr>
      <tr>
        <td class="text-right indicator">num_instances</td>
        <td :class="{ highlight2: connectedToMatcher2 }" class="text-right">
          {{ props.numInstances }}
        </td>
      </tr>
      <tr>
        <td class="text-right indicator">min_date</td>
        <td :class="{ highlight2: connectedToMatcher2 }" class="text-right">{{ props.minDate }}</td>
      </tr>
      <tr>
        <td class="text-right indicator">max_date</td>
        <td :class="{ highlight2: connectedToMatcher2 }" class="text-right">{{ props.maxDate }}</td>
      </tr>
    </tbody>
  </q-markup-table>
</template>

<script setup>
const props = defineProps({
  id: { type: String, required: true },
  title: { type: String, required: true },
  numInstances: { type: String, required: true },
  minDate: { type: String, required: true },
  maxDate: { type: String, required: true },
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
