from src.domain.repositories.AlgorithmBiasRepository import AlgorithmBiasRepository
from src.domain.value_objects.AlgorithmCode import AlgorithmCode
from src.domain.value_objects.BiasCode import BiasCode
from src.domain.value_objects.DataSetSource import DataSetSource
from src.domain.value_objects.Graph import Graph
from src.infrastructure.repositories.algorithm_bias.AlgorithmBias import AlgorithmBias


class AnalyzeAlgorithmBias:
    # TODO Use a Dependency injection container
    def __init__(self, analyze_algorithm_bias_repository: AlgorithmBiasRepository = AlgorithmBias()):
        self.analyze_algorithm_bias_repository = analyze_algorithm_bias_repository

    def invoke(self, data_set_source: DataSetSource, bias_code: BiasCode, algorithm_code: AlgorithmCode) -> Graph:
        algorithm_bias_graph: Graph = self.analyze_algorithm_bias_repository.analyze(
            data_set_source=data_set_source,
            bias_code=bias_code,
            algorithm_code=algorithm_code
        )

        return algorithm_bias_graph
