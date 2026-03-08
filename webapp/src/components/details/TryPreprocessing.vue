<template>
  <q-card flat>
    <!-- Draggable Elements Container -->
    <q-card-section class="q-pa-md">
      <div class="row justify-between q-mb-lg">
        <q-card class="input-data-container col-8" flat>
          <q-card-section class="small-heading">Input-Daten</q-card-section>
          <q-card-section>
            <div class="row justify-between no-wrap">
              <div
                class="input-column-container drag-el q-mb-sm"
                :class="{ disabled: droppedComponent === 'SingleColumnNameGeburtsdatum' }"
                draggable="true"
                @dragstart="onDragStart('SingleColumnGeburtsdatum')"
              >
                <single-column-geburtsdatum />
              </div>
              <div
                class="input-column-container drag-el q-mb-sm"
                :class="{ disabled: droppedComponent === 'SingleColumnDiagnose' }"
                draggable="true"
                @dragstart="onDragStart('SingleColumnDiagnose')"
              >
                <single-column-diagnose />
              </div>
              <div
                class="input-column-container drag-el q-mb-sm"
                :class="{ disabled: droppedComponent === 'SingleColumnPid' }"
                draggable="true"
                @dragstart="onDragStart('SingleColumnPid')"
              >
                <single-column-pid />
              </div>
              <div
                class="input-column-container drag-el q-mb-sm"
                :class="{ disabled: droppedComponent === 'SingleColumnDiagnosis' }"
                draggable="true"
                @dragstart="onDragStart('SingleColumnDiagnosis')"
              >
                <single-column-diagnosis />
              </div>
            </div>
          </q-card-section>
        </q-card>
        <div class="col column justify-center items-center">
          <q-icon name="keyboard_double_arrow_right" size="xl" />
        </div>
        <div class="col-3">
          <!-- Dropzone Container -->
          <q-card class="dropzone-container">
            <q-card-section class="small-heading" style="background: rgb(179, 232, 155)"
              >Preprocessor</q-card-section
            >
            <q-card-section
              class="column items-center justify-center q-pa-md"
              @dragover.prevent
              @drop="onDrop"
            >
              <div class="dropzone col text-center">
                <div v-if="!droppedComponent">Ziehe Input-Daten in dieses Feld.</div>
                <component :is="droppedComponentMap[droppedComponent]" v-if="droppedComponent" />
              </div>
            </q-card-section>
          </q-card>
        </div>
      </div>
      <transition name="fade">
        <div v-if="droppedComponent">
          <q-card class="q-mt-lg" flat>
            <q-card-section class="small-heading">Output </q-card-section>
            <q-card-section class="row justify-center no-padding">
              <q-card class="meta-data-container col-4 q-mr-sm q-py-md q-mb-md">
                <div
                  class="items-center justify-center row no-wrap"
                  @dragover.prevent
                  @drop="onDrop"
                >
                  <div class="small-heading vertical-text q-mr-md">Meta-Daten</div>
                  <transition name="fade">
                    <div v-if="droppedComponent" :key="droppedComponent">
                      <component
                        :is="preprocessingComponentMap[droppedComponent]"
                        v-bind="componentPropsMap[droppedComponent]"
                      />
                    </div>
                  </transition>
                </div>
              </q-card>
              <q-card class="vector-container col-6 q-py-md colum q-mb-md">
                <div
                  class="items-center justify-center row no-wrap"
                  @dragover.prevent
                  @drop="onDrop"
                >
                  <div class="small-heading vertical-text q-mr-md">Vektor</div>
                  <transition name="fade">
                    <div v-if="droppedComponent" :key="droppedComponent">
                      <component :is="PreprocVector" v-bind="vectorPropsMap[droppedComponent]" />
                    </div>
                  </transition>
                </div>
              </q-card>
            </q-card-section>
          </q-card>
        </div>
      </transition>
    </q-card-section>
  </q-card>
</template>

<script setup>
import { ref } from 'vue'
import SingleColumnPid from 'components/columns/preprocessing/ColumnPid.vue'
import SingleColumnDiagnose from 'components/columns/preprocessing/ColumnDiagnose.vue'
import SingleColumnDiagnosis from 'components/columns/preprocessing/ColumnDiagnosis.vue'
import SingleColumnGeburtsdatum from 'components/columns/preprocessing/ColumnGeburtsdatum.vue'
import PreprocColumnDate from 'components/columns/preprocessing/PreprocColumnDate.vue'
import PreprocColumnNumber from 'components/columns/preprocessing/PreprocColumnNumber.vue'
import PreprocColumnString from 'components/columns/preprocessing/PreprocColumnString.vue'
import PreprocVector from 'components/columns/preprocessing/PreprocVector.vue'

