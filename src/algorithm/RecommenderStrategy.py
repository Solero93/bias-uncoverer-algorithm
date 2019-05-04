from abc import ABC, abstractmethod
from typing import List

from pandas import DataFrame


class RecommenderStrategy(ABC):
    @abstractmethod
    def analyze(self, input_data: DataFrame) -> List[int]:
        pass
