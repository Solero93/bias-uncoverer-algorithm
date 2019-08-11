from pprint import pprint

from src.domain.AnalysisResult import AnalysisResult
from src.domain.repositories.AnalysisResultRepository import AnalysisResultRepository


class StdOutAnalysisResult(AnalysisResultRepository):
    def store(self, analysis_result: AnalysisResult) -> None:
        pprint(analysis_result.serialize())
