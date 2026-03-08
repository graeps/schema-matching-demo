<template>
  <q-page padding class="main-page column text-body1 text-justify">
    <h3>Schema Matching im Detail</h3>
    <div class="q-mb-xl">
      Das Finden übereinstimmender Paare in einem Datensatz kann selbst für Menschen knifflig sein.
      In diesem Abschnitt erfährst du, wie genau das Schema Matching Tool funktioniert.
    </div>
    <div class="col q-mb-xl">
      <div class="q-mb-xl">
        <div class="text-h6">Überblick</div>
        Im Schaubild ist der Prozess von den <b>Input-Daten</b> bis zum fertigen
        <b>Matching</b> skizziert. Im ersten Schritt werden zu jeder Spalte in jeder Datenbank im
        <b>Preprocessing</b> relevante Metadaten extrahiert und in Vektoren von Zahlen codiert. Zu
        allen möglichen Kombination zweier Spalten aus je einer Datenbank werden anschließend von
        sogenannten <b>Matchern</b> einzelne Vergleichs-Scores berechnet. Die
        <b>Combiner</b> mitteln und gewichten diese Scores anhand einer bestimmten Konfiguration, um
        sie auf eine einzige Zahl zu bringen. Zuletzt entscheidet ein <b>Selector</b> für jedes Paar
        von Spalten, ob der Vergleichswert hoch genug ist, um von einem Match auszugehen. Wir
        erklären nun jeden Schritt im Detail mit Beispielen.
      </div>
      <div class="row justify-center">
        <q-img class="diagram-overview" src="../assets/diagrams/details-diagram-final.png" />
      </div>
    </div>
    <div class="col q-my-xl">
      <div class="q-mb-md">
        <div class="text-h6">Preprocessing</div>
        Als Eingabedaten dienen zwei Tabellen, für die das Schema-Matching-Tool semantische
        Äquivalenzen zwischen den Spalten finden soll. Beim Preprocessing wird der konkrete Inhalt
        der Spalten verworfen, stattdessen wird für jede Spalte eine Liste charakteristischer
        Eigenschaften und Werte extrahiert und weitergegeben. Diese Metadaten unterscheiden sich je
        nach Datentyp und werden als Vektoren codiert. Für den Titel einer Spalte kommt dabei das
        <a href="https://de.wikipedia.org/wiki/Worteinbettung">Word Embedding</a> Word2Vec zum
        Einsatz.
      </div>
      <try-preprocessing />
    </div>

    <div class="q-mb-xl column">
      <div class="col q-mb-md">
        <div class="text-h6">Matcher</div>
        Anschließend werden die Metadaten und Vektoren zwischen allen Spalten mithilfe sogenannter
        Matcher verglichen. Es kommen vier Typen von Matchern zum Einsatz:
        String-Vergleichs-Matcher, Instanz-Vergleichs-Matcher, Clustering-Matcher und
        Classifier-Matcher. Um die Funktionsweise der Matcher nachzuvollziehen, kannst du sie hier
        anhand eines kleinen Beispiels ausprobieren. Links und rechts siehst du die Ausgaben des
        Preprocessings für jeweils zwei Spalten pro Datenbank. Wenn du mit der Maus einen Matcher
        mit je einer Spalte aus Datenbank I und II verbindest, wird der Similarity Score dieser
        beiden Spalten für den jeweiligen Matcher angezeigt. Halte die Maus länger über einem
        Matcher, um zusätzliche Informationen zu erhalten.
      </div>

      <div class="try-matcher-container">
        <try-matcher />
      </div>
      <div>
        Der Similarity-Score unseres String-Vergleichs wird auch
        <a href="https://de.wikipedia.org/wiki/Jaccard-Koeffizient">Jaccard-Koeffizient</a> genannt.
        Im Clustering wird der
        <a href="https://de.wikipedia.org/wiki/K-Means-Algorithmus"><i>k</i>-Means Algorithmus</a>
        verwendet, wobei <i>k</i> die Anzahl der Spalten pro Datenbank ist.
      </div>
    </div>
    <div class="bg-white">
      <div class="text-h6">Combiner und Config</div>
      <div>
        Die von den Matchern berechneten Vergleichswerte werden dann an den
        <b>Combiner</b> weitergegeben. Dieser kombiniert die Ergebnisse der Matcher anhand einer
        gegebenen Konfigurationsdatei <b>Config</b> und versucht so die Wahrscheinlichkeit für die
        semantische Äquivalenz zweier Spalten zu bestimmen. Die Konfigurationsdatei gibt hierbei
        vor, wie schwer die Übereinstimmung bestimmter Werte zu gewichten ist. Ist beispielsweise
        der Titel zweier Spalten identisch, so ist das ein starkes Indiz für semantische Äquivalenz,
        wohingegen eine ähnliche Anzahl von Worten weniger wichtig erscheint. Zuletzt entscheidet
        der <b>Selector</b> darüber, ab welcher Schwelle wir zwei Spalten als Match zurückgeben
        wollen und gibt das Ergebnis aus. Eine Konfiguration zu finden, die auf beliebigen Daten
        gute Ergebnisse liefert, ist sehr schwierig. Die im Tool verwendete Konfiguration, wurde mit
        Hilfe von
        <a href="https://de.wikipedia.org/wiki/Best%C3%A4rkendes_Lernen">Reinforcement learning</a>
        berechnet.
      </div>
      <div class="try-combiner-container q-mt-lg">
        <try-combiner />
      </div>
      <div>
        Schalte oben rechts zwischen zwei Beispielkonfigurationen hin und her. Sie verwenden
        unterschiedliche Hierarchien, um die Scores der Matcher und verschiedener Combiner
        miteinander zu verrechnen. In welcher Reihenfolge diese Berechnungen stattfinden, lässt sich
        gut in einem Baum darstellen, der von unten nach oben zu lesen ist. Zum Schluss entscheidet
        ein Selector darüber, ob ein Match vorliegt oder nicht. Halte lange mit der Maus über die
        Combiner und den Selector, um dir weitere Informationen anzeigen zu lassen. Um ein
        vollständiges Matching zu erhalten, müssen diese Schritte mit jeder möglichen Kombination
        von Spalten aus Datenbank I und II durchgeführt werden.
      </div>
    </div>
    <div class="q-mt-md">
      Jetzt weißt du, wie das Tool funktioniert! Hier gelangst du weiter zum Ausprobierteil, wo du
      das Schema-Matching-Tool auf künstlichen Datenbanken testen kannst.
    </div>
    <div class="q-my-xl col-1">
      <move-vertical-btn link="/try-it" direction="down" />
    </div>
  </q-page>
</template>

<script setup>
import MoveVerticalBtn from 'components/buttons/MoveVerticalBtn.vue'
import TryPreprocessing from 'components/details/TryPreprocessing.vue'
import TryMatcher from 'components/details/TryMatcher.vue'
import TryCombiner from 'components/details/TryCombiner.vue'
</script>

<style>
.diagram-overview {
  width: 100%;
}

.try-matcher-container {
  height: 80vh;
  width: 100%;
}

.try-combiner-container {
  height: 70vh;
  width: 100%;
}
</style>
