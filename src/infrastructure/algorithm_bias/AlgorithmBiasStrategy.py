from abc import abstractmethod, ABC

from src.domain.value_objects.Graph import Graph
from src.infrastructure.algorithm_bias.AlgorithmBiasStrategyContext import AlgorithmBiasStrategyContext


class AlgorithmBiasStrategy(ABC):
    @abstractmethod
    def run(self, strategy_context: AlgorithmBiasStrategyContext) -> Graph:
        pass
