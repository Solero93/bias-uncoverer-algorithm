from typing import List

import numpy as np
import pandas
from pandas import DataFrame

from src.domain.value_objects.Graph import Graph
from src.domain.value_objects.GraphPoint import GraphPoint
from src.infrastructure.algorithm_bias.AlgorithmBiasStrategy import AlgorithmBiasStrategy
from src.infrastructure.algorithm_bias.AlgorithmBiasStrategyContext import AlgorithmBiasStrategyContext
from src.infrastructure.parse.DataFrameReaderStrategy import DataFrameReaderStrategy
from src.infrastructure.parse.DataFrameReaderStrategyContext import DataFrameReaderStrategyContext
from src.infrastructure.parse.DataFrameReaderStrategyFactory import DataFrameReaderStrategyFactory
from src.infrastructure.recommender_algorithms.RecommenderAlgorithmStrategyContext import \
    RecommenderAlgorithmStrategyContext


class PopularityAlgorithmBias(AlgorithmBiasStrategy):
    def __init__(self, data_frame_reader_factory: DataFrameReaderStrategyFactory = DataFrameReaderStrategyFactory()):
        self.data_frame_reader_factory = data_frame_reader_factory

    def run(self, strategy_context: AlgorithmBiasStrategyContext) -> Graph:
        data_set_source = strategy_context.data_set_source
        recommendations: np.ndarray = strategy_context.recommender_strategy.run(RecommenderAlgorithmStrategyContext(
            data_set_source=data_set_source,
            number_of_recommendations=10
        ))

        data_frame_reader: DataFrameReaderStrategy = self.data_frame_reader_factory.create(data_set_source)
        data_set: DataFrame = data_frame_reader.parse(DataFrameReaderStrategyContext(data_set_source))

        # TODO See how to obtain this programatically, without hardcoding column
        all_items: np.ndarray = data_set['item_id'].unique()

        recommendation_frequencies: pandas.Series = pandas.Series(data=recommendations.flatten()).value_counts()
        series_with_zero_frequencies_for_all_items: pandas.Series = pandas.Series(
            data=np.zeros(shape=(all_items.size,)), index=all_items, dtype=np.int
        )
        frequencies_of_all_items: pandas.Series = recommendation_frequencies \
            .combine_first(series_with_zero_frequencies_for_all_items)

        frequencies_of_frequencies_of_all_items = frequencies_of_all_items.value_counts().sort_index()

        graph_points: List[GraphPoint] = [
            GraphPoint(x=k, y=v) for k, v in frequencies_of_frequencies_of_all_items.to_dict().items()
        ]  # TODO optimize if necessary

        return Graph(points=graph_points)
