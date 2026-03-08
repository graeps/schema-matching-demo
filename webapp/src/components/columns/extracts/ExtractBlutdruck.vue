<!-- A simple markup table with only one column.-->
<template>
  <div class="q-pa-md">
    <q-markup-table bordered flat :separator="'vertical'" :table-layout="'fixed'">
      <thead>
        <tr>
          <th class="text-right">Blutdruck</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="text-right">...</td>
        </tr>
        <tr>
          <td class="text-right">hoch</td>
        </tr>
        <tr>
          <td class="text-right">hoch</td>
        </tr>
        <tr>
          <td class="text-right text-green">normal</td>
        </tr>
        <tr>
          <td class="text-right text-red">hoch</td>
        </tr>
        <tr>
          <td class="text-right text-green">normal</td>
        </tr>
      </tbody>
    </q-markup-table>
  </div>
</template>

<script setup></script>
<style></style>
