from abc import ABC, abstractmethod
from typing import List

from pandas import Series


class AnalyzeBiasStrategy(ABC):
    @abstractmethod
    def analyze(self, input_data: Series) -> List[int]:
        pass
