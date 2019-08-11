from dataclasses import dataclass

from domain.value_objects.AnalysisID import AnalysisID
from src.domain.value_objects.AlgorithmCode import AlgorithmCode
from src.domain.value_objects.BiasCode import BiasCode
from src.domain.value_objects.DataSetSource import DataSetSource


@dataclass
class AnalysisQuery:
    analysis_id: AnalysisID
    data_set_source: DataSetSource
    bias_code: BiasCode
    algorithm_code: AlgorithmCode
