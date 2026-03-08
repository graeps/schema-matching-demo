import { useNodesData } from '@vue-flow/core'
import { computed } from 'vue'

export function useStringMatcher(connections) {
  // Extracting title data from the nodes
  const titleData = useNodesData(() => connections.value.map((connection) => connection.source))

  // Function to calculate Jaccard Similarity
  const calculateJaccardSimilarity = (str1, str2) => {
    const setA = new Set(str1)
    const setB = new Set(str2)
    const intersection = new Set([...setA].filter((x) => setB.has(x)))
    const union = new Set([...setA, ...setB])
    return (intersection.size / union.size || 0).toFixed(2)
  }

  // Computed property to compare titles
  const compareTitlesResult = computed(() => {
    if (connections.value.length === 2) {
      return calculateJaccardSimilarity(
        titleData.value[0].data.preprocProps.title,
        titleData.value[1].data.preprocProps.title,
      )
    } else {
      return '[Matcher verbinden]'
    }
  })

  return {
    compareTitlesResult,
  }
}
