import numpy as np
from pandas import DataFrame

from src.infrastructure.parse.DataFrameReaderStrategy import DataFrameReaderStrategy
from src.infrastructure.parse.DataFrameReaderStrategyContext import DataFrameReaderStrategyContext
from src.infrastructure.parse.DataFrameReaderStrategyFactory import DataFrameReaderStrategyFactory
from src.infrastructure.recommender_algorithms.RecommenderAlgorithmStrategy import RecommenderAlgorithmStrategy
from src.infrastructure.recommender_algorithms.RecommenderAlgorithmStrategyContext import \
    RecommenderAlgorithmStrategyContext


class ItemAverageRecommender(RecommenderAlgorithmStrategy):
    # TODO Use a Dependency injection container
    def __init__(self, data_frame_reader_factory: DataFrameReaderStrategyFactory = DataFrameReaderStrategyFactory()):
        self.data_frame_reader_factory = data_frame_reader_factory

    def run(self, strategy_context: RecommenderAlgorithmStrategyContext) -> np.ndarray:
        data_set_source = strategy_context.data_set_source
        data_frame_reader: DataFrameReaderStrategy = self.data_frame_reader_factory.create(data_set_source)
        data_set: DataFrame = data_frame_reader.parse(DataFrameReaderStrategyContext(data_set_source))

        all_users: np.ndarray = data_set['user'].unique()

        return np.repeat(data_set.pivot_table(index='item', values='rating', fill_value=float('-inf'))
                         .sort_values(by='rating', ascending=False)[
                         :strategy_context.number_of_recommendations].index.values, repeats=all_users.size)
