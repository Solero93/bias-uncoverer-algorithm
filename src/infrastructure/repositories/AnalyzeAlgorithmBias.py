from pandas import DataFrame

from src.domain.repositories.AnalyzeAlgorithmBiasRepository import AnalyzeAlgorithmBiasRepository
from src.domain.value_objects.AlgorithmCode import AlgorithmCode
from src.domain.value_objects.BiasCode import BiasCode
from src.domain.value_objects.DataSetSource import DataSetSource
from src.domain.value_objects.Graph import Graph
from src.infrastructure.algorithm_bias.AlgorithmBiasStrategy import AlgorithmBiasStrategy
from src.infrastructure.algorithm_bias.AlgorithmBiasStrategyContext import AlgorithmBiasStrategyContext
from src.infrastructure.algorithm_bias.AlgorithmBiasStrategyFactory import AlgorithmBiasStrategyFactory
from src.infrastructure.parse.ReadDataFrameFromCSV import ReadDataFrameFromCSV
from src.infrastructure.parse.ReadDataFrameFromDataSetStrategyContext import ReadDataFrameFromDataSetStrategyContext
from src.infrastructure.recommender_algorithms.RecommenderAlgorithmStrategy import RecommenderAlgorithmStrategy
from src.infrastructure.recommender_algorithms.RecommenderAlgorithmStrategyFactory import \
    RecommenderAlgorithmStrategyFactory


class AnalyzeAlgorithmBias(AnalyzeAlgorithmBiasRepository):
    def __init__(self, algorithm_bias_factory: AlgorithmBiasStrategyFactory,
                 recommender_algorithm_factory: RecommenderAlgorithmStrategyFactory):
        self.algorithm_bias_factory = algorithm_bias_factory
        self.recommender_algorithm_factory = recommender_algorithm_factory

    def analyze(self, data_set_path: DataSetSource, bias_code: BiasCode, algorithm_code: AlgorithmCode) \
            -> Graph:
        data_set: DataFrame = ReadDataFrameFromCSV().parse(ReadDataFrameFromDataSetStrategyContext(data_set_path))
        algorithm_bias_strategy: AlgorithmBiasStrategy = self.algorithm_bias_factory.create(bias_code)
        recommender_strategy: RecommenderAlgorithmStrategy = self.recommender_algorithm_factory.create(
            algorithm_code=algorithm_code)
        return algorithm_bias_strategy.run(
            AlgorithmBiasStrategyContext(recommender_strategy=recommender_strategy, data_set=data_set)
        )
