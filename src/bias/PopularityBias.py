from typing import Dict

from pandas import Series

from src.bias.AnalyzeBiasStrategy import AnalyzeBiasStrategy


class PopularityBias(AnalyzeBiasStrategy):
    def analyze(self, input_data: Series) -> Dict:
        return input_data.value_counts().to_dict()
