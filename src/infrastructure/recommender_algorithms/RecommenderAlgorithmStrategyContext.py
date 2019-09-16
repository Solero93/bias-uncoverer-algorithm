from dataclasses import dataclass

from src.domain.value_objects.DataSetSource import DataSetSource


@dataclass
class RecommenderAlgorithmStrategyContext:
    data_set_source: DataSetSource
    number_of_recommendations: int
