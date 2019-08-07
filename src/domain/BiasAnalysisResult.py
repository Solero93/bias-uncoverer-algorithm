from dataclasses import dataclass

from src.domain.value_objects.Graph import Graph


@dataclass
class BiasAnalysisResult:
    data_bias_graph: Graph
    algorithm_bias_graph: Graph

    def to_dict(self):
        return {
            'data_bias_graph': self.data_bias_graph.to_dict(),
            'algorithm_bias_graph': self.algorithm_bias_graph.to_dict()
        }
