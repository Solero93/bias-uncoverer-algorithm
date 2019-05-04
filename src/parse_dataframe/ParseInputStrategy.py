from abc import ABC, abstractmethod
from typing import Any

from pandas import DataFrame


class ParseDataFrameStrategy(ABC):
    @abstractmethod
    def parse(self, input_data: Any) -> DataFrame:
        pass
