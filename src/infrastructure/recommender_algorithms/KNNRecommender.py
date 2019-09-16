import lenskit
import numpy as np
from lenskit import crossfold
from lenskit.algorithms import item_knn, Recommender
from lenskit.crossfold import partition_users
from pandas import DataFrame

from src.infrastructure.parse.DataFrameReaderStrategy import DataFrameReaderStrategy
from src.infrastructure.parse.DataFrameReaderStrategyContext import DataFrameReaderStrategyContext
from src.infrastructure.parse.DataFrameReaderStrategyFactory import DataFrameReaderStrategyFactory
from src.infrastructure.recommender_algorithms.RecommenderAlgorithmStrategy import RecommenderAlgorithmStrategy
from src.infrastructure.recommender_algorithms.RecommenderAlgorithmStrategyContext import \
    RecommenderAlgorithmStrategyContext


class KNNRecommender(RecommenderAlgorithmStrategy):
    # TODO Use a Dependency injection container
    def __init__(self, data_frame_reader_factory: DataFrameReaderStrategyFactory = DataFrameReaderStrategyFactory()):
        self.data_frame_reader_factory = data_frame_reader_factory

    def run(self, strategy_context: RecommenderAlgorithmStrategyContext) -> np.ndarray:
        data_set_source = strategy_context.data_set_source
        data_frame_reader: DataFrameReaderStrategy = self.data_frame_reader_factory.create(data_set_source)
        data_set: DataFrame = data_frame_reader.parse(DataFrameReaderStrategyContext(data_set_source))

        partition = list(partition_users(data=data_set, partitions=1, method=crossfold.SampleFrac(0.2)))[0]
        test, train = partition.test, partition.train
        algorithm = Recommender.adapt(item_knn.ItemItem(20))
        trained_algorithm = algorithm.fit(train)
        number_of_recommendations = strategy_context.number_of_recommendations
        recommendations = lenskit.batch.recommend(trained_algorithm, test['user'].unique(), number_of_recommendations)
        return recommendations.groupby('user')['item'].apply(lambda x: x).to_numpy().reshape(
            (-1, number_of_recommendations))
