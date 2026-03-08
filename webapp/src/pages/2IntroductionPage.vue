<template>
  <q-page padding class="main-page column text-body1 text-justify">
    <div class="col">
      <h3>Einführung</h3>
      <div>
        Willkommen im Schema-Matching-Demonstrator! Im Folgenden geht es um die automatisierte
        Zusammenführung und Vereinheitlichung großer Datensätze. Auf den nächsten Seiten wirst du
        einiges über die wissenschaftlichen Hintergründe erfahren und anschließend die Möglichkeit
        haben, ein am ScaDS.AI entwickeltes Programm selbst auszuprobieren.
      </div>
    </div>

    <q-card class="col q-my-xl" flat>
      <q-card-section class="text-h5 blue-bg blue-border">Beispiel</q-card-section>

      <q-card-section>
        <div class="row justify-between items-center q-my-xl">
          <div class="col-5">
            <q-img src="../assets/diagrams/example-diagram.png" />
            <div class="row justify-between q-mt-md">
              <q-btn
                class="primary-button"
                :class="{ pulseBtn: isShaking }"
                flat
                :icon="folder1"
                name="Patientendaten"
              >
                Patientendaten
                <q-popup-proxy @before-show="onClick($event, 1)" @before-hide="onClick($event, 1)">
                  <example-table1 />
                </q-popup-proxy>
              </q-btn>
              <q-btn
                class="primary-button"
                :class="{ pulseBtn: isShaking }"
                flat
                :icon="folder2"
                name="patient data"
              >
                patient data
                <q-popup-proxy @before-show="onClick($event, 2)" @before-hide="onClick($event, 2)">
                  <example-table2 />
                </q-popup-proxy>
              </q-btn>
            </div>
          </div>
          <div class="col-5 offset-md-1">
            <div class="text-h6">Gemeinsame Gesundheitsversorgung</div>
            Stell dir vor, einige Länder hätten ein Abkommen geschlossen, um die medizinische
            Versorgung ihrer Bürgerinnen und Bürger im Ausland zu verbessern. Zu diesem Zweck sollen
            Patientendaten aus allen Mitgliedstaaten zentral in einer großen Datenbank erfasst
            werden. Die verschiedenen Krankenkassen und Krankenhäuser der jeweiligen Länder
            übermitteln ihre gespeicherten Daten in Form von unzähligen Tabellen voller
            Patientendaten und Fallgeschichten an eine zentrale Datenbank.
          </div>
        </div>
        <div class="row items-end justify-between">
          <div class="col-6">
            <div class="text-h6">Das Problem</div>
            Die Länder haben sich in der Vergangenheit nie auf ein gemeinsames Muster zur
            Datenerhebung geeinigt. So führt im Schaubild ein Krankenhaus die Datenbank
            <span class="text-bold"> PATIENTENDATEN</span> und ein anderes die Datenbank
            <span class="text-bold">PATIENT DATA</span>. Der neu entstandene Datensatz enthält also
            Angaben in unterschiedlichen Sprachen, verschiedenen Maßeinheiten, Diagnosecodes,
            Fallnummern und demografischen Angaben. Aufgrund der Menge an Daten kommt ein händisches
            Zusammenführen nicht infrage - aber könnte das nicht auch ein Programm für uns
            erledigen?
          </div>
          <div class="col-5 offset-md-1">
            <q-img src="../assets/scads-corp-design/loops/loop-darkblue.png"></q-img>
          </div>
        </div>
      </q-card-section>
    </q-card>
    <div class="col q-my-lg">
      <move-vertical-btn link="/sm" direction="down" />
    </div>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'
import MoveVerticalBtn from 'components/buttons/MoveVerticalBtn.vue'
import ExampleTable1 from 'components/tables/ExampleTablePatientendaten.vue'
import ExampleTable2 from 'components/tables/ExampleTablePatientData.vue'

const folder1 = ref('folder')
const folder2 = ref('folder')

const isShaking = ref(true)

const onClick = (event, folderId) => {
  isShaking.value = false
  if (folderId === 1) {
    folder1.value = folder1.value === 'folder' ? 'folder_open' : 'folder'
  }
  if (folderId === 2) {
    folder2.value = folder2.value === 'folder' ? 'folder_open' : 'folder'
  }
}
</script>

<style scoped>
@keyframes shakeJumpPause {
  0% {
    transform: translateX(0) rotate(0deg);
    background: #b3e89b;
  }
  3% {
    transform: translateX(-1px) rotate(-0.5deg);
  }
  6% {
    transform: translateX(1px) rotate(0.5deg);
  }
  7% {
    background: rgba(179, 232, 155, 0.77);
  }
  9% {
    transform: translateX(-1px) rotate(-0.5deg);
  }
  12% {
    transform: translateX(1px) rotate(0.5deg);
  }
  15% {
    transform: translateX(0) rotate(0deg);
    background: #b3e89b;
  }
}

.pulseBtn {
  animation: shakeJumpPause 5s infinite;
}

.pulseBtn:nth-child(1) {
  animation-delay: 0s;
}

.pulseBtn:nth-child(2) {
  animation-delay: 2.5s;
}
</style>
