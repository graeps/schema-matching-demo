import { useNodesData } from '@vue-flow/core'
import { computed } from 'vue'

export function useInstanceMatcher(connections) {
  const connectedNodes = useNodesData(computed(() => connections.value.map((conn) => conn.source)))

  const compareDataType = computed(() => {
    const [node1, node2] = connectedNodes.value
    const ready = connections.value.length === 2 && node1 && node2

    if (!ready) return '[Matcher verbinden]'

    const type1 = node1.data.preprocProps.dataType
    const type2 = node2.data.preprocProps.dataType

    return type1 === type2 ? 0.48 : `0.0 (${type1} ≠ ${type2})`
  })

  return { compareDataType }
}
