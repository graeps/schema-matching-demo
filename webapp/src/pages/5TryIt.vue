<!-- Page to actually try out the demonstrator. The main components are:
1. Request two random databases from the backend.
2. Show the two databases as two tables interactive vue-flow graph, in which one can match columns manually.
2. Request a matching from the backend using the schema matching tool and compare the results with your own matching.-->

<template>
  <q-page padding class="column text-body1 text-justify" style="width: 80vw; max-width: 1200px">
    <!-- Section to chose attributes and request generate databases.-->
    <div class="col">
      <div class="row justify-between">
        <h3>Probiere es aus!</h3>
        <div />
      </div>
      <div class="q-mb-md">
        In diesem Teil kannst du das Schema-Matching-Tool auf künstlich generierten Datenbank
        ausprobieren und mit deinem eigenen Matching vergleichen. Falls du den Rest übersprungen
        hast und du dieser Teil zu verwirrend ist, gelangst du
        <router-link to="/intro">hier</router-link> zurück zu Einführung.
      </div>
    </div>
    <div class="col">
      <q-card id="tour-dbgenerator" flat class="blue-border">
        <q-card-section class="blue-bg">
          <div class="row justify-between">
            <div class="text-h6">Datenbank-Generator</div>
            <q-btn icon="help" flat round size="md">
              <q-tooltip class="tooltip" anchor="top middle" self="bottom middle">
                Wähle ein Schema und eine Sprache aus. <br />
                Klicke anschließend auf "Tabellen Generieren".
              </q-tooltip>
            </q-btn>
          </div>
        </q-card-section>
        <q-card-section>
          <div class="row justify-between">
            <div id="tour-schema" class="col-3">
              <q-select v-model="schemaChoice" outlined :options="schemaOptions" label="Datenbank">
                <template #prepend>
                  <q-icon name="view_week" />
                </template>
              </q-select>
            </div>
            <div id="tour-lang" class="col-3">
              <q-select v-model="langChoice" outlined :options="langOptions" label="Sprache">
                <template #prepend>
                  <q-icon name="language" />
                </template>
              </q-select>
            </div>
            <q-btn
              id="tour-datagen"
              class="primary-button col-3 offset-md-2"
              size="md"
              label="Datenbanken generieren"
              :disable="btnDisabled"
              @click="generateData(options)"
            ></q-btn>
          </div>
        </q-card-section>
      </q-card>
    </div>
    <div style="height: 3vh" id="tour-start" />

    <!-- Section to match manually and request to matching of the tool -->
    <div class="col">
      <q-card flat class="blue-border">
        <q-card-section class="row justify-between blue-bg">
          <div class="text-h6">Schema Matcher</div>
          <div>
            <q-btn icon="help" flat round size="md">
              <q-tooltip class="tooltip" anchor="top middle" self="bottom middle">
                Matche die Tabellen, indem du sie mit der Maus verbindest. <br />
                Klicke anschließend auf "Berechne Schema Matching".
              </q-tooltip>
            </q-btn>
          </div>
        </q-card-section>
        <q-separator />
        <q-card-section style="height: 80vh; max-height: 800px; width: 100%">
          <q-spinner-gears
            v-if="loading_data || loading_matching"
            :color="spinnerColor"
            size="10em"
            class="absolute-center"
            style="z-index: 1"
          />
          <div v-if="hideMatcher" class="absolute-center" style="height: 80vh; max-height: 800px">
            <q-img
              src="../assets/scads-corp-design/bubbles/bubble-darkblue-2.svg"
              height="100%"
              width="800px"
              fit="contain"
            ></q-img>
          </div>
          <div id="tour-matcher" />
          <gen-connect-tables
            ref="connectTables"
            :table1="table1"
            :table2="table2"
          ></gen-connect-tables>
        </q-card-section>
        <q-card-section class="q-mt-md blue-border blue-bg">
          <div class="row">
            <div class="col-3">
              <q-select
                v-model="configChoice"
                class="bg-white"
                outlined
                :options="configOptions"
                label="Konfiguration"
              >
                <template #prepend> <q-icon name="view_week" /> </template>
              </q-select>
            </div>
            <div class="col-1 self-center q-pl-md">
              <q-btn icon="help" flat round size="mg">
                <q-tooltip class="tooltip" anchor="top middle" self="bottom middle">
                  Die Konfiguration legt fest, wie zwei Spalten auf Ähnlichkeit verglichen werden.
                  <br />
                  Bei der <b>einfachen</b> Konfiguration werden nur der Spaltenname und der Datentyp
                  verglichen. <br />
                  Die <b>optimale</b> Konfiguration wurde mit Hilfe von KI berechnet.
                </q-tooltip>
              </q-btn>
            </div>
            <q-btn
              id="tour-matchgen"
              class="primary-button col-3 offset-5"
              size="md"
              label="Berechne Schema Matching"
              :disabled="loading_data || hideMatcher"
              @click="generateMatching(configChoice)"
            />
          </div>
        </q-card-section>
      </q-card>
      <div class="q-mt-xl bg-white">
        Falls du mehr über die Hintergründe und die Funktionsweise erfahren möchtest, kannst du über
        diesen Pfeil zur Einführung gelangen, oder dich oben durch die weiteren Menüpunkte klicken.
      </div>
    </div>
    <div class="col q-my-lg">
      <move-vertical-btn link="/intro" direction="down" />
    </div>

    <VTour :steps="tourSteps" :name="tourName" ref="vTour" autoStart :startDelay="delay">
      <template #actions="{ lastStep, nextStep, endTour, _CurrentStep, props }">
        <div class="vjt-actions">
          <button
            v-if="_CurrentStep.lastStep < _CurrentStep.currentStep"
            type="button"
            @click.prevent="lastStep()"
          >
            Zurück
          </button>
          <button id="skip-button" v-if="!props.hideSkip" type="button" @click.prevent="endTour()">
            x
          </button>
          <button type="button" @click.prevent="nextStep()">Weiter</button>
        </div>
      </template></VTour
    >
  </q-page>
