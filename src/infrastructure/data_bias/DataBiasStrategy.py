from abc import abstractmethod, ABC

import numpy as np

from src.domain.value_objects.Graph import Graph
from src.infrastructure.data_bias.DataBiasStrategyContext import DataBiasStrategyContext


class DataBiasStrategy(ABC):
    @abstractmethod
    def run(self, strategy_context: DataBiasStrategyContext) -> Graph:
        pass
