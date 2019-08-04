from abc import ABC, abstractmethod

from src.domain.value_objects.AlgorithmCode import AlgorithmCode
from src.domain.value_objects.BiasCode import BiasCode
from src.domain.value_objects.DataSetSource import DataSetSource
from src.domain.value_objects.Graph import Graph


class AnalyzeAlgorithmBiasRepository(ABC):
    @abstractmethod
    def analyze(self, data_set_source: DataSetSource, bias_code: BiasCode, algorithm_code: AlgorithmCode) -> Graph:
        pass
