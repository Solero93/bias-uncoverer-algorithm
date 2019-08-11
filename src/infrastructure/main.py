from pprint import pprint

from src.application.AnalyzeAlgorithmBias import AnalyzeAlgorithmBias
from src.application.AnalyzeDataBias import AnalyzeDataBias
from src.domain.value_objects.AlgorithmCode import AlgorithmCode
from src.domain.value_objects.BiasCode import BiasCode
from src.domain.value_objects.DataSetSource import DataSetSource


def read_from_queue():
    algorithm_code: AlgorithmCode = AlgorithmCode('random')
    bias_code: BiasCode = BiasCode('popularity')
    data_set_source: DataSetSource = DataSetSource('random_path_to_file')

    data_bias_graph: Graph = AnalyzeDataBias().invoke(data_set_source=data_set_source, bias_code=bias_code)
    algorithm_bias_graph: Graph = AnalyzeAlgorithmBias().invoke(data_set_source=data_set_source, bias_code=bias_code,
                                                                algorithm_code=algorithm_code)

    result = {
        'data_bias': data_bias_graph.to_dict(),
        'algorithm_bias': algorithm_bias_graph.to_dict()
    }

    pprint(result)

    # TODO
    # Wait for something in queue
    # Process stuff
    # Send results to queue back again


if __name__ == '__main__':
    read_from_queue()
