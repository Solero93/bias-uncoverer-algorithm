from dataclasses import dataclass

from src.domain.value_objects.DataSetSource import DataSetSource


@dataclass
class DataFrameReaderStrategyContext:
    data_set_path: DataSetSource
