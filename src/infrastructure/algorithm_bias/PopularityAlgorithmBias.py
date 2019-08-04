from typing import List

import numpy as np
import pandas

from src.domain.value_objects.Graph import Graph
from src.domain.value_objects.GraphPoint import GraphPoint
from src.infrastructure.algorithm_bias.AlgorithmBiasStrategy import AlgorithmBiasStrategy
from src.infrastructure.algorithm_bias.AlgorithmBiasStrategyContext import AlgorithmBiasStrategyContext
from src.infrastructure.recommender_algorithms.RecommenderAlgorithmStrategyContext import \
    RecommenderAlgorithmStrategyContext


class PopularityAlgorithmBias(AlgorithmBiasStrategy):
    def run(self, strategy_context: AlgorithmBiasStrategyContext) -> Graph:
        recommendations: np.ndarray = strategy_context.recommender_strategy.run(RecommenderAlgorithmStrategyContext(
            data_set=strategy_context.data_set,
            number_of_recommendations=10
        ))
        # TODO We should also see what movies where recommended 0 times!! => those currently don't appear
        recommendation_frequencies: pandas.Series = pandas.Series(recommendations.flatten()).value_counts()
        graph_points: List[GraphPoint] = [GraphPoint(x=k, y=v) for k, v in
                                          recommendation_frequencies.to_dict().items()]  # TODO optimize

        return Graph(points=graph_points)
