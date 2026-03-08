import { useNodesData } from '@vue-flow/core'
import { computed } from 'vue'

export function useClassifierMatcher(connections) {
  const connectedNodes = useNodesData(computed(() => connections.value.map((conn) => conn.source)))

  const compareClassifier = computed(() => {
    const [node1, node2] = connectedNodes.value
    const ready = connections.value.length === 2 && node1 && node2

    if (!ready) return '[Matcher verbinden]'

    const title1 = node1.data.preprocProps.title
    const title2 = node2.data.preprocProps.title

    if (
      (title1 === 'Diagnose' && title2 === 'Diagnosis') ||
      (title1 === 'Diagnosis' && title2 === 'Diagnose')
    ) {
      return '0.91'
    }
    if (
      (title1 === 'Diagnose' && title2 === 'PID') ||
      (title1 === 'PID' && title2 === 'Diagnose')
    ) {
      return '0.05'
    }
    if (
      (title1 === 'Geburtsdatum' && title2 === 'Diagnosis') ||
      (title1 === 'Diagnosis' && title2 === 'Geburtsdatum')
    ) {
      return '0.1 (true)'
    }
    if (
      (title1 === 'Geburtsdatum' && title2 === 'PID') ||
      (title1 === 'PID' && title2 === 'Geburtsdatum')
    ) {
      return '0.4'
    } else {
      return '0.0 (false)'
    }
  })

  return { compareClassifier }
}
