<template>
  <div>
    <q-markup-table bordered flat :separator="'vertical'" :table-layout="'fixed'">
      <thead>
        <tr>
          <th class="text-right">Patienten-ID</th>
          <th class="text-right">Vorname</th>
          <th class="text-right">Name</th>
          <th class="text-right">Geburtsdatum</th>
          <th class="text-right">Diagnose</th>
          <th class="text-right">Blutdruck</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="text-right">1</td>
          <td class="text-left">Maximilian</td>
          <td class="text-right">Schmidt</td>
          <td class="text-right">03.04.1983</td>
          <td class="text-right">Diabetes</td>
          <td class="text-right">hoch</td>
        </tr>
        <tr>
          <td class="text-right">2</td>
          <td class="text-left">Sophia</td>
          <td class="text-right">Wagner</td>
          <td class="text-right">17.12.2001</td>
          <td class="text-right">Asthma</td>
          <td class="text-right">normal</td>
        </tr>
        <tr>
          <td class="text-right">3</td>
          <td class="text-left">Katrin</td>
          <td class="text-right">Kowalski</td>
          <td class="text-right">06.10.1958</td>
          <td class="text-right">Grippe</td>
          <td class="text-right">hoch</td>
        </tr>
        <tr>
          <td class="text-right">...</td>
          <td class="text-right">...</td>
          <td class="text-right">...</td>
          <td class="text-right">...</td>
          <td class="text-right">...</td>
          <td class="text-right">...</td>
        </tr>
      </tbody>
    </q-markup-table>
  </div>
</template>

<script></script>
