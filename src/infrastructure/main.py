from infrastructure import StoreResult
from src.application.AnalyzeAlgorithmBias import AnalyzeAlgorithmBias
from src.application.AnalyzeDataBias import AnalyzeDataBias
from src.domain.AnalysisResult import AnalysisResult
from src.domain.value_objects.Graph import Graph
from src.infrastructure import GetInput


def main():
    for message in GetInput.get_message():
        data_bias_graph: Graph = AnalyzeDataBias().invoke(
            data_set_source=message.data_set_source,
            bias_code=message.bias_code
        )
        algorithm_bias_graph: Graph = AnalyzeAlgorithmBias().invoke(
            data_set_source=message.data_set_source,
            bias_code=message.bias_code,
            algorithm_code=message.algorithm_code
        )

        result = AnalysisResult(
            data_bias_graph=data_bias_graph,
            algorithm_bias_graph=algorithm_bias_graph
        )

        StoreResult.store(result)


if __name__ == '__main__':
    main()
