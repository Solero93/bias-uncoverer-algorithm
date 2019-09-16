from src.domain.value_objects.Graph import Graph
from src.infrastructure.graph_postprocessors.GraphPostProcessor import GraphPostProcessor


class LimitToN(GraphPostProcessor):
    def __init__(self, n: int):
        self.n = n

    def process_graph(self, graph: Graph) -> Graph:
        # TODO Do interpolation so limiting doesn't deform graph
        return Graph(points=graph.points[:self.n])
