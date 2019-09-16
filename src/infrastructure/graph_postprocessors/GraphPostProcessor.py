from abc import ABC, abstractmethod

from src.domain.value_objects.Graph import Graph


class GraphPostProcessor(ABC):
    @abstractmethod
    def process_graph(self, graph: Graph) -> Graph:
        pass
