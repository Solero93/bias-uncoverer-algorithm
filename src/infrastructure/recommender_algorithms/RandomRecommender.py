import numpy as np
from pandas import DataFrame, Series

from src.infrastructure.parse.DataFrameReaderStrategy import DataFrameReaderStrategy
from src.infrastructure.parse.DataFrameReaderStrategyContext import DataFrameReaderStrategyContext
from src.infrastructure.parse.DataFrameReaderStrategyFactory import DataFrameReaderStrategyFactory
from src.infrastructure.recommender_algorithms.RecommenderAlgorithmStrategy import RecommenderAlgorithmStrategy
from src.infrastructure.recommender_algorithms.RecommenderAlgorithmStrategyContext import \
    RecommenderAlgorithmStrategyContext


class RandomRecommender(RecommenderAlgorithmStrategy):
    # TODO Use a Dependency injection container
    def __init__(self, data_frame_reader_factory: DataFrameReaderStrategyFactory = DataFrameReaderStrategyFactory()):
        self.data_frame_reader_factory = data_frame_reader_factory

    def run(self, strategy_context: RecommenderAlgorithmStrategyContext) -> np.ndarray:
        data_set_source = strategy_context.data_set_source
        data_frame_reader: DataFrameReaderStrategy = self.data_frame_reader_factory.create(data_set_source)
        data_set: DataFrame = data_frame_reader.parse(DataFrameReaderStrategyContext(data_set_source))

        # TODO See how to obtain this programatically, without hardcoding column
        all_items: np.ndarray = data_set['item'].unique()
        relative_frequency_of_each_item: Series = data_set['item'].value_counts(sort=False, normalize=True)
        all_users: np.ndarray = data_set['user'].unique()
        all_recommendations: np.ndarray = np.random.choice(
            all_items, size=(all_users.size, strategy_context.number_of_recommendations), replace=True,
            p=relative_frequency_of_each_item.values
        )
        return all_recommendations
