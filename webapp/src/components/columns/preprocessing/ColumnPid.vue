<!--Individual column of the example tables. Used in the matching game in 3ScientificBackground.vue-->
<template>
  <q-markup-table
    class="no-pointer-events"
    bordered
    dense
    :separator="'vertical'"
    style="background: rgb(231, 231, 255)"
  >
    <thead>
      <tr>
        <th class="text-center title">PID</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="text-right">001</td>
      </tr>
      <tr>
        <td class="text-right">002</td>
      </tr>
      <tr>
        <td class="text-right">003</td>
      </tr>
      <tr>
        <td class="text-right">...</td>
      </tr>
    </tbody>
  </q-markup-table>
</template>

<script></script>

<style>
.title {
  font-family: 'Barlow', sans-serif;
  font-size: 11pt !important;
}
</style>
