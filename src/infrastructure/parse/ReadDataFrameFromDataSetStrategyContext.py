from dataclasses import dataclass

from src.domain.value_objects.DataSetSource import DataSetSource


@dataclass
class ReadDataFrameFromDataSetStrategyContext:
    data_set_path: DataSetSource
