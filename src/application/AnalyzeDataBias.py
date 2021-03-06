from src.domain.repositories.DataBiasRepository import DataBiasRepository
from src.domain.value_objects.BiasCode import BiasCode
from src.domain.value_objects.DataSetSource import DataSetSource
from src.domain.value_objects.Graph import Graph
from src.infrastructure.repositories.data_bias.DataBias import DataBias


class AnalyzeDataBias:
    # TODO Use a Dependency injection container
    def __init__(self, analyze_data_bias_repository: DataBiasRepository = DataBias()):
        self.analyze_data_bias_repository = analyze_data_bias_repository

    def invoke(self, data_set_source: DataSetSource, bias_code: BiasCode) -> Graph:
        data_bias_graph: Graph = self.analyze_data_bias_repository.analyze(
            data_set_source=data_set_source,
            bias_code=bias_code
        )

        return data_bias_graph
