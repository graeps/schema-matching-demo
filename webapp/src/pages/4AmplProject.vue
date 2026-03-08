<template>
  <q-page padding class="main-page column text-body1 text-justify">
    <div class="col">
      <h3>Schema Matching in der Praxis</h3>
      <div class="text-body1">
        Die Zusammenführung heterogener Datenbanken ist nicht nur im Gesundheitswesen interessant.
        Beispielsweise bei Unternehmen in der Einzel- und Großhandelsbranche, die
        Produktinformationen von verschiedenen Lieferanten zusammenführen möchten, oder auch im
        Finanzwesen bei der Integration verschiedener Finanzdatenquellen kommt Schema Matching zur
        Anwendung.
      </div>
    </div>
    <q-card flat class="q-my-xl">
      <q-card-section class="blue-bg text-h5 blue-border">
        <div class="text-h6">Grundlegende Verwendung des Tools</div>
      </q-card-section>
      <q-card-section>
        In der Praxis interessieren wir uns selten für das eigentliche Schema Matching, sondern
        möchten Antworten auf komplexere Fragestellungen erhalten. Hierzu wird das Schema Matching
        Tool in eine größere Analyse-Software integriert, in welcher wir unsere Anfragen formulieren
        können.
        <div class="row justify-center q-my-xl" @mouseover="slide = 2" @mouseleave="slide = 1">
          <q-carousel
            v-model="slide"
            style="height: 60vh; max-height: 400px; width: 100%; max-width: 750px"
          >
            <q-carousel-slide
              :name="1"
              img-src="../assets/diagrams/schema-matching.png"
              class="carousel"
            />
            <q-carousel-slide
              :name="2"
              img-src="../assets/diagrams/schema-matching-requests.png"
              class="carousel"
            />
          </q-carousel>
        </div>
        <div class="col">
          Die Analyse-Software ist dabei für den spezifischen Anwendungsfall programmiert. Um die
          geforderten Daten zu erhalten, formuliert diese die passende Anfrage an das Schema
          Matching Tool. Dieses greift anschließend auf die Datenbanken zu, berechnet das
          Schema-Matching und gibt das Ergebnis an die Analyse-Software zurück. Auf der Basis davon
          erhalten wir anschließend eine Antwort auf unsere ursprüngliche Anfrage.
        </div>
      </q-card-section>
      <q-card-section>
        <div>
          Da beim automatisierten Schema Matching auch Fehler passieren können, sollte ein Mensch
          das Ergebnis auf Richtigkeit überprüfen.
        </div>
      </q-card-section>
    </q-card>

    <q-dialog v-model="confirm">
      <q-card class="q-pb-md">
        <q-card-section class="row items-center">
          <span class="q-ml-sm"
            >Du kannst nun entweder mehr Details über das Schema Matching Tool erfahren, oder direkt
            zu Ausprobierteil springen.</span
          >
        </q-card-section>

        <q-card-actions align="center">
          <div style="width: 20%">
            <move-vertical-btn
              v-close-popup
              label="Details"
              link="/details"
              direction="down"
              @click="confirm = true"
            ></move-vertical-btn>
          </div>
          <div style="width: 20%">
            <move-vertical-btn
              v-close-popup
              label="Ausprobieren"
              link="/try-it"
              direction="down"
              @click="confirm = true"
            ></move-vertical-btn>
          </div>
        </q-card-actions>
      </q-card>
    </q-dialog>
    <div class="col q-my-lg">
      <move-vertical-btn link="" direction="down" @click="confirm = true" />
    </div>
  </q-page>
</template>

<script setup>
import MoveVerticalBtn from 'components/buttons/MoveVerticalBtn.vue'

import { ref } from 'vue'

const confirm = ref(false)

const slide = ref(1)
</script>

<style>
.carousel {
  background-size: contain;
  background-repeat: no-repeat;
}
</style>