</template>

<script setup>
import { VTour } from '@globalhive/vuejs-tour'
import '@globalhive/vuejs-tour/dist/style.css'

import { computed, ref } from 'vue'
import axios from 'axios'

import MoveVerticalBtn from 'components/buttons/MoveVerticalBtn.vue'
import GenConnectTables from 'components/demo/ConnectTablesDemo.vue'

const table1 = ref({})
const table2 = ref({})
const matching = ref([])

const loading_matching = ref(false)
const loading_data = ref(false)
const hideMatcher = ref(true)
const spinnerColor = ref('blue')
const connectTables = ref(null)

const configChoice = ref('optimal')
const configOptions = ['optimal', 'einfach']

// Stores if choices where already done.
const optionsChosen = computed(() => schemaChoice.value && langChoice.value)

// Deactivates generateData button, if choices are not made yet, or while waiting on response from backend
const btnDisabled = computed(() => !optionsChosen.value || loading_data.value)

// Possible choices and variables to store the choices. schemaOptions have to be contained in schemas_dict in backend file server.data_gen.data_generation_for_demo.py.
const schemaChoice = ref('')
const schemaOptions = [
  'Kunde',
  'Diabetes Patient',
  'TikTok Nutzer',
  'Prominenter',
  'Konzert',
  'Kreditkarte',
  'Wein Bewertung',
  'Film',
  'Autounfall',
]
const langChoice = ref('')
const langOptions = ['Deutsch', 'Englisch', 'gemischt']

const options = computed(() => {
  return {
    schema: schemaChoice.value,
    lang: langChoice.value,
  }
})

const generateData = async (options) => {
  loading_data.value = true
  hideMatcher.value = false
  connectTables.value.clearAll()
  try {
    let path
    if (process.env.DEV) {
      path = 'http://localhost:5000/generateData'
    } else {
      path = '/schema-matching/generateData'
    }

    if (options != null) {
      const optionsToSend = JSON.stringify(options)
      const params = {
        options: optionsToSend,
      }
      const { data } = await axios.get(path, { params, withCredentials: true })
      // data.matching contains the matching result and data.data contains the tables
      if (Array.isArray(data.data)) {
        table1.value = data.data[0]
        table2.value = data.data[1]
      } else {
        console.error('Response data format is not as expected.')
      }
    } else {
      console.error('No options lang or schema.')
    }
  } catch (error) {
    console.error('Error fetching data:', error)
  } finally {
    loading_data.value = false
  }
  switchTour()
}

