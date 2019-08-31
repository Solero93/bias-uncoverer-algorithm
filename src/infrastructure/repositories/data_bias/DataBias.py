from pandas import DataFrame

from src.domain.repositories.DataBiasRepository import DataBiasRepository
from src.domain.value_objects.BiasCode import BiasCode
from src.domain.value_objects.DataSetSource import DataSetSource
from src.domain.value_objects.Graph import Graph
from src.infrastructure.data_bias.DataBiasStrategy import DataBiasStrategy
from src.infrastructure.data_bias.DataBiasStrategyContext import DataBiasStrategyContext
from src.infrastructure.data_bias.DataBiasStrategyFactory import DataBiasStrategyFactory
from src.infrastructure.parse.DataFrameReaderStrategy import DataFrameReaderStrategy
from src.infrastructure.parse.DataFrameReaderStrategyContext import DataFrameReaderStrategyContext
from src.infrastructure.parse.DataFrameReaderStrategyFactory import DataFrameReaderStrategyFactory


class DataBias(DataBiasRepository):
    # TODO Use a Dependency injection container
    def __init__(self, data_frame_reader_factory: DataFrameReaderStrategyFactory = DataFrameReaderStrategyFactory(),
                 data_bias_factory: DataBiasStrategyFactory = DataBiasStrategyFactory()):
        self.data_frame_reader_factory = data_frame_reader_factory
        self.data_bias_factory = data_bias_factory

    def analyze(self, data_set_source: DataSetSource, bias_code: BiasCode) -> Graph:
        data_frame_reader: DataFrameReaderStrategy = self.data_frame_reader_factory.create(data_set_source)
        data_set: DataFrame = data_frame_reader.parse(DataFrameReaderStrategyContext(data_set_source))
        data_bias_strategy: DataBiasStrategy = self.data_bias_factory.create(bias_code)
        return data_bias_strategy.run(
            DataBiasStrategyContext(data_set=data_set)
        )
