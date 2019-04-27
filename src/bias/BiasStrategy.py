from abc import ABC, abstractmethod
from typing import Dict

from pandas import DataFrame


class BiasStrategy(ABC):
    @abstractmethod
    def execute(self, input_data_frame: DataFrame) -> Dict:
        pass
