from src.domain.value_objects.DataSetSource import DataSetSource
from src.infrastructure.parse.DataFrameReaderFromCSV import DataFrameReaderFromCSV
from src.infrastructure.parse.DataFrameReaderStrategy import DataFrameReaderStrategy


class DataFrameReaderStrategyFactory:
    def create(self, data_set_source: DataSetSource) -> DataFrameReaderStrategy:
        if data_set_source.isCSV():
            return DataFrameReaderFromCSV()

        # TODO Raise exception or default strategy?
        return None
