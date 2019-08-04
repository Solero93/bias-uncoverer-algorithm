from abc import abstractmethod, ABC

import numpy as np

from src.infrastructure.recommender_algorithms.RecommenderAlgorithmStrategyContext import \
    RecommenderAlgorithmStrategyContext


class RecommenderAlgorithmStrategy(ABC):
    @abstractmethod
    def run(self, strategy_context: RecommenderAlgorithmStrategyContext) -> np.ndarray:
        pass
