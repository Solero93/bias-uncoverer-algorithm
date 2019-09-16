from dataclasses import dataclass

from src.domain.value_objects.DataSetSource import DataSetSource


@dataclass
class DataBiasStrategyContext:
    data_set_source: DataSetSource