const generateMatching = async (config_choice) => {
  loading_matching.value = true
  matching.value = []
  try {
    let path
    if (process.env.DEV) {
      path = 'http://localhost:5000/generateMatching'
      console.log('DEV environment', path)
    } else {
      path = '/schema-matching/generateMatching'
    }

    if (config_choice != null) {
      const params = {
        config: config_choice,
      }
      const { data } = await axios.get(path, { params, withCredentials: true })
      console.log(data)
      // Assuming data.matching contains the matching result and data.data contains the tables
      if (data.matching) {
        matching.value = data.matching
      } else {
        console.error('Response data format is not as expected.')
      }
    } else {
      console.error('No config chosen.')
    }
  } catch (error) {
    console.error('Error fetching data:', error)
  } finally {
    loading_matching.value = false
  }
  spinnerColor.value = 'blue'
  connectTables.value.showMatching(matching.value)
}

const tourSteps1 = [
  {
    target: '#tour-start',
    content:
      '<b>Willkommen im Ausprobierteil!</b> 👋 </br> Ich erkläre dir kurz, wie du dich gut auf dieser Seite zurechtfindest.',
    placement: 'right',
    noScroll: true,
    backdrop: true,
  },
  {
    target: '#tour-dbgenerator',
    content:
      'Beginne damit, <b>zwei zufällige Datenbanken</b> zu generieren. Sie werden nach unterschiedlichen Regeln erstellt, beziehen sich aber auf die gleiche Art von Daten.',
    placement: 'top',
    noScroll: true,
    highlight: true,
  },
  {
    target: '#tour-schema',
    content:
      'Für jede Datenbank legt jeweils ein <b>Schema</b> diese Regeln fest. Du entscheidest hier nur, auf welche Art von Daten es sich handeln soll. Die Wahl der Schemata überlassen wir dem Zufall.',
    placement: 'top',
    noScroll: true,
  },
  {
    target: '#tour-lang',
    content: 'Sollen die Einträge beider Datenbanken in der selben Sprache sein?.',
    placement: 'top',
    noScroll: true,
  },
  {
    target: '#tour-datagen',
    content:
      'Klicke hier, um die Datenbanken zu generieren. Du kannst den Datenbank-Generator immer wieder betätigen und alle Optionen ausprobieren.',
    placement: 'top',
    noScroll: true,
  },
]

const tourSteps2 = [
  {
    target: '#tour-matcher',
    content:
      'Super! 🎉</br> Du siehst nun übereinander zwei Ausschnitte der Datenbanken. </br>' +
      'Obwohl vielleicht die Spaltentitel, Datentypen und Sprachen verschieden sind, beinhalten manche Spalten dieselben Informationen. </br> <b>Finde sie und verbinde sie mit der Maus!</b>',
    placement: 'bottom',
    noScroll: false,
  },
  {
    target: '#tour-matchgen',
    content:
      'Klicke anschließend hier, um ein Matching vom Schema-Matching-Tool berechnen zu lassen. </br> Vergleiche die Ergebnisse! Sieht das Tool dieselben Ähnlichkeiten, wie ein Mensch?',
    placement: 'top',
    noScroll: true,
  },
]

const tourSteps = ref(tourSteps1)
const tourName = ref('tour1')
const delay = ref('3000')
const vTour = ref()

function switchTour() {
  tourSteps.value = tourSteps2
  tourName.value = 'tour2'
  delay.value = '0'
  vTour.value.startTour()
}
</script>

<style scoped></style>

<style>
#vjt-tooltip {
  font-size: 10pt;
  background-color: rgb(243, 186, 253);
  color: rgb(15 23 42);
  box-shadow: rgba(29, 29, 29, 0.46) 2px 2px 5px 1px;
  padding: 40px 20px 20px;
}
#vjt-arrow::before {
  background-color: rgb(241, 177, 253);
  /*box-shadow: rgba(29, 29, 29, 0.24) 2px 2px 0 0;*/
}
.vjt-actions button {
  border: 1px solid rgb(15 23 42);
  color: rgb(15 23 42);
}
.vjt-actions button:hover {
  background: rgba(84, 29, 53, 0.2);
}
.vjt-actions button#skip-button {
  position: absolute;
  top: 5px;
  right: 5px;
  background: none;
  border: rgb(15 23 42);
  color: rgb(84, 29, 53);
  font-size: 18px;
  font-weight: bold;
  cursor: pointer;
  width: 30px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  transition: background 0.3s;
}

.vjt-actions button#skip-button:hover {
  background: rgba(84, 29, 53, 0.2);
}
#vjt-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.19);
  z-index: 9998;
}
</style>
