from dataclasses import dataclass

from src.domain.value_objects.DataSetSource import DataSetSource
from src.infrastructure.recommender_algorithms.RecommenderAlgorithmStrategy import RecommenderAlgorithmStrategy


@dataclass
class AlgorithmBiasStrategyContext:
    recommender_strategy: RecommenderAlgorithmStrategy
    data_set_source: DataSetSource
