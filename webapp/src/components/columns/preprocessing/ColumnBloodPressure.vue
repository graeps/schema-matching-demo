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
        <th class="text-center title">Blood Pressure</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="text-right">118/76 mmHg</td>
      </tr>
      <tr>
        <td class="text-right">145/95 mmHg</td>
      </tr>
      <tr>
        <td class="text-right">122/78 mmHg</td>
      </tr>
      <tr>
        <td class="text-center">...</td>
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
