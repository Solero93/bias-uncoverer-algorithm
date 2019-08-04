from src.domain.BiasAnalysisResult import BiasAnalysisResult
from src.domain.repositories.AnalyzeAlgorithmBiasRepository import AnalyzeAlgorithmBiasRepository
from src.domain.repositories.AnalyzeDataBiasRepository import AnalyzeDataBiasRepository
from src.domain.value_objects.AlgorithmCode import AlgorithmCode
from src.domain.value_objects.BiasCode import BiasCode
from src.domain.value_objects.DataSetSource import DataSetSource
from src.domain.value_objects.Graph import Graph
from src.infrastructure.algorithm_bias.AlgorithmBiasStrategyFactory import AlgorithmBiasStrategyFactory
from src.infrastructure.data_bias.DataBiasStrategyFactory import DataBiasStrategyFactory
from src.infrastructure.recommender_algorithms.RecommenderAlgorithmStrategyFactory import \
    RecommenderAlgorithmStrategyFactory
from src.infrastructure.repositories.AnalyzeAlgorithmBias import AnalyzeAlgorithmBias
from src.infrastructure.repositories.AnalyzeDataBias import AnalyzeDataBias


class AnalyzeBias:
    # TODO Dependency injection
    def __init__(self, analyze_algorithm_bias_repository: AnalyzeAlgorithmBiasRepository = AnalyzeAlgorithmBias(
        AlgorithmBiasStrategyFactory(), RecommenderAlgorithmStrategyFactory()),
                 analyze_data_bias_repository: AnalyzeDataBiasRepository = AnalyzeDataBias(DataBiasStrategyFactory())):
        self.analyze_algorithm_bias_repository = analyze_algorithm_bias_repository
        self.analyze_data_bias_repository = analyze_data_bias_repository

    def invoke(self, data_set_source: DataSetSource, bias_code: BiasCode, algorithm_code: AlgorithmCode):

        data_bias_graph: Graph = self.analyze_data_bias_repository.analyze(
            data_set_path=data_set_source,
            bias_code=bias_code
        )

        algorithm_bias_graph: Graph = self.analyze_algorithm_bias_repository.analyze(
            data_set_path=data_set_source,
            bias_code=bias_code,
            algorithm_code=algorithm_code
        )

        return BiasAnalysisResult(data_bias_graph=data_bias_graph, algorithm_bias_graph=algorithm_bias_graph)
