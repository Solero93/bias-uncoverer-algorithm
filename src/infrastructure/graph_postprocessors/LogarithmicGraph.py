from math import log

from src.domain.value_objects.Graph import Graph
from src.domain.value_objects.GraphPoint import GraphPoint
from src.infrastructure.graph_postprocessors.GraphPostProcessor import GraphPostProcessor


class LogarithmicGraph(GraphPostProcessor):
    def process_graph(self, graph: Graph) -> Graph:
        return Graph(points=[GraphPoint(x=point.x, y=log(point.y)) for point in graph.points])
