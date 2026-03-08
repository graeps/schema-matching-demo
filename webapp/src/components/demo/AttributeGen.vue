<!-- Component to chose attributes to generate random databases in the backend.
Chose a language and a schema via dropdown menus and emit the chosen values to the parent component -->
<template>
  <q-card flat class="blue-border">
    <q-card-section class="blue-bg">
      <div class="row justify-between">
        <div class="text-h6">Datenbank-Generator</div>
        <q-btn icon="help" flat round size="md">
          <q-tooltip class="text-body1 bg-grey-1 shadow-10 text-grey-9 q-pa-md" anchor="top middle" self="bottom middle" style="font-family: Barlow, sans-serif">
            Wähle ein Schema und eine Sprache aus. <br />
            Klicke anschließend auf "Tabellen Generieren".
          </q-tooltip>
        </q-btn>
      </div>
    </q-card-section>
    <q-card-section>
      <div class="row justify-between">
        <q-select v-model="schemaChoice" class="col-3" outlined :options="schemaOptions" label="Schema" id="tour-schema">
          <template #prepend>
            <q-icon name="view_week" />
          </template>
        </q-select>
        <q-select v-model="langChoice" class="col-3" outlined :options="langOptions" label="Sprache" id="tour-lang">
          <template #prepend>
            <q-icon name="language" />
          </template>
        </q-select>
        <q-btn class="primary-button col-3 offset-md-2" size="md" label="Datenbanken generieren" :disable="btnDisabled" @click="generateTables" id="tour-datagen"></q-btn>
      </div>
    </q-card-section>
  </q-card>
</template>

<script setup>
import { computed, ref, defineEmits } from "vue"

const props = defineProps({
  // loading prop used to deactivate the generateData button, while waiting on response from backend.
  loading: {
    type: Boolean,
    required: true,
  },
})

// Stores if choices where already done.
const optionsChosen = computed(() => schemaChoice.value && langChoice.value)

// Deactivates generateData button, if choices are not made yet, or while waiting on response from backend
const btnDisabled = computed(() => !optionsChosen.value || props.loading)

// Possible choices and variables to store the choices. schemaOptions have to be contained in schemas_dict in backend file server.data_gen.data_generation_for_demo.py.
const schemaChoice = ref(null)
const schemaOptions = ["Kunde", "Diabetes Patient", "TikTok Nutzer", "Prominenter", "Konzert", "Kreditkarte", "Wein Bewertung", "Film", "Autounfall"]
const langChoice = ref(null)
const langOptions = ["Deutsch", "Englisch", "gemischt"]

const options = computed(() => {
  return {
    schema: schemaChoice.value,
    lang: langChoice.value,
  }
})

// Emit chosen options to parent
const emit = defineEmits(["generate-tables"])

const generateTables = () => {
  emit("generate-tables", options.value)
}
</script>
