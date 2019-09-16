from src.domain.repositories.DataBiasRepository import DataBiasRepository
from src.domain.value_objects.BiasCode import BiasCode
from src.domain.value_objects.DataSetSource import DataSetSource
from src.domain.value_objects.Graph import Graph
from src.infrastructure.data_bias.DataBiasStrategy import DataBiasStrategy
from src.infrastructure.data_bias.DataBiasStrategyContext import DataBiasStrategyContext
from src.infrastructure.data_bias.DataBiasStrategyFactory import DataBiasStrategyFactory


class DataBias(DataBiasRepository):
    # TODO Use a Dependency injection container
    def __init__(self, data_bias_factory: DataBiasStrategyFactory = DataBiasStrategyFactory()):
        self.data_bias_factory = data_bias_factory

    def analyze(self, data_set_source: DataSetSource, bias_code: BiasCode) -> Graph:
        data_bias_strategy: DataBiasStrategy = self.data_bias_factory.create(bias_code)
        return data_bias_strategy.run(
            DataBiasStrategyContext(data_set_source=data_set_source)
        )
