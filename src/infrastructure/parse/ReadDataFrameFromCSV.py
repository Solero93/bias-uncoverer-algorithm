from pandas import DataFrame, read_csv

from src.infrastructure.parse.ReadDataFrameFromDataSetStrategy import ReadDataFrameFromDataSetStrategy
from src.infrastructure.parse.ReadDataFrameFromDataSetStrategyContext import ReadDataFrameFromDataSetStrategyContext


class ReadDataFrameFromCSV(ReadDataFrameFromDataSetStrategy):
    def parse(self, strategy_context: ReadDataFrameFromDataSetStrategyContext) -> DataFrame:
        return read_csv(strategy_context.data_set_path.path)