// Map component names to actual components
const droppedComponentMap = {
  SingleColumnDiagnosis,
  SingleColumnDiagnose,
  SingleColumnPid,
  SingleColumnGeburtsdatum,
}

const preprocessingComponentMap = {
  SingleColumnDiagnosis: PreprocColumnString,
  SingleColumnDiagnose: PreprocColumnString,
  SingleColumnPid: PreprocColumnNumber,
  SingleColumnGeburtsdatum: PreprocColumnDate,
}

const componentPropsMap = {
  SingleColumnDiagnose: {
    id: 't1_c5',
    title: 'Diagnose',
    numInstances: '3.485',
    avgLength: '10.3',
    fracUpper: '0.16',
    fracLetters: '1.0',
  },
  SingleColumnGeburtsdatum: {
    id: 't1_c4',
    title: 'Geburtsdatum',
    numInstances: '3.485',
    minDate: '24.02.1938',
    maxDate: '3.03.2017',
  },
  SingleColumnDiagnosis: {
    id: 't2_c6',
    title: 'Diagnosis',
    numInstances: '24.304',
    avgLength: '8.0',
    fracUpper: '0.09',
    fracLetters: '0.36',
  },
  SingleColumnPid: {
    id: 't2_c1',
    title: 'PID',
    numInstances: '24.304',
    minValue: '1',
    maxValue: '24.304',
    avgValue: '12.152',
  },
}

const vectorPropsMap = {
  SingleColumnDiagnose: {
    featureVector: [0.52, '--', 0.34, 0.69, '--', 0.56, 0.57, 0.42, 0.21, '--', 0.62],
    wordEmbedding: [0.23, 0.13, 0.94, 0.34, 0.71, 0.55, 0.24, 0.01, 0.98],
  },
  SingleColumnGeburtsdatum: {
    featureVector: [0.87, 0.34, 0.56, '--', 0.92, '--', '--', 0.43, '--', '--', '--', '--'],

    wordEmbedding: [0.55, 0.32, 0.78, 0.13, 0.33, 0.58, 0.41, 0.96, 0.74],
  },
  SingleColumnDiagnosis: {
    featureVector: [0.64, '--', 0.45, 0.23, '--', 0.89, 0.77, 0.38, 0.74, '--', 0.38],
    wordEmbedding: [0.84, 0.93, 0.79, 0.98, 0.68, 0.44, 0.13, 0.42, 0.94],
  },
  SingleColumnPid: {
    featureVector: [0.52, 0.18, '--', 0.77, 0.34, '--', '--', 0.65, '--', 0.91, 0.12],
    wordEmbedding: [0.77, 0.98, 0.83, 0.12, 0.54, 0.38, 0.3, 0.17, 0.74],
  },
}

// Track the currently dragged component and dropped component
const draggedItem = ref(null)
const droppedComponent = ref(null)

const onDragStart = (componentName) => {
  draggedItem.value = componentName
}

const onDrop = () => {
  if (draggedItem.value) {
    droppedComponent.value = draggedItem.value
  }
}
</script>

<style scoped>
.input-data-container {
  background: rgb(255, 255, 255);
}

.input-column-container {
  width: 10vw;
}

.drag-el {
  cursor: grab;
  transition: transform 0.1s ease;
}

.drag-el.disabled {
  pointer-events: none;
}

.dropzone-container {
  background: repeating-linear-gradient(
    45deg,
    rgb(179, 232, 155),
    rgb(179, 232, 155) 10px,
    rgba(179, 232, 155, 0.51) 10px,
    rgba(179, 232, 155, 0.51) 20px
  );
  height: 100%;
}

.dropzone {
  border-radius: 5px;
  border-style: solid;
  border-color: gray;
  width: 10vw;
  min-height: 140px;
}

.meta-data-container {
  background: rgba(179, 232, 155, 0.79);
}

.vector-container {
  background: rgba(179, 232, 155, 0.79);
}

.small-heading {
  font-family: Barlow, sans-serif;
}

.fade-enter-active {
  transition: opacity 0.5s ease;
  transition-delay: 0.5s;
}

.fade-leave-active {
  opacity: 0;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.vertical-text {
  writing-mode: vertical-lr;
  transform: rotate(-180deg);
}
</style>
