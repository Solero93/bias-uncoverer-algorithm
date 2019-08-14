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

        all_movies: np.ndarray = strategy_context.data_set['movie_id'].unique()

        recommendation_frequencies: pandas.Series = pandas.Series(data=recommendations.flatten()).value_counts()
        series_with_zero_frequencies_for_all_movies: pandas.Series = pandas.Series(
            data=np.zeros(shape=(all_movies.size,)), index=all_movies, dtype=np.int
        )
        frequencies_of_all_items: pandas.Series = recommendation_frequencies \
            .combine_first(series_with_zero_frequencies_for_all_movies)

        frequencies_of_frequencies_of_all_items = frequencies_of_all_items.value_counts().sort_index()

        graph_points: List[GraphPoint] = [
            GraphPoint(x=k, y=v) for k, v in frequencies_of_frequencies_of_all_items.to_dict().items()
        ]  # TODO optimize if necessary

        return Graph(points=graph_points)
