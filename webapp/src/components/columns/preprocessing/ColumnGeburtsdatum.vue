<!--Individual column of the example tables. Used in the matching game in 3ScientificBackground.vue-->
<template>
  <q-markup-table
    class="no-pointer-events"
    bordered
    dense
    :separator="'vertical'"
    style="background: rgb(255, 233, 255)"
  >
    <thead>
      <tr>
        <th class="text-center title">Geburtsdatum</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="text-right">03.04.1983</td>
      </tr>
      <tr>
        <td class="text-right">17.12.2001</td>
      </tr>
      <tr>
        <td class="text-right">06.10.1958</td>
      </tr>
      <tr>
        <td class="text-right">...</td>
      </tr>
    </tbody>
  </q-markup-table>
</template>

<style>
.title {
  font-family: 'Barlow', sans-serif;
  font-size: 11pt !important;
}
</style>
