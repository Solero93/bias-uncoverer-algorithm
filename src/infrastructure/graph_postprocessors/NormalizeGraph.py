from decimal import Decimal

from src.domain.value_objects.Graph import Graph
from src.domain.value_objects.GraphPoint import GraphPoint
from src.infrastructure.graph_postprocessors.GraphPostProcessor import GraphPostProcessor


class NormalizeGraph(GraphPostProcessor):
    def __init__(self, maximum: float):
        self.maximum = maximum

    def process_graph(self, graph: Graph) -> Graph:
        return Graph(points=[
            GraphPoint(x=point.x, y=float(Decimal(str(point.y)) / Decimal(str(self.maximum)) * Decimal('100')))
            for point in graph.points
        ])
