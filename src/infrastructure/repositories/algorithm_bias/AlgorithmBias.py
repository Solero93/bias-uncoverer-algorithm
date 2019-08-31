from pandas import DataFrame

from src.domain.repositories.AlgorithmBiasRepository import AlgorithmBiasRepository
from src.domain.value_objects.AlgorithmCode import AlgorithmCode
from src.domain.value_objects.BiasCode import BiasCode
from src.domain.value_objects.DataSetSource import DataSetSource
from src.domain.value_objects.Graph import Graph
from src.infrastructure.algorithm_bias.AlgorithmBiasStrategy import AlgorithmBiasStrategy
from src.infrastructure.algorithm_bias.AlgorithmBiasStrategyContext import AlgorithmBiasStrategyContext
from src.infrastructure.algorithm_bias.AlgorithmBiasStrategyFactory import AlgorithmBiasStrategyFactory
from src.infrastructure.parse.DataFrameReaderStrategy import DataFrameReaderStrategy
from src.infrastructure.parse.DataFrameReaderStrategyContext import DataFrameReaderStrategyContext
from src.infrastructure.parse.DataFrameReaderStrategyFactory import DataFrameReaderStrategyFactory
from src.infrastructure.recommender_algorithms.RecommenderAlgorithmStrategy import RecommenderAlgorithmStrategy
from src.infrastructure.recommender_algorithms.RecommenderAlgorithmStrategyFactory import \
    RecommenderAlgorithmStrategyFactory


class AlgorithmBias(AlgorithmBiasRepository):
    # TODO Use a Dependency injection container
    def __init__(self, data_frame_reader_factory: DataFrameReaderStrategyFactory = DataFrameReaderStrategyFactory(),
                 algorithm_bias_factory: AlgorithmBiasStrategyFactory = AlgorithmBiasStrategyFactory(),
                 recommender_algorithm_factory: RecommenderAlgorithmStrategyFactory = RecommenderAlgorithmStrategyFactory()):
        self.data_frame_reader_factory = data_frame_reader_factory
        self.algorithm_bias_factory = algorithm_bias_factory
        self.recommender_algorithm_factory = recommender_algorithm_factory

    def analyze(self, data_set_source: DataSetSource, bias_code: BiasCode, algorithm_code: AlgorithmCode) \
            -> Graph:
        data_frame_reader: DataFrameReaderStrategy = self.data_frame_reader_factory.create(data_set_source)
        data_set: DataFrame = data_frame_reader.parse(DataFrameReaderStrategyContext(data_set_source))
        algorithm_bias_strategy: AlgorithmBiasStrategy = self.algorithm_bias_factory.create(bias_code)
        recommender_strategy: RecommenderAlgorithmStrategy = self.recommender_algorithm_factory.create(
            algorithm_code=algorithm_code)
        return algorithm_bias_strategy.run(
            AlgorithmBiasStrategyContext(recommender_strategy=recommender_strategy, data_set=data_set)
        )
