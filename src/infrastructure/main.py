from src.application.AnalyzeBias import AnalyzeBias
from src.domain.value_objects.AlgorithmCode import AlgorithmCode
from src.domain.value_objects.BiasCode import BiasCode
from src.domain.value_objects.DataSetSource import DataSetSource


def read_from_queue():
    algorithm_code: AlgorithmCode = AlgorithmCode('random')
    bias_code: BiasCode = BiasCode('popularity')
    data_set_source: DataSetSource = DataSetSource('random_path_to_file')

    result = AnalyzeBias().invoke(data_set_source=data_set_source, bias_code=bias_code, algorithm_code=algorithm_code)

    print(result)

    # TODO
    # Wait for something in queue
    # Process stuff
    # Send results to queue back again


if __name__ == '__main__':
    read_from_queue()
