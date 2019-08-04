from dataclasses import dataclass

from src.domain.value_objects.Graph import Graph


@dataclass
class BiasAnalysisResult:
    data_bias_graph: Graph
    algorithm_bias_graph: Graph
