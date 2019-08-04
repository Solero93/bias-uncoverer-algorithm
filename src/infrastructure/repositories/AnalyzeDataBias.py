from pandas import DataFrame

from src.domain.repositories.AnalyzeDataBiasRepository import AnalyzeDataBiasRepository
from src.domain.value_objects.BiasCode import BiasCode
from src.domain.value_objects.DataSetSource import DataSetSource
from src.domain.value_objects.Graph import Graph
from src.infrastructure.data_bias.DataBiasStrategy import DataBiasStrategy
from src.infrastructure.data_bias.DataBiasStrategyContext import DataBiasStrategyContext
from src.infrastructure.data_bias.DataBiasStrategyFactory import DataBiasStrategyFactory
from src.infrastructure.parse.ReadDataFrameFromCSV import ReadDataFrameFromCSV
from src.infrastructure.parse.ReadDataFrameFromDataSetStrategyContext import ReadDataFrameFromDataSetStrategyContext


class AnalyzeDataBias(AnalyzeDataBiasRepository):
    def __init__(self, data_bias_factory: DataBiasStrategyFactory):
        self.data_bias_factory = data_bias_factory

    def analyze(self, data_set_path: DataSetSource, bias_code: BiasCode) -> Graph:
        data_set: DataFrame = ReadDataFrameFromCSV().parse(ReadDataFrameFromDataSetStrategyContext(data_set_path))
        data_bias_strategy: DataBiasStrategy = self.data_bias_factory.create(bias_code)
        return data_bias_strategy.run(DataBiasStrategyContext(data_set=data_set))
