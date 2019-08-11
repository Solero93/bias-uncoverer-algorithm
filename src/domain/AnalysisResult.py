from dataclasses import dataclass
from typing import Dict, List

from src.domain.value_objects.Graph import Graph


@dataclass
class AnalysisResult:
    data_bias_graph: Graph
    algorithm_bias_graph: Graph

    def serialize(self) -> Dict[str, List[dict]]:
        return {
            'data_bias': self.data_bias_graph.serialize(),
            'algorithm_bias': self.algorithm_bias_graph.serialize()
        }
