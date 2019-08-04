from dataclasses import dataclass

from pandas import DataFrame

from src.infrastructure.recommender_algorithms.RecommenderAlgorithmStrategy import RecommenderAlgorithmStrategy


@dataclass
class AlgorithmBiasStrategyContext:
    recommender_strategy: RecommenderAlgorithmStrategy
    data_set: DataFrame
