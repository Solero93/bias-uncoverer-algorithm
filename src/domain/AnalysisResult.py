from dataclasses import dataclass

from src.domain.value_objects.AnalysisID import AnalysisID
from src.domain.value_objects.Graph import Graph


@dataclass
class AnalysisResult:
    analysis_id: AnalysisID
    data_bias_graph: Graph
    algorithm_bias_graph: Graph
