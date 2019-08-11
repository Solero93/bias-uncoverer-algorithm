from dataclasses import dataclass
from typing import Dict, List

from src.domain.value_objects.AnalysisID import AnalysisID
from src.domain.value_objects.Graph import Graph


@dataclass
class AnalysisResult:
    analysis_id: AnalysisID
    data_bias_graph: Graph
    algorithm_bias_graph: Graph

    def serialize(self) -> Dict[str, List[dict]]:
        return {
            'analysis_id': self.analysis_id.content,
            'data_bias': self.data_bias_graph.serialize(),
            'algorithm_bias': self.algorithm_bias_graph.serialize()
        }
