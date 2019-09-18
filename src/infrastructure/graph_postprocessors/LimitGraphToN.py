from src.domain.value_objects.Graph import Graph
from src.infrastructure.graph_postprocessors.GraphPostProcessor import GraphPostProcessor


class LimitGraphToN(GraphPostProcessor):
    def __init__(self, n: int):
        self.n = n

    def process_graph(self, graph: Graph) -> Graph:
        # TODO Do interpolation so limiting doesn't deform graph
        final_graph_points = [graph.points[0]]
        i = 1
        for p in graph.points[1:]:
            if p.x >= pow(2, i):
                final_graph_points.append(p)
                i += 1
            if i == self.n:
                break

        return Graph(points=final_graph_points)
