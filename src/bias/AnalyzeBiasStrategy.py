from abc import ABC, abstractmethod
from typing import Dict

from pandas import Series


class AnalyzeBiasStrategy(ABC):
    @abstractmethod
    def analyze(self, input_data: Series) -> Dict:
        pass
