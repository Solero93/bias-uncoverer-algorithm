from src.application.AnalyzeAlgorithmBias import AnalyzeAlgorithmBias
from src.application.AnalyzeDataBias import AnalyzeDataBias
from src.domain.AnalysisResult import AnalysisResult
from src.domain.repositories.AnalysisQueryRepository import AnalysisQueryRepository
from src.domain.repositories.AnalysisResultRepository import AnalysisResultRepository
from src.domain.value_objects.Graph import Graph
from src.infrastructure.repositories.analysis_query.RabbitMQAnalysisQuery import RabbitMQAnalysisQuery
from src.infrastructure.repositories.analysis_result.RabbitMQAnalysisResult import RabbitMQAnalysisResult


class Main:
    def __init__(self, analysis_query_repository: AnalysisQueryRepository = RabbitMQAnalysisQuery(),
                 analysis_result_repository: AnalysisResultRepository = RabbitMQAnalysisResult()):
        self.analysis_query_repository = analysis_query_repository
        self.analysis_result_repository = analysis_result_repository

    def main(self):
        for message in self.analysis_query_repository.wait_and_get():
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
                analysis_id=message.analysis_id,
                data_bias_graph=data_bias_graph,
                algorithm_bias_graph=algorithm_bias_graph
            )

            self.analysis_result_repository.store(result)


if __name__ == '__main__':
    Main().main()
