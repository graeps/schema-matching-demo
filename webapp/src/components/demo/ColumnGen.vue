<!-- Generates a simple markup table with one column, given title and content. E.g. used as content of the vue-flow nodes in connecting tables game. -->
<template>
  <q-markup-table class="no-pointer-events inset-shadow-down" bordered flat :separator="'vertical'" :table-layout="'fixed'">
    <thead>
      <tr>
        <th class="text-left table-title">{{ shortString(props.title) }}</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(row, index) in props.content" :key="index">
        <td class="text-left table-content">{{ shortString(row) }}</td>
      </tr>
    </tbody>
  </q-markup-table>
</template>

<script setup>
const props = defineProps({
  // Title of the column.
  title: {
    type: String,
    required: true,
  },
  // Content of the column as array.
  content: {
    type: Array,
    required: true,
  },
})

// Cuts length of entries to fit in the fixed size of ConnectTablesGen.vue
const shortString = (word) => {
  if (typeof word === "string") {
    return word.length > 20 ? word.slice(0, 20) + "..." : word
  }
  return word
}
</script>
