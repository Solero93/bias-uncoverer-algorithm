from abc import ABC, abstractmethod

from pandas import DataFrame

from src.infrastructure.parse.ReadDataFrameFromDataSetStrategyContext import ReadDataFrameFromDataSetStrategyContext


class ReadDataFrameFromDataSetStrategy(ABC):
    @abstractmethod
    def parse(self, strategy_context: ReadDataFrameFromDataSetStrategyContext) -> DataFrame:
        pass
