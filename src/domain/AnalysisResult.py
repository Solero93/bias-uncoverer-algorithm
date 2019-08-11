from dataclasses import dataclass

from src.domain.value_objects.Graph import Graph


@dataclass
class AnalysisResult:
    data_bias_graph: Graph
    algorithm_bias_graph: Graph

    def to_dict(self):
        return {
            'data_bias': self.data_bias_graph.to_dict(),
            'algorithm_bias': self.algorithm_bias_graph.to_dict()
        }
