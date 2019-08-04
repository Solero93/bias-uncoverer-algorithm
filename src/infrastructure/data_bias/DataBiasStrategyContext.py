from dataclasses import dataclass

from pandas import DataFrame


@dataclass
class DataBiasStrategyContext:
    data_set: DataFrame
