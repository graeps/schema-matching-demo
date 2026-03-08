<!-- A simple markup table with only one column.-->
<template>
  <div class="q-pa-md">
    <q-markup-table bordered flat :separator="'vertical'" :table-layout="'fixed'">
      <thead>
        <tr>
          <th class="text-right">Blood pressure</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="text-right text-green">118/76 mmHg</td>
        </tr>
        <tr>
          <td class="text-right text-red">145/95 mmHg</td>
        </tr>
        <tr>
          <td class="text-right text-green">122/78 mmHg</td>
        </tr>
      </tbody>
    </q-markup-table>
  </div>
</template>
<script setup></script>
<style>
.highlight {
  color: #d79b00; /* Text color */
}
</style>
