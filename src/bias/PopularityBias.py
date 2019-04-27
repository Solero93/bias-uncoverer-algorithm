from typing import Dict

from pandas import DataFrame

from src.bias.BiasStrategy import BiasStrategy


class PopularityBias(BiasStrategy):
    def execute(self, input_data_frame: DataFrame) -> Dict:
        return input_data_frame['movie'].value_counts().to_dict()
