from abc import ABC, abstractmethod

from pandas import DataFrame

from src.infrastructure.parse.DataFrameReaderStrategyContext import DataFrameReaderStrategyContext


class DataFrameReaderStrategy(ABC):
    @abstractmethod
    def parse(self, strategy_context: DataFrameReaderStrategyContext) -> DataFrame:
        pass
