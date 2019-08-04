from pandas import DataFrame, read_csv

from src.infrastructure.parse.DataFrameReaderStrategy import DataFrameReaderStrategy
from src.infrastructure.parse.DataFrameReaderStrategyContext import DataFrameReaderStrategyContext


class DataFrameReaderFromCSV(DataFrameReaderStrategy):
    def parse(self, strategy_context: DataFrameReaderStrategyContext) -> DataFrame:
        return read_csv(strategy_context.data_set_path.path)
