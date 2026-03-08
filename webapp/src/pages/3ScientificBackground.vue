<template>
  <q-page padding class="main-page column text-body1 text-justify">
    <div class="col">
      <h3>Wissenschaftlicher Hintergrund</h3>
      <div>
        Das Zusammenführen und Vereinheitlichen vieler Datenbanken zu einer Großen wird auch
        Datenintegration genannt. In unserem Beispiel möchten wir am Ende eine große Datenbank mit
        allen Patientendaten. Wir können uns das als riesige Tabelle vorstellen, in der jede Zeile
        einem Patienten zugeordnet ist und es keine inhaltlichen Dopplungen unter den Spalten gibt.
        Diese Aufgabe können wir konzeptuell in zwei Schritte unterteilen: zuerst das
        <b>Schema Matching</b>, gefolgt vom <b>Schema Mapping</b>.
      </div>
    </div>
    <q-card class="col q-my-xl" flat>
      <q-card-section class="text-h5 blue-bg blue-border">Schema Matching</q-card-section>
      <q-card-section>
        <div class="row justify-between q-mt-md">
          <div class="col-5">
            <div class="text-h6">Schema</div>
            Allgemein bezeichnet man das Muster, nach dem eine Datenbank erstellt wird, als
            <b>Schema</b>. Ein Schema ist also eine Art Blaupause dafür, welche Spalten es in der
            Tabelle gibt und stellt Bedingungen an deren Inhalt.
          </div>
          <div class="col-6 q-pa-sm">
            <div class="q-mb-xs"><b>Datenbank: </b>Patientendaten</div>
            <example-table-schema
              class="col shadow-2"
              @hover-column-1="highlightColumn1"
              @hover-column-2="highlightColumn2"
              @hover-column-3="highlightColumn3"
              @hover-column-4="highlightColumn4"
              @no-hover="resetHighlight"
            />
            <div class="q-mt-sm q-px-xs">
              <div class="text-caption">
                <q-icon name="info" size="xs" />
                Fahre mit der Maus über die Datenbank.
              </div>
            </div>
            <q-tooltip
              anchor="center left"
              self="center right"
              class="text-grey-14 no-padding shadow-2"
            >
              <div class="schema-popup q-pa-md">
                <pre><code style="font-weight: bold">SCHEMA: </code><code> PATIENT</code>

<code style="font-weight: bold">| Spaltenname  | Datentyp    | Beschreibung                     |</code>
<code>|--------------|-------------|----------------------------------|</code>
<code :class="{highlight: highlight1}">| Patienten-ID | INTEGER     | Eindeutige Identifikationsnummer |</code>
<code :class="{highlight: highlight2}">| Name         | STRING      | Nachname des Patienten           |</code>
<code :class="{highlight: highlight3}">| Geburtsdatum | DATE        | Geburtsdatum des Patienten       |</code>
<code :class="{highlight: highlight4}">| Blutdruck    | hoch/normal | Vorliegen von Übergewicht        |</code></pre>
              </div>
            </q-tooltip>
          </div>
        </div>

        <div class="row justify-between q-mt-xl">
          <div class="col-5">
            <div class="text-h6">Schema Matching</div>
            <div class="col-5">
              Um die Daten zusammenzuführen, muss im ersten Schritt herausgefunden werden, welche
              Spalten denselben oder ähnlichen Informationsgehalt liefern, das sogenannte
              <b>Schema Matching</b>. Wir versuchen dem Sinn nach gleiche, man sagt auch
              <i>semantisch äquivalente</i>, Spalten zu identifizieren. Was semantisch äquivalent im
              konkreten Fall bedeutet, ist allerdings unter Umständen schwierig zu entscheiden und
              hängt vom Kontext ab.
            </div>
          </div>
          <div class="col-6">
            <div class="text-h6">Strategien</div>
            Im Finden der relevanten Merkmale und der richtigen Entscheidungskriterien für ein
            Match, liegt die Schwierigkeit einer Automatisierung. Für einen Menschen ist klar, dass
            <b>Alter</b> und <b>Geburtsdatum</b> in etwa dasselbe meinen - für einen Computer nicht!
            Ein Programm ohne Hintergrundwissen muss sich dies erst durch eine Analyse der Tabellen
            erschließen: Sind die Spaltennamen zumindest ähnlich? Welche Datentypen werden
            verwendet? In welchem Wertebereich liegen die Spalteninhalte? Was davon ist wie wichtig
            für die Wahrscheinlichkeit eines Matches?
          </div>
        </div>
      </q-card-section>
    </q-card>

    <q-card class="col q-my-xl" flat>
      <q-card-section class="text-h5 blue-bg blue-border">Schema Matching von Hand</q-card-section>
      <q-card-section>
        <div class="q-pb-xl" style="width: 100%; height: 80vh; max-height: 800px">
          <connect-tables />
        </div>
      </q-card-section>
    </q-card>

    <q-card class="col q-my-xl" flat>
      <q-card-section class="text-h5 blue-bg blue-border">Schema Mapping</q-card-section>
      <q-card-section>
        <div class="row justify-center">
          <div class="mapping-box">
            <div class="mapping-text-box">
              Haben wir dann Kandidaten für ein Matching gefunden, folgt im nächsten Schritt die
              Vereinheitlichung der Spalten in Daten gleichen Typs, das sogenannte
              <b>Schema Mapping</b>. Hier werden Inches in Centimeter umgerechnet, Sprachen
              übersetzt, Diagnosen in Codes umgewandelt und ein Blutdruck von über 140/90mmHg zu
              einem "Ja".
            </div>
          </div>
        </div>
      </q-card-section>
    </q-card>

    <div class="col q-my-lg">
      <move-vertical-btn link="/ampl-project" direction="down" />
    </div>
  </q-page>
</template>

<script setup>
import ConnectTables from 'components/demo/SimpleConnectTablesGame.vue'
import MoveVerticalBtn from 'components/buttons/MoveVerticalBtn.vue'
import ExampleTableSchema from 'components/tables/ExampleTableSchema.vue'

import { ref } from 'vue'

const highlight1 = ref(false)
const highlight2 = ref(false)
const highlight3 = ref(false)
const highlight4 = ref(false)

function highlightColumn1() {
  highlight1.value = true
}

function highlightColumn2() {
  highlight2.value = true
}

function highlightColumn3() {
  highlight3.value = true
}

function highlightColumn4() {
  highlight4.value = true
}

function resetHighlight() {
  highlight1.value = false
  highlight2.value = false
  highlight3.value = false
  highlight4.value = false
}
</script>

<style scoped>
.mapping-box {
  background-image: url('../assets/diagrams/schema-mapping.png');
  background-repeat: no-repeat;
  background-position: right;
  background-size: contain;
  height: 50vh;
  max-height: 500px;
}

.mapping-text-box {
  width: 80%;
}

.highlight {
  font-weight: bold;
  color: rgb(215, 81, 241);
  background-color: rgba(159, 159, 159, 0.31);
}

.schema-popup {
  background-color: #b3e89b;
  font-family: 'Barlow', sans-serif;
  font-size: 11pt;
}
</style>
