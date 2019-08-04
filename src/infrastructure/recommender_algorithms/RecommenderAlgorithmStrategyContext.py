from dataclasses import dataclass

from pandas import DataFrame


@dataclass
class RecommenderAlgorithmStrategyContext:
    data_set: DataFrame
    number_of_recommendations: int
