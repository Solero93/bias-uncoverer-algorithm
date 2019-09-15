from src.application.AnalyzeAlgorithmBias import AnalyzeAlgorithmBias
from src.application.AnalyzeDataBias import AnalyzeDataBias
from src.domain.AnalysisQuery import AnalysisQuery
from src.domain.AnalysisResult import AnalysisResult
from src.domain.repositories.AnalysisQueryRepository import AnalysisQueryRepository
from src.domain.repositories.AnalysisResultRepository import AnalysisResultRepository
from src.domain.value_objects.Graph import Graph
from src.infrastructure.repositories.analysis_query.RabbitMQAnalysisQuery import RabbitMQAnalysisQuery
from src.infrastructure.repositories.analysis_result.RabbitMQAnalysisResult import RabbitMQAnalysisResult


class AnalysisQueryProcessor:
    def __init__(self, analysis_query_repository: AnalysisQueryRepository = RabbitMQAnalysisQuery(),
                 analysis_result_repository: AnalysisResultRepository = RabbitMQAnalysisResult()):
        self.analysis_query_repository = analysis_query_repository
        self.analysis_result_repository = analysis_result_repository

    def run(self):
        print("Waiting for query...")
        analysis_query: AnalysisQuery = self.analysis_query_repository.get_query()
        print("Query obtained!", analysis_query)

        data_bias_graph: Graph = AnalyzeDataBias().invoke(
            data_set_source=analysis_query.data_set_source,
            bias_code=analysis_query.bias_code
        )

        algorithm_bias_graph: Graph = AnalyzeAlgorithmBias().invoke(
            data_set_source=analysis_query.data_set_source,
            bias_code=analysis_query.bias_code,
            algorithm_code=analysis_query.algorithm_code
        )

        result = AnalysisResult(
            analysis_id=analysis_query.analysis_id,
            data_bias_graph=data_bias_graph,
            algorithm_bias_graph=algorithm_bias_graph
        )

        print("Analysis done!", result)

        self.analysis_result_repository.store(result)
